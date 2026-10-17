#!/usr/bin/env python3
"""
logic_engine_starter.py -- reference starter kit for Chapter 8 of "Mastering Mathematical Logic".

It implements, in one readable file, the milestones that are hardest to get right:

  M1  syntax: AST, parser (ASCII and Unicode), pretty-printer
  M2  free variables, capture-avoiding substitution, alpha-equivalence
  M3  semantics: finite structures, evaluator, countermodel finder
  M4  propositional tools: truth tables, NNF/CNF, Tseitin, DPLL
  M5  the KERNEL: a Fitch-style proof checker, including the freshness
      conditions of forall-I and exists-E
  M7  an automatic prover: clausification, Skolemization, unification,
      resolution + factoring with a given-clause loop

Not included (these are your exercises): M6 tactics, M8 paramodulation, M9 UI.

Run the self-tests with:   python3 test_starter.py
Requires Python 3.10+ (structural pattern matching).
"""
from __future__ import annotations

import itertools
import re
from dataclasses import dataclass
from itertools import count, product


# =============================================================================
# M1. SYNTAX
# =============================================================================

@dataclass(frozen=True)
class Var:
    name: str

@dataclass(frozen=True)
class Fn:                       # constants are Fn with no arguments
    name: str
    args: tuple = ()

@dataclass(frozen=True)
class Pred:                     # 0-ary predicates are propositional atoms
    name: str
    args: tuple = ()

@dataclass(frozen=True)
class Not:      f: object
@dataclass(frozen=True)
class And:      l: object; r: object
@dataclass(frozen=True)
class Or:       l: object; r: object
@dataclass(frozen=True)
class Implies:  l: object; r: object
@dataclass(frozen=True)
class Iff:      l: object; r: object
@dataclass(frozen=True)
class Forall:   var: str; body: object
@dataclass(frozen=True)
class Exists:   var: str; body: object
@dataclass(frozen=True)
class Eq:       l: object; r: object
@dataclass(frozen=True)
class Bottom:   pass


class ParseError(Exception):
    pass


# Convention used by the parser:
#   * identifiers starting with one of u v w x y z are VARIABLES;
#   * every other identifier is a constant / function / predicate symbol.
def is_var_name(n: str) -> bool:
    return n[:1] in "uvwxyz"


_UNICODE = {"¬": "~", "∧": "&", "∨": "|", "→": "->", "↔": "<->", "⇒": "->", "⇔": "<->",
            "⊥": " false ", "∀": " forall ", "∃": " exists ", "≠": "!="}


def _normalize(s: str) -> str:
    for k, v in _UNICODE.items():
        s = s.replace(k, v)
    return s


_TOKEN = re.compile(r"\s*(<->|->|!=|[~&|().,=]|[A-Za-z_][A-Za-z0-9_']*|\S)")


def tokenize(s: str) -> list[str]:
    s = _normalize(s)
    pos, out = 0, []
    while pos < len(s):
        m = _TOKEN.match(s, pos)
        if not m:
            break                                  # only trailing whitespace is left
        out.append(m.group(1))
        pos = m.end()
    return out


class _Parser:
    """Precedence (loosest to tightest):  <->   ->(right-assoc)   |   &   ~ and quantifiers.

    Quantifier scope:  'forall x. A'  (with a dot) extends as far right as possible;
                       '∀x A' / 'forall x A' (no dot) binds as tightly as '~'.
    """

    def __init__(self, text: str):
        self.toks = tokenize(text)
        self.i = 0

    def peek(self):
        return self.toks[self.i] if self.i < len(self.toks) else None

    def next(self):
        t = self.peek()
        if t is None:
            raise ParseError("unexpected end of input")
        self.i += 1
        return t

    def expect(self, t):
        got = self.next()
        if got != t:
            raise ParseError(f"expected '{t}' but found '{got}'")

    def parse(self):
        f = self.iff()
        if self.peek() is not None:
            raise ParseError(f"unexpected '{self.peek()}'")
        return f

    def iff(self):
        l = self.imp()
        while self.peek() == "<->":
            self.next()
            l = Iff(l, self.imp())
        return l

    def imp(self):
        l = self.disj()
        if self.peek() == "->":
            self.next()
            return Implies(l, self.imp())              # right-associative
        return l

    def disj(self):
        l = self.conj()
        while self.peek() == "|":
            self.next()
            l = Or(l, self.conj())
        return l

    def conj(self):
        l = self.unary()
        while self.peek() == "&":
            self.next()
            l = And(l, self.unary())
        return l

    def unary(self):
        t = self.peek()
        if t == "~":
            self.next()
            return Not(self.unary())
        if t in ("forall", "exists"):
            self.next()
            v = self.next()
            if not (re.match(r"[A-Za-z_]", v) and is_var_name(v)):
                raise ParseError(f"bound variable '{v}' must start with one of u v w x y z")
            if self.peek() == ".":
                self.next()
                body = self.iff()                       # as far right as possible
            else:
                body = self.unary()                     # tight binding
            return (Forall if t == "forall" else Exists)(v, body)
        if t == "(":
            self.next()
            f = self.iff()
            self.expect(")")
            return f
        if t == "false":
            self.next()
            return Bottom()
        tm = self.term()
        if self.peek() in ("=", "!="):
            op = self.next()
            e = Eq(tm, self.term())
            return e if op == "=" else Not(e)
        if isinstance(tm, Fn):
            return Pred(tm.name, tm.args)
        raise ParseError(f"'{tm.name}' is a variable, not a formula")

    def term(self):
        name = self.next()
        if not re.match(r"[A-Za-z_]", name) or name in ("forall", "exists", "false"):
            raise ParseError(f"expected a term but found '{name}'")
        if self.peek() == "(":
            self.next()
            args = [self.term()]
            while self.peek() == ",":
                self.next()
                args.append(self.term())
            self.expect(")")
            return Fn(name, tuple(args))
        return Var(name) if is_var_name(name) else Fn(name)


def parse(text: str):
    """Parse a formula. ASCII:  ~ & | -> <-> forall x. exists x. =  !=  false   (Unicode also accepted)."""
    return _Parser(text).parse()


def fmt_term(t) -> str:
    if isinstance(t, Var):
        return t.name
    if not t.args:
        return t.name
    return f"{t.name}({', '.join(fmt_term(a) for a in t.args)})"


