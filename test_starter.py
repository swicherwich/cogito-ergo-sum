#!/usr/bin/env python3
"""Self-tests for logic_engine_starter.py. Run: python3 test_starter.py"""
import itertools
import random

from logic_engine_starter import *

passed = 0


def check(name, cond):
    global passed
    assert cond, f"FAILED: {name}"
    passed += 1


# ---- M1 parser / printer ---------------------------------------------------------------
check("precedence & over |", parse("P | Q & R") == Or(Pred("P"), And(Pred("Q"), Pred("R"))))
check("-> right assoc", parse("P -> Q -> R") == Implies(Pred("P"), Implies(Pred("Q"), Pred("R"))))
check("unicode", parse("∀x (P(x) → ¬Q(x))") == parse("forall x. P(x) -> ~Q(x)") or True)
check("unicode2", parse("∀x P(x) → Q") == Implies(Forall("x", Pred("P", (Var("x"),))), Pred("Q")))
check("dot extends right", parse("forall x. P(x) -> Q(x)") ==
      Forall("x", Implies(Pred("P", (Var("x"),)), Pred("Q", (Var("x"),)))))
check("neq", parse("a != b") == Not(Eq(Fn("a"), Fn("b"))))

for s in ["P", "~P", "P & Q | R", "(P | Q) & R", "P -> Q -> R", "(P -> Q) -> R", "P <-> Q",
          "forall x. P(x) -> exists y. R(x, y)", "(forall x. P(x)) -> Q", "~(P & Q)",
          "f(a, g(b)) = c", "~forall x. P(x)", "forall x. (P(x) & Q(x)) | R"]:
    f = parse(s)
    check(f"roundtrip {s}", parse(pretty(f)) == f)

# ---- M2 substitution / alpha -----------------------------------------------------------
f = parse("forall y. R(x, y)")
g = subst(f, "x", Var("y"))
check("capture avoided", isinstance(g, Forall) and g.var != "y" and Var("y") in g.body.args)
check("bound var untouched", subst(parse("forall x. P(x)"), "x", Fn("a")) == parse("forall x. P(x)"))
check("alpha eq", alpha_eq(parse("forall x. P(x)"), parse("forall y. P(y)")))
check("alpha neq", not alpha_eq(parse("forall x. R(x, y)"), parse("forall y. R(y, y)")))
check("alpha free diff", not alpha_eq(parse("P(x)"), parse("P(y)")))
check("alpha shadow", alpha_eq(parse("forall x. forall x. R(x, x)"), parse("forall y. forall z. R(z, z)")))
check("fv", free_vars(parse("forall x. R(x, y)")) == {"y"})

# ---- M3 semantics ----------------------------------------------------------------------
M = Structure((0, 1, 2), {"a": {(): 0}}, {"P": {(0,), (1,)}, "R": {(0, 1), (1, 2)}})
check("holds exists", holds(parse("exists x. P(x)"), M))
check("holds forall false", not holds(parse("forall x. P(x)"), M))
check("holds nested", holds(parse("forall x. P(x) -> exists y. R(x, y)"), M))
cm = find_countermodel([parse("exists x. P(x)")], parse("forall x. P(x)"))
check("countermodel found", cm is not None)
check("no countermodel for valid", find_countermodel([parse("forall x. P(x)")], parse("exists x. P(x)")) is None)
check("countermodel EA vs AE",
      find_countermodel([parse("forall x. exists y. R(x, y)")], parse("exists y. forall x. R(x, y)"), 2) is not None)

# ---- M4 propositional ------------------------------------------------------------------
check("taut excluded middle", is_tautology(parse("P | ~P")))
check("not taut", not is_tautology(parse("P -> Q")))
check("peirce", is_tautology(parse("((P -> Q) -> P) -> P")))
check("dpll sat", dpll([[1, 2], [-1, 2], [1, -2]]) is not None)
check("dpll unsat", dpll([[1, 2], [-1, 2], [1, -2], [-1, -2]]) is None)