def pretty(f, need: int = 0) -> str:
    """ASCII pretty-printer with minimal parentheses. parse(pretty(f)) == f."""
    match f:
        case Pred(n, args):
            s, p = (n if not args else f"{n}({', '.join(map(fmt_term, args))})"), 6
        case Eq(l, r):
            s, p = f"{fmt_term(l)} = {fmt_term(r)}", 6
        case Bottom():
            s, p = "false", 6
        case Not(Eq(l, r)):
            s, p = f"{fmt_term(l)} != {fmt_term(r)}", 6
        case Not(g):
            s, p = "~" + pretty(g, 5), 5
        case And(l, r):
            s, p = f"{pretty(l, 4)} & {pretty(r, 5)}", 4
        case Or(l, r):
            s, p = f"{pretty(l, 3)} | {pretty(r, 4)}", 3
        case Implies(l, r):
            s, p = f"{pretty(l, 3)} -> {pretty(r, 2)}", 2
        case Iff(l, r):
            s, p = f"{pretty(l, 2)} <-> {pretty(r, 2)}", 1
        case Forall(v, b):
            s, p = f"forall {v}. {pretty(b, 0)}", 0
        case Exists(v, b):
            s, p = f"exists {v}. {pretty(b, 0)}", 0
        case _:
            raise TypeError(f"not a formula: {f!r}")
    return f"({s})" if p < need else s


# =============================================================================
# M2. FREE VARIABLES, SUBSTITUTION, ALPHA-EQUIVALENCE
# =============================================================================

def free_vars(x) -> set[str]:
    match x:
        case Var(n):
            return {n}
        case Fn(_, args) | Pred(_, args):
            return set().union(*map(free_vars, args)) if args else set()
        case Eq(l, r) | And(l, r) | Or(l, r) | Implies(l, r) | Iff(l, r):
            return free_vars(l) | free_vars(r)
        case Not(f):
            return free_vars(f)
        case Forall(v, b) | Exists(v, b):
            return free_vars(b) - {v}
        case Bottom():
            return set()
    raise TypeError(x)


_fresh_ids = count()


def fresh_var(base: str) -> str:
    base = base.split("_")[0]
    return f"{base}_{next(_fresh_ids)}"


def subst(x, v: str, t):
    """x[t/v]: replace the FREE occurrences of variable v in x by term t, avoiding capture."""
    match x:
        case Var(n):
            return t if n == v else x
        case Fn(f, args):
            return Fn(f, tuple(subst(a, v, t) for a in args))
        case Pred(p, args):
            return Pred(p, tuple(subst(a, v, t) for a in args))
        case Eq(l, r):
            return Eq(subst(l, v, t), subst(r, v, t))
        case Not(f):
            return Not(subst(f, v, t))
        case And(l, r):
            return And(subst(l, v, t), subst(r, v, t))
        case Or(l, r):
            return Or(subst(l, v, t), subst(r, v, t))
        case Implies(l, r):
            return Implies(subst(l, v, t), subst(r, v, t))
        case Iff(l, r):
            return Iff(subst(l, v, t), subst(r, v, t))
        case Bottom():
            return x
        case Forall(n, body) | Exists(n, body):
            ctor = type(x)
            if n == v:                                   # v is bound here: nothing to replace
                return x
            if n in free_vars(t) and v in free_vars(body):
                n2 = fresh_var(n)                        # rename the bound variable: avoid capture
                body = subst(body, n, Var(n2))
                n = n2
            return ctor(n, subst(body, v, t))
    raise TypeError(x)


def _depth_of(env: tuple, n: str):
    for i in range(len(env) - 1, -1, -1):
        if env[i] == n:
            return len(env) - 1 - i
    return None


def alpha_eq(a, b, ea: tuple = (), eb: tuple = ()) -> bool:
    """Equality up to renaming of bound variables."""
    if type(a) is not type(b):
        return False
    match a:
        case Var(n):
            ia, ib = _depth_of(ea, n), _depth_of(eb, b.name)
            if ia is None and ib is None:
                return n == b.name
            return ia == ib
        case Fn(f, args) | Pred(f, args):
            return f == b.name and len(args) == len(b.args) and all(
                alpha_eq(x, y, ea, eb) for x, y in zip(args, b.args))
        case Eq(l, r) | And(l, r) | Or(l, r) | Implies(l, r) | Iff(l, r):
            return alpha_eq(l, b.l, ea, eb) and alpha_eq(r, b.r, ea, eb)
        case Not(f):
            return alpha_eq(f, b.f, ea, eb)
        case Bottom():
            return True
        case Forall(v, body) | Exists(v, body):
            return alpha_eq(body, b.body, ea + (v,), eb + (b.var,))
    raise TypeError(a)


def occurs_name(x, name: str) -> bool:
    """Does the function/constant symbol `name` occur anywhere in x?"""
    match x:
        case Var():
            return False
        case Fn(f, args):
            return f == name or any(occurs_name(a, name) for a in args)
        case Pred(_, args):
            return any(occurs_name(a, name) for a in args)
        case Eq(l, r) | And(l, r) | Or(l, r) | Implies(l, r) | Iff(l, r):
            return occurs_name(l, name) or occurs_name(r, name)
        case Not(f):
            return occurs_name(f, name)
        case Forall(_, b) | Exists(_, b):
            return occurs_name(b, name)
        case Bottom():
            return False
    raise TypeError(x)


def subterms(x):
    """All terms occurring in x (with repetitions removed)."""
    out: list = []

    def term(t):
        if t not in out:
            out.append(t)
        if isinstance(t, Fn):
            for a in t.args:
                term(a)

    def walk_f(f):
        match f:
            case Pred(_, args):
                for a in args:
                    term(a)
            case Eq(l, r):
                term(l); term(r)
            case Not(g):
                walk_f(g)
            case And(l, r) | Or(l, r) | Implies(l, r) | Iff(l, r):
                walk_f(l); walk_f(r)
            case Forall(_, b) | Exists(_, b):
                walk_f(b)
    walk_f(x) if not isinstance(x, (Var, Fn)) else term(x)
    return out


# =============================================================================
# M3. SEMANTICS: FINITE STRUCTURES
# =============================================================================

@dataclass
class Structure:
    domain: tuple
    funcs: dict          # name -> {args tuple -> element}      (constants: key ())
    preds: dict          # name -> set of argument tuples

    def __str__(self):
        parts = [f"D = {list(self.domain)}"]
        for n, t in sorted(self.funcs.items()):
            parts.append(f"{n}: {dict(sorted(t.items()))}")
        for n, s in sorted(self.preds.items()):
            parts.append(f"{n} = {sorted(s)}")
        return "; ".join(parts)


def eval_term(t, M: Structure, env: dict):
    if isinstance(t, Var):
        return env[t.name]
    return M.funcs[t.name][tuple(eval_term(a, M, env) for a in t.args)]


def holds(f, M: Structure, env: dict | None = None) -> bool:
    """Tarski semantics by expanding quantifiers over the (finite) domain."""
    env = env or {}
    match f:
        case Pred(n, args):
            return tuple(eval_term(a, M, env) for a in args) in M.preds.get(n, set())
        case Eq(l, r):
            return eval_term(l, M, env) == eval_term(r, M, env)
        case Bottom():
            return False
        case Not(g):
            return not holds(g, M, env)
        case And(l, r):
            return holds(l, M, env) and holds(r, M, env)
        case Or(l, r):
            return holds(l, M, env) or holds(r, M, env)
        case Implies(l, r):
            return (not holds(l, M, env)) or holds(r, M, env)
        case Iff(l, r):
            return holds(l, M, env) == holds(r, M, env)
        case Forall(v, b):
            return all(holds(b, M, {**env, v: d}) for d in M.domain)
        case Exists(v, b):
            return any(holds(b, M, {**env, v: d}) for d in M.domain)
    raise TypeError(f)


def signature(*formulas):
    """(functions, predicates) as dicts name -> arity."""
    funcs: dict = {}
    preds: dict = {}

    def term(t):
        if isinstance(t, Fn):
            funcs[t.name] = len(t.args)
            for a in t.args:
                term(a)

    def walk(f):
        match f:
            case Pred(n, args):
                preds[n] = len(args)
                for a in args:
                    term(a)
            case Eq(l, r):
                term(l); term(r)
            case Not(g):
                walk(g)
            case And(l, r) | Or(l, r) | Implies(l, r) | Iff(l, r):
                walk(l); walk(r)
            case Forall(_, b) | Exists(_, b):
                walk(b)
    for f in formulas:
        walk(f)
    return funcs, preds


def structures(funcs: dict, preds: dict, n: int):
    """Enumerate ALL structures with domain {0..n-1} for the given signature (lazy)."""
    dom = tuple(range(n))
    fnames, pnames = sorted(funcs), sorted(preds)
    f_opts = []
    for name in fnames:
        keys = list(product(dom, repeat=funcs[name]))
        f_opts.append([dict(zip(keys, vals)) for vals in product(dom, repeat=len(keys))])
    p_opts = []
    for name in pnames:
        keys = list(product(dom, repeat=preds[name]))
        p_opts.append([{k for k, b in zip(keys, bits) if b} for bits in product([False, True], repeat=len(keys))])
    for fc in product(*f_opts):
        for pc in product(*p_opts):
            yield Structure(dom, dict(zip(fnames, fc)), dict(zip(pnames, pc)))


def find_countermodel(premises, conclusion, max_size: int = 3, limit: int = 2_000_000):
    """Search structures of size 1..max_size where all premises hold and the conclusion fails.
    Returns a Structure, or None if none was found within `limit` structures per size."""
    funcs, preds = signature(*premises, conclusion)
    for n in range(1, max_size + 1):
        for k, M in enumerate(structures(funcs, preds, n)):
            if k >= limit:
                break
            if all(holds(p, M) for p in premises) and not holds(conclusion, M):
                return M
    return None


# =============================================================================
# M4. PROPOSITIONAL TOOLS
# =============================================================================

def prop_atoms(f) -> list[str]:
    out: list[str] = []

    def walk(g):
        match g:
            case Pred(n, ()):
                if n not in out:
                    out.append(n)
            case Not(h):
                walk(h)
            case And(l, r) | Or(l, r) | Implies(l, r) | Iff(l, r):
                walk(l); walk(r)
            case Bottom():
                pass
            case _:
                raise ValueError("not a propositional formula")
    walk(f)
    return out


def eval_prop(f, v: dict) -> bool:
    match f:
        case Pred(n, ()):
            return v[n]
        case Bottom():
            return False
        case Not(g):
            return not eval_prop(g, v)
        case And(l, r):
            return eval_prop(l, v) and eval_prop(r, v)
        case Or(l, r):
            return eval_prop(l, v) or eval_prop(r, v)
        case Implies(l, r):
            return (not eval_prop(l, v)) or eval_prop(r, v)
        case Iff(l, r):
            return eval_prop(l, v) == eval_prop(r, v)
    raise ValueError("not a propositional formula")


def truth_table(f):
    atoms = prop_atoms(f)
    for bits in product([True, False], repeat=len(atoms)):
        v = dict(zip(atoms, bits))
        yield v, eval_prop(f, v)


def is_tautology(f) -> bool:
    return all(val for _, val in truth_table(f))


def is_satisfiable_bruteforce(f) -> bool:
    return any(val for _, val in truth_table(f))


def elim_arrows(f):
    """Eliminate -> and <-> (works for first-order formulas too)."""
    match f:
        case Implies(l, r):
            return Or(Not(elim_arrows(l)), elim_arrows(r))
        case Iff(l, r):
            a, b = elim_arrows(l), elim_arrows(r)
            return And(Or(Not(a), b), Or(Not(b), a))
        case Not(g):
            return Not(elim_arrows(g))
        case And(l, r):
            return And(elim_arrows(l), elim_arrows(r))
        case Or(l, r):
            return Or(elim_arrows(l), elim_arrows(r))
        case Forall(v, b):
            return Forall(v, elim_arrows(b))
        case Exists(v, b):
            return Exists(v, elim_arrows(b))
        case _:
            return f


def nnf(f, neg: bool = False):
    """Negation normal form of an arrow-free formula."""
    match f:
        case Not(g):
            return nnf(g, not neg)
        case And(l, r):
            return (Or if neg else And)(nnf(l, neg), nnf(r, neg))
        case Or(l, r):
            return (And if neg else Or)(nnf(l, neg), nnf(r, neg))
        case Forall(v, b):
            return (Exists if neg else Forall)(v, nnf(b, neg))
        case Exists(v, b):
            return (Forall if neg else Exists)(v, nnf(b, neg))
        case Bottom():
            return Not(Bottom()) if neg else f
        case _:                                    # atoms (Pred, Eq)
            return Not(f) if neg else f


def _lit_of(f):
    """NNF literal -> (sign, atom)."""
    match f:
        case Not(Eq(l, r)):
            return (False, Pred("=", (l, r)))
        case Not(a):
            return (False, a if not isinstance(a, Eq) else Pred("=", (a.l, a.r)))
        case Eq(l, r):
            return (True, Pred("=", (l, r)))
        case _:
            return (True, f)


def nnf_to_clauses(f):
    """Quantifier-free NNF -> list of clauses (frozensets of (sign, atom)) by distribution."""
    match f:
        case And(l, r):
            return nnf_to_clauses(l) + nnf_to_clauses(r)
        case Or(l, r):
            return [a | b for a in nnf_to_clauses(l) for b in nnf_to_clauses(r)]
        case Bottom():
            return [frozenset()]
        case Not(Bottom()):
            return []
        case _:
            return [frozenset([_lit_of(f)])]