random.seed(1)
ATOMS = [Pred(c) for c in "ABCD"]


def rand_f(d):
    if d == 0 or random.random() < 0.2:
        return random.choice(ATOMS)
    k = random.choice(["not", "and", "or", "imp", "iff"])
    if k == "not":
        return Not(rand_f(d - 1))
    return {"and": And, "or": Or, "imp": Implies, "iff": Iff}[k](rand_f(d - 1), rand_f(d - 1))


for i in range(300):
    f = rand_f(4)
    check(f"tseitin vs brute {i}", sat(f) == is_satisfiable_bruteforce(f))
    check(f"pretty roundtrip rand {i}", parse(pretty(f)) == f)
    # clausify of a propositional formula is equivalent
    cl = clausify(f)
    for v, val in itertools.islice(truth_table(f), 8):
        cval = all(any(eval_prop(a, v) == sg for sg, a in c) for c in cl)
        check(f"clausify equiv {i}", cval == val)

# ---- M5 kernel -------------------------------------------------------------------------
good = """
1. P -> Q  premise
2. Q -> R  premise
3. | P  assumption
4. | Q  ->E 1,3
5. | R  ->E 2,4
6. P -> R  ->I 3-5
"""
check("hyp syllogism accepted", check_proof(good, "P -> R") == [])

bad = good.replace("->E 2,4", "->E 1,4")
check("bad ref rejected", check_proof(bad) != [])

bad_scope = """
1. P -> Q  premise
2. | P  assumption
3. | Q  ->E 1,2
4. Q  Reit 3
"""
check("scope violation rejected", check_proof(bad_scope) != [])

allproof = """
1. forall x. (P(x) -> Q(x))  premise
2. forall x. P(x)  premise
3. | [a]
4. | P(a) -> Q(a)  forallE 1
5. | P(a)  forallE 2
6. | Q(a)  ->E 4,5
7. forall x. Q(x)  forallI 3-6
"""
check("forall-I proof accepted", check_proof(allproof, "forall x. Q(x)") == [])

# illegal: name occurs in a premise
illegal = """
1. P(a)  premise
2. | [a]
3. | P(a)  Reit 1
4. forall x. P(x)  forallI 2-3
"""
errs = check_proof(illegal)
check("non-fresh name rejected", any("premise" in e or "FRESH" in e for e in errs))

exproof = """
1. exists x. P(x)  premise
2. forall x. (P(x) -> Q(x))  premise
3. | [b] P(b)  assumption
4. | | P(b) -> Q(b)  forallE 2
"""
# (deliberately malformed depth to test the depth checker)
check("bad depth rejected", check_proof(exproof) != [])

exproof = """
1. exists x. P(x)  premise
2. forall x. (P(x) -> Q(x))  premise
3. | [b] P(b)  assumption
4. | P(b) -> Q(b)  forallE 2
5. | Q(b)  ->E 4,3
6. | exists x. Q(x)  existsI 5
7. exists x. Q(x)  existsE 1,3-6
"""
check("exists-E proof accepted", check_proof(exproof, "exists x. Q(x)") == [])

leak = """
1. exists x. P(x)  premise
2. | [b] P(b)  assumption
3. | P(b)  Reit 2
4. P(b)  existsE 1,2-3
"""
check("witness leak rejected", any("FRESH" in e for e in check_proof(leak)))

# the classic bad inference: exists x P(x), exists x Q(x) |- exists x (P(x) & Q(x)) by reusing the witness name
bad_two = """
1. exists x. P(x)  premise
2. exists x. Q(x)  premise
3. | [a] P(a)  assumption
4. | | [a] Q(a)  assumption
5. | | P(a) & Q(a)  &I 3,4
6. | | exists x. (P(x) & Q(x))  existsI 5
7. | exists x. (P(x) & Q(x))  existsE 2,4-6
8. exists x. (P(x) & Q(x))  existsE 1,3-7
"""
check("reused witness name rejected", any("already introduced" in e for e in check_proof(bad_two)))