def dpll(clauses, assignment=None):
    """clauses: list of lists of nonzero ints (DIMACS style). Returns a model dict or None."""
    def simplify(cs, lit):
        return [[l for l in c if l != -lit] for c in cs if lit not in c]

    assignment = dict(assignment or {})
    while True:                                        # unit propagation
        unit = next((c[0] for c in clauses if len(c) == 1), None)
        if unit is None:
            break
        assignment[abs(unit)] = unit > 0
        clauses = simplify(clauses, unit)
    if any(len(c) == 0 for c in clauses):
        return None
    lits = {l for c in clauses for l in c}             # pure literals
    pure = next((l for l in lits if -l not in lits), None)
    while pure is not None:
        assignment[abs(pure)] = pure > 0
        clauses = simplify(clauses, pure)
        lits = {l for c in clauses for l in c}
        pure = next((l for l in lits if -l not in lits), None)
    if not clauses:
        return assignment
    l = clauses[0][0]
    for choice in (l, -l):
        r = dpll(simplify(clauses, choice), {**assignment, abs(choice): choice > 0})
        if r is not None:
            return r
    return None


def tseitin(f):
    """Equisatisfiable CNF of linear size. Returns (clauses of ints, {atom name: variable number})."""
    ids: dict = {}
    memo: dict = {}
    clauses: list[list[int]] = []
    counter = count(1)

    def new():
        return next(counter)

    def enc(g) -> int:
        if g in memo:
            return memo[g]
        match g:
            case Pred(n, ()):
                if n not in ids:
                    ids[n] = new()
                lit = ids[n]
            case Bottom():
                x = new(); clauses.append([-x]); lit = x
            case Not(h):
                lit = -enc(h)
            case And(l, r):
                a, b, x = enc(l), enc(r), new()
                clauses.extend([[-x, a], [-x, b], [x, -a, -b]]); lit = x
            case Or(l, r):
                a, b, x = enc(l), enc(r), new()
                clauses.extend([[-x, a, b], [x, -a], [x, -b]]); lit = x
            case Implies(l, r):
                a, b, x = enc(l), enc(r), new()
                clauses.extend([[-x, -a, b], [x, a], [x, -b]]); lit = x
            case Iff(l, r):
                a, b, x = enc(l), enc(r), new()
                clauses.extend([[-x, -a, b], [-x, a, -b], [x, a, b], [x, -a, -b]]); lit = x
            case _:
                raise ValueError("not a propositional formula")
        memo[g] = lit
        return lit

    top = enc(f)
    clauses.append([top])
    return clauses, ids


def sat(f) -> bool:
    """Satisfiability of a propositional formula via Tseitin + DPLL."""
    clauses, _ = tseitin(f)
    return dpll(clauses) is not None


# =============================================================================
# M5. THE KERNEL: A FITCH-STYLE PROOF CHECKER
# =============================================================================
#
# Proof text format (one line per step):
#
#     3.  |  |  [a]  P(a)        assumption          <- opens a box; [a] introduces a fresh name
#     4.  |  |  Q(a)             ->E 1,3             <- rule name, then line numbers
#     7.  |  P -> Q              ->I 3-6             <- a range m-n cites a whole box
#
#   * the number of '|' is the depth (nesting of boxes);
#   * the formula and the justification are separated by two or more spaces;
#   * '[a]' alone on a line opens a forall-I box (a fresh name, no assumption);
#   * '[a] phi  assumption' opens an exists-E box;
#   * everything after ';' is a comment.
#
# Rules (ASCII or Unicode names):  premise assumption &I &E |I |E ->I ->E ~I ~E falseE RAA
#                                  <->I <->E forallE forallI existsI existsE =I =E Reit

class ProofError(Exception):
    pass


_RULE_NORM = {"→": "->", "∧": "&", "∨": "|", "¬": "~", "↔": "<->", "⊥": "false", "∀": "forall", "∃": "exists"}

_RULES = {
    "premise": "premise", "assumption": "assumption", "assume": "assumption",
    "&I": "andI", "andI": "andI", "&E": "andE", "andE": "andE",
    "|I": "orI", "orI": "orI", "|E": "orE", "orE": "orE",
    "->I": "impI", "impI": "impI", "->E": "impE", "impE": "impE",
    "~I": "notI", "notI": "notI", "~E": "notE", "notE": "notE",
    "falseE": "botE", "botE": "botE", "RAA": "raa", "raa": "raa",
    "<->I": "iffI", "iffI": "iffI", "<->E": "iffE", "iffE": "iffE",
    "forallE": "allE", "allE": "allE", "forallI": "allI", "allI": "allI",
    "existsI": "exI", "exI": "exI", "existsE": "exE", "exE": "exE",
    "=I": "eqI", "eqI": "eqI", "=E": "eqE", "eqE": "eqE", "Reit": "reit", "reit": "reit",
}


@dataclass
class PLine:
    num: int
    depth: int
    formula: object | None
    name: str | None
    rule: str
    refs: list
    box: int


@dataclass
class Box:
    id: int
    depth: int
    start: int
    end: int
    parent: int
    name: str | None
    assume: object | None


class _Proof:
    def __init__(self):
        self.lines: dict[int, PLine] = {}
        self.boxes: dict[int, Box] = {0: Box(0, 0, 0, 0, -1, None, None)}

    def encloses(self, outer: int, inner: int) -> bool:
        b = inner
        while b != -1:
            if b == outer:
                return True
            b = self.boxes[b].parent
        return False

    def ancestors(self, box_id: int):
        """The boxes strictly enclosing box_id (nearest first), excluding the root."""
        b = self.boxes[box_id].parent
        while b > 0:
            yield self.boxes[b]
            b = self.boxes[b].parent


def _parse_ref(tok: str):
    tok = tok.strip().replace("–", "-")
    m = re.fullmatch(r"(\d+)-(\d+)", tok)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    if re.fullmatch(r"\d+", tok):
        return int(tok)
    raise ProofError(f"bad line reference '{tok}'")


def _parse_proof(text: str) -> _Proof:
    P = _Proof()
    stack: list[int] = []                       # ids of open boxes, outermost first
    next_box = count(1)
    prev_num = 0
    for raw in text.splitlines():
        line = raw.split(";")[0].rstrip()
        if not line.strip():
            continue
        m = re.match(r"\s*(\d+)\s*[.)]?\s*(.*)$", line)
        if not m:
            raise ProofError(f"cannot read line: {raw!r}")
        num, rest = int(m.group(1)), m.group(2)
        if num != prev_num + 1:
            raise ProofError(f"line numbers must be consecutive (found {num} after {prev_num})")
        prev_num = num
        mb = re.match(r"((?:\s*[|│])*)\s*(.*)$", rest)
        depth = len(re.findall(r"[|│]", mb.group(1)))
        content = mb.group(2).strip()
        name = None
        h = re.match(r"\[(\w+)\]\s*(.*)$", content)
        if h:
            name, content = h.group(1), h.group(2).strip()
        formula = None
        rule = "header" if name and not content else ""
        refs: list = []
        if content:
            parts = re.split(r"\s{2,}", content, maxsplit=1)
            try:
                formula = parse(parts[0])
            except ParseError as e:
                raise ProofError(f"line {num}: {e}")
            if len(parts) < 2 or not parts[1].strip():
                raise ProofError(f"line {num}: missing justification (put 2+ spaces after the formula)")
            jm = re.match(r"(\S+)\s*(.*)$", parts[1].strip())
            raw_rule = jm.group(1)
            for k, v in _RULE_NORM.items():
                raw_rule = raw_rule.replace(k, v)
            if raw_rule not in _RULES:
                raise ProofError(f"line {num}: unknown rule '{jm.group(1)}'")
            rule = _RULES[raw_rule]
            argstr = jm.group(2)
            if rule not in ("assumption", "premise") and argstr.strip():
                refs = [_parse_ref(t) for t in argstr.split(",") if t.strip()]
        elif not name:
            raise ProofError(f"line {num}: empty line content")

        starts_box = rule in ("assumption", "header")
        # --- box bookkeeping ----------------------------------------------------------------
        if depth == 0:
            if starts_box:
                raise ProofError(f"line {num}: an assumption must be inside a box (depth >= 1)")
            stack.clear()
        else:
            while stack and P.boxes[stack[-1]].depth > depth:
                stack.pop()
            if starts_box:
                if stack and P.boxes[stack[-1]].depth == depth:
                    stack.pop()                          # a sibling box ends here
                expected_parent_depth = depth - 1
                cur = P.boxes[stack[-1]].depth if stack else 0
                if cur != expected_parent_depth:
                    raise ProofError(f"line {num}: indentation jumps (depth {depth} after depth {cur})")
                bid = next(next_box)
                P.boxes[bid] = Box(bid, depth, num, num, stack[-1] if stack else 0, name, formula)
                stack.append(bid)
            else:
                if not stack or P.boxes[stack[-1]].depth != depth:
                    raise ProofError(f"line {num}: depth {depth} does not match any open box")
        cur_box = stack[-1] if stack else 0
        for b in stack:
            P.boxes[b].end = num
        P.lines[num] = PLine(num, depth, formula, name, rule, refs, cur_box)
    if not P.lines:
        raise ProofError("empty proof")
    return P


class _Fail(Exception):
    pass