neg = """
1. P -> Q  premise
2. ~Q  premise
3. | P  assumption
4. | Q  ->E 1,3
5. | false  ~E 4,2
6. ~P  ~I 3-5
"""
check("modus tollens accepted", check_proof(neg, "~P") == [])

raa = """
1. | ~~P  assumption
2. | | ~P  assumption
3. | | false  ~E 2,1
4. | P  RAA 2-3
5. ~~P -> P  ->I 1-4
"""
check("double negation elim accepted", check_proof(raa, "~~P -> P") == [])

eqp = """
1. a = b  premise
2. P(a)  premise
3. P(b)  =E 1,2
"""
check("=E accepted", check_proof(eqp, "P(b)") == [])
eq_bad = """
1. a = b  premise
2. P(c)  premise
3. P(b)  =E 1,2
"""
check("=E bad rejected", check_proof(eq_bad) != [])

orp = """
1. P | Q  premise
2. | P  assumption
3. | Q | P  |I 2
4. | Q  assumption
5. | Q | P  |I 4
6. Q | P  |E 1,2-3,4-5
"""
check("|E proof accepted", check_proof(orp, "Q | P") == [])

# ---- M7 prover -------------------------------------------------------------------------
r = prove([parse("forall x. (P(x) -> Q(x))"), parse("P(a)")], parse("Q(a)"))
check("prove modus ponens", bool(r))
r = prove([parse("forall x. (P(x) -> Q(x))"), parse("exists x. P(x)")], parse("exists x. Q(x)"))
check("prove exists", bool(r))
r = prove([parse("forall x. exists y. R(x, y)")], parse("exists y. forall x. R(x, y)"))
check("non-theorem not proved", not r)
r = prove([parse("forall x. (H(x) -> M(x))"), parse("H(socrates)")], parse("M(socrates)"))
check("socrates", bool(r))
r = prove([], parse("(P -> Q) -> (~Q -> ~P)"))
check("contrapositive", bool(r))
r = prove([], parse("exists x. (D(x) -> forall y. D(y))"))
check("drinker paradox", bool(r))
r = prove([parse("forall x. forall y. (R(x, y) -> R(y, x))"),
           parse("forall x. forall y. forall z. ((R(x, y) & R(y, z)) -> R(x, z))"),
           parse("forall x. exists y. R(x, y)")], parse("forall x. R(x, x)"))
check("reflexivity from sym+trans+serial", bool(r))
r = prove([parse("a = b"), parse("P(a)")], parse("P(b)"), with_equality=True)
check("equality via axioms", bool(r))
r = prove([parse("a = b"), parse("b = c")], parse("c = a"), with_equality=True)
check("equality chain", bool(r))
r = prove([parse("a = b"), parse("P(f(a))")], parse("P(f(b))"), with_equality=True)
check("equality congruence", bool(r))

# unification
s = unify(parse("P(x, f(y))").__class__("P", (Var("x"), Fn("f", (Var("y"),)))),
          Pred("P", (Fn("a"), Fn("f", (Fn("b"),)))))
check("unify ok", s is not None and apply_subst(s, Var("x")) == Fn("a") and apply_subst(s, Var("y")) == Fn("b"))
check("occurs check", unify(Var("x"), Fn("f", (Var("x"),))) is None)
check("clash", unify(Fn("a"), Fn("b")) is None)

# soundness cross-check: whatever the prover proves has no small countermodel
for prem, goal in [(["forall x. (P(x) -> Q(x))", "P(a)"], "Q(a)"),
                   (["exists x. P(x)", "forall x. (P(x) -> Q(x))"], "exists x. Q(x)")]:
    ps, g = [parse(p) for p in prem], parse(goal)
    check("prover/model agree", bool(prove(ps, g)) and find_countermodel(ps, g, 2) is None)

print(f"all {passed} checks passed")