def check_proof(text: str, goal=None) -> list[str]:
    """Check a Fitch proof. Returns a list of error messages; an empty list means ACCEPTED.
    `goal` (optional): a formula or string that the last line must be (up to alpha-equivalence)."""
    try:
        P = _parse_proof(text)
    except ProofError as e:
        return [str(e)]
    errors: list[str] = []
    premises = [l.formula for l in P.lines.values() if l.rule == "premise"]

    # ---- freshness at box creation: a new name must not clash with anything already "in play"
    for b in P.boxes.values():
        if b.id == 0 or not b.name:
            continue
        a = b.name
        problems = []
        if is_var_name(a):
            problems.append(f"name '{a}' must not start with u..z (those are variables)")
        if any(occurs_name(p, a) for p in premises):
            problems.append(f"name '{a}' occurs in a premise")
        for anc in P.ancestors(b.id):
            if anc.assume is not None and occurs_name(anc.assume, a):
                problems.append(f"name '{a}' occurs in the open assumption of the box at line {anc.start}")
            if anc.name == a:
                problems.append(f"name '{a}' is already introduced by the enclosing box at line {anc.start}")
        for msg in problems:
            errors.append(f"line {b.start} (fresh name): {msg}")

    def visible(n: int, i: int) -> bool:
        return i < n and i in P.lines and P.encloses(P.lines[i].box, P.lines[n].box)

    def get(n: int, ref):
        if not isinstance(ref, int):
            raise _Fail(f"expected a single line number, got a range {ref[0]}-{ref[1]}")
        if ref not in P.lines:
            raise _Fail(f"line {ref} does not exist")
        if not visible(n, ref):
            raise _Fail(f"line {ref} is not available here (it is later, or inside a closed box)")
        f = P.lines[ref].formula
        if f is None:
            raise _Fail(f"line {ref} has no formula")
        return f

    def box_of(n: int, ref) -> Box:
        if isinstance(ref, int):
            raise _Fail(f"expected a box range m-n, got the single line {ref}")
        i, j = ref
        if i not in P.lines:
            raise _Fail(f"line {i} does not exist")
        b = P.boxes[P.lines[i].box]
        if b.id == 0 or b.start != i or b.end != j:
            raise _Fail(f"{i}-{j} is not exactly one box (the box starting at line {i} ends at line {b.end if b.id else '?'})")
        if j >= n or not P.encloses(b.parent, P.lines[n].box):
            raise _Fail(f"box {i}-{j} is not available here")
        return b

    def last(b: Box):
        f = P.lines[b.end].formula
        if f is None:
            raise _Fail(f"the last line of box {b.start}-{b.end} has no formula")
        return f

    def instance_exists(body, x: str, target) -> bool:
        if x not in free_vars(body):
            return alpha_eq(body, target)
        return any(alpha_eq(subst(body, x, t), target) for t in subterms(target))

    def rep_term(a, b, s, t, bound) -> bool:
        if a == b:
            return True
        if a == s and b == t:
            return not ((free_vars(s) | free_vars(t)) & bound)      # would be captured by a binder
        if isinstance(a, Fn) and isinstance(b, Fn) and a.name == b.name and len(a.args) == len(b.args):
            return all(rep_term(x, y, s, t, bound) for x, y in zip(a.args, b.args))
        return False

    def rep(a, b, s, t, bound=frozenset()) -> bool:
        if type(a) is not type(b):
            return False
        match a:
            case Pred(n, args):
                return n == b.name and len(args) == len(b.args) and all(
                    rep_term(x, y, s, t, bound) for x, y in zip(args, b.args))
            case Eq(l, r):
                return rep_term(l, b.l, s, t, bound) and rep_term(r, b.r, s, t, bound)
            case Not(g):
                return rep(g, b.f, s, t, bound)
            case And(l, r) | Or(l, r) | Implies(l, r) | Iff(l, r):
                return rep(l, b.l, s, t, bound) and rep(r, b.r, s, t, bound)
            case Forall(v, g) | Exists(v, g):
                return v == b.var and rep(g, b.body, s, t, bound | {v})
            case Bottom():
                return True
        return False

    for n in sorted(P.lines):
        L = P.lines[n]
        r = L.rule
        try:
            if r in ("header", "assumption"):
                continue
            if r == "premise":
                if L.depth != 0:
                    raise _Fail("premises must be at depth 0")
                continue
            f = L.formula
            refs = L.refs
            need = {"andI": 2, "andE": 1, "orI": 1, "orE": 3, "impI": 1, "impE": 2, "notI": 1, "notE": 2,
                    "botE": 1, "raa": 1, "iffI": 2, "iffE": 2, "allE": 1, "allI": 1, "exI": 1, "exE": 2,
                    "eqI": 0, "eqE": 2, "reit": 1}[r]
            if len(refs) != need:
                raise _Fail(f"rule needs {need} reference(s) but {len(refs)} given")

            if r == "andI":
                a, b = get(n, refs[0]), get(n, refs[1])
                if not alpha_eq(f, And(a, b)):
                    raise _Fail("conclusion must be (line1 & line2)")
            elif r == "andE":
                a = get(n, refs[0])
                if not (isinstance(a, And) and (alpha_eq(f, a.l) or alpha_eq(f, a.r))):
                    raise _Fail("cited line must be a conjunction and the conclusion one of its parts")
            elif r == "orI":
                a = get(n, refs[0])
                if not (isinstance(f, Or) and (alpha_eq(a, f.l) or alpha_eq(a, f.r))):
                    raise _Fail("conclusion must be a disjunction having the cited line as a disjunct")
            elif r == "orE":
                d = get(n, refs[0])
                b1, b2 = box_of(n, refs[1]), box_of(n, refs[2])
                if not isinstance(d, Or):
                    raise _Fail("first reference must be a disjunction")
                if b1.assume is None or b2.assume is None or b1.name or b2.name:
                    raise _Fail("both boxes must open with a plain assumption")
                ok = (alpha_eq(b1.assume, d.l) and alpha_eq(b2.assume, d.r)) or \
                     (alpha_eq(b1.assume, d.r) and alpha_eq(b2.assume, d.l))
                if not ok:
                    raise _Fail("the two box assumptions must be the two disjuncts")
                if not (alpha_eq(last(b1), f) and alpha_eq(last(b2), f)):
                    raise _Fail("both boxes must END with the conclusion")
            elif r == "impI":
                b = box_of(n, refs[0])
                if b.assume is None or b.name:
                    raise _Fail("box must open with a plain assumption")
                if not alpha_eq(f, Implies(b.assume, last(b))):
                    raise _Fail("conclusion must be (assumption -> last line of the box)")
            elif r == "impE":
                a, b = get(n, refs[0]), get(n, refs[1])
                if not ((isinstance(a, Implies) and alpha_eq(a.l, b) and alpha_eq(a.r, f)) or
                        (isinstance(b, Implies) and alpha_eq(b.l, a) and alpha_eq(b.r, f))):
                    raise _Fail("need A -> B and A, concluding B")
            elif r == "notI":
                b = box_of(n, refs[0])
                if b.assume is None or b.name:
                    raise _Fail("box must open with a plain assumption")
                if not isinstance(last(b), Bottom):
                    raise _Fail("box must end with false")
                if not alpha_eq(f, Not(b.assume)):
                    raise _Fail("conclusion must be the negation of the box assumption")
            elif r == "notE":
                a, b = get(n, refs[0]), get(n, refs[1])
                if not isinstance(f, Bottom):
                    raise _Fail("conclusion must be false")
                if not (alpha_eq(b, Not(a)) or alpha_eq(a, Not(b))):
                    raise _Fail("cited lines must be A and ~A")
            elif r == "botE":
                a = get(n, refs[0])
                if not isinstance(a, Bottom):
                    raise _Fail("cited line must be false")
            elif r == "raa":
                b = box_of(n, refs[0])
                if b.assume is None or b.name:
                    raise _Fail("box must open with a plain assumption")
                if not isinstance(last(b), Bottom):
                    raise _Fail("box must end with false")
                if not (isinstance(b.assume, Not) and alpha_eq(f, b.assume.f)):
                    raise _Fail("box must assume ~A and the conclusion must be A")
            elif r == "iffI":
                b1, b2 = box_of(n, refs[0]), box_of(n, refs[1])
                if b1.assume is None or b2.assume is None:
                    raise _Fail("both boxes must open with an assumption")
                ok = alpha_eq(f, Iff(b1.assume, b2.assume)) and alpha_eq(last(b1), b2.assume) \
                    and alpha_eq(last(b2), b1.assume)
                if not ok:
                    raise _Fail("boxes must prove A => B and B => A for the conclusion A <-> B")
            elif r == "iffE":
                a, b = get(n, refs[0]), get(n, refs[1])
                ok = False
                for e, o in ((a, b), (b, a)):
                    if isinstance(e, Iff) and ((alpha_eq(e.l, o) and alpha_eq(e.r, f)) or
                                               (alpha_eq(e.r, o) and alpha_eq(e.l, f))):
                        ok = True
                if not ok:
                    raise _Fail("need A <-> B and one side, concluding the other side")
            elif r == "allE":
                a = get(n, refs[0])
                if not isinstance(a, Forall):
                    raise _Fail("cited line must be a universal formula")
                if not instance_exists(a.body, a.var, f):
                    raise _Fail("conclusion is not an instance of the universal formula "
                                "(or the term would be captured by a quantifier)")
            elif r == "exI":
                a = get(n, refs[0])
                if not isinstance(f, Exists):
                    raise _Fail("conclusion must be existential")
                if not instance_exists(f.body, f.var, a):
                    raise _Fail("cited line is not an instance of the existential formula's body")
            elif r == "allI":
                b = box_of(n, refs[0])
                if not b.name:
                    raise _Fail("box must open with a fresh name, like '[a]'")
                if b.assume is not None:
                    raise _Fail("a forall-I box must not carry an assumption")
                if not isinstance(f, Forall):
                    raise _Fail("conclusion must be universal")
                if not alpha_eq(subst(f.body, f.var, Fn(b.name)), last(b)):
                    raise _Fail(f"last line of the box must be the body of the conclusion with {b.name} for {f.var}")
                if occurs_name(f, b.name):
                    raise _Fail(f"FRESHNESS: name '{b.name}' occurs in the conclusion")
            elif r == "exE":
                ex = get(n, refs[0])
                b = box_of(n, refs[1])
                if not isinstance(ex, Exists):
                    raise _Fail("first reference must be an existential formula")
                if not b.name or b.assume is None:
                    raise _Fail("box must open with '[a] A(a)': a fresh name and an assumption")
                if not alpha_eq(b.assume, subst(ex.body, ex.var, Fn(b.name))):
                    raise _Fail(f"box assumption must be the body of the existential with {b.name} for {ex.var}")
                if not alpha_eq(last(b), f):
                    raise _Fail("the box must END with the conclusion")
                if occurs_name(f, b.name):
                    raise _Fail(f"FRESHNESS: the witness name '{b.name}' occurs in the conclusion")
                if occurs_name(ex, b.name):
                    raise _Fail(f"FRESHNESS: the witness name '{b.name}' occurs in the existential formula")
            elif r == "eqI":
                if not (isinstance(f, Eq) and f.l == f.r):
                    raise _Fail("conclusion must be t = t")
            elif r == "eqE":
                a, b = get(n, refs[0]), get(n, refs[1])
                ok = False
                for e, o in ((a, b), (b, a)):
                    if isinstance(e, Eq):
                        for s, t in ((e.l, e.r), (e.r, e.l)):
                            if rep(o, f, s, t):
                                ok = True
                if not ok:
                    raise _Fail("conclusion must come from the other line by replacing some occurrences "
                                "of one side of the equation by the other side")
            elif r == "reit":
                if not alpha_eq(get(n, refs[0]), f):
                    raise _Fail("must repeat the cited line")
        except _Fail as e:
            errors.append(f"line {n} ({r}): {e}")

    last_line = P.lines[max(P.lines)]
    if last_line.depth != 0:
        errors.append("the proof must end at depth 0 (an open box remains)")
    if goal is not None:
        g = parse(goal) if isinstance(goal, str) else goal
        if last_line.formula is None or not alpha_eq(last_line.formula, g):
            errors.append("the last line is not the stated goal")
    return errors


# =============================================================================
# M7. AUTOMATIC PROVER: CLAUSIFICATION, UNIFICATION, RESOLUTION
# =============================================================================

_sk = count(1)


def standardize_apart(f, ren=None):
    """Rename every bound variable to a globally fresh one."""
    ren = ren or {}

    def t(x):
        if isinstance(x, Var):
            return Var(ren.get(x.name, x.name))
        return Fn(x.name, tuple(t(a) for a in x.args))

    match f:
        case Pred(n, args):
            return Pred(n, tuple(t(a) for a in args))
        case Eq(l, r):
            return Eq(t(l), t(r))
        case Not(g):
            return Not(standardize_apart(g, ren))
        case And(l, r):
            return And(standardize_apart(l, ren), standardize_apart(r, ren))
        case Or(l, r):
            return Or(standardize_apart(l, ren), standardize_apart(r, ren))
        case Forall(v, b) | Exists(v, b):
            v2 = fresh_var(v)
            return type(f)(v2, standardize_apart(b, {**ren, v: v2}))
        case _:
            return f


def skolemize(f, univs: tuple = ()):
    """Remove existentials from a standardized-apart NNF formula (universal variables stay)."""
    match f:
        case Forall(v, b):
            return Forall(v, skolemize(b, univs + (v,)))
        case Exists(v, b):
            sk = Fn(f"sk{next(_sk)}", tuple(Var(u) for u in univs))
            return skolemize(subst(b, v, sk), univs)
        case And(l, r):
            return And(skolemize(l, univs), skolemize(r, univs))
        case Or(l, r):
            return Or(skolemize(l, univs), skolemize(r, univs))
        case _:
            return f


def drop_universals(f):
    match f:
        case Forall(_, b):
            return drop_universals(b)
        case And(l, r):
            return And(drop_universals(l), drop_universals(r))
        case Or(l, r):
            return Or(drop_universals(l), drop_universals(r))
        case _:
            return f


def clausify(f):
    """First-order formula -> list of clauses (frozenset of (sign, atom)); equisatisfiable."""
    g = nnf(elim_arrows(f))
    g = standardize_apart(g)
    g = skolemize(g)
    g = drop_universals(g)
    return nnf_to_clauses(g)


def walk(t, s):
    while isinstance(t, Var) and t.name in s:
        t = s[t.name]
    return t


def occurs(v, t, s) -> bool:
    t = walk(t, s)
    if isinstance(t, Var):
        return t.name == v
    return any(occurs(v, a, s) for a in t.args)


def unify(a, b, s=None):
    """Most general unifier (triangular form) or None. Works for terms and atoms. Has the occurs check."""
    s = {} if s is None else s
    a, b = walk(a, s), walk(b, s)
    if a == b:
        return s
    if isinstance(a, Var):
        return None if occurs(a.name, b, s) else {**s, a.name: b}
    if isinstance(b, Var):
        return unify(b, a, s)
    if a.name != b.name or len(a.args) != len(b.args):
        return None
    for x, y in zip(a.args, b.args):
        s = unify(x, y, s)
        if s is None:
            return None
    return s


def apply_subst(s, t):
    t = walk(t, s)
    if isinstance(t, Var):
        return t
    return type(t)(t.name, tuple(apply_subst(s, a) for a in t.args))


_rename_ids = count()


def rename_apart(clause):
    suffix = f"#{next(_rename_ids)}"

    def rt(t):
        if isinstance(t, Var):
            return Var(t.name + suffix)
        return type(t)(t.name, tuple(rt(a) for a in t.args))
    return frozenset((sg, rt(atom)) for sg, atom in clause)


def resolvents(c1, c2):
    c2 = rename_apart(c2)
    for (s1, a1) in c1:
        for (s2, a2) in c2:
            if s1 != s2:
                th = unify(a1, a2)
                if th is not None:
                    rest = (c1 - {(s1, a1)}) | (c2 - {(s2, a2)})
                    yield frozenset((sg, apply_subst(th, a)) for sg, a in rest)


def factors(c):
    lits = list(c)
    for i, (s1, a1) in enumerate(lits):
        for (s2, a2) in lits[i + 1:]:
            if s1 == s2:
                th = unify(a1, a2)
                if th is not None:
                    yield frozenset((sg, apply_subst(th, a)) for sg, a in c)


def is_tautology_clause(c) -> bool:
    return any((not sg, a) in c for sg, a in c)


def canon(c):
    """Rename the variables of a clause in order of first appearance (cheap duplicate detection)."""
    lits = sorted(c, key=lambda l: (l[1].name, l[0], repr(l[1])))
    ren: dict = {}

    def rt(t):
        if isinstance(t, Var):
            if t.name not in ren:
                ren[t.name] = f"V{len(ren)}"
            return Var(ren[t.name])
        return type(t)(t.name, tuple(rt(a) for a in t.args))
    return frozenset((sg, rt(a)) for sg, a in lits)


def _match(p, t, s):
    if isinstance(p, Var):
        if p.name in s:
            return s if s[p.name] == t else None
        return {**s, p.name: t}
    if type(p) is not type(t) or p.name != t.name or len(p.args) != len(t.args):
        return None
    for x, y in zip(p.args, t.args):
        s = _match(x, y, s)
        if s is None:
            return None
    return s


def subsumes(c, d) -> bool:
    """Does clause c subsume clause d (c*theta is a subset of d for some theta)?"""
    if len(c) > len(d):
        return False
    cl = list(c)

    def go(i, s):
        if i == len(cl):
            return True
        sg, a = cl[i]
        for sg2, b in d:
            if sg2 == sg:
                s2 = _match(a, b, s)
                if s2 is not None and go(i + 1, s2):
                    return True
        return False
    return go(0, {})


def clause_str(c) -> str:
    if not c:
        return "[]"
    return "{" + ", ".join(("" if sg else "~") + pretty(a) for sg, a in sorted(c, key=lambda l: (l[1].name, l[0], repr(l[1])))) + "}"


@dataclass
class Result:
    status: str                 # 'proved' | 'saturated' | 'limit'
    steps: int
    proof: list                 # list of (clause, reason) leading to the empty clause (if proved)

    def __bool__(self):
        return self.status == "proved"


def equality_axioms(*formulas):
    """Reflexivity, symmetry, transitivity and congruence axioms for the symbols of the formulas."""
    funcs, preds = signature(*formulas)
    x, y, z = Var("x"), Var("y"), Var("z")
    ax = [Eq(x, x),
          Implies(Eq(x, y), Eq(y, x)),
          Implies(And(Eq(x, y), Eq(y, z)), Eq(x, z))]
    for name, k in funcs.items():
        if k:
            xs = tuple(Var(f"x{i}") for i in range(k))
            ys = tuple(Var(f"y{i}") for i in range(k))
            hyp = None
            for a, b in zip(xs, ys):
                e = Eq(a, b)
                hyp = e if hyp is None else And(hyp, e)
            ax.append(Implies(hyp, Eq(Fn(name, xs), Fn(name, ys))))
    for name, k in preds.items():
        if k and name != "=":
            xs = tuple(Var(f"x{i}") for i in range(k))
            ys = tuple(Var(f"y{i}") for i in range(k))
            hyp = None
            for a, b in zip(xs, ys):
                e = Eq(a, b)
                hyp = e if hyp is None else And(hyp, e)
            ax.append(Implies(And(hyp, Pred(name, xs)), Pred(name, ys)))
    return ax


def _size(t) -> int:
    return 1 + sum(_size(a) for a in t.args) if not isinstance(t, Var) else 1


def clause_weight(c) -> int:
    return sum(_size(a) for _, a in c)


def prove(premises, goal, max_clauses: int = 4000, with_equality: bool = False,
          max_weight: int = 60) -> Result:
    """Refutation prover: clausify premises and ~goal, run a given-clause loop with factoring,
    tautology deletion and subsumption. Never answers 'invalid' -- FOL is only semi-decidable:
    'saturated' means no more clauses can be derived (so the clause set, hence premises & ~goal, is
    satisfiable), 'limit' means resources ran out or some clause was discarded for being too heavy."""
    premises = list(premises)
    if with_equality:
        premises = premises + equality_axioms(*premises, goal)
    clauses: list = []
    for p in premises:
        clauses += clausify(p)
    clauses += clausify(Not(goal))

    store: list = []               # (clause, reason)
    index: dict = {}               # canonical clause -> id

    dropped = [False]

    def add(c, reason):
        if is_tautology_clause(c):
            return None
        if clause_weight(c) > max_weight:         # keeps term growth finite; makes the search incomplete
            dropped[0] = True
            return None
        k = canon(c)
        if k in index:
            return None
        store.append((c, reason))
        index[k] = len(store) - 1
        return len(store) - 1

    passive: list[int] = []
    for c in clauses:
        i = add(c, ("input", ()))
        if i is not None:
            passive.append(i)
    active: list[int] = []
    steps = 0

    def trace(i):
        seen, order = set(), []

        def go(j):
            if j in seen:
                return
            seen.add(j)
            for p in store[j][1][1]:
                go(p)
            order.append(j)
        go(i)
        return [(store[j][0], store[j][1][0]) for j in order]

    for i in passive:
        if not store[i][0]:
            return Result("proved", 0, trace(i))

    while passive:
        if len(store) > max_clauses:
            return Result("limit", steps, [])
        passive.sort(key=lambda j: (len(store[j][0]), sum(1 for _ in repr(store[j][0]))))
        g = passive.pop(0)
        gc = store[g][0]
        if any(subsumes(store[a][0], gc) for a in active):
            continue
        steps += 1
        new: list = []
        for a in active + [g]:
            for r in resolvents(gc, store[a][0]):
                new.append((r, ("resolve", (g, a))))
        for r in factors(gc):
            new.append((r, ("factor", (g,))))
        active.append(g)
        for r, why in new:
            i = add(r, why)
            if i is not None:
                if not r:
                    return Result("proved", steps, trace(i))
                passive.append(i)
    return Result("limit" if dropped[0] else "saturated", steps, [])


def format_proof(result: Result) -> str:
    return "\n".join(f"{i + 1:3}. {clause_str(c):45} {why}" for i, (c, why) in enumerate(result.proof))


# =============================================================================
# A tiny command-line interface
# =============================================================================

def _main(argv):
    import sys
    usage = ("usage:\n"
             "  python3 logic_engine_starter.py parse  'forall x. P(x) -> Q(x)'\n"
             "  python3 logic_engine_starter.py prove  'premise1' 'premise2' ... '|-' 'goal'\n"
             "  python3 logic_engine_starter.py countermodel 'premise1' ... '|-' 'goal'\n"
             "  python3 logic_engine_starter.py check  proof.txt ['goal']\n")
    if len(argv) < 2:
        print(usage); return 1
    cmd, rest = argv[1], argv[2:]
    if cmd == "parse":
        f = parse(rest[0]); print(pretty(f)); print(f); return 0
    if cmd in ("prove", "countermodel") and "|-" in rest:
        k = rest.index("|-")
        prem, goal = [parse(s) for s in rest[:k]], parse(rest[k + 1])
        if cmd == "prove":
            r = prove(prem, goal)
            print(r.status)
            if r:
                print(format_proof(r))
        else:
            M = find_countermodel(prem, goal)
            print(M if M else "no countermodel up to size 3")
        return 0
    if cmd == "check":
        text = open(rest[0], encoding="utf-8").read()
        errs = check_proof(text, rest[1] if len(rest) > 1 else None)
        print("ACCEPTED" if not errs else "\n".join(errs))
        return 0 if not errs else 2
    print(usage); return 1


if __name__ == "__main__":
    import sys
    sys.exit(_main(sys.argv))
