# Mastering Mathematical Logic: Complete Edition

### From absolute zero to proofs, predicate logic, metatheory, and a working logic engine

---

## How to use this book

This is a self-study book. It was written for a reader who **may know nothing about logic**: not the symbols, not the vocabulary, not the habits of mathematical writing. Everything is explained before it is used. If you already know the connectives (∧, ∨, ¬, →) and can fill in truth tables, you can skip parts of Part Zero, but you are encouraged to skim them: many "obvious" things (what exactly a *proposition* is, why `→` behaves oddly, what a variable really is) are where later confusion starts.

**The book has four layers.**

| Layer | What it is | Where |
|---|---|---|
| **Part Zero** | Mathematics and reasoning from scratch: what an argument is, mathematical language, sets, functions, relations, sequences, trees; a complete atlas of every symbol and its variants; the many notations and proof formats used in textbooks and tools | Chapters Z1–Z5 |
| **Core chapters** | The main line of the course: ideas, worked examples, strategy | Chapters 0–9, sections numbered 1.1, 1.2, … |
| **"Complete detail" companions** | At the end of each chapter's numbered sections, a companion that revisits the chapter from zero: every definition, every symbol and variant, every rule, every format, more examples and a quick-check with answers | Sections 1.8, 2.9, 3.8, 4.7, 5.14, 6.7, 7.9, 8.8 |
| **Problems and appendices** | Graded problems at the end of each chapter; rule sheets; a mistakes catalogue; hints and solutions; a glossary; a typing and tool-syntax cheat sheet | "Problems for Chapter N"; Appendices A–E |

**Suggested reading orders.**

- *Complete beginner:* Part Zero (Z1 → Z5), then for each chapter: core sections, companion, problems.
- *You know truth tables but cannot prove anything:* skim Z1–Z3, read Z4 once, then Chapter 1 quickly, and slow down at Chapter 2.
- *You want only the practical engine:* Chapters 1, 3, 7, 8 (plus the companions 7.9 and 8.8), consulting others when needed.
- *You are stuck on a symbol or word:* Z4 (symbols) or Appendix D (glossary). *Stuck on how to type or run something:* Appendix E.

**Structure of every chapter:** ideas, then worked examples, then the companion, then problems.

**Difficulty marks on problems:**
- ★ warm-up, should take a few minutes
- ★★ standard, the core of the course
- ★★★ challenging, expect to get stuck and come back

**Rules for effective study:**
1. **Write proofs on paper.** Reading a proof and producing a proof are different skills. Only the second one is the goal.
2. **Struggle first.** Spend at least 15-20 minutes on a problem before opening the hints in Appendix C.
3. **Justify every line.** In formal proofs, each line gets a rule name and line references. In informal proofs, each sentence should follow from earlier ones for a reason you could state.
4. **Redo, don't re-read.** A week later, redo a proof you solved from a blank page. If you can't, you memorized it instead of understanding it.
5. **Keep an error log.** Whenever you make a mistake (wrong quantifier order, illegal ∀-introduction, circular reasoning), write it down. Your mistakes are very repetitive, and the log makes them visible.
6. **Build the project in parallel** (Chapter 8). Implementing a rule is the strictest test of whether you understood it.
7. **Use the quick-checks.** Each companion ends with a quick-check with answers. Cover the answer, write yours, then compare.

**Reading conventions in this book.**
- `Code and formulas typed on a keyboard` appear in monospace; mathematical formulas are usually in ordinary text with symbols such as ∀x (P(x) → Q(x)).
- *Italics* introduce a term at its definition. **Bold** marks something you must not forget.
- "Section 3.5" means the numbered section in the core text; "3.8.5" means subsection 5 of the Chapter 3 companion (section 3.8).
- Where a statement was checked by computer (truth tables, the SAT solver, Z3, the Chapter 8 test-suite), the text says so.

**Companion files.** The Chapter 8 starter kit is shipped as two files next to this document: `logic_engine_starter.py` (the engine) and `test_starter.py` (its 2,520 checks). Section 8.8 explains how to use them.

**Suggested pace:** about 12 weeks at 6-8 hours per week for the core text (Chapter 9, Section 9.3); about 16 weeks if you start from zero and read all of Part Zero and the companions (Section 9.4).

---

## Table of contents

*Click an entry to jump to it. Chapters are in bold; their sections are indented below.*

- **[PART ZERO. Starting from absolute zero](#part-zero-starting-from-absolute-zero)**
- **[Chapter Z1. What logic is, and what we are trying to do](#chapter-z1-what-logic-is-and-what-we-are-trying-to-do)**
  - [Z1.1 Reasoning, statements and arguments](#z11-reasoning-statements-and-arguments)
  - [Z1.2 Validity: the central idea](#z12-validity-the-central-idea)
  - [Z1.3 Form versus content](#z13-form-versus-content)
  - [Z1.4 Kinds of reasoning](#z14-kinds-of-reasoning)
  - [Z1.5 Why make logic formal?](#z15-why-make-logic-formal)
  - [Z1.6 The three pillars](#z16-the-three-pillars)
  - [Z1.7 A map of the field](#z17-a-map-of-the-field)
  - [Z1.8 A very short history](#z18-a-very-short-history)
  - [Z1.9 Try it](#z19-try-it)
- **[Chapter Z2. The language of mathematics](#chapter-z2-the-language-of-mathematics)**
  - [Z2.1 Kinds of mathematical text](#z21-kinds-of-mathematical-text)
  - [Z2.2 A dictionary of mathematical English](#z22-a-dictionary-of-mathematical-english)
  - [Z2.3 The common shapes of mathematical statements](#z23-the-common-shapes-of-mathematical-statements)
  - [Z2.4 Anatomy of a proof (a first complete example, narrated)](#z24-anatomy-of-a-proof-a-first-complete-example-narrated)
  - [Z2.5 How to read mathematics](#z25-how-to-read-mathematics)
  - [Z2.6 A note on notation habits](#z26-a-note-on-notation-habits)
  - [Z2.7 Try it](#z27-try-it)
- **[Chapter Z3. The mathematics you need first: sets, numbers, functions, relations, strings, trees](#chapter-z3-the-mathematics-you-need-first-sets-numbers-functions-relations-strings-trees)**
  - [Z3.1 Sets](#z31-sets)
  - [Z3.2 Numbers and arithmetic notation](#z32-numbers-and-arithmetic-notation)
  - [Z3.3 Functions](#z33-functions)
  - [Z3.4 Relations](#z34-relations)
  - [Z3.5 Sequences, strings, alphabets, languages](#z35-sequences-strings-alphabets-languages)
  - [Z3.6 Trees and recursive (inductive) definitions](#z36-trees-and-recursive-inductive-definitions)
  - [Z3.7 Try it](#z37-try-it)
- **[Chapter Z4. The Symbol Atlas: every sign you will meet](#chapter-z4-the-symbol-atlas-every-sign-you-will-meet)**
  - [Z4.1 The core connectives (propositional logic)](#z41-the-core-connectives-propositional-logic)
  - [Z4.2 Quantifiers, binders, and related symbols (predicate logic)](#z42-quantifiers-binders-and-related-symbols-predicate-logic)
  - [Z4.3 Symbols of consequence, proof and metalanguage](#z43-symbols-of-consequence-proof-and-metalanguage)
  - [Z4.4 The many signs of "equals", "defined as", and "equivalent"](#z44-the-many-signs-of-equals-defined-as-and-equivalent)
  - [Z4.5 Sets, functions, relations](#z45-sets-functions-relations)
  - [Z4.6 Arithmetic and number-theory symbols](#z46-arithmetic-and-number-theory-symbols)
  - [Z4.7 Brackets, punctuation and layout](#z47-brackets-punctuation-and-layout)
  - [Z4.8 Letters: the conventional use of Latin and Greek symbols](#z48-letters-the-conventional-use-of-latin-and-greek-symbols)
  - [Z4.9 Symbols with multiple meanings: the ambiguity table](#z49-symbols-with-multiple-meanings-the-ambiguity-table)
  - [Z4.10 Symbols of other logics (preview)](#z410-symbols-of-other-logics-preview)
  - [Z4.11 Reading formulas aloud](#z411-reading-formulas-aloud)
- **[Chapter Z5. Dialects and formats: the same logic in many costumes](#chapter-z5-dialects-and-formats-the-same-logic-in-many-costumes)**
  - [Z5.1 Notation dialects for formulas](#z51-notation-dialects-for-formulas)
  - [Z5.2 Proof formats: an overview](#z52-proof-formats-an-overview)
  - [Z5.3 The running example in every format](#z53-the-running-example-in-every-format)
  - [Z5.4 Comparison: which format when?](#z54-comparison-which-format-when)
  - [Z5.5 Translating between formats: a cheat table](#z55-translating-between-formats-a-cheat-table)
  - [Z5.6 Quick-check](#z56-quick-check)
- **[Chapter 0. The big picture](#chapter-0-the-big-picture)**
  - [0.1 Two sides of logic](#01-two-sides-of-logic)
  - [0.2 Why a proof is a different skill from a truth table](#02-why-a-proof-is-a-different-skill-from-a-truth-table)
  - [0.3 Three levels](#03-three-levels)
  - [0.4 Object language vs. metalanguage](#04-object-language-vs-metalanguage)
- **[Chapter 1. Propositional logic: precise foundations](#chapter-1-propositional-logic-precise-foundations)**
  - [1.1 Syntax: formulas are defined inductively](#11-syntax-formulas-are-defined-inductively)
  - [1.2 Semantics](#12-semantics)
  - [1.3 Implication in depth](#13-implication-in-depth)
  - [1.4 The laws you must know cold](#14-the-laws-you-must-know-cold)
  - [1.5 Normal forms](#15-normal-forms)
  - [1.6 Functional completeness](#16-functional-completeness)
  - [1.7 Why truth tables are not enough](#17-why-truth-tables-are-not-enough)
  - [1.8 Chapter 1 in complete detail (the from-zero companion)](#18-chapter-1-in-complete-detail-the-from-zero-companion)
  - [Problems for Chapter 1](#problems-for-chapter-1)
- **[Chapter 2. Natural deduction for propositional logic](#chapter-2-natural-deduction-for-propositional-logic)**
  - [2.1 What is a proof?](#21-what-is-a-proof)
  - [2.2 Reading and writing Fitch proofs](#22-reading-and-writing-fitch-proofs)
  - [2.3 The rules](#23-the-rules)
  - [2.4 How to find proofs: the strategy](#24-how-to-find-proofs-the-strategy)
  - [2.5 Worked examples](#25-worked-examples)
  - [2.6 Useful derived results](#26-useful-derived-results)
  - [2.7 Classical vs. intuitionistic logic](#27-classical-vs-intuitionistic-logic)
  - [2.8 Common mistakes](#28-common-mistakes)
  - [2.9 Chapter 2 in complete detail (the from-zero companion)](#29-chapter-2-in-complete-detail-the-from-zero-companion)
  - [Problems for Chapter 2](#problems-for-chapter-2)
- **[Chapter 3. Predicate logic: language, translation, semantics](#chapter-3-predicate-logic-language-translation-semantics)**
  - [3.1 Why propositional logic is not enough](#31-why-propositional-logic-is-not-enough)
  - [3.2 Syntax](#32-syntax)
  - [3.3 Free and bound variables](#33-free-and-bound-variables)
  - [3.4 The art of translation](#34-the-art-of-translation)
  - [3.5 Semantics: structures and truth](#35-semantics-structures-and-truth)
  - [3.6 Quantifier laws](#36-quantifier-laws)
  - [3.7 Prenex normal form](#37-prenex-normal-form)
  - [3.8 Chapter 3 in complete detail (the from-zero companion)](#38-chapter-3-in-complete-detail-the-from-zero-companion)
  - [Problems for Chapter 3](#problems-for-chapter-3)
- **[Chapter 4. Natural deduction for predicate logic](#chapter-4-natural-deduction-for-predicate-logic)**
  - [4.1 The four quantifier rules](#41-the-four-quantifier-rules)
  - [4.2 What "fresh" means, and why it matters](#42-what-fresh-means-and-why-it-matters)
  - [4.3 Worked examples](#43-worked-examples)
  - [4.4 Equality](#44-equality)
  - [4.5 Proof strategy for quantifiers](#45-proof-strategy-for-quantifiers)
  - [4.6 Common mistakes](#46-common-mistakes)
  - [4.7 Chapter 4 in complete detail (the from-zero companion)](#47-chapter-4-in-complete-detail-the-from-zero-companion)
  - [Problems for Chapter 4](#problems-for-chapter-4)
- **[Chapter 5. Mathematical proof technique](#chapter-5-mathematical-proof-technique)**
  - [5.1 The dictionary: logic to prose](#51-the-dictionary-logic-to-prose)
  - [5.2 Direct proof](#52-direct-proof)
  - [5.3 Proof by contrapositive](#53-proof-by-contrapositive)
  - [5.4 Proof by contradiction](#54-proof-by-contradiction)
  - [5.5 Proof by cases](#55-proof-by-cases)
  - [5.6 Existence, uniqueness, and counterexamples](#56-existence-uniqueness-and-counterexamples)
  - [5.7 Proofs with nested quantifiers (ε-δ style)](#57-proofs-with-nested-quantifiers-ε-δ-style)
  - [5.8 Mathematical induction](#58-mathematical-induction)
  - [5.9 Strong induction](#59-strong-induction)
  - [5.10 Structural induction](#510-structural-induction)
  - [5.11 Common induction errors](#511-common-induction-errors)
  - [5.12 Sets and functions: where logic meets mathematics](#512-sets-and-functions-where-logic-meets-mathematics)
  - [5.13 Writing proofs well](#513-writing-proofs-well)
  - [5.14 Chapter 5 in complete detail (the from-zero companion)](#514-chapter-5-in-complete-detail-the-from-zero-companion)
  - [Problems for Chapter 5](#problems-for-chapter-5)
- **[Chapter 6. Metatheory: what logic can and cannot do](#chapter-6-metatheory-what-logic-can-and-cannot-do)**
  - [6.1 Soundness and completeness](#61-soundness-and-completeness)
  - [6.2 Consistency, theories, and compactness](#62-consistency-theories-and-compactness)
  - [6.3 Löwenheim-Skolem](#63-löwenheim-skolem)
  - [6.4 Decidability](#64-decidability)
  - [6.5 Gödel's incompleteness theorems](#65-gödels-incompleteness-theorems)
  - [6.6 Other semantic and syntactic notions worth knowing](#66-other-semantic-and-syntactic-notions-worth-knowing)
  - [6.7 Chapter 6 in complete detail (the from-zero companion)](#67-chapter-6-in-complete-detail-the-from-zero-companion)
  - [Problems for Chapter 6](#problems-for-chapter-6)
- **[Chapter 7. Automated reasoning: from formulas to resolution](#chapter-7-automated-reasoning-from-formulas-to-resolution)**
  - [7.1 The refutation idea](#71-the-refutation-idea)
  - [7.2 Propositional resolution and DPLL](#72-propositional-resolution-and-dpll)
  - [7.3 From first-order formulas to clauses](#73-from-first-order-formulas-to-clauses)
  - [7.4 Unification](#74-unification)
  - [7.5 First-order resolution](#75-first-order-resolution)
  - [7.6 Search strategy and why provers can run forever](#76-search-strategy-and-why-provers-can-run-forever)
  - [7.7 The Herbrand connection (why it works)](#77-the-herbrand-connection-why-it-works)
  - [7.9 Chapter 7 in complete detail (the from-zero companion)](#79-chapter-7-in-complete-detail-the-from-zero-companion)
  - [Problems for Chapter 7](#problems-for-chapter-7)
- **[Chapter 8. Project: build your own logic engine](#chapter-8-project-build-your-own-logic-engine)**
  - [8.1 Goal and scope](#81-goal-and-scope)
  - [8.2 Architecture](#82-architecture)
  - [8.3 Milestones](#83-milestones)
  - [8.4 Core data structures (Python)](#84-core-data-structures-python)
  - [8.5 Designing the proof checker (the kernel)](#85-designing-the-proof-checker-the-kernel)
  - [8.6 Testing strategy](#86-testing-strategy)
  - [8.7 Extensions](#87-extensions)
  - [8.8 Chapter 8 in complete detail: the starter kit](#88-chapter-8-in-complete-detail-the-starter-kit)
- **[Chapter 9. Beyond the basics, resources, and a 12-week plan](#chapter-9-beyond-the-basics-resources-and-a-12-week-plan)**
  - [9.1 Where to go next](#91-where-to-go-next)
  - [9.2 Resources](#92-resources)
  - [9.3 The 12-week plan](#93-the-12-week-plan)
  - [9.4 Pace for the Complete Edition (starting from absolute zero)](#94-pace-for-the-complete-edition-starting-from-absolute-zero)
- **[Appendix A. Rule cheat sheet](#appendix-a-rule-cheat-sheet)**
  - [A.1 Natural deduction: propositional rules](#a1-natural-deduction-propositional-rules)
  - [A.2 Quantifier and equality rules](#a2-quantifier-and-equality-rules)
  - [A.3 Proof-finding strategy at a glance](#a3-proof-finding-strategy-at-a-glance)
  - [A.4 Translation patterns](#a4-translation-patterns)
  - [A.5 Key equivalences](#a5-key-equivalences)
  - [A.6 Symbol glossary](#a6-symbol-glossary)
- **[Appendix B. Common mistakes catalog](#appendix-b-common-mistakes-catalog)**
  - [Propositional logic and proofs](#propositional-logic-and-proofs)
  - [Predicate logic](#predicate-logic)
  - [Informal mathematical proofs](#informal-mathematical-proofs)
  - [Metatheory](#metatheory)
  - [Engineering the logic engine](#engineering-the-logic-engine)
- **[Appendix C. Hints and solutions](#appendix-c-hints-and-solutions)**
  - [Chapter 1](#chapter-1)
  - [Chapter 2](#chapter-2)
  - [Chapter 3](#chapter-3)
  - [Chapter 4](#chapter-4)
  - [Chapter 5](#chapter-5)
  - [Chapter 6](#chapter-6)
  - [Chapter 7](#chapter-7)
- **[Appendix D. Glossary of logic terms (A–Z)](#appendix-d-glossary-of-logic-terms-az)**
  - [A](#a)
  - [B](#b)
  - [C](#c)
  - [D](#d)
  - [E](#e)
  - [F](#f)
  - [G](#g)
  - [H](#h)
  - [I](#i)
  - [K](#k)
  - [L](#l)
  - [M](#m)
  - [N](#n)
  - [O](#o)
  - [P](#p)
  - [Q](#q)
  - [R](#r)
  - [S](#s)
  - [T](#t)
  - [U](#u)
  - [V](#v)
  - [W–Z](#wz)
- **[Appendix E. Typing symbols and tool syntax: a cheat sheet](#appendix-e-typing-symbols-and-tool-syntax-a-cheat-sheet)**
  - [E.1 Typing logic symbols](#e1-typing-logic-symbols)
  - [E.2 LaTeX in practice](#e2-latex-in-practice)
  - [E.3 One formula in every syntax](#e3-one-formula-in-every-syntax)
  - [E.4 The connectives in every syntax](#e4-the-connectives-in-every-syntax)
  - [E.5 Z3 from Python (tested)](#e5-z3-from-python-tested)
  - [E.6 SMT-LIB (tested)](#e6-smt-lib-tested)
  - [E.7 DIMACS CNF for SAT solvers](#e7-dimacs-cnf-for-sat-solvers)
  - [E.8 TPTP and Prover9 files](#e8-tptp-and-prover9-files)
  - [E.9 Lean 4 cheat sheet](#e9-lean-4-cheat-sheet)
  - [E.10 Coq / Rocq cheat sheet](#e10-coq--rocq-cheat-sheet)
  - [E.11 Prolog (Horn clauses in practice)](#e11-prolog-horn-clauses-in-practice)
  - [E.12 Choosing a tool](#e12-choosing-a-tool)

---

# PART ZERO. Starting from absolute zero

*This part assumes nothing. If a word, a symbol, or a habit of mathematical writing appears later in the course, it is explained here first. Read it in order the first time. Later you can use it as a reference: Chapter Z4 is a complete atlas of symbols, and Appendix D is an A-Z glossary.*

---

# Chapter Z1. What logic is, and what we are trying to do

## Z1.1 Reasoning, statements and arguments

Every day you move from things you accept to new things you accept:

> "The shop closes at 6. It is now 6:30. So the shop is closed."

You did not look at the shop. You *reasoned*. **Logic is the study of which such moves are correct, and why.**

To study reasoning precisely we need names for its parts.

**A statement** (also called a *proposition* or *declarative sentence*) is a sentence that claims something is the case, so that it makes sense to ask "is it true or false?". Examples:

| Statement | Truth value |
|---|---|
| "Paris is the capital of France." | true |
| "2 + 2 = 5" | false |
| "There are infinitely many prime numbers." | true |
| "Every even number greater than 2 is the sum of two primes." | nobody knows yet (Goldbach's conjecture), but it is *either* true *or* false |
| "It is raining in Lviv right now." | true or false depending on the moment |

A statement has exactly one **truth value**: **true** or **false**. (In classical logic, which is the main subject of this course, there is no third option and no "both".)

**Things that are not statements:**

| Sentence | Why not |
|---|---|
| "What time is it?" | a question, it does not claim anything |
| "Close the door!" | a command |
| "Wow!" | an exclamation |
| "x is greater than 3." | its truth depends on what x is (an *open sentence*, see Z2) |
| "This sentence is false." | it cannot consistently be assigned true or false (the *liar paradox*) |

**An argument** is a collection of statements in which some, the **premises**, are offered as support for another, the **conclusion**. Words that often signal a conclusion: *therefore, thus, hence, so, consequently, it follows that*. Words that often signal a premise: *because, since, given that, for, as*.

> Premise 1: All humans are mortal.
> Premise 2: Socrates is a human.
> Conclusion: Therefore, Socrates is mortal.

## Z1.2 Validity: the central idea

The most important concept in all of logic:

> **An argument is *valid* when it is impossible for all the premises to be true and the conclusion false at the same time.**

Equivalently: *if* the premises were all true, the conclusion would *have to be* true. Validity is about the **connection** between premises and conclusion, not about whether the premises are actually true.

Study these four arguments carefully.

| # | Argument | Premises true? | Conclusion true? | Valid? |
|---|---|---|---|---|
| 1 | All dogs are mammals. Rex is a dog. So Rex is a mammal. | yes | yes | **valid** |
| 2 | All dogs are reptiles. Rex is a dog. So Rex is a reptile. | no (first) | no | **valid** (!) |
| 3 | All dogs are mammals. Rex is a mammal. So Rex is a dog. | yes | maybe not | **invalid** |
| 4 | Some cats are black. Tom is a cat. So Tom is black. | yes | maybe not | **invalid** |

Argument 2 is valid *even though everything in it is false*. The shape is perfect: if all dogs really were reptiles, and Rex really were a dog, then Rex would have to be a reptile. Argument 3 is invalid even though its premises and conclusion might all be true: the premises do not *force* the conclusion (Rex could be a cat, which is also a mammal).

**Soundness of an argument** (a different, everyday word that logicians also use): an argument is *sound* if it is valid **and** all its premises are true. A sound argument guarantees a true conclusion. Argument 1 is sound. Argument 2 is valid but unsound.

> **Warning on vocabulary.** In everyday speech "valid" is used loosely ("that is a valid point"). In logic it has *only* the meaning above, and it applies to **arguments**, never to single statements. Single statements are called *true*/*false* (in one situation) or *logically true*/*tautologies* (in all situations). We will make this precise in Chapters 1 and 3. Also, in Chapter 6, "soundness" gets a second, technical meaning for proof systems.

## Z1.3 Form versus content

Why is argument 1 valid? Look at what happens when we *erase the specific words* and keep only the pattern:

```
All A are B.
x is an A.
Therefore x is a B.
```

Any argument with this shape is valid, whatever A, B, and x stand for:
- A = "birds", B = "animals", x = "Tweety": valid.
- A = "prime numbers greater than 2", B = "odd numbers", x = "17": valid.

Logic is the study of **forms** (patterns, schemas) of arguments. We replace words by **letters** (variables) so that the pattern is what remains. This is the reason logic uses symbols at all: not to look scary, but to isolate the pattern from the subject matter. A form is **valid** when *every* argument of that form is valid.

**Invalid form** (affirming the consequent):
```
If A then B.
B.
Therefore A.
```
Counterexample: "If it is raining, the street is wet. The street is wet. Therefore it is raining." (Perhaps a street cleaner passed by.)

**A counterexample to an argument form** is an argument of that exact form with true premises and a false conclusion. One counterexample proves invalidity. This idea (find a world where premises are true and conclusion is false) will return as the *countermodel* in Chapter 3.

## Z1.4 Kinds of reasoning

| Kind | What it does | Example | Guarantee |
|---|---|---|---|
| **Deduction** | conclusion is *forced* by premises | "All primes > 2 are odd. 17 is a prime > 2. So 17 is odd." | If premises true, conclusion certainly true |
| **Induction** | generalizes from observed cases | "Every swan I saw was white, so all swans are white." | Probable, not certain (and this one is false: black swans exist) |
| **Abduction** | infers the best explanation | "The grass is wet, so it probably rained." | Plausible, not certain |

**Mathematical logic is about deduction.** (Do not confuse *mathematical induction*, a deductive proof technique in Chapter 5, with inductive reasoning.)

## Z1.5 Why make logic formal?

Natural language is wonderful but ambiguous.

| Sentence | Two readings |
|---|---|
| "I saw the man with the telescope." | I used a telescope / the man had a telescope |
| "All the students did not pass." | none passed / not all passed |
| "Tea or coffee?" | one of them (exclusive) / either or both |
| "Every student reads some book." | each student has their own book / one particular book is read by all |
| "If you mow the lawn I'll give you $5." | (also implies: otherwise no $5?) |

To reason with total certainty we need a language where each sentence has **exactly one meaning**. That is a **formal language**: a collection of symbols, together with exact rules for which strings of symbols count as legitimate sentences (**syntax**), what each sentence means (**semantics**), and how to derive sentences from others using mechanical rules (**proof theory**, or **deduction**).

Advantages of formalization:
1. **No ambiguity.** One formula, one meaning.
2. **Checkability.** A proof becomes a finite object that a program can verify, step by step, with no understanding at all. (This is how proof assistants such as Lean work.)
3. **Generality.** The same rules apply to arithmetic, geometry, software specifications, legal contracts, circuit design.
4. **Theorems about reasoning itself.** Once reasoning is a mathematical object, we can prove things *about* it: that it is correct, that it is complete, that some questions cannot be settled by any algorithm (Chapter 6).

## Z1.6 The three pillars

Every logical system we study has three components. Keep this triangle in mind for the entire course:

```
                SYNTAX
        (symbols, formulas, rules
         for what is well-formed)
               /        \
              /          \
     SEMANTICS ────────── PROOF THEORY
   (meaning: truth,       (derivations:
    models, ⊨)             rules, proofs, ⊢)
```

| Pillar | Question it answers | Chapters |
|---|---|---|
| **Syntax** | Which strings of symbols are sentences? | 1.1, 3.2, Z4 |
| **Semantics** | When is a sentence true? What follows from what *in meaning*? | 1.2, 3.5 |
| **Proof theory** | What can be *derived* by rules, without looking at meaning? | 2, 4, 7 |

The deepest results (soundness and completeness, Chapter 6) say that the last two pillars agree.

## Z1.7 A map of the field

| Branch | Studies | Appears in |
|---|---|---|
| **Propositional logic** | statements combined by *and, or, not, if...then* | Ch. 1-2 |
| **Predicate / first-order logic** | objects, properties, relations, "for all", "there exists" | Ch. 3-4 |
| **Proof techniques** | how mathematicians actually prove things | Ch. 5 |
| **Model theory** | structures that make sentences true | Ch. 3, 6 |
| **Proof theory** | proofs as mathematical objects | Ch. 2, 4, 6 |
| **Computability** | what algorithms can and cannot do | Ch. 6 |
| **Set theory** | the foundation in which mathematics is formalized | Z3, Ch. 5-6 |
| **Automated reasoning** | making computers prove things | Ch. 7-8 |
| **Non-classical logics** | modal, temporal, intuitionistic, many-valued... | Ch. 2.7, 3, 6 |

## Z1.8 A very short history

| When | Who | Contribution |
|---|---|---|
| c. 350 BC | Aristotle | Syllogisms: first systematic study of valid argument forms |
| c. 300 BC | Stoics (Chrysippus) | Logic of "if...then", "or", "and": early propositional logic |
| 1847 | George Boole | Logic as algebra (the root of Boolean algebra and digital circuits) |
| 1879 | Gottlob Frege | *Begriffsschrift*: the first full predicate logic with quantifiers |
| 1889 | Giuseppe Peano | Axioms for the natural numbers; modern symbols such as ∈ and ∃ |
| 1901-10 | Russell, Whitehead | Russell's paradox; *Principia Mathematica* |
| 1920s | Hilbert and school | Formal systems; the program to prove mathematics consistent |
| 1929-31 | Kurt Gödel | Completeness theorem (FOL), then the incompleteness theorems |
| 1934-35 | Gerhard Gentzen | Natural deduction and sequent calculus |
| 1936 | Church, Turing | Undecidability of first-order validity; models of computation |
| 1950s-60s | Robinson, Davis, Putnam | Resolution, unification, automated theorem proving |
| 1960s-today | Howard, de Bruijn, Martin-Löf, Coquand... | Proofs as programs; proof assistants (Lean, Coq/Rocq, Isabelle) |

## Z1.9 Try it

**Q1.** Which of these are statements? (a) "7 is prime." (b) "Is 7 prime?" (c) "x + 1 = 8." (d) "Every planet has a moon." (e) "Stop!"
**Q2.** Is this argument valid? "If I win the lottery, I'll be rich. I am rich. Therefore I won the lottery." Why or why not?
**Q3.** Give an example of a *valid but unsound* argument.
**Q4.** What is the *form* of: "If the battery is dead then the car won't start. The battery is dead. So the car won't start."?

**Answers.**
**A1.** (a) and (d) are statements ((d) is false but still a statement). (b) is a question, (e) a command, (c) is an open sentence (depends on x).
**A2.** Invalid (affirming the consequent): one can be rich for other reasons (inheritance).
**A3.** "All fish can fly. A shark is a fish. So a shark can fly." Valid form, false premise.
**A4.** "If A then B. A. Therefore B." (modus ponens, valid).

---

# Chapter Z2. The language of mathematics

Mathematical writing has its own grammar and vocabulary. Misreading it is the most common source of mistakes for beginners. This chapter is a field guide.

## Z2.1 Kinds of mathematical text

| Term | Meaning | Example |
|---|---|---|
| **Definition** | Gives a precise meaning to a new word or symbol | "An integer n is *even* if n = 2k for some integer k." |
| **Axiom** (or **postulate**) | A statement accepted without proof, as a starting point | "For any two points there is exactly one line through them." |
| **Theorem** | An important statement that has been **proved** | "√2 is irrational." |
| **Proposition** | A less central theorem | "The sum of two even integers is even." |
| **Lemma** | A helper theorem, proved on the way to a bigger result | "If n² is even then n is even." |
| **Corollary** | A theorem that follows quickly from a previous one | "No integer of the form 4k + 3 is a sum of two squares." |
| **Conjecture** | A statement believed true but **not yet proved** | Goldbach's conjecture |
| **Claim** | A statement to be proved within a larger proof | "Claim: x is positive." |
| **Remark / Note** | Comment, not part of the logical chain | |
| **Example / Counterexample** | A specific case supporting / refuting a general statement | |
| **Proof** | A convincing, step-by-step argument that a statement follows from accepted facts | |

**End-of-proof marks:** ∎ (the "tombstone" or Halmos symbol), □, ■, *Q.E.D.* (Latin *quod erat demonstrandum*, "which was to be shown"), sometimes // or "as required". All mean "the proof is complete".

**Defined terms vs. defining symbols.** When a definition introduces notation, mathematicians use one of: `:=`, `≔`, `=:`, `≝`, `≜`, `def=`, `:⇔` (for statements), or just words ("we write ... for ..."). The colon sits on the side of the thing being defined: `A := B` defines A to be B.

**A subtle but crucial convention: definitions are "if and only if", even when written with "if".**
"An integer is *even* if it is divisible by 2." really means *even exactly when* divisible by 2. It is a definition, so both directions hold. (Theorems written with "if" are one-directional. Context tells you which you are reading.)

## Z2.2 A dictionary of mathematical English

| Phrase | What it means (precisely) | Logical form |
|---|---|---|
| **if P then Q**, **P implies Q**, **P ⇒ Q** | Whenever P holds, Q holds. | P → Q |
| **P only if Q** | P can be true only when Q is; i.e., if P then Q. | P → Q |
| **P if Q** | If Q then P. (Arrow points the other way!) | Q → P |
| **P if and only if Q**, **P iff Q**, **P ⇔ Q**, **P is equivalent to Q** | They stand or fall together. | P ↔ Q |
| **P is sufficient for Q** | P guarantees Q. | P → Q |
| **P is necessary for Q** | Without P, no Q. | Q → P |
| **P unless Q** | If not Q then P. | ¬Q → P |
| **not P**, **it is not the case that P** | P is false. | ¬P |
| **P and Q**, **both P and Q** | Both hold. | P ∧ Q |
| **P or Q**, **P or Q or both** | At least one holds (**inclusive or**, the default in mathematics). | P ∨ Q |
| **either P or Q (but not both)**, **exactly one of** | **exclusive or**. | P ⊕ Q |
| **neither P nor Q** | Both fail. | ¬P ∧ ¬Q |
| **for all x, for every x, for each x, for any x** | The claim holds no matter which x. | ∀x |
| **there exists x such that**, **for some x**, **there is an x** | At least one x makes it true. | ∃x |
| **there exists a unique x**, **exactly one x** | Exactly one. | ∃!x |
| **no x satisfies P** | None. | ¬∃x P(x) |
| **such that**, **s.t.**, **with**, **where** (sometimes also `∋`, `\|`, `:`) | Introduces a condition on the object just named. | (part of ∃ or set-builder) |
| **Let x be ...**, **Suppose ...**, **Assume ...** | Introduces an object or hypothesis for the rest of the argument. | ∀I, →I |
| **WLOG**, **without loss of generality** | One case is stated, and the others follow by symmetry. | (case reduction) |
| **it suffices to show** | Proving this smaller thing proves everything. | |
| **hence, thus, therefore, so, consequently** | The next statement follows from what precedes. | |
| **since, because, as** | Introduces a reason already established. | |
| **i.e.** (*id est*) | "that is" (restating) | |
| **e.g.** (*exempli gratia*) | "for example" | |
| **in particular** | a special case of what was just said | ∀E |
| **conversely** | the reverse implication | |
| **vacuously true** | true only because the "if" part never occurs | |
| **trivial**, **obvious**, **clearly** | A signal that justification is routine (be careful!) | |
| **well-defined** | The definition does not depend on arbitrary choices | |
| **arbitrary but fixed** | A generic, unspecified element about which only the stated assumptions are known | |
| **contrapositive** of "if P then Q" | "if not Q then not P" (equivalent) | ¬Q → ¬P |
| **converse** of "if P then Q" | "if Q then P" (**not** equivalent) | Q → P |

### Six traps that catch every beginner

**1. "Or" is inclusive.** "n is even or n > 10" is true for n = 12 (both). Everyday "or" is often exclusive ("soup or salad"), so you must override your habit.

**2. "Some" means "at least one" (possibly all).** "Some primes are odd" is true. It does *not* suggest that some primes are not odd.

**3. "A" can mean "any" or "some".** "A prime greater than 2 is odd" means *every* prime greater than 2 is odd. "A prime is bigger than 100" means *some* prime. Always decide whether a hidden "for all" or "there exists" is present.

**4. "Any" is slippery.** "If any student fails, the class is delayed" (= *some*: if at least one fails). "Any student can answer this" (= *every*). Replace "any" by "every" or "some" explicitly when writing mathematics.

**5. Order of quantifiers.** "For every person there is someone they love" is not the same as "there is someone whom every person loves". Compare: ∀x ∃y L(x, y) and ∃y ∀x L(x, y). In ordinary mathematical prose the order of phrases is the order of quantifiers: read left to right.

**6. "If...then" is not about causes.** "If 2 + 2 = 5 then the moon is cheese" is *true* in logic. It is a claim about truth values only (we will explain why in Chapter 1.3).

## Z2.3 The common shapes of mathematical statements

Almost every theorem fits one of these shapes. Recognizing the shape tells you what the proof must look like (this becomes precise in Chapter 5).

| Shape | Example | What you prove |
|---|---|---|
| **Universal** "for all x, P(x)" | "Every square is nonnegative." | Take an arbitrary x, show P(x) |
| **Existential** "there is x with P(x)" | "There is a prime between 20 and 30." | Exhibit one x (23), show P(x) |
| **Conditional** "if P then Q" | "If n is even then n² is even." | Assume P, show Q |
| **Universal conditional** "for all x, if P(x) then Q(x)" | "Every even number's square is even." | Take arbitrary x, assume P(x), show Q(x) |
| **Biconditional** "P iff Q" | "n is even iff n² is even." | Prove P → Q and Q → P |
| **Uniqueness** "exactly one x" | "The identity element is unique." | Existence, then: two such x are equal |
| **Negation** "not P" | "√2 is not rational." | Assume P, derive absurdity |
| **Disjunction** "P or Q" | "x² = 4 ⇒ x = 2 or x = −2" | Show one of them (often by cases) |
| **Conjunction** "P and Q" | "n is even and positive." | Prove each |

### How to negate each shape (essential skill)

| Statement | Negation (in words) | Symbolic |
|---|---|---|
| P and Q | not P, or not Q (or both) | ¬P ∨ ¬Q |
| P or Q | not P, and not Q | ¬P ∧ ¬Q |
| if P then Q | P holds and Q fails | P ∧ ¬Q |
| for all x, P(x) | there is some x where P fails | ∃x ¬P(x) |
| there exists x, P(x) | for every x, P fails | ∀x ¬P(x) |
| for all x there exists y, R(x, y) | there is some x such that for every y, R fails | ∃x ∀y ¬R(x, y) |
| P iff Q | exactly one of P, Q holds | (P ∧ ¬Q) ∨ (¬P ∧ Q) |

Examples:
- Negate "Every student passed." → "At least one student did not pass." (**Not** "No student passed"!)
- Negate "Some birds can't fly." → "Every bird can fly."
- Negate "If it rains, I stay home." → "It rains and I do not stay home."

## Z2.4 Anatomy of a proof (a first complete example, narrated)

We prove this very simple statement and mark every move.

> **Theorem.** If n is an even integer, then n + 1 is odd.
>
> *Definitions used.* An integer n is **even** if there exists an integer k with n = 2k. An integer n is **odd** if there exists an integer k with n = 2k + 1.

| Step | What is written | What it is doing |
|---|---|---|
| 0 | The statement has the shape *"if P then Q"*: P = "n is even", Q = "n + 1 is odd". | **Identify the shape**: to prove an "if...then", assume the "if" part. |
| 1 | "Let n be an even integer." | **Introduce the object** and assume P. Here n is arbitrary: we know nothing about it except that it is even. |
| 2 | "By definition of even, there is an integer k with n = 2k." | **Unpack the definition** of the hypothesis. It gives us a concrete equation to work with. |
| 3 | "Then n + 1 = 2k + 1." | **Calculation**: we substitute equals for equals. |
| 4 | "Since k is an integer, this is of the form 2k + 1, so n + 1 is odd by definition." | **Repack**: we match the result against the definition of the goal Q. |
| 5 | ∎ | The goal was reached; the "if" part was used, so the conditional is proved. |

The pattern **identify the shape, unpack definitions, calculate, repack definitions** is the heart of most introductory proofs. In Chapter 5 we make each move precise as a rule of logic.

## Z2.5 How to read mathematics

1. **Slowly, with a pencil.** A page of mathematics can need an hour.
2. **Read definitions twice**, and write examples. If a definition says "n is even if n = 2k", test n = 6 (k = 3), n = 7 (impossible), n = 0 (k = 0).
3. **When you meet a symbol you do not know**, look it up (Chapter Z4) *before* continuing.
4. **For a theorem, find the hypotheses and the conclusion.** Rewrite it as "Assume ... Then ...".
5. **Test with an example, then a non-example**, then see where the proof uses each hypothesis. A proof that never uses a hypothesis is suspicious (or the hypothesis is redundant).
6. **Rewrite the proof in your own words** from memory.

## Z2.6 A note on notation habits

- **Variables and letters.** Mathematicians use letters as placeholders. Typical conventions: n, m, k, i, j for integers; x, y, z for real numbers or "any object"; a, b, c for fixed constants; ε, δ for small positive numbers; f, g, h for functions; A, B, C for sets; P, Q, R for statements or predicates. These are only habits, not rules. Always check the author's declaration ("Let n be an integer...").
- **Subscripts** distinguish related objects: x₁, x₂, ..., xₙ.
- **Primes and bars** ( x′, x″, x̄ ) distinguish related objects too; context decides whether x̄ is a complement, a conjugate, or a mean.
- **Parentheses** group, but also appear in function application f(x) and in tuples (a, b). Context decides.
- **A comma** between conditions usually means "and": "x > 0, y > 0" means x > 0 *and* y > 0.
- **Equality signs** in a chain a = b = c mean a = b and b = c. A chain of inequalities a ≤ b < c means a ≤ b and b < c, so a < c.

## Z2.7 Try it

**Q1.** Rewrite using "if...then": (a) "n is divisible by 6 only if n is even." (b) "A number is positive if it is greater than 5." (c) "Passing the exam is necessary for graduating."
**Q2.** Negate: (a) "All dogs bark." (b) "There is a number which is both even and prime greater than 2." (c) "If it is Monday then the shop is open."
**Q3.** Is "If 2 is odd then 3 is even" true or false? Explain.
**Q4.** What does "for every real x there is a real y with y > x" say? What does "there is a real y such that for every real x, y > x" say? Are both true?
**Q5.** What is the *contrapositive* of "If n is prime and n > 2 then n is odd"?

**Answers.**
**A1.** (a) If n is divisible by 6 then n is even. (b) If a number is greater than 5 then it is positive. (c) If you graduate then you passed the exam.
**A2.** (a) Some dog does not bark. (b) Every number that is even is either not prime or is not greater than 2 (equivalently: every even prime is ≤ 2). (c) It is Monday and the shop is not open.
**A3.** True: the "if" part (2 is odd) is false, so the conditional is vacuously true (Chapter 1.3).
**A4.** The first says there is no largest real number (true). The second says there is a largest real number (false). So order of quantifiers changes the meaning.
**A5.** If n is not odd (i.e., n is even) then n is not prime or n ≤ 2. (Negating a conjunction: ¬(n prime ∧ n > 2) = n not prime ∨ n ≤ 2.)

---

---

# Chapter Z3. The mathematics you need first: sets, numbers, functions, relations, strings, trees

Logic talks about *things*, *collections of things*, and *connections between things*. Mathematics gives us standard words for these. You need them for predicate logic (Chapter 3) and for every proof in Chapter 5. Everything below is introduced from scratch.

## Z3.1 Sets

### Z3.1.1 What a set is

A **set** is a collection of distinct objects, called its **elements** or **members**. What matters is *which* objects are in it. Not order, not repetition.

| Notation | Reads | Meaning |
|---|---|---|
| `a ∈ A` | "a is an element of A", "a belongs to A", "a in A" | a is one of the members of A |
| `a ∉ A` | "a is not an element of A" | a is not a member of A |
| `∋` | "contains as a member" (rare) | `A ∋ a` means `a ∈ A` |

### Z3.1.2 Ways to describe a set

**1. Listing (roster notation):** `{1, 2, 3}`, `{red, green, blue}`. Order and repetition do not matter: `{1, 2, 3} = {3, 2, 1} = {1, 1, 2, 3}`.

**2. Dots for pattern:** `{1, 2, 3, ..., 100}`, `{2, 4, 6, ...}` (infinite). Only use when the pattern is obvious.

**3. Set-builder notation:** `{ x | P(x) }` or `{ x : P(x) }`, read "the set of all x such that P(x)". Examples:

| Set-builder | Reads | Elements |
|---|---|---|
| `{ x ∈ ℤ \| x > 0 }` | the integers x such that x is positive | 1, 2, 3, ... |
| `{ n² : n ∈ ℕ }` | the squares n² where n is a natural number | 0, 1, 4, 9, ... |
| `{ x ∈ ℝ \| x² = 4 }` | real solutions of x² = 4 | { −2, 2 } |
| `{ n ∈ ℤ \| 2 divides n }` | even integers | ..., −2, 0, 2, ... |

Note: the vertical bar `|` here means "such that". Elsewhere `|` means "divides" (`3 | 12`) or absolute value (`|x|`). Context disambiguates, which is why many authors prefer the colon in set-builder.

**4. By a rule or definition** ("the set of all prime numbers").

### Z3.1.3 Special sets

| Symbol | Name | Meaning |
|---|---|---|
| `∅` or `{}` | the **empty set** | the set with no elements. Note `∅ ≠ {∅}`: the second has one element (the empty set). |
| `U` or `𝒰` or `Ω` | the **universe** (universal set) | everything under discussion |
| `{a}` | a **singleton** | the set whose only member is a |
| `{a, b}` | a **pair set** | exactly two elements (if a ≠ b) |

### Z3.1.4 Equality, subsets, supersets

Two sets are **equal** when they have exactly the same elements (*extensionality*):

> `A = B` iff for every x: `x ∈ A` ↔ `x ∈ B`.

**Subset.** `A ⊆ B` ("A is a subset of B", "A is contained in B") means every element of A is also an element of B:

> `A ⊆ B` iff `∀x (x ∈ A → x ∈ B)`.

| Symbol | Meaning | Caution |
|---|---|---|
| `A ⊆ B` | A is a subset of B (A may equal B) | |
| `A ⊂ B` | **Ambiguous!** Some books: same as ⊆. Other books: proper subset (A ⊆ B and A ≠ B). | Check the author's convention |
| `A ⊊ B` | proper subset: A ⊆ B and A ≠ B | unambiguous |
| `A ⊇ B` | A is a superset of B (B ⊆ A) | |
| `A ⊄ B` | A is **not** a subset of B | |

Facts: `∅ ⊆ A` for every set A (vacuously true: there is no element of ∅ that could fail to be in A). `A ⊆ A`. If `A ⊆ B` and `B ⊆ C` then `A ⊆ C`. `A = B` iff `A ⊆ B` and `B ⊆ A` (this is how equality of sets is proved: show both inclusions).

### Z3.1.5 Operations on sets

Let A and B be sets, inside a universe U.

| Operation | Symbols (variants) | Definition | Reads |
|---|---|---|---|
| **Union** | `A ∪ B` | `{ x \| x ∈ A ∨ x ∈ B }` | "A union B", "A cup B" |
| **Intersection** | `A ∩ B` | `{ x \| x ∈ A ∧ x ∈ B }` | "A intersect B", "A cap B" |
| **Difference** | `A ∖ B`, `A − B`, `A \ B` | `{ x \| x ∈ A ∧ x ∉ B }` | "A minus B", "A without B" |
| **Complement** | `Aᶜ`, `A′`, `Ā`, `∁A`, `~A`, `U ∖ A` | `{ x ∈ U \| x ∉ A }` | "complement of A", "not A" |
| **Symmetric difference** | `A △ B`, `A ⊕ B`, `A Δ B` | `(A ∖ B) ∪ (B ∖ A)` | elements in exactly one of them |
| **Cartesian product** | `A × B` | `{ (a, b) \| a ∈ A ∧ b ∈ B }` | "A cross B" (see Z3.1.7) |
| **Power set** | `𝒫(A)`, `P(A)`, `2^A` | `{ S \| S ⊆ A }` | set of all subsets of A |
| **Cardinality** | `\|A\|`, `#A`, `card(A)` | the number of elements (finite case) | "size of A" |

**The correspondence with logic is exact (and worth memorizing):**

| Set operation | Logical connective | Condition for membership |
|---|---|---|
| A ∩ B | **and** (∧) | x ∈ A ∧ x ∈ B |
| A ∪ B | **or** (∨, inclusive) | x ∈ A ∨ x ∈ B |
| Aᶜ | **not** (¬) | ¬(x ∈ A) |
| A ∖ B | and-not | x ∈ A ∧ ¬(x ∈ B) |
| A △ B | exclusive or (⊕) | (x ∈ A) ⊕ (x ∈ B) |
| A ⊆ B | **implies** (→) for all x | ∀x (x ∈ A → x ∈ B) |
| A = B | **iff** (↔) for all x | ∀x (x ∈ A ↔ x ∈ B) |

Because of this, every logical law has a set-theoretic twin: De Morgan's law ¬(P ∧ Q) ≡ ¬P ∨ ¬Q becomes `(A ∩ B)ᶜ = Aᶜ ∪ Bᶜ`.

**Example.** A = {1, 2, 3, 4}, B = {3, 4, 5}, U = {1, 2, 3, 4, 5, 6}.
- A ∪ B = {1, 2, 3, 4, 5}
- A ∩ B = {3, 4}
- A ∖ B = {1, 2}; B ∖ A = {5}
- A △ B = {1, 2, 5}
- Aᶜ = {5, 6}
- |A| = 4; 𝒫({1, 2}) = {∅, {1}, {2}, {1, 2}}, which has 2² = 4 elements. In general |𝒫(A)| = 2^|A|.

### Z3.1.6 Venn diagrams

A Venn diagram draws sets as overlapping regions inside a rectangle (the universe). Text sketch for two sets:

```
 ┌──────────────────────────────────────┐
 │ U                                    │
 │      ╭──────────╮╭──────────╮        │
 │     ╱   A only   ╳  A ∩ B   ╲ B only│
 │     ╲            ╳           ╱       │
 │      ╰──────────╯╰──────────╯        │
 │                 outside both = (A ∪ B)ᶜ│
 └──────────────────────────────────────┘
```

The four regions are exactly the four rows of a two-variable truth table (A and B, A only, B only, neither). That is why Venn diagrams can verify propositional laws.

### Z3.1.7 Ordered pairs, tuples, Cartesian products

A set ignores order. When order matters we use an **ordered pair** `(a, b)`: it satisfies `(a, b) = (c, d)` iff `a = c` and `b = d`. So `(1, 2) ≠ (2, 1)` but `{1, 2} = {2, 1}`. (Formally one can *define* `(a, b)` as the set `{{a}, {a, b}}`, but you only need the equality property.)

An **n-tuple** `(a₁, a₂, ..., aₙ)` generalizes: ordered, repetition allowed. `A × B` is the set of all pairs with first entry from A and second from B. `Aⁿ` is the set of n-tuples of elements of A: `A² = A × A`, `ℝ³` is 3-dimensional space. If |A| = m and |B| = n then |A × B| = m·n.

### Z3.1.8 Indexed families, big union, big intersection

If for each i in an index set I we have a set Aᵢ:

- `⋃ᵢ∈I Aᵢ = { x | ∃i ∈ I, x ∈ Aᵢ }` (x lies in *at least one* Aᵢ)
- `⋂ᵢ∈I Aᵢ = { x | ∀i ∈ I, x ∈ Aᵢ }` (x lies in *every* Aᵢ)

Notice the pattern: **big union is an existential statement, big intersection is a universal one.** Same as ∃ and ∀.

### Z3.1.9 Partitions

A **partition** of a set S is a family of non-empty, pairwise disjoint sets whose union is S. Example: the even and the odd integers partition ℤ.

### Z3.1.10 Intervals of real numbers

| Notation | Set | Name |
|---|---|---|
| `[a, b]` | `{ x ∈ ℝ : a ≤ x ≤ b }` | closed interval |
| `(a, b)` | `{ x ∈ ℝ : a < x < b }` | open interval |
| `[a, b)` , `(a, b]` | half-open | |
| `(a, ∞)`, `[a, ∞)`, `(−∞, b)`, ... | unbounded | ∞ is a symbol, not a number |

Warning: `(a, b)` also denotes an ordered pair. Context decides.

### Z3.1.11 A caution: not every collection is a set

If we allowed "the set of all sets that are not members of themselves", we would get **Russell's paradox** (it would belong to itself exactly when it does not). Modern set theory (ZFC) avoids this by restricting how sets can be formed. You will meet this again in Chapter 6.

## Z3.2 Numbers and arithmetic notation

### Z3.2.1 The standard number systems

| Symbol | Name | Elements | Notes |
|---|---|---|---|
| `ℕ` | natural numbers | 0, 1, 2, 3, ... **or** 1, 2, 3, ... | **Convention varies!** Logic and computer science usually include 0. Many analysis texts start at 1. State your convention. Some write ℕ₀ = {0, 1, 2, ...} and ℕ⁺ or ℕ₁ = {1, 2, ...}. |
| `ℤ` | integers | ..., −2, −1, 0, 1, 2, ... | from German *Zahlen* |
| `ℚ` | rational numbers | fractions p/q with p, q ∈ ℤ, q ≠ 0 | from *quotient* |
| `ℝ` | real numbers | all points on the number line | includes √2, π, e |
| `ℂ` | complex numbers | a + bi with a, b ∈ ℝ, i² = −1 | |
| `ℙ` | prime numbers (sometimes) | 2, 3, 5, 7, 11, ... | |
| `ℤ⁺`, `ℝ⁺`, `ℝ>0` | positive integers / reals | | |
| `ℤₙ`, `ℤ/nℤ` | integers modulo n | {0, 1, ..., n − 1} | "clock arithmetic" |

Inclusions: ℕ ⊆ ℤ ⊆ ℚ ⊆ ℝ ⊆ ℂ.

### Z3.2.2 Order and comparison

| Symbol | Reads | Meaning |
|---|---|---|
| `<` | less than | |
| `>` | greater than | |
| `≤` | less than or equal | (also written `⩽`, `≦`) |
| `≥` | greater than or equal | |
| `≠` | not equal | |
| `≪`, `≫` | much less / much greater | informal |
| `≈` | approximately equal | not exact |

### Z3.2.3 Operations and common functions

| Symbol | Meaning | Examples |
|---|---|---|
| `+`, `−` | addition, subtraction | |
| `×`, `·`, juxtaposition `ab` | multiplication | 3 × 4 = 3·4 = 12 |
| `÷`, `/`, `a/b`, fraction bar | division | 12 / 4 = 3 |
| `aⁿ`, `a^n`, `a**n` | exponentiation (n copies of a multiplied) | 2⁵ = 32 |
| `√a`, `a^(1/2)` | square root | √9 = 3 |
| `\|x\|` | absolute value | `\|−5\| = 5`; `\|x − y\|` is the distance between x and y |
| `n!` | factorial | 5! = 5·4·3·2·1 = 120; 0! = 1 |
| `⌊x⌋` | floor (round down) | ⌊3.7⌋ = 3 |
| `⌈x⌉` | ceiling (round up) | ⌈3.2⌉ = 4 |
| `a mod n`, `a % n` | remainder of dividing a by n | 17 mod 5 = 2 |
| `a ≡ b (mod n)` | a and b leave the same remainder when divided by n | 17 ≡ 2 (mod 5) |
| `a \| b` | a **divides** b: there is an integer k with b = a·k | `3 \| 12` is true, `5 \| 12` is false |
| `a ∤ b` | a does not divide b | |
| `gcd(a, b)` | greatest common divisor | gcd(12, 18) = 6 |
| `lcm(a, b)` | least common multiple | lcm(4, 6) = 12 |
| `∑ᵢ₌₁ⁿ aᵢ` | sum a₁ + a₂ + ... + aₙ | ∑ᵢ₌₁⁴ i = 1 + 2 + 3 + 4 = 10 |
| `∏ᵢ₌₁ⁿ aᵢ` | product a₁ · a₂ ··· aₙ | ∏ᵢ₌₁⁴ i = 24 |
| `∞` | infinity (a symbol meaning "unbounded") | not a real number |
| `min`, `max` | smallest, largest | max(3, 7) = 7 |

**The sign `≡` is overloaded:** in logic it means "logically equivalent"; in number theory "congruent modulo n"; in some books "is defined as" or "identically equal". Always read it in context.

### Z3.2.4 Basic number-theory vocabulary

| Term | Definition |
|---|---|
| **even** | n = 2k for some integer k (equivalently 2 divides n) |
| **odd** | n = 2k + 1 for some integer k |
| **prime** | an integer p > 1 whose only positive divisors are 1 and p |
| **composite** | an integer > 1 that is not prime (it has a divisor strictly between 1 and itself) |
| **rational** | a real number equal to p/q with p, q integers, q ≠ 0 |
| **irrational** | a real number that is not rational |
| **divisor / factor** | a divides n |
| **multiple** | n is a multiple of a if a divides n |
| **coprime** | gcd(a, b) = 1 |

Note: 1 is **not** prime; 0 is even; negative integers can be even or odd (−4 = 2·(−2)).

## Z3.3 Functions

### Z3.3.1 Definition

A **function** f from a set A to a set B, written **f : A → B**, assigns to *each* element x of A exactly one element f(x) of B.

| Term | Meaning |
|---|---|
| **domain** (of f) | A, the set of allowed inputs |
| **codomain** (of f) | B, the set where outputs live |
| **range** or **image** (of f) | `{ f(x) \| x ∈ A }`, the set of outputs that actually occur (a subset of the codomain) |
| `x ↦ f(x)` | "x maps to f(x)": a way to describe the rule, e.g. `x ↦ x²` |
| `f(x) = y` | "the value of f at x is y" |

**Example.** `f : ℤ → ℤ`, `f(x) = x²`. Domain ℤ, codomain ℤ, range {0, 1, 4, 9, ...}. Two things to note: every input has *exactly one* output (so f(2) = 4 only), but different inputs can share an output (f(2) = f(−2) = 4).

**Functions with several inputs:** `f : A × B → C`, written f(a, b). Equivalent: a function of an n-tuple. We say f has **arity** n. A **constant** is a function of arity 0 (no inputs): it just names an element.

**Partial functions** are defined only on part of the domain (division is a partial function on ℝ, undefined at 0). "Function" without qualification means *total*: defined everywhere on the domain.

**Predicates as functions:** a statement-valued function `P : A → {true, false}` is a **predicate**. For instance `Even(n)` is true exactly when n is even. The set `{ x ∈ A | P(x) }` is the **extension** of P (the set of things the predicate holds of).

### Z3.3.2 Composition, identity, inverse

| Concept | Notation | Meaning |
|---|---|---|
| **Composition** | `g ∘ f`, "g after f" | `(g ∘ f)(x) = g(f(x))` (apply f first, then g) |
| **Identity function** | `id_A`, `1_A`, `id` | `id(x) = x` |
| **Inverse function** | `f⁻¹` | a function with `f⁻¹(f(x)) = x` for all x in A and `f(f⁻¹(y)) = y` for all y in B. Exists exactly when f is a bijection. |
| **Image of a set** | `f[S]`, `f(S)` | `{ f(x) \| x ∈ S }` |
| **Preimage of a set** | `f⁻¹[T]`, `f⁻¹(T)` | `{ x ∈ A \| f(x) ∈ T }`. Defined even when f has no inverse. |

Caution: `f⁻¹` can mean the inverse function **or** the preimage operation, and `f⁻¹(x)` is not `1/f(x)`.

### Z3.3.3 Three key properties

| Property | Meaning | Formal statement |
|---|---|---|
| **Injective** (one-to-one, "1-1", an injection) | different inputs give different outputs | ∀a ∀b (f(a) = f(b) → a = b) |
| **Surjective** (onto, a surjection) | every element of the codomain is hit | ∀y ∈ B ∃x ∈ A (f(x) = y) |
| **Bijective** (a bijection, "one-to-one correspondence") | both injective and surjective | |

Examples:
- `f : ℤ → ℤ`, f(x) = x²: neither (f(2) = f(−2); −1 is never hit).
- `f : ℤ → ℤ`, f(x) = x + 1: bijective (inverse x − 1).
- `f : ℕ → ℤ`, f(n) = n: injective, not surjective.
- `f : ℝ → ℝ`, f(x) = x³: bijective.

### Z3.3.4 Counting with functions: cardinality

Two sets **have the same cardinality** if there is a bijection between them. A set is **finite** if it has the same cardinality as {1, ..., n} for some n; otherwise **infinite**. A set is **countably infinite** if it has the same cardinality as ℕ ("it can be listed in a sequence"); ℤ and ℚ are countably infinite. **Uncountable** sets (like ℝ, and 𝒫(ℕ)) are infinite sets *too big* to list; Cantor proved this with a diagonal argument (Chapter 5.12). The cardinality of ℕ is written **ℵ₀** ("aleph-null").

## Z3.4 Relations

### Z3.4.1 Definition

A **binary relation** R from A to B is a subset of A × B. If (a, b) ∈ R we say "a is related to b by R" and write **a R b**, **R(a, b)**, or **(a, b) ∈ R**.

Examples (relations *on* a set, meaning A = B):
- `<` on ℤ: `3 < 5`.
- `=` on any set.
- "divides" on ℕ: `3 | 12`.
- "is a parent of" on a set of people.
- "is connected by an edge to" on the vertices of a graph.

**An n-ary relation** on A is a subset of Aⁿ: e.g., the ternary relation "x is between y and z".

**Relations are the semantics of predicates.** The predicate "L(x, y): x loves y" corresponds to the set of pairs { (x, y) | x loves y }.

### Z3.4.2 Properties of a relation R on a set A

| Property | Meaning | Symbolic |
|---|---|---|
| **Reflexive** | everything is related to itself | ∀x R(x, x) |
| **Irreflexive** | nothing is related to itself | ∀x ¬R(x, x) |
| **Symmetric** | if x R y then y R x | ∀x∀y (R(x, y) → R(y, x)) |
| **Antisymmetric** | if x R y and y R x then x = y | ∀x∀y ((R(x, y) ∧ R(y, x)) → x = y) |
| **Asymmetric** | if x R y then not y R x | ∀x∀y (R(x, y) → ¬R(y, x)) |
| **Transitive** | if x R y and y R z then x R z | ∀x∀y∀z ((R(x, y) ∧ R(y, z)) → R(x, z)) |
| **Total / connected** (trichotomy-like) | any two distinct elements are related one way or the other | ∀x∀y (x = y ∨ R(x, y) ∨ R(y, x)) |
| **Serial** | everything has something it is related to | ∀x ∃y R(x, y) |

Examples: `≤` on ℤ is reflexive, antisymmetric, transitive, total. `<` is irreflexive, asymmetric, transitive, connected. "Is a sibling of" is symmetric, not reflexive (usually), not transitive in general. `=` is reflexive, symmetric, transitive.

### Z3.4.3 Two especially important kinds of relation

**Equivalence relation:** reflexive + symmetric + transitive. It formalizes "being the same in some respect". Example: *congruence modulo n* on ℤ ("a and b have the same remainder"). An equivalence relation splits the set into **equivalence classes** `[a] = { x | x R a }`, and these classes form a **partition** of the set (and every partition comes from an equivalence relation).

**Partial order:** reflexive + antisymmetric + transitive (like ≤ or ⊆). A **strict partial order**: irreflexive + transitive (like < or ⊂). A **total (linear) order** is a partial order in which every two elements are comparable. A **well-order** is a total order in which every non-empty subset has a least element (ℕ with ≤ is one; ℤ and ℝ are not, because they have no least element). Partial orders are drawn as **Hasse diagrams**, with a line going upward from x to y whenever x < y with nothing in between.

### Z3.4.4 Graphs as relations (we will use them as examples)

A **directed graph** is a set V of **vertices** (nodes) and a relation E ⊆ V × V of **edges**. Drawing: dots and arrows. An **undirected graph** has a symmetric E. A **path** is a sequence of vertices with an edge between consecutive ones. Graphs are the easiest nontrivial *structures* for practicing predicate logic: the sentence `∀x ∃y E(x, y)` says "every vertex has an outgoing edge".

## Z3.5 Sequences, strings, alphabets, languages

A **sequence** is an ordered list `a₁, a₂, ..., aₙ` (finite) or `a₁, a₂, ...` (infinite). Same as a function from {1, ..., n} or ℕ.

An **alphabet** Σ is a finite non-empty set of **symbols**. A **string** (or word) over Σ is a finite sequence of symbols. Examples over Σ = {a, b}: `a`, `abba`, and the **empty string** (written `ε` or `λ` or `""`), which has length 0. `|w|` is the length of w. **Concatenation** `uv` (or `u · v`) puts strings end to end: `ab · ba = abba`. `Σ*` is the set of all finite strings over Σ. A **formal language** is any subset of Σ*.

**Why this matters for logic:** a *formula* is a string of symbols from the logical alphabet. "Is this string a well-formed formula?" is a question about membership in a formal language, settled by exact **formation rules** (Chapter 1.1 and 3.2). The statement "(P → Q" is a string but not a formula (unbalanced bracket).

## Z3.6 Trees and recursive (inductive) definitions

### Z3.6.1 Trees

A **tree** is a graph with a designated **root** where every other node is reached from the root by exactly one path. Vocabulary: **node**, **edge**, **parent / child**, **leaf** (no children), **depth** (distance from the root), **height** (maximum depth). Trees are drawn upside-down, the root at the top:

```
          →             ← root (the main connective)
         / \
        ∧   R
       / \
      P   Q
```

This is the **parse tree** (syntax tree) of `(P ∧ Q) → R`. Every formula has such a tree. Reading a formula means reconstructing its tree.

### Z3.6.2 Inductive definitions

Many objects in logic are defined **inductively**: by stating (1) some **base** objects, (2) **construction rules** that build new objects from old ones, and (3) a **closure clause**: "nothing else is an object of this kind". Example, the set of propositional formulas over atoms p, q, r:

1. (Base) p, q, r are formulas.
2. (Rule) If A is a formula then ¬A is a formula.
3. (Rule) If A and B are formulas then (A ∧ B) is a formula, and likewise (A ∨ B), (A → B), (A ↔ B).
4. (Closure) Nothing else is a formula.

Two powerful consequences:

- **Definition by recursion.** To define a function on formulas it is enough to say what it does on the base cases and how to compute it for ¬A, (A ∧ B), ... from the values for A and B. Example: *the number of connectives* `c`: c(p) = 0; c(¬A) = c(A) + 1; c((A ∧ B)) = c(A) + c(B) + 1.
- **Proof by induction (structural).** To prove that *every* formula has some property, prove it for the base cases, and show that the construction rules preserve it (Chapter 5.10).

**Unique readability.** Each formula can be built in only one way, so its parse tree is unique. That is why the parentheses in the definition matter; without them `P ∨ Q ∧ R` would be ambiguous.

### Z3.6.3 The same idea for numbers

The natural numbers are inductively defined: **0 is a natural number; if n is, so is its successor n + 1; nothing else is.** That is the source of mathematical induction (Chapter 5.8).

## Z3.7 Try it

**Q1.** Let A = {2, 4, 6}, B = {4, 6, 8, 10}, U = {1, ..., 10}. Compute A ∪ B, A ∩ B, A ∖ B, Aᶜ, |𝒫(A)|, and the number of elements of A × B.
**Q2.** Is ∅ ⊆ {1, 2}? Is ∅ ∈ {1, 2}? Is ∅ ∈ {∅}?
**Q3.** For f : ℤ → ℤ, f(n) = 2n: is f injective? surjective? What is its range?
**Q4.** For each relation on ℤ decide reflexive / symmetric / transitive: (a) a R b iff a ≤ b; (b) a R b iff a − b is even; (c) a R b iff a ≠ b.
**Q5.** Which of these is a well-formed formula built by Z3.6.2: (a) (P ∧ Q) (b) P ∧ Q (c) ¬¬P (d) (P ∧ ¬)?

**Answers.**
**A1.** A ∪ B = {2, 4, 6, 8, 10}; A ∩ B = {4, 6}; A ∖ B = {2}; Aᶜ = {1, 3, 5, 7, 8, 9, 10}; |𝒫(A)| = 2³ = 8; |A × B| = 3·4 = 12.
**A2.** ∅ ⊆ {1, 2}: yes (empty set is a subset of every set). ∅ ∈ {1, 2}: no (the elements are 1 and 2). ∅ ∈ {∅}: yes (the only element of {∅} is ∅).
**A3.** Injective: yes (2a = 2b ⇒ a = b). Surjective: no (1 is not hit). Range: the even integers.
**A4.** (a) reflexive, transitive, not symmetric. (b) all three: it is an equivalence relation (same parity). (c) symmetric only: not reflexive (a = a fails), not transitive (1 ≠ 2, 2 ≠ 1, but 1 = 1).
**A5.** (a) yes; (b) no under the strict grammar of Z3.6.2 (binary connectives need parentheses; many books allow dropping the outermost pair, which is why we say "under the strict grammar"); (c) yes: ¬¬P is ¬ applied to the formula ¬P; (d) no: ¬ needs a formula after it.

---

---

# Chapter Z4. The Symbol Atlas: every sign you will meet

Logic is written in symbols. The same idea is often written in several different ways by different authors, and the same symbol sometimes means different things in different books. This chapter is the dictionary. Use it in three ways:

1. **First reading:** skim to see the symbols once.
2. **Whenever you meet an unknown sign** anywhere in the course: look it up here.
3. **When reading other books:** use the "variants" columns and the tables in Z4.11 (ambiguities) and Z5 (dialects).

**Columns:** *Symbol*; *Name*; *Read aloud*; *Meaning*; *Variants* (other signs for the same idea); *LaTeX* (how to typeset it); *Unicode* (code point, so you can type or copy it).

---

## Z4.1 The core connectives (propositional logic)

| Symbol | Name | Read aloud | Meaning | Variants | LaTeX | Unicode |
|---|---|---|---|---|---|---|
| `¬A` | **negation** | "not A", "it is not the case that A" | true exactly when A is false | `~A`, `∼A`, `-A`, `!A` (programming), `Ā` (overbar, Boolean algebra), `A′` (prime, Boolean algebra), `NOT A`, `Np` (Polish) | `\neg A`, `\lnot A` | U+00AC |
| `A ∧ B` | **conjunction** | "A and B" | true exactly when both are true | `A & B`, `A · B`, `A . B`, `AB` (juxtaposition), `A && B`, `A AND B`, `K A B` (Polish) | `A \wedge B`, `A \land B` | U+2227 |
| `A ∨ B` | **disjunction** (inclusive or) | "A or B", "A or B or both", "A vel B" | true when at least one is true | `A \| B`, `A + B` (Boolean algebra), `A \|\| B`, `A OR B`, `A A B` (Polish "Apq") | `A \vee B`, `A \lor B` | U+2228 |
| `A → B` | **conditional** (material implication) | "if A then B", "A implies B", "A arrow B" | false only when A is true and B is false | `A ⊃ B` (older books), `A ⇒ B`, `A ⟶ B`, `A -> B`, `A => B`, `A ≤ B` (Boolean order), `C A B` (Polish) | `A \to B`, `A \rightarrow B`, `A \supset B`, `A \Rightarrow B`, `A \implies B` | U+2192 (also U+2283 ⊃, U+21D2 ⇒, U+27F6 ⟶) |
| `A ↔ B` | **biconditional** | "A if and only if B", "A iff B", "A is equivalent to B" | true exactly when A and B have the same truth value | `A ≡ B` (older books), `A ⇔ B`, `A <-> B`, `A <=> B`, `A ~ B`, `A XNOR B`, `E A B` (Polish) | `A \leftrightarrow B`, `A \iff B`, `A \Leftrightarrow B`, `A \equiv B` | U+2194 (also U+21D4 ⇔, U+2261 ≡) |
| `A ⊕ B` | **exclusive or** (xor) | "A xor B", "either A or B but not both" | true exactly when A and B differ | `A ⊻ B`, `A ≢ B`, `A ≠ B` (on truth values), `A ^ B` (bitwise in C/Java/Python), `A XOR B` | `A \oplus B`, `A \veebar B`, `A \not\equiv B` | U+2295 (⊕), U+22BB (⊻) |
| `A ↑ B` | **NAND**, Sheffer stroke | "A nand B", "not both A and B" | `¬(A ∧ B)` | `A \| B` (Sheffer's original stroke!), `A ⊼ B` | `A \uparrow B`, `A \barwedge B` (⊼) | U+2191, U+22BC |
| `A ↓ B` | **NOR**, Peirce arrow | "A nor B", "neither A nor B" | `¬(A ∨ B)` | `A ⊽ B` | `A \downarrow B` | U+2193, U+22BD |
| `⊤` | **verum**, "true", top | "top", "true" | a statement that is always true | `T`, `1`, `tt`, `True`, `⊤` | `\top` | U+22A4 |
| `⊥` | **falsum**, "false", absurdity, bottom | "bottom", "falsum", "absurd", "contradiction" | a statement that is always false | `F`, `0`, `ff`, `False`, `⊥`, `λ` (older), `#` (some natural-deduction books) | `\bot` | U+22A5 |
| `A ← B` | **converse conditional** | "A if B" | `B → A` | `A ⊂ B` (older books) | `A \leftarrow B`, `A \subset B` | U+2190 |
| `A ↛ B` | **non-implication** | "A and not B" | `¬(A → B)`, i.e. `A ∧ ¬B` | `A ⊅ B` | `A \nrightarrow B` | U+219B |
| `( )` `[ ]` `{ }` | **brackets** | | group subformulas | dots as brackets in *Principia* style | `( )` | U+0028... |

### Z4.1.1 Where the variants come from

- **¬ vs ~:** `~` is the ASCII tilde, the usual keyboard substitute for ¬. Frege used a small vertical stroke; Russell and Whitehead wrote `~p`; Heyting wrote `¬p`.
- **∧ vs & vs ·:** Boole (and Boolean algebra, electrical engineering) used multiplication: `AB` or `A·B`. Principia used the dot. Hilbert wrote `&`. Modern logic uses ∧, which looks like the "intersection" ∩ turned sharp.
- **∨ vs +:** from Latin *vel* ("or"). Boolean algebra writes `A + B`. In Boolean algebra `1 + 1 = 1`, since "true or true" is true.
- **→ vs ⊃ vs ⇒:** Peano and Russell introduced ⊃ (a reversed "C" for "consequence"). Modern logic prefers →. In many books **⇒** is the *metalanguage* "implies" between *statements about statements* (see Z4.5), while → is the object-language connective.
- **↔ vs ≡ vs ⇔:** similarly. `≡` in older books is the biconditional connective; in modern books it often means "logically equivalent" (a metalanguage claim), and ⇔ often means "iff" in mathematical prose.

### Z4.1.2 Names of the parts

| Compound | Parts are called |
|---|---|
| `¬A` | **negand** (A) |
| `A ∧ B` | **conjuncts** (A and B) |
| `A ∨ B` | **disjuncts** (A and B) |
| `A → B` | **antecedent** (A, the "if" part, also called *hypothesis* or *premise*) and **consequent** (B, the "then" part, also called *conclusion*) |
| `A ↔ B` | the two **sides** (left and right) |
| main connective | the connective that was applied last when building the formula (the root of the parse tree) |

---

## Z4.2 Quantifiers, binders, and related symbols (predicate logic)

| Symbol | Name | Read aloud | Meaning | Variants | LaTeX | Unicode |
|---|---|---|---|---|---|---|
| `∀x A` | **universal quantifier** | "for all x, A", "for every x", "for each x", "for any x" | A holds for every object x in the domain | `(x) A` (*Principia*, Quine), `(∀x) A`, `∀x. A`, `∀x : A`, `⋀ₓ A`, `Πx A` (Polish/Łukasiewicz-Bocheński style), `ALL x A` (Prover9), `![X]: A` (TPTP), `forall x, A` (Coq) | `\forall x\, A` | U+2200 |
| `∃x A` | **existential quantifier** | "there exists x such that A", "for some x, A", "there is an x with A" | A holds for at least one x in the domain | `(∃x) A`, `(Ex) A`, `∃x. A`, `⋁ₓ A`, `Σx A`, `EX x A`, `?[X]: A` (TPTP), `exists x, A` (Coq) | `\exists x\, A` | U+2203 |
| `∃!x A` | **unique existence** | "there exists exactly one x such that A" | exactly one x satisfies A | `∃₁x A`, `∃!x. A` | `\exists! x\, A` | U+2203 + U+0021 |
| `∄x A` | **non-existence** | "there is no x such that A" | `¬∃x A` | | `\nexists x\, A` | U+2204 |
| `∀x ∈ S, A` | **bounded (restricted) universal** | "for all x in S, A" | shorthand for `∀x (x ∈ S → A)` | `(∀x ∈ S) A`, `∀x:S. A` | `\forall x \in S,\ A` | |
| `∃x ∈ S, A` | **bounded existential** | "there is an x in S such that A" | shorthand for `∃x (x ∈ S ∧ A)` | `(∃x ∈ S) A` | `\exists x \in S,\ A` | |
| `ιx A` or `℩x A` | **definite description** (iota operator) | "the x such that A" | the unique x satisfying A (if there is one) | `ι`, `℩`, `the x. A` | `\iota x\, A` | U+03B9, U+2129 |
| `εx A` | **Hilbert's epsilon operator** | "some x such that A" | an arbitrary witness for ∃x A | `ε` | `\varepsilon x\, A` | U+03B5 |
| `λx. t` | **lambda abstraction** | "lambda x, t" | the function that maps x to t | `x ↦ t`, `\x -> t` (Haskell), `fun x => t` (Lean, Coq) | `\lambda x.\ t` | U+03BB |
| `μx A` | **least-number operator** | "the least x such that A" | the smallest natural number satisfying A | `μ` | `\mu x\, A` | U+03BC |
| `{ x : A }` | **set-builder** | "the set of all x such that A" | the set whose members are exactly the x satisfying A | `{x \| A}` | `\{x : A\}`, `\{x \mid A\}` | |
| `∑ᵢ₌₁ⁿ`, `∏ᵢ₌₁ⁿ` | **sum, product binders** | "the sum from i = 1 to n" | bind a running variable i | | `\sum_{i=1}^n`, `\prod_{i=1}^n` | U+2211, U+220F |
| `⋃ᵢ`, `⋂ᵢ` | **big union / intersection** | "union over i" | ∃i / ∀i over a family of sets | | `\bigcup_i`, `\bigcap_i` | U+22C3, U+22C2 |

**All binders do the same job:** they introduce a *bound* variable whose name does not matter (`∀x P(x)` and `∀y P(y)` say the same). See Chapter 3.3.

**Quantifier scope conventions differ.** After `∀x`, some authors apply the quantifier only to the *next* immediate formula (as with ¬); others extend it as far to the right as possible. Always parenthesize: `∀x (P(x) → Q(x))`.

---

## Z4.3 Symbols of consequence, proof and metalanguage

These symbols are **not** part of the formulas. They are used to *talk about* formulas (**metalanguage**).

| Symbol | Name | Read aloud | Meaning | LaTeX | Unicode |
|---|---|---|---|---|---|
| `Γ ⊢ A` | **turnstile**, derivability | "Gamma proves A", "A is derivable from Γ" | there is a formal proof of A from the premises Γ | `\Gamma \vdash A` | U+22A2 |
| `⊢ A` | **theoremhood** | "A is a theorem", "A is provable" | A is provable from no premises | `\vdash A` | U+22A2 |
| `Γ ⊬ A` | | "Γ does not prove A" | no proof exists | `\nvdash` | U+22AC |
| `A ⊣⊢ B` | **interderivability** | "A and B are provably equivalent" | `A ⊢ B` and `B ⊢ A` | `A \dashv\vdash B` | U+22A3 U+22A2 |
| `Γ ⊨ A` | **double turnstile**, semantic consequence | "Gamma entails A", "A is a logical consequence of Γ", "Γ semantically implies A" | every model of Γ is a model of A | `\Gamma \models A`, `\vDash` | U+22A8 (also U+22A7) |
| `⊨ A` | **validity** | "A is valid", "A is a tautology" | A is true in every model | `\models A` | U+22A8 |
| `Γ ⊭ A` | | "Γ does not entail A" | some model makes Γ true and A false | `\nvDash` | U+22AD |
| `M ⊨ A` | **satisfaction** | "M satisfies A", "A is true in M", "M is a model of A" | A is true in the structure M | `\mathcal{M} \models A` | U+22A8 |
| `M, s ⊨ A` | satisfaction under an assignment | "A is true in M under assignment s" | for formulas with free variables | `\mathcal{M}, s \models A` | |
| `⟦A⟧ᵥ`, `v(A)`, `⟦A⟧_M` | **denotation / valuation** | "the truth value of A under v" | semantic value | `[\![A]\!]_v` (stmaryrd), `\llbracket A \rrbracket_v` | U+27E6 U+27E7 |
| `⊩` | **forcing** | "forces" | used in Kripke semantics, set theory | `\Vdash` | U+22A9 |
| `A ≡ B` | **logical equivalence** | "A is logically equivalent to B" | `⊨ A ↔ B` | `A \equiv B` | U+2261 |
| `Γ, A` | comma in a premise list | | the set Γ together with A: `Γ ∪ {A}` | | |
| `Γ ⇒ Δ` | **sequent arrow** (Gentzen) | "Γ sequent Δ" | in sequent calculus: if all of Γ hold, then some of Δ holds | `\Gamma \Rightarrow \Delta` | U+21D2 |
| `Γ ⊢ Δ` | sequent, alternate | | (many books write the turnstile for sequents) | | |
| `⇒`, `⟹` | **metalanguage implication** | "implies", "then" | between *statements about formulas* | `\Rightarrow`, `\implies` | U+21D2, U+27F9 |
| `⇔`, `⟺` | **metalanguage iff** | "if and only if" | | `\Leftrightarrow`, `\iff` | U+21D4, U+27FA |
| `∴` | therefore | "therefore" | introduces a conclusion | `\therefore` | U+2234 |
| `∵` | because | "because", "since" | introduces a reason | `\because` | U+2235 |
| `∎` | end of proof | | marks the end of a proof | `\qed`, `\blacksquare`, `\square` | U+220E (∎), U+25A0 (■), U+25A1 (□) |
| `⊦` | **Frege's judgement stroke** | "it is asserted that" | historical | | U+22A6 |

### Z4.3.1 Reading the notations out loud

- `A ⊢ B` — "A proves B".
- `A, B ⊢ C` — "from A and B one can prove C" (comma = both premises).
- `⊢ A → A` — "A implies A is a theorem" (it can be proved with no premises).
- `Γ ⊨ A` — "every model of Γ makes A true".
- `A₁, ..., Aₙ ⊢ B` — an argument or *sequent* with n premises and a conclusion.

### Z4.3.2 ⊢ versus ⊨ versus → versus ⇒ (the confusion table)

| Sign | Level | What it relates | Example |
|---|---|---|---|
| `→` | object language (inside formulas) | two **formulas**, forming a new formula | `P → Q` is itself a formula |
| `⇒` (or `⟹`) | metalanguage | two **statements about the world/logic** | "if A is a tautology, then A ∨ B is a tautology" |
| `⊢` | metalanguage | a **set of formulas** and a formula: *provable* | `P, P → Q ⊢ Q` |
| `⊨` | metalanguage | a **set of formulas** and a formula: *true in all models* | `P, P → Q ⊨ Q` |
| `≡` | metalanguage (usually) | two formulas: *same truth value always* | `P → Q ≡ ¬P ∨ Q` |
| `↔` | object language | two formulas, forming a new formula | `P ↔ Q` |

---

## Z4.4 The many signs of "equals", "defined as", and "equivalent"

| Symbol | Meaning | Where |
|---|---|---|
| `=` | equality: the two things are the very same object | everywhere |
| `≠` | not equal | |
| `:=`, `≔`, `=:`, `≝`, `≜`, `\overset{\text{def}}{=}` | "is defined to be" | definitions |
| `:⇔`, `⇔ (def)` | "is defined to hold iff" | defining a property |
| `≡` | (i) logical equivalence, (ii) congruence mod n, (iii) "identical as functions/polynomials", (iv) sometimes defined-as | context! |
| `≈` | approximately equal | numerics |
| `≅` | isomorphic or congruent (as structures or shapes) | algebra, model theory, geometry |
| `≃` | homotopy equivalent, or asymptotically equal, or isomorphic | |
| `∼` | "is related to"; in probability "is distributed as"; in logic sometimes negation (`∼p`) | |
| `∝` | proportional to | |
| `↔`, `⇔` | iff | logic |
| `≐` | "is equal in the limit" or "by definition" | |
| `==` | equality *test* in programming | Python, Java, C |
| `===` | strict equality (JavaScript), definitional equality (some proof assistants) | |
| `=?=`, `≟` | "is this equal?" (question) | |

---

## Z4.5 Sets, functions, relations

(Defined in Z3. This is the compact atlas.)

| Symbol | Name | Read aloud | Variants | LaTeX | Unicode |
|---|---|---|---|---|---|
| `∈` | element of | "in", "belongs to" | `ε` (Peano's original form of the symbol) | `\in` | U+2208 |
| `∉` | not an element of | "not in" | | `\notin` | U+2209 |
| `∋` | contains as an element | "such that" in some texts | | `\ni` | U+220B |
| `∅` | empty set | "empty set" | `{}`, `Ø`, `∅` | `\emptyset`, `\varnothing` | U+2205 |
| `⊆` | subset or equal | "is a subset of" | `⊂`, `⊑` | `\subseteq`, `\subset` | U+2286, U+2282 |
| `⊊` | proper subset | | `⊂` | `\subsetneq` | U+228A |
| `⊇`, `⊃` | superset | | | `\supseteq`, `\supset` | U+2287, U+2283 |
| `⊄`, `⊈` | not a subset | | | `\not\subset`, `\nsubseteq` | U+2284, U+2288 |
| `∪` | union | "cup" | | `\cup` | U+222A |
| `∩` | intersection | "cap" | | `\cap` | U+2229 |
| `∖`, `−`, `\` | set difference | "minus" | | `\setminus` | U+2216 |
| `Aᶜ`, `A′`, `Ā`, `∁A` | complement | "A complement" | | `A^c`, `A'`, `\overline{A}`, `\complement` | U+1D9C, U+2201 |
| `△`, `⊕`, `Δ` | symmetric difference | | | `\triangle`, `\Delta`, `\oplus` | U+25B3, U+0394 |
| `×` | Cartesian product | "cross" | | `\times` | U+00D7 |
| `𝒫(A)`, `℘(A)`, `2^A` | power set | "power set of A" | `P(A)` | `\mathcal{P}(A)`, `\wp(A)`, `2^A` | U+1D4AB, U+2118 |
| `\|A\|`, `#A`, `card A` | cardinality | "size of A" | | `\lvert A \rvert`, `\#A` | |
| `f : A → B` | function type | "f from A to B" | `f ∈ B^A`, `A →ᶠ B` | `f \colon A \to B` | |
| `x ↦ f(x)` | maps-to | "x maps to f of x" | `x \|→ f(x)` | `x \mapsto f(x)` | U+21A6 |
| `g ∘ f` | composition | "g after f", "g composed with f" | `g f`, `g·f` | `g \circ f` | U+2218 |
| `f⁻¹` | inverse / preimage | "f inverse" | | `f^{-1}` | |
| `↪` | injection (embedding) | | `↣`, `⤖` | `\hookrightarrow` | U+21AA |
| `↠` | surjection | | `⤀` | `\twoheadrightarrow` | U+21A0 |
| `⤖`, `≅`, `↔` | bijection | | | `\leftrightarrow`, `\cong` | |
| `ℕ ℤ ℚ ℝ ℂ ℙ` | number sets | "N, Z, Q, R, C, P" | `N`, `Z`, `Q`, `R`, `C` (plain bold) | `\mathbb{N}`, `\mathbb{Z}`, ... | U+2115, U+2124, U+211A, U+211D, U+2102, U+2119 |
| `ℵ₀`, `ω` | smallest infinite cardinal / ordinal | "aleph null", "omega" | `\|ℕ\|` | `\aleph_0`, `\omega` | U+2135, U+03C9 |
| `R(a, b)`, `a R b`, `(a, b) ∈ R` | relation holds | "a is R-related to b" | | | |
| `[a]`, `[a]_R`, `ā` | equivalence class of a | | | `[a]_R` | |
| `a ≤ b`, `a ≼ b`, `a ⊑ b` | order | | `\le`, `\preceq`, `\sqsubseteq` | | U+2264, U+227C |

---

## Z4.6 Arithmetic and number-theory symbols

| Symbol | Name | Meaning | LaTeX | Unicode |
|---|---|---|---|---|
| `+`, `−`, `×`, `·`, `÷`, `/` | arithmetic operations | add, subtract, multiply, divide | `+`, `-`, `\times`, `\cdot`, `\div`, `/` | U+00D7, U+22C5, U+00F7 |
| `aⁿ`, `a^n`, `a**n` | exponent | a multiplied n times | `a^n` | U+207F (ⁿ) |
| `√`, `ⁿ√` | root | square root, n-th root | `\sqrt{a}`, `\sqrt[n]{a}` | U+221A |
| `<`, `>`, `≤`, `≥`, `≠` | order and non-equality | | `<`, `>`, `\leq`, `\geq`, `\neq` | U+2264, U+2265, U+2260 |
| `≪`, `≫` | much smaller / larger | | `\ll`, `\gg` | U+226A, U+226B |
| `a ∣ b` | divides | b is a multiple of a | `a \mid b` | U+2223 (also ASCII `\|`) |
| `a ∤ b` | does not divide | | `a \nmid b` | U+2224 |
| `a ≡ b (mod n)`, `a ≡ₙ b` | congruence modulo n | n divides a − b | `a \equiv b \pmod n` | U+2261 |
| `a mod n`, `a % n` | remainder | the remainder of a ÷ n | `a \bmod n` | |
| `gcd(a, b)`, `lcm(a, b)` | greatest common divisor, least common multiple | | `\gcd`, `\operatorname{lcm}` | |
| `n!` | factorial | n·(n−1)···1 | `n!` | |
| `(n over k)` = `C(n, k)` | binomial coefficient | "n choose k" | `\binom{n}{k}` | |
| `∑`, `∏` | sum, product | | `\sum`, `\prod` | U+2211, U+220F |
| `\|x\|` | absolute value (or cardinality, or divides) | | `\lvert x \rvert` | |
| `⌊x⌋`, `⌈x⌉` | floor, ceiling | | `\lfloor x \rfloor`, `\lceil x \rceil` | U+230A.., U+2308.. |
| `∞` | infinity | | `\infty` | U+221E |
| `min`, `max`, `sup`, `inf` | extremes | | | |
| `lim` | limit | | `\lim_{x \to a}` | |

---

## Z4.7 Brackets, punctuation and layout

| Sign | Typical uses in logic |
|---|---|
| `( )` | grouping; function arguments `f(x)`; predicate arguments `P(x, y)`; ordered pairs `(a, b)` |
| `[ ]` | alternate grouping; intervals `[a, b]`; substitution `A[t/x]`; equivalence classes `[a]`; TPTP quantifier variable lists `![X]` |
| `{ }` | sets `{1, 2}`; set-builder `{x : P}`; grouping in LaTeX |
| `⟨ ⟩` | tuples `⟨a, b⟩`; sequences; structures `⟨D, I⟩`; inner products |
| `⟦ ⟧` | **semantic brackets**: denotation `⟦A⟧` |
| `⌜ ⌝` | **Gödel corner quotes**: `⌜A⌝` is the Gödel number (code) of formula A |
| `\| \|` | absolute value, cardinality, norm, "divides" (as one bar) |
| `.` (after a binder) | `∀x. A` the dot says "and now the body": scope extends as far right as possible |
| `:` (after a binder) | `∀x : A` or set-builder `{x : P}` |
| `,` | list separator; between premises (`A, B ⊢ C`); sometimes "and" (`x, y > 0`) |
| `;` | separator of different kinds of items (e.g., premises ; assumptions) |
| `⋯`, `…`, `...` | "and so on", ellipsis |
| `_` and `^` | subscript and superscript in text/LaTeX/ASCII (`x_1`, `x^2`) |
| `'` , `″` | prime marks to create new names (`x'`, `x''`) |
| `/` | in substitution `A[t/x]`: "replace x by t" (some books write `A[x/t]`: **check the convention!**) |
| `→` inside `[ ]` | `A[x ↦ t]` or `A[t/x]` or `A(x := t)` or `A{t/x}`: all mean "substitute t for x" |

**Substitution notation varies.** The following all mean "A with t substituted for the free occurrences of x": `A[t/x]`, `A(t/x)`, `A_x[t]`, `A[x := t]`, `A[x ↦ t]`, `A{x ↦ t}`, `{x/t}A`, `A(t)` (if A has been written as A(x)). In this course we use **A[t/x]**.

---

## Z4.8 Letters: the conventional use of Latin and Greek symbols

These are *habits*, not laws. Always trust the author's declaration.

| Letters | Typical meaning in logic |
|---|---|
| `p, q, r, s, t` | **propositional variables** (atoms), also `P, Q, R, S` |
| `A, B, C, D` | **metavariables for arbitrary formulas**: "for any formulas A and B, A ∧ B is a formula" |
| `φ, ψ, χ, θ` (phi, psi, chi, theta) | metavariables for formulas (phi is most common); `φ(x)` is a formula with x free |
| `Γ, Δ` (Gamma, Delta) | **sets (or lists) of formulas**; Γ = premises, Δ = conclusions (sequents) |
| `Σ, Π, Φ, Ψ` | other sets of formulas, **theories**; Σ sometimes the **alphabet** or **signature** |
| `T` | a **theory** (a set of sentences) |
| `x, y, z, u, v, w` | **individual variables** |
| `a, b, c, d, e` | **individual constants** (names of particular objects); also `c₀, c₁, ...` |
| `f, g, h` | **function symbols**; `f(x, y)` |
| `P, Q, R, S, F, G, H` | **predicate (relation) symbols**; `P(x)`, `R(x, y)` |
| `s, t, u` | **terms** (when not variables) |
| `α, β, γ, δ` | other formulas, ordinals (`α, β, γ`), or small quantities (`ε, δ`) |
| `ε` (epsilon) | a small positive number in analysis; the **empty string**; Hilbert's choice operator |
| `δ` (delta) | a small positive number in analysis |
| `σ, τ, ρ` (sigma, tau, rho) | **substitutions**, **assignments**, **valuations**, or **signatures** |
| `θ, μ` | substitutions; "most general unifier" is often `θ` or `μ` |
| `v, w, ν` | **valuations** (assignments of truth values) |
| `M, N, 𝔄, 𝔅, 𝒜, ℳ` | **structures (models)**; domain written `D`, `\|M\|`, `dom(M)`, or `A` |
| `I`, `·ᴹ`, `Pᴹ` | **interpretation function**; `Pᴹ` is the relation that P denotes in M |
| `λ` | lambda (functions); the empty string in some books |
| `ω` (omega) | the first infinite ordinal (the order type of ℕ); ℕ as a structure |
| `ℵ` (aleph) | infinite cardinal numbers |
| `i, j, k, l, m, n` | **integers** (indices, counters, sizes) |
| `Σ*` | all strings over alphabet Σ |
| `⊤, ⊥` | true, false |
| `□, ◇` | **modal** operators: "necessarily", "possibly" (Z4.10) |

---

## Z4.9 Symbols with multiple meanings: the ambiguity table

This is where most beginner confusion hides.

| Sign | Meaning 1 | Meaning 2 | Meaning 3 |
|---|---|---|---|
| `⊃` | "implies" (older logic books) | superset | |
| `⊂` | proper subset | any subset (⊆) | "implied by" (older logic) |
| `≡` | logical equivalence | biconditional connective (older) | congruence mod n; "defined as" |
| `→` | conditional connective | function type `A → B` | "tends to" (limits), "maps to" |
| `⇒` | metalanguage implies | conditional connective | sequent arrow |
| `⇔` | metalanguage iff | biconditional | |
| `⊥` | falsum (contradiction) | perpendicular (geometry) | bottom element (lattices, types); independent |
| `⊤` | verum (true) | top element | |
| `~` | negation | "is distributed as"; "is similar to"; "is equivalent to" | tilde as approximate |
| `\|` | "such that" (set-builder) | "divides" | absolute value / cardinality; NAND (Sheffer stroke); "or" in programming |
| `(x)` before a formula | universal quantifier `∀x` | a function argument `f(x)` | |
| `+` | Boolean "or" | addition | exclusive or (modulo 2) |
| `·` or juxtaposition | Boolean "and" | multiplication | function application (`f x`) |
| `∘` | composition | ring/group operation | |
| `ε` | element of (historical `∈`) | small positive number | empty string; Hilbert's operator |
| `Δ` | symmetric difference | change / increment | Laplacian; a set of formulas (sequents) |
| `σ, ρ` | substitution | assignment / valuation | signature |
| `λ` | lambda abstraction | empty string | wavelength / eigenvalue |
| `Σ` | sum | alphabet / set of formulas | `Σ` classes in the arithmetical hierarchy |
| `Π` | product | universal quantifier (Polish style) | `Π` classes in the arithmetical hierarchy; dependent function type |
| `ω` | ℕ as an ordinal | omega-rule | angular frequency |
| `[x]` | equivalence class | substitution list / bracket grouping | integer part (floor) |
| `Γ` | set of premises | Gamma function; a context (type theory) | |
| `¯` (overbar) | negation (Boolean) | complement (sets) | complex conjugate; mean |

**How to survive this:** at the start of any text, look for a "Notation" section or the first definitions. When in doubt, ask yourself which *kind* of object each side of the sign is: formulas? sets? numbers? statements about formulas?

---

## Z4.10 Symbols of other logics (preview)

You will not need these for the core course, but you will meet them next.

| Symbol | Name | Reads | Logic |
|---|---|---|---|
| `□A` | box, necessity | "necessarily A" | modal logic (also "A holds in all accessible worlds") |
| `◇A` | diamond, possibility | "possibly A" | modal logic (`◇A ≡ ¬□¬A`) |
| `○A`, `X A` | next | "A holds at the next time step" | temporal logic (LTL) |
| `◇A`, `F A` | eventually, "future" | "A holds at some future time" | temporal logic |
| `□A`, `G A` | always, "globally" | "A holds at all future times" | temporal logic |
| `A U B` | until | "A holds until B holds" | temporal logic |
| `A ⊗ B` | tensor ("times") | "A and B together, both resources" | linear logic |
| `A ⅋ B` | par | | linear logic |
| `A ⊸ B` | linear implication ("lollipop") | "consume A to produce B" | linear logic |
| `!A`, `?A` | of course, why not | unlimited use of resource | linear logic |
| `A ⊕ B`, `A & B` | additive disjunction, conjunction | | linear logic |
| `⟨a⟩A`, `[a]A` | dynamic modalities | "after program a, possibly / necessarily A" | dynamic logic, Hoare-style reasoning |
| `{P} C {Q}` | Hoare triple | "if P holds before command C, then Q holds after" | program verification |
| `∀P` (P a predicate variable) | second-order quantifier | "for all properties P" | second-order logic |
| `Π x:A. B`, `Σ x:A. B` | dependent product / sum types | "for all x of type A, B" / "exists x of type A with B" | type theory (Curry-Howard) |
| `t : A` | typing judgment | "t has type A" / "t is a proof of A" | type theory |
| `Γ ⊢ t : A` | typing sequent | "in context Γ, t has type A" | type theory |
| `⇝`, `→_β` | reduction / rewriting | "reduces to" | λ-calculus |

---

## Z4.11 Reading formulas aloud

The skill of reading a formula in good English is the best test that you understand it.

| Formula | Reading |
|---|---|
| `P ∧ Q` | "P and Q" |
| `¬(P ∨ Q)` | "it is not the case that P or Q", "neither P nor Q" |
| `P → (Q → R)` | "if P, then (if Q then R)" |
| `(P ∧ Q) → R` | "if P and Q, then R" |
| `¬P ∨ Q` | "not P, or Q" |
| `∀x P(x)` | "for all x, P of x", "everything is P" |
| `∃x P(x)` | "there is an x such that P of x", "something is P" |
| `∀x (S(x) → P(x))` | "for every x, if S of x then P of x" = "every S is P" |
| `∃x (S(x) ∧ P(x))` | "there is an x such that S of x and P of x" = "some S is P" |
| `∀x ∃y R(x, y)` | "for every x there is a y such that R of x and y" |
| `∃y ∀x R(x, y)` | "there is a y such that for every x, R of x and y" |
| `∀ε>0 ∃δ>0 ∀x (\|x − a\| < δ → \|f(x) − f(a)\| < ε)` | "for every ε greater than zero there is a δ greater than zero such that for all x, if the distance from x to a is less than δ, then the distance from f of x to f of a is less than ε" |
| `Γ ⊢ A` | "Gamma proves A" |
| `Γ ⊨ A` | "Gamma entails A" |
| `⟦A⟧ᵥ = T` | "the value of A under v is true" |
| `A[t/x]` | "A with t substituted for x" |
| `∃!x P(x)` | "there is exactly one x such that P of x" |

### Try it: decode and encode

**Q1.** Read aloud (in plain English): (a) `¬∃x (P(x) ∧ ¬Q(x))` (b) `∀x ∀y (x < y → ∃z (x < z ∧ z < y))` (c) `A, B ⊢ A ∧ B`.
**Q2.** Write in symbols: (a) "No S is P." (b) "If it rains or snows, the game is cancelled." (c) "Every number has a successor."
**Q3.** Which sign: (i) "the empty set", (ii) "therefore", (iii) "is not a subset of", (iv) "is provable from", (v) "is true in every model of".
**Q4.** What is the difference between `A → B`, `A ⇒ B` and `A ⊢ B`?
**Q5.** Rewrite `P ⊃ (Q ≡ R)` (older style) in modern symbols.

**Answers.**
**A1.** (a) "It is not the case that there is something that is P and not Q" (= every P is Q). (b) "For all x and y, if x is less than y then there is a z strictly between them." (c) "From A and B one can prove A and B."
**A2.** (a) `∀x (S(x) → ¬P(x))` or `¬∃x (S(x) ∧ P(x))`. (b) `(R ∨ S) → C`. (c) `∀n ∃m (m = n + 1)` or `∀n ∃m Succ(n, m)`.
**A3.** (i) `∅`, (ii) `∴`, (iii) `⊄` (or `⊈`), (iv) `⊢`, (v) `⊨`.
**A4.** `A → B` is a *formula* (object language). `A ⇒ B` usually means "if A [is true / holds] then B" said *about* statements (metalanguage). `A ⊢ B` says that a *proof* of B from A exists.
**A5.** `P → (Q ↔ R)`.

---

---

# Chapter Z5. Dialects and formats: the same logic in many costumes

Logic has one core and many **costumes**. Two things vary from book to book and tool to tool:

1. **Notation dialects**: how formulas are *written* (which symbols, which precedence, prefix or infix).
2. **Proof formats**: how proofs are *laid out* (a table, a tree, a boxed list, a one-sided tableau, a set of clauses...).

Nothing in this chapter adds new logical power. Everything here is a different way to write down the same truths. The skill you want is **fluent translation**: when a book or tool uses a different costume, you recognize it and mentally convert.

---

## Z5.1 Notation dialects for formulas

### Z5.1.1 Precedence and associativity (how to drop brackets)

A formula like `P ∨ Q ∧ R` is ambiguous unless we agree on **binding strength**. The most common convention:

| Order (tightest first) | Connective |
|---|---|
| 1 | `¬` |
| 2 | `∧` |
| 3 | `∨` |
| 4 | `→` (right-associative) |
| 5 | `↔` |

So under this convention `¬P ∧ Q → R ∨ S` means `((¬P) ∧ Q) → (R ∨ S)`, and `P → Q → R` means `P → (Q → R)`.

**Quantifiers are the troublemakers.** Books disagree: some let `∀x` bind only the *next* formula (like ¬), so `∀x P(x) → Q(x)` means `(∀x P(x)) → Q(x)`; others let the scope extend *as far right as possible*, so the same string means `∀x (P(x) → Q(x))`. **This course uses the second convention** (Section 3.2), but you should never rely on it: **always parenthesize the body of a quantifier.**

**Warnings.**

- Some books give `∧` and `∨` equal strength, or make `→` left-associative. Programming languages differ again (in C, `&&` binds tighter than `||`, as here, but there is no implication operator).
- `∧` and `∨` are associative, so `P ∧ Q ∧ R` is harmless. But `→` is **not** associative: `(P → Q) → R` and `P → (Q → R)` are different formulas.
- **Rule for this course:** whenever in doubt, add brackets. Brackets are free.

### Z5.1.2 Infix, prefix, postfix

| Style | Example for "(P and Q) implies R" | Where used |
|---|---|---|
| **Infix** (operator between) | `(P ∧ Q) → R` | standard mathematics |
| **Prefix / Polish** (operator first) | `→ ∧ P Q R` | Łukasiewicz, Lisp-like systems, SMT-LIB, parsers |
| **Postfix / Reverse Polish** | `P Q ∧ R →` | stack machines, calculators |
| **Fully parenthesized prefix (S-expression)** | `(=> (and P Q) R)` | SMT-LIB, Lisp |

Prefix and postfix need **no brackets and no precedence rules**: the structure is determined by the arity of each symbol.

### Z5.1.3 Łukasiewicz (Polish) notation

Jan Łukasiewicz (1920s) used capital letters as prefix operators:

| Letter | Connective | Mnemonic |
|---|---|---|
| `N` | ¬ | **N**egation |
| `K` | ∧ | **K**onjunktion |
| `A` | ∨ | **A**lternative |
| `C` | → | **C**onditional (implication) |
| `E` | ↔ | **E**quivalence |
| `D` | ↑ (NAND) | **D**isjunction in Sheffer's sense |
| `J` | ⊕ (xor, in some texts) | |
| `Π`, `Σ` | ∀, ∃ | |

Atoms are lowercase: `p, q, r`.

| Standard | Polish |
|---|---|
| `p → q` | `Cpq` |
| `¬p` | `Np` |
| `p ∧ q` | `Kpq` |
| `(p ∧ q) → r` | `CKpqr` |
| `p → (q → r)` | `CpCqr` |
| `¬(p ∨ q) ↔ (¬p ∧ ¬q)` | `ENApqKNpNq` |

**How to read Polish notation:** scan left to right; every operator "demands" its arguments: `C` wants two formulas. `CKpqr`: C takes (1) `Kpq` and (2) `r`. `K` takes `p` and `q`.

### Z5.1.4 Principia Mathematica (dot notation)

Whitehead and Russell avoided brackets by using **dots** whose number indicates the strength of the grouping.

| Meaning | *Principia* style |
|---|---|
| p and q | `p . q` |
| p or q | `p ∨ q` |
| p implies q | `p ⊃ q` |
| p iff q | `p ≡ q` |
| not p | `~p` |
| for all x | `(x)` |
| there exists x | `(∃x)` |
| `(p ∨ q) ⊃ r` | `p ∨ q . ⊃ . r` |

You rarely meet dots today, but ⊃, ≡, `~` and `(x)` survive in philosophy texts and older papers.

### Z5.1.5 Boolean-algebra / engineering dialect

| Logic | Boolean algebra |
|---|---|
| `P ∧ Q` | `P·Q` or `PQ` |
| `P ∨ Q` | `P + Q` |
| `¬P` | `P̄` or `P'` |
| `⊤`, `⊥` | `1`, `0` |
| `P ⊕ Q` | `P ⊕ Q` |
| `P → Q` | `P̄ + Q` (no special symbol; you write out the disjunction) |

Laws look like arithmetic but are not identical: in Boolean algebra `P + P = P` and `P + 1 = 1`.

### Z5.1.6 ASCII and keyboard dialects

| Concept | Common ASCII | Python | C/Java/JS | Haskell |
|---|---|---|---|---|
| not | `~P`, `-P`, `!P` | `not P` | `!P` | `not p` |
| and | `P & Q`, `P /\ Q`, `P && Q` | `P and Q` | `P && Q` | `p && q` |
| or | `P \| Q`, `P \/ Q`, `P \|\| Q` | `P or Q` | `P \|\| Q` | `p \|\| q` |
| implies | `P -> Q`, `P => Q` | `(not P) or Q` (no operator) | `!P \|\| Q` | `not p \|\| q`, or `p <= q` on `Bool` |
| iff | `P <-> Q`, `P <=> Q` | `P == Q` (on bools) | `P == Q` | `p == q` |
| xor | `P ^ Q`, `P xor Q` | `P != Q`, `P ^ Q` | `P ^ Q` | `p /= q` |
| true / false | `true`/`false`, `T`/`F` | `True`/`False` | `true`/`false` | `True`/`False` |

**Warning on programming languages.** In programs `&&` and `||` are usually **short-circuit** (they may skip evaluating the second argument), which has no counterpart in logic; and `P -> Q` is often *not* an implication at all (in C, `->` is field access; in Haskell, `->` is the function type). Programming "if" is control flow, not the logical conditional.

### Z5.1.7 Theorem-prover input languages (a preview of Appendix E)

| Concept | TPTP (FOF) | Prover9 / Mace4 | SMT-LIB 2 | Lean 4 | Coq / Rocq |
|---|---|---|---|---|---|
| not | `~ P` | `- P` | `(not P)` | `¬ P` or `Not P` | `~ P` |
| and | `P & Q` | `P & Q` | `(and P Q)` | `P ∧ Q` or `P /\ Q` | `P /\ Q` |
| or | `P \| Q` | `P \| Q` | `(or P Q)` | `P ∨ Q` or `P \/ Q` | `P \/ Q` |
| implies | `P => Q` | `P -> Q` | `(=> P Q)` | `P → Q` or `P -> Q` | `P -> Q` |
| iff | `P <=> Q` | `P <-> Q` | `(= P Q)` | `P ↔ Q` or `P <-> Q` | `P <-> Q` |
| forall | `![X]: P(X)` | `all x P(x)` | `(forall ((x S)) (P x))` | `∀ x, P x` | `forall x, P x` |
| exists | `?[X]: P(X)` | `exists x P(x)` | `(exists ((x S)) (P x))` | `∃ x, P x` | `exists x, P x` |
| equals | `X = Y` | `x = y` | `(= x y)` | `x = y` | `x = y` |
| not equal | `X != Y` | `x != y` | `(distinct x y)` | `x ≠ y` | `x <> y` |

Conventions: in TPTP, variables start with an **uppercase** letter, constants and predicates with lowercase; in Prover9, variables are the lowercase letters `u`-`z` by default. We study these in detail in Appendix E and Chapter 8.

### Z5.1.8 Typesetting dialects: LaTeX vs Unicode vs plain text

| You want | LaTeX source | Unicode text | Plain ASCII |
|---|---|---|---|
| ∀x ∃y (x < y) | `\forall x\, \exists y\, (x < y)` | `∀x ∃y (x < y)` | `forall x exists y (x < y)` |
| P → Q | `P \to Q` | `P → Q` | `P -> Q` |
| Γ ⊢ A | `\Gamma \vdash A` | `Γ ⊢ A` | `G \|- A` |
| ¬(A ∧ B) | `\neg (A \wedge B)` | `¬(A ∧ B)` | `~(A & B)` |

For notes, Unicode is easiest (copy from Z4). For papers, LaTeX. For machines, ASCII or the tool's own syntax.

---

## Z5.2 Proof formats: an overview

A **proof format** (or **proof system**, **calculus**) fixes the rules of the game: what a legal proof line looks like and how lines may be combined. The main families:

| # | Format | Main idea | Natural for |
|---|---|---|---|
| 1 | **Semantic / truth tables** | try every valuation | propositional, small |
| 2 | **Informal mathematical proof** | prose reasoning in steps | humans, mathematics |
| 3 | **Hilbert (axiomatic) system** | many axioms, one or two rules (modus ponens) | metatheory, theory |
| 4 | **Natural deduction: tree (Gentzen)** | intro/elim rules arranged as a tree | proof theory, Curry-Howard |
| 5 | **Natural deduction: Fitch (flag/box)** | indented boxes for subproofs | teaching, this course |
| 6 | **Natural deduction: Lemmon (numbered with dependency sets)** | each line lists the assumptions it depends on | British-tradition textbooks |
| 7 | **Sequent calculus** | judgments `Γ ⇒ Δ` and rules acting on them; proof search by decomposition | proof theory, automated search |
| 8 | **Analytic tableaux** | refute by growing a tree of consequences | hand-checking validity, automated provers |
| 9 | **Resolution** | refute a set of clauses by resolving pairs | automated theorem proving |
| 10 | **Equational / calculational proof** | chain of equivalences, each justified | algebra, program derivation |
| 11 | **Type-theoretic (proof terms, tactics)** | proofs as programs; scripts that build them | Lean, Coq, Agda |

We now show **one running example** in all of them.

**Running example (hypothetical syllogism).** From `P → Q` and `Q → R`, conclude `P → R`.
In sequent notation: `P → Q, Q → R ⊢ P → R`.

---

## Z5.3 The running example in every format

### Format 1. Truth table (semantic)

We want to show `{P → Q, Q → R} ⊨ P → R`: every row making both premises true makes the conclusion true. There are 2³ = 8 rows.

| P | Q | R | P→Q | Q→R | P→R | premises both true? |
|---|---|---|---|---|---|---|
| T | T | T | T | T | T | yes, conclusion T ✓ |
| T | T | F | T | F | F | no |
| T | F | T | F | T | T | no |
| T | F | F | F | T | F | no |
| F | T | T | T | T | T | yes, conclusion T ✓ |
| F | T | F | T | F | T | no |
| F | F | T | T | T | T | yes, conclusion T ✓ |
| F | F | F | T | T | T | yes, conclusion T ✓ |

Every row that makes both premises true makes the conclusion true. So the entailment holds. This shows **⊨**, not **⊢** (it is not a derivation), and it does not scale to predicate logic (infinitely many structures).

### Format 2. Informal mathematical proof

> **Claim.** If `P → Q` and `Q → R`, then `P → R`.
> **Proof.** Assume `P → Q` and `Q → R`. To show `P → R`, assume `P`. By `P → Q` and `P` we get `Q`. By `Q → R` and `Q` we get `R`. Since assuming `P` led to `R`, we conclude `P → R`. ∎

This is the style of real mathematics. Every step is secretly an instance of a formal rule (modus ponens, then implication introduction).

### Format 3. Hilbert-style (axiomatic)

Axiom schemes (for the `→` fragment):

- **K:** `A → (B → A)`
- **S:** `(A → (B → C)) → ((A → B) → (A → C))`

Single rule: **modus ponens (MP):** from `A` and `A → B`, infer `B`.

| # | Line | Justification |
|---|---|---|
| 1 | `Q → R` | premise |
| 2 | `(Q → R) → (P → (Q → R))` | axiom K (A := Q→R, B := P) |
| 3 | `P → (Q → R)` | MP 1, 2 |
| 4 | `(P → (Q → R)) → ((P → Q) → (P → R))` | axiom S (A := P, B := Q, C := R) |
| 5 | `(P → Q) → (P → R)` | MP 3, 4 |
| 6 | `P → Q` | premise |
| 7 | `P → R` | MP 6, 5 |

Notice how unnatural this is: no assumptions can be made "temporarily". Hilbert systems are **short to specify** (good for proving metatheorems) but **painful to use**. The **Deduction Theorem** (Chapter 6) repairs this: it proves that if `Γ, A ⊢ B` then `Γ ⊢ A → B`, which is exactly what natural deduction builds in.

### Format 4. Natural deduction, Gentzen tree style

Each inference is a horizontal line; premises above, conclusion below; a bracketed `[P]¹` is a discharged assumption and the superscript names the rule that discharges it.

```
             [P]¹   P → Q
             ──────────── →E
                  Q            Q → R
                  ─────────────────── →E
                            R
                  ─────────────────── →I¹
                          P → R
```

Read bottom-up: to get `P → R`, use `→I` discharging assumption 1 (`P`); this needs `R`; get `R` by `→E` from `Q` and `Q → R`; get `Q` by `→E` from `P` and `P → Q`. Premises `P → Q` and `Q → R` remain open (undischarged) hypotheses of the whole proof.

### Format 5. Natural deduction, Fitch style (used in this course)

```
1 │ P → Q                 premise
2 │ Q → R                 premise
3 │ ┌─ P                  assumption (for →I)
4 │ │  Q                  →E 1, 3
5 │ │  R                  →E 2, 4
6 │ └───
  │ P → R                 →I 3–5
```

The indented box (lines 3-5) is a **subproof**: inside it we may use `P`, but nothing derived inside escapes the box except through the closing rule (`→I`).

### Format 6. Natural deduction, Lemmon style

Each line carries the **set of premise line numbers it depends on** (left), a line number, the formula, and its justification.

```
{1}       (1)  P → Q    Premise
{2}       (2)  Q → R    Premise
{3}       (3)  P        Assumption
{1,3}     (4)  Q        1,3 →E (modus ponens)
{1,2,3}   (5)  R        2,4 →E
{1,2}     (6)  P → R    3,5 →I (conditional proof; discharges 3)
```

Line 6 depends on lines 1 and 2 only: the dependency on line 3 has been removed (discharged).

### Format 7. Sequent calculus (Gentzen's LK, two-sided)

A **sequent** `Γ ⇒ Δ` means: "if all formulas in Γ are true, then at least one in Δ is true". A proof is a tree of sequents whose leaves are **axioms** `A, Γ ⇒ A, Δ`. We search *bottom-up*:

```
                                       ─────────── ax            ───────────── ax
                                       Q, P ⇒ Q, R              R, Q, P ⇒ R
 ───────────────── ax                  ─────────────────────────────────────── →L
 P, Q→R ⇒ P, R                                  Q, P, Q→R ⇒ R
 ─────────────────────────────────────────────────────────────── →L
                   P, P→Q, Q→R ⇒ R
                   ──────────────────── →R
                   P→Q, Q→R ⇒ P→R
```

Reading bottom-up: `→R` moves the antecedent `P` to the left; `→L` on `P→Q` splits into two goals (prove `P`, or use `Q`); `→L` on `Q→R` again splits; every leaf closes by the axiom (the same formula appears on both sides). Each step only **decomposes** a formula, which is why sequent calculus is ideal for automatic proof search.

### Format 8. Analytic tableau (refutation tree)

To prove the entailment, assume the premises and the **negation** of the conclusion and look for a contradiction.

```
 P → Q                         (premise)
 Q → R                         (premise)
 ¬(P → R)                      (negated conclusion)
   │
   P                           (from ¬(P→R))
   ¬R                          (from ¬(P→R))
   ├── ¬P   ✗ (clashes with P)         (branch for P→Q)
   └── Q
        ├── ¬Q  ✗ (clashes with Q)     (branch for Q→R)
        └── R   ✗ (clashes with ¬R)
```

Rules used: `¬(A→B)` yields `A` and `¬B` (no branching); `A→B` branches into `¬A | B`. **Every branch closes**, so the premises together with `¬(P→R)` are unsatisfiable: the entailment holds.

### Format 9. Resolution

Convert premises and the negated conclusion to **clauses** (sets of literals; read as a disjunction):

| Clause | From |
|---|---|
| `{¬P, Q}` | `P → Q` |
| `{¬Q, R}` | `Q → R` |
| `{P}` | `¬(P → R)`, first part |
| `{¬R}` | `¬(P → R)`, second part |

Resolve (cancel a literal against its negation):

1. `{P}` and `{¬P, Q}` give `{Q}`
2. `{Q}` and `{¬Q, R}` give `{R}`
3. `{R}` and `{¬R}` give `{}` (the **empty clause** ⊥)

The empty clause means the clause set is unsatisfiable, so the entailment holds.

### Format 10. Equational / calculational proof

This format shines for **equivalences** rather than single entailments. Example: the contrapositive law `P → Q ≡ ¬Q → ¬P`.

```
      P → Q
  ≡     { definition of → }
      ¬P ∨ Q
  ≡     { commutativity of ∨ }
      Q ∨ ¬P
  ≡     { double negation: Q ≡ ¬¬Q }
      ¬¬Q ∨ ¬P
  ≡     { definition of →, read right to left }
      ¬Q → ¬P
```

Each step says "this equals that, because of <law>" in braces. Chains of equivalences are transitive, so the first and last lines are equivalent.

### Format 11. Type-theoretic / proof assistant

Under Curry-Howard, a proof of `P → Q` **is** a function turning proofs of `P` into proofs of `Q`.

**Lean 4 (term mode):**

```lean
theorem hs (p q r : Prop) (h1 : p → q) (h2 : q → r) : p → r :=
  fun hp => h2 (h1 hp)
```

**Lean 4 (tactic mode):**

```lean
theorem hs (p q r : Prop) (h1 : p → q) (h2 : q → r) : p → r := by
  intro hp
  apply h2
  apply h1
  exact hp
```

**Coq / Rocq:**

```coq
Theorem hs : forall p q r : Prop, (p -> q) -> (q -> r) -> p -> r.
Proof.
  intros p q r h1 h2 hp.
  apply h2.
  apply h1.
  exact hp.
Qed.
```

`intro hp` is `→I` (assume `p`); `apply h2` reduces goal `r` to goal `q` (backwards `→E`); `exact hp` closes the final goal.

---

## Z5.4 Comparison: which format when?

| Format | Pros | Cons | Use it when |
|---|---|---|---|
| Truth table | mechanical, no creativity | exponential; propositional only | quick check of propositional validity |
| Informal proof | fastest to read and write; real math | no mechanical checker | communicating with humans |
| Hilbert | tiny rule set; easy metatheory | proofs are long and opaque | proving soundness/completeness |
| ND tree | elegant; connects to λ-calculus | wide, awkward to write | proof theory; reading papers |
| **ND Fitch** | readable; mirrors real reasoning; box = scope | needs vertical space | **learning; writing proofs by hand** |
| ND Lemmon | compact; dependencies explicit | dependency sets are fiddly | UK-style textbooks |
| Sequent | systematic; subformula property; terminates (propositional) | verbose | automated search; cut-elimination |
| Tableau | very visual; finds countermodels from open branches | tree can blow up | decide validity by hand |
| Resolution | single rule; the engine of provers | needs clausal form (loses readability) | automated provers (Chapter 7, 8) |
| Calculational | clean for equivalences; great for algebra | awkward for non-equational goals | simplifying/normalizing formulas |
| Proof assistant | machine-checked; scales | learning curve | serious formalization |

**Soundness and completeness cut across all of them**: each of Formats 3-9 is a *sound and complete* calculus for classical propositional logic (and, with quantifier rules, for first-order logic). They differ only in convenience, never in what can be proved. This is Chapter 6.

---

## Z5.5 Translating between formats: a cheat table

| Fitch / ND idea | Hilbert counterpart | Sequent counterpart | Tableau counterpart |
|---|---|---|---|
| assume `A` (open box) | deduction theorem | move `A` to the left of `⇒` | add `A` to the branch |
| `→I` (close box) | deduction theorem | `→R` | n/a (refutation) |
| `→E` (modus ponens) | MP | `→L` (with cut/ax) | `A→B` branches to `¬A \| B` |
| `∧I` / `∧E` | via axioms | `∧R` / `∧L` | `A∧B` yields `A` and `B` |
| `∨E` (cases) | via axioms | `∨L` (two premises) | `A∨B` branches to `A \| B` |
| `¬I` / RAA (contradiction) | axiom for ¬ | `¬R` / `¬L` | branch closes when `A` and `¬A` both appear |
| goal is `⊥` | goal is a contradiction | empty right side `Γ ⇒` | closed tree |

---

## Z5.6 Quick-check

**Q1.** Write `(p ∨ q) → ¬r` in Łukasiewicz notation.
**Q2.** Insert all hidden brackets in `¬P ∧ Q → R ∨ S ↔ T`.
**Q3.** In which format would you naturally find a "closed branch"? "The empty clause"? "A discharged assumption with a superscript"? "Dependency set"?
**Q4.** Translate `∀x (P(x) → Q(x))` into TPTP and into Prover9 syntax.
**Q5.** Why can a truth table not serve as a proof format for predicate logic?
**Q6.** What does Lean's `intro hp` correspond to in Fitch style?

**Answers.**
**A1.** `CApqNr`. (`C` first; its first argument is `Apq`, its second is `Nr`.)
**A2.** `(((¬P) ∧ Q) → (R ∨ S)) ↔ T`. The `↔` is loosest, so the whole implication is its left side.
**A3.** Tableau; resolution; Gentzen-tree natural deduction; Lemmon.
**A4.** TPTP: `![X]: (p(X) => q(X))`. Prover9: `all x (P(x) -> Q(x))`.
**A5.** A structure can have an infinite domain, and there are infinitely many structures; you cannot enumerate them all. Predicate logic needs proof calculi (or countermodel search), and by Church-Turing it is only semi-decidable (Chapter 6).
**A6.** Opening a box with the assumption `p` (the start of an `→I` subproof).

---

---

# Chapter 0. The big picture

## 0.1 Two sides of logic

Logic studies reasoning from two complementary angles.

| | **Semantics** (meaning, truth) | **Syntax / proof theory** (form, derivation) |
|---|---|---|
| Question | Is the statement *true*? | Can the statement be *derived*? |
| Tool | Truth tables, structures, models | Inference rules, proofs |
| Symbol | Γ ⊨ A ("Γ entails A") | Γ ⊢ A ("Γ proves A") |
| Style | "Check every possible world" | "Build an argument step by step" |
| Weakness | Infinitely many worlds (in predicate logic) | Finding a proof is a search problem |

Truth tables are *semantic*: you inspect every interpretation. A proof is *syntactic*: you start from premises and apply rules that preserve truth, never looking at a model at all.

The deep fact that connects the two sides is that, for first-order logic, **Γ ⊨ A if and only if Γ ⊢ A** (soundness and completeness, Chapter 6). This is why proofs are trustworthy and why they are enough.

## 0.2 Why a proof is a different skill from a truth table

A truth table is an algorithm: follow the procedure and you get the answer. A proof is a *search* through a space of possible arguments. There is no mechanical recipe, but there are **strategies**, and the main one is:

> **The goal determines the shape of the proof.**
> Look at the main connective of what you want to prove, and that tells you how to start.

This single idea, developed in Chapters 2 and 4, removes most of the apparent mystery.

## 0.3 Three levels

1. **Formal proofs** in a proof system (natural deduction). Every step is a named rule. This is how a computer checks a proof, and how you will learn the *anatomy* of proofs.
2. **Informal mathematical proofs** ("Let ε > 0 be arbitrary. Choose δ = ε/2..."). These are the same arguments written in prose. Chapter 5 shows the translation precisely.
3. **Metatheory**: theorems *about* logic itself (soundness, completeness, Gödel). Chapter 6.

You will move between the three constantly. Formal proofs teach you why informal proofs work. Informal proofs show you what formal proofs are for.

## 0.4 Object language vs. metalanguage

When you write "P → Q", the arrow is a symbol *inside* the formal language (the **object language**). When you write "if A is a tautology then A ∨ B is a tautology" in English, you are reasoning *about* formulas in the **metalanguage**. Keep these separate. Confusing `→` (a connective) with `⊢` or `⊨` (relations between sets of formulas and formulas) is a classic beginner error.

---

# Chapter 1. Propositional logic: precise foundations

You know the basics. This chapter makes them precise, because precision is what proofs need.

## 1.1 Syntax: formulas are defined inductively

Formulas are built from **atoms** p, q, r, ... by this grammar:

```
A ::= p | ⊤ | ⊥ | ¬A | (A ∧ A) | (A ∨ A) | (A → A) | (A ↔ A)
```

This is an **inductive definition**: every formula is either an atom or built from smaller formulas by exactly one connective. Two consequences matter a lot:

- You can **define functions by recursion** on formulas (for example, "the number of connectives" or "the truth value under v").
- You can **prove statements about all formulas by structural induction** (Chapter 5).

**Precedence** (tightest first): ¬, ∧, ∨, →, ↔. Implication is **right-associative**: P → Q → R means P → (Q → R). When in doubt, use parentheses.

## 1.2 Semantics

A **valuation** v assigns T or F to each atom. It extends uniquely to all formulas using the truth tables. Write ⟦A⟧ᵥ for the value of A under v.

| Concept | Definition |
|---|---|
| A is a **tautology** (valid), written ⊨ A | ⟦A⟧ᵥ = T for **every** valuation v |
| A is **satisfiable** | ⟦A⟧ᵥ = T for **some** valuation v |
| A is a **contradiction** | ⟦A⟧ᵥ = F for every valuation v |
| **Γ ⊨ A** (entailment) | every valuation making **all** formulas in Γ true also makes A true |
| A ≡ B (equivalence) | A and B have the same value under every valuation |

Three facts you will use constantly:

- **(F1) Refutation principle.** Γ ⊨ A  ⇔  Γ ∪ {¬A} is unsatisfiable. *(This is how SAT solvers and resolution provers work: to prove A, try to refute ¬A.)*
- **(F2) Semantic deduction theorem.** Γ, A ⊨ B  ⇔  Γ ⊨ A → B. In particular, A ⊨ B ⇔ ⊨ A → B.
- **(F3)** A ≡ B  ⇔  ⊨ A ↔ B.

**Explosion.** If Γ is unsatisfiable, then Γ ⊨ B for *every* B (there is no valuation to check, so the condition holds vacuously). This semantic fact is the reason the proof rule "from ⊥ derive anything" is sound.

## 1.3 Implication in depth

Implication causes more confusion than all other connectives combined.

**The promise reading.** "If A then B" is a promise. It is broken (false) only when A happens and B does not. If A never happens, the promise is not broken, so it is true.

**Why vacuous truth is forced.** Consider the claim: "for every integer n, if n > 2 then n² > 4." This is true. Now test n = 1: the antecedent (1 > 2) is false, and the claim must *not* be refuted by it. A universal statement is a big conjunction of its instances, so each instance, including the ones with false antecedent, must come out true. That is exactly the truth table of →.

**Four related statements** (for "if A then B"):

| Name | Form | Equivalent to the original? |
|---|---|---|
| Converse | B → A | No |
| Inverse | ¬A → ¬B | No (it is the contrapositive of the converse) |
| **Contrapositive** | ¬B → ¬A | **Yes** |
| Negation | A ∧ ¬B | It is the *opposite* of the original |

**English vocabulary dictionary:**

| English | Logic |
|---|---|
| A implies B; if A then B; B if A | A → B |
| A only if B | A → B |
| A is sufficient for B | A → B |
| B is necessary for A | A → B |
| A if and only if B | A ↔ B |
| A unless B | ¬B → A (equivalently A ∨ B) |
| Not both A and B | ¬(A ∧ B) |
| Neither A nor B | ¬A ∧ ¬B |

The pair "A **only if** B" versus "A **if** B" trips everyone at first: *only if* is the arrow pointing *toward* the necessary condition.

## 1.4 The laws you must know cold

| Law | Statement |
|---|---|
| Double negation | ¬¬A ≡ A |
| De Morgan | ¬(A ∧ B) ≡ ¬A ∨ ¬B,  ¬(A ∨ B) ≡ ¬A ∧ ¬B |
| Distributivity | A ∧ (B ∨ C) ≡ (A ∧ B) ∨ (A ∧ C),  A ∨ (B ∧ C) ≡ (A ∨ B) ∧ (A ∨ C) |
| Implication as disjunction | A → B ≡ ¬A ∨ B |
| Negated implication | ¬(A → B) ≡ A ∧ ¬B |
| Contrapositive | A → B ≡ ¬B → ¬A |
| Exportation | (A ∧ B) → C ≡ A → (B → C) |
| Biconditional | A ↔ B ≡ (A → B) ∧ (B → A) ≡ (A ∧ B) ∨ (¬A ∧ ¬B) |
| Excluded middle | ⊨ A ∨ ¬A |
| Non-contradiction | ⊨ ¬(A ∧ ¬A) |
| Absorption | A ∧ (A ∨ B) ≡ A,  A ∨ (A ∧ B) ≡ A |
| Idempotence, commutativity, associativity | for ∧ and ∨ |

## 1.5 Normal forms

- **NNF** (negation normal form): negations only in front of atoms, only ∧, ∨ otherwise.
- **CNF** (conjunctive normal form): an AND of ORs of literals (a literal is an atom or a negated atom). Example: (P ∨ ¬Q) ∧ (Q ∨ R).
- **DNF**: an OR of ANDs of literals.

**Algorithm to reach CNF:**
1. Eliminate ↔ and →: A → B becomes ¬A ∨ B, and A ↔ B becomes (¬A ∨ B) ∧ (¬B ∨ A).
2. Push negations inward with De Morgan and double negation (this gives NNF).
3. Distribute ∨ over ∧.

**Example.** Convert (P → Q) → R.
- Eliminate: ¬(¬P ∨ Q) ∨ R
- Push negation: (P ∧ ¬Q) ∨ R
- Distribute: **(P ∨ R) ∧ (¬Q ∨ R)**

Step 3 can cause exponential blowup. Practical SAT tools use the **Tseitin transformation**, which introduces fresh atoms and produces a CNF that is only *equisatisfiable* (not equivalent) but linear in size. You will meet this again in Chapter 7.

## 1.6 Functional completeness

A set of connectives is **functionally complete** if every truth function can be expressed with it. The sets {¬, ∧}, {¬, ∨}, {¬, →} are complete, and so is the single connective NAND (A | B ≡ ¬(A ∧ B)). On the other hand, {∧, ∨, →, ↔} is *not* complete (Problem 1.9). This matters later: a prover can restrict itself to a minimal set of connectives without losing expressive power.

## 1.7 Why truth tables are not enough

A truth table for n atoms has 2ⁿ rows. That is already hopeless for n = 60 (SAT solvers do better, but the problem is NP-complete). For predicate logic it is worse: "every structure" includes infinite ones, so there is no finite table at all. We need a method that does not enumerate worlds. That method is **proof**.

## 1.8 Chapter 1 in complete detail (the from-zero companion)

Sections 1.1-1.7 gave you the skeleton of propositional logic. This companion rebuilds the whole subject **from absolute zero, slowly, with every definition spelled out, every connective examined, and every standard fact proved or demonstrated**. If you already feel solid, skim the headings and use the tables as reference. If anything above felt too fast, read this section from the top.

### 1.8.1 What is a proposition?

**Definition.** A **proposition** (also called a **statement** or **sentence** in the logician's sense) is a declarative sentence that is, in the situation under discussion, **either true or false, but not both**.

Two requirements are hidden in that sentence:

1. **Declarative:** it *asserts* something about the world.
2. **Bivalent:** it has exactly one of two **truth values**, True (T) or False (F). Classical logic assumes this (the **principle of bivalence**).

| Sentence | Proposition? | Why |
|---|---|---|
| "7 is prime." | yes (true) | declarative, definite |
| "7 is even." | yes (false) | declarative, definite |
| "Paris is the capital of France." | yes (true) | |
| "Every even number greater than 2 is a sum of two primes." (Goldbach) | yes | it is *either* true or false even though nobody knows which |
| "Close the door." | no | a command, asserts nothing |
| "Is it raining?" | no | a question |
| "How beautiful!" | no | an exclamation |
| "x + 1 = 5" | **no (not yet)** | an **open sentence**: true for x = 4, false otherwise. It becomes a proposition when x is replaced by a value or quantified (Chapter 3) |
| "This sentence is false." | no | paradoxical (the liar), cannot consistently be given a truth value |
| "The present king of France is bald." | disputed | presupposes a king exists; logicians avoid such sentences |
| "Mozart's music is better than Beethoven's." | not precisely | vague and subjective; we must first make it exact |

**Key point:** logic cares about **truth conditions**, not about whether *we know* the truth. "There is life on Mars" is a proposition even though we do not know its value.

#### Atomic and compound propositions

- An **atomic proposition** (atom) is one that we do **not** analyze further: "It is raining." We give it a letter: `R`.
- A **compound proposition** is built from others using **connectives**: "It is raining **and** it is cold."

**Atoms are a choice.** "John is tall" might be an atom `T`, or it might be analyzed in predicate logic as `Tall(john)`. In propositional logic we decide where to stop.

**Golden rule for choosing atoms:**

1. Each atom should be a complete declarative sentence (not a fragment).
2. Use the **same** letter for the **same** statement every time.
3. Make atoms as **small** as the argument requires, no smaller than necessary, and **positive** (prefer `R` = "it rains" over `N` = "it does not rain"; negation is the job of ¬).

### 1.8.2 The connectives, one at a time

For each connective: its **truth table**, its **English forms**, its **traps**.

#### Negation ¬A

| A | ¬A |
|---|---|
| T | F |
| F | T |

*English:* "not A"; "it is not the case that A"; "it is false that A"; "A is not true"; "A fails".
*Traps:*

- Negation flips **the whole statement**. The negation of "All swans are white" is **not** "All swans are black" but "Not all swans are white" (Chapter 3).
- The negation of "A and B" is "not A **or** not B" (De Morgan), never "not A and not B".
- "A is unhappy" is not necessarily ¬"A is happy" in ordinary language (there may be a middle ground). In logic, ¬ always means exactly "not true".

#### Conjunction A ∧ B

| A | B | A ∧ B |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

*English:* "A and B"; "both A and B"; "A but B"; "A although B"; "A however B"; "A yet B"; "A while B"; "A moreover B"; "A, B" (comma); "not only A but also B"; "A as well as B".
*Traps:*

- **"But" is logically "and".** "It is sunny but cold" = `S ∧ C`. The contrast is *rhetorical*, not logical.
- "and" in ordinary English can mean **"and then"** ("He opened the door and walked out" is order-sensitive) or a **collective** meaning ("Ann and Bob lifted the piano" probably means *together*). Logic's ∧ is **only** "both are true". It is commutative: `A ∧ B ≡ B ∧ A`.
- "John and Mary are married" does not always split as "John is married and Mary is married".

#### Disjunction A ∨ B (inclusive or)

| A | B | A ∨ B |
|---|---|---|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

*English:* "A or B"; "A or B or both"; "at least one of A, B"; "A and/or B"; "either A or B" (often, but see below).
*Traps:*

- **Inclusive vs. exclusive.** Logic's ∨ is **inclusive**: true when both hold. The English "or" is sometimes exclusive ("soup or salad" usually means one but not both). The **exclusive or** is ⊕: `A ⊕ B ≡ (A ∨ B) ∧ ¬(A ∧ B)`.
- In legal and mathematical texts "or" is inclusive unless it says "exactly one of" or "but not both".
- The word *vel* (Latin for inclusive "or") is the origin of the symbol ∨. Latin *aut* is exclusive.

#### Conditional (implication) A → B

| A | B | A → B |
|---|---|---|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

*Parts:* A = **antecedent** (hypothesis, premise, "if-part"); B = **consequent** (conclusion, "then-part").

*English forms, all meaning A → B:*

| English | Note |
|---|---|
| if A, then B | basic form |
| A implies B | |
| B if A | the **if** clause is the antecedent, wherever it stands |
| B provided that A; B given that A; B as long as A; B when A; B whenever A; B in case A | all "if" words |
| A only if B | **only if** introduces the *consequent*: A → B, not B → A |
| A is sufficient for B | A suffices to guarantee B |
| B is necessary for A | if A happens, B must have |
| B follows from A | |
| A, therefore B (as a claim) | |
| not A unless B (i.e. `¬A unless B`) | careful, see "unless" below |

*Why is the table the way it is?* **A → B says "you will never find A true and B false."** It is violated only in row 2. In rows 3-4 the antecedent is false, so the promise "if A then B" is **vacuously true** (nothing was promised for those cases). This is the **material conditional** (also *material implication*). It is *not* the "because" or "causes" of ordinary speech:

- "If 2 + 2 = 5 then the moon is cheese" is **true** (false antecedent).
- "If the moon is cheese then 2 + 2 = 4" is **true** (true consequent).
- "If it rains, the street is wet" says nothing about causation; it only rules out (rain ∧ dry street).

These are the so-called **paradoxes of material implication**. They are not errors; they are the price of making → truth-functional (its value depends only on the values of A and B). Other logics (relevance logic, conditional logic, Chapter 7) refine →, but classical mathematics uses the material conditional, and so does this course.

*Four statements around A → B* (see Section 1.3): converse `B → A`, inverse `¬A → ¬B`, contrapositive `¬B → ¬A` (equivalent to the original), negation `A ∧ ¬B`.

*Necessary vs. sufficient, once and for all:*
"A is **sufficient** for B" = having A is *enough* to get B = `A → B`.
"B is **necessary** for A" = you *can't have A without B* = `A → B`. (Same statement, viewed from the two ends.)
Example: "Being a square is sufficient for being a rectangle; being a rectangle is necessary for being a square."

*Unless.* "A unless B" has two readings; the standard logical reading is `¬B → A`, equivalent to `A ∨ B`. ("You will fail unless you study" = if you don't study you fail = you fail or you study.) If you want to also say "if you study you pass", add the converse: that is a biconditional.

#### Biconditional A ↔ B

| A | B | A ↔ B |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

*English:* "A if and only if B"; "A iff B" (math shorthand); "A exactly when B"; "A precisely if B"; "A just in case B"; "A is necessary and sufficient for B"; "A is equivalent to B".
*Facts:* `A ↔ B ≡ (A → B) ∧ (B → A)`; it says **A and B always have the same truth value**; it is commutative **and associative**; `¬(A ↔ B) ≡ A ⊕ B`.
*Trap:* English "if" in definitions often *means* "iff" ("A number is even if it is divisible by 2" is a definition, meaning iff). In **theorems**, "if" means →.

#### Exclusive or A ⊕ B

True exactly when A and B have **different** values: `A ⊕ B ≡ ¬(A ↔ B) ≡ (A ∨ B) ∧ ¬(A ∧ B)`.
Properties: commutative, associative, `A ⊕ A ≡ ⊥`, `A ⊕ ⊥ ≡ A`, `A ⊕ ⊤ ≡ ¬A`. It is addition modulo 2.

#### NAND (A ↑ B) and NOR (A ↓ B)

| A | B | A ↑ B (NAND) | A ↓ B (NOR) |
|---|---|---|---|
| T | T | F | F |
| T | F | T | F |
| F | T | T | F |
| F | F | T | T |

NAND = "not both": `¬(A ∧ B)`. NOR = "neither": `¬(A ∨ B)`. Each of them **alone** can express every other connective (Section 1.8.8). Real computer chips are built from NAND or NOR gates.

#### The constants ⊤ and ⊥

⊤ is a formula that is always true; ⊥ is a formula that is always false. They are **0-ary connectives** (take no arguments). They behave like identity/zero elements: `A ∧ ⊤ ≡ A`, `A ∨ ⊥ ≡ A`, `A ∧ ⊥ ≡ ⊥`, `A ∨ ⊤ ≡ ⊤`. Many proof systems define `¬A` as an abbreviation for `A → ⊥`.

#### Summary: common English patterns

| English | Formula |
|---|---|
| A and B; A but B; A although B | A ∧ B |
| A or B (or both) | A ∨ B |
| either A or B, but not both; A or else B | A ⊕ B |
| not A | ¬A |
| neither A nor B; not (A or B) | ¬A ∧ ¬B, i.e. ¬(A ∨ B) |
| not both A and B | ¬(A ∧ B), i.e. ¬A ∨ ¬B |
| A and not B; A but not B | A ∧ ¬B |
| if A then B; B if A; A only if B | A → B |
| A if and only if B | A ↔ B |
| A unless B | ¬B → A, i.e. A ∨ B |
| at least one of A, B, C | A ∨ B ∨ C |
| exactly one of A, B | A ⊕ B |
| at most one of A, B, C | ¬(A ∧ B) ∧ ¬(A ∧ C) ∧ ¬(B ∧ C) |
| at least two of A, B, C | (A ∧ B) ∨ (A ∧ C) ∨ (B ∧ C) |
| all of A, B, C | A ∧ B ∧ C |
| none of A, B, C | ¬A ∧ ¬B ∧ ¬C |
| A is necessary for B | B → A |
| A is sufficient for B | A → B |
| A is necessary and sufficient for B | A ↔ B |
| if A then B, else C | (A → B) ∧ (¬A → C) |

### 1.8.3 Syntax in complete detail

**Syntax** is the study of the **form** of formulas (what strings count as well-formed), with no mention of truth.

#### The alphabet (vocabulary)

A propositional language has:

1. **Atoms** (propositional variables): `p, q, r, s, ...` or `p₀, p₁, p₂, ...`; a countable (usually infinite) supply.
2. **Connectives:** `¬ ∧ ∨ → ↔` (and optionally `⊤ ⊥ ⊕ ↑ ↓`).
3. **Auxiliary symbols:** parentheses `(` and `)`.

Everything not in the alphabet is **not** part of the formal language. (When we write `A`, `B`, `Γ` we are using **metavariables**, which stand for formulas but are not themselves part of the language. Compare "Let n be any integer": n is not one specific integer.)

#### The formation rules (inductive definition)

The set **Form** of formulas is the **smallest** set such that:

1. Every atom is a formula; `⊤` and `⊥` are formulas.
2. If `A` is a formula, so is `¬A`.
3. If `A` and `B` are formulas, so are `(A ∧ B)`, `(A ∨ B)`, `(A → B)`, `(A ↔ B)`.

"**Smallest**" means: *nothing else* is a formula. In BNF (the grammar notation used in Section 1.1):

```
A ::= p | ⊤ | ⊥ | ¬A | (A ∧ A) | (A ∨ A) | (A → A) | (A ↔ A)
```

Read `::=` as "is defined as" and `|` as "or" (here `|` is part of BNF, not the logical connective).

**Examples**

| String | Formula? | Why |
|---|---|---|
| `p` | yes | atom |
| `¬¬p` | yes | negation of a negation |
| `(p ∧ q)` | yes | rule 3 |
| `(p → (q ∨ ¬r))` | yes | built in 4 steps |
| `p ∧ q` | yes by convention | outer parentheses dropped (abbreviation) |
| `(p ∧)` | no | missing an argument |
| `p q` | no | two atoms side by side |
| `∧ p q` | not in infix syntax | but valid in Polish notation (Z5.1.3) |
| `(p ∧ q ∨ r)` | no (strictly) | ambiguous; needs brackets |
| `p → → q` | no | connective without argument |
| `¬(p)` | informally ok | redundant brackets are tolerated |

#### Parse trees (syntax trees)

Every formula has a unique **tree**: the main connective is the root, immediate subformulas are children, atoms are leaves.

Formula: `(P ∧ ¬Q) → (R ∨ P)`

```
            →
          /   \
        ∧       ∨
       / \     / \
      P   ¬   R   P
          |
          Q
```

- The **main connective** (principal connective) is the root: `→`. Everything about the formula's type is decided by it: this formula **is an implication**.
- **Immediate subformulas** of the root: `P ∧ ¬Q` and `R ∨ P`.
- **Subformulas** (all): `P`, `Q`, `¬Q`, `P ∧ ¬Q`, `R`, `R ∨ P`, and the whole formula. That is 7 distinct subformulas, though the tree has 8 nodes because `P` occurs twice. A **subformula occurrence** is a particular position in the tree.
- **Atoms:** `P, Q, R` (3 distinct atoms). **Connectives:** 4 occurrences (→, ∧, ¬, ∨).
- **Height** (depth): the number of edges on the longest root-to-leaf path: here 3 (→, ∧, ¬, Q).
- **Size:** number of nodes (8), or sometimes the number of symbols.

**Why the main connective matters:** a rule or law only applies to the *main* connective. `(P ∧ Q) → R` is an implication, not a conjunction, even though it contains `∧`. This is the source of error #5 in Section 2.8.

#### Unique readability

**Theorem (unique readability).** Every formula can be parsed in exactly one way.

This is why brackets matter. Without them, `P ∧ Q ∨ R` has two parses with different meanings. Take the valuation P = F, Q = F, R = T:

- `(P ∧ Q) ∨ R` = (F ∧ F) ∨ T = **T**
- `P ∧ (Q ∨ R)` = F ∧ (F ∨ T) = **F**

so the two readings really differ. Precedence conventions (Z5.1.1) tell you which brackets may be omitted. Prefix (Polish) notation needs no brackets at all.

#### Defining functions by recursion on formulas

Because formulas are built inductively, you can **define a function** on them by saying what it does to each kind of formula.

*Number of connectives* `c(A)`:

- `c(p) = 0`, `c(⊤) = c(⊥) = 0`
- `c(¬A) = 1 + c(A)`
- `c(A ∘ B) = 1 + c(A) + c(B)` for each binary connective ∘

*Set of atoms* `atoms(A)`:

- `atoms(p) = {p}`, `atoms(⊤) = atoms(⊥) = ∅`
- `atoms(¬A) = atoms(A)`
- `atoms(A ∘ B) = atoms(A) ∪ atoms(B)`

*Truth value* `⟦A⟧ᵥ` (the semantics, next section) is defined the same way.

Example: `c((P ∧ ¬Q) → (R ∨ P)) = 1 + c(P ∧ ¬Q) + c(R ∨ P) = 1 + (1 + 0 + 1) + (1 + 0 + 0) = 4`. ✓.

#### Proving things by structural induction (preview of Chapter 5)

To prove a property **for all formulas**, prove it for atoms (base case) and show it is preserved by each connective (inductive step). Example: *every formula has as many "(" as ")"*.

- Base: an atom has 0 and 0.
- `¬A`: parentheses are exactly those of `A`. Equal by hypothesis.
- `(A ∘ B)`: one "(" and one ")" added to those of A and B. Equal by hypothesis.

Hence true for all formulas. ∎

### 1.8.4 Semantics in complete detail

**Semantics** gives formulas **meaning**: which are true, in which situations.

#### Valuations

A **valuation** (assignment, interpretation, "world") is a function `v` from atoms to `{T, F}`. It says, for each atom, whether it is true or false in the situation being considered. With n atoms there are exactly **2ⁿ valuations**: one for each row of the truth table.

#### Truth value of a compound: the recursive definition

The valuation extends **uniquely** to all formulas by:

| Formula | Value |
|---|---|
| atom p | `⟦p⟧ᵥ = v(p)` |
| ⊤ | `⟦⊤⟧ᵥ = T` |
| ⊥ | `⟦⊥⟧ᵥ = F` |
| ¬A | T iff `⟦A⟧ᵥ = F` |
| A ∧ B | T iff `⟦A⟧ᵥ = T` **and** `⟦B⟧ᵥ = T` |
| A ∨ B | T iff `⟦A⟧ᵥ = T` **or** `⟦B⟧ᵥ = T` (or both) |
| A → B | T iff `⟦A⟧ᵥ = F` **or** `⟦B⟧ᵥ = T` |
| A ↔ B | T iff `⟦A⟧ᵥ = ⟦B⟧ᵥ` |

This is the **only** place truth tables come from. A truth table is just this definition tabulated for all valuations.

#### Evaluating a formula under one valuation

Evaluate `(P ∧ ¬Q) → (R ∨ P)` under `v: P = T, Q = F, R = F`. Work **bottom-up** on the parse tree:

| Subformula | Computation | Value |
|---|---|---|
| `P` | given | T |
| `Q` | given | F |
| `¬Q` | not F | T |
| `P ∧ ¬Q` | T and T | T |
| `R` | given | F |
| `R ∨ P` | F or T | T |
| whole | T → T | **T** |

#### Building a truth table systematically

1. List the atoms: n of them. You need **2ⁿ rows**.
2. Fill the atom columns in a standard order so none is missed. Convention: first atom changes slowest, last atom changes fastest, starting with all T:
   `TTT, TTF, TFT, TFF, FTT, FTF, FFT, FFF` for n = 3.
3. Add one column per subformula, **smallest first**, so every column only uses columns to its left.
4. The last column is the formula's value for each row.

n atoms → 2ⁿ rows: 5 atoms → 32 rows; 10 atoms → 1 024; 20 atoms → 1 048 576; 60 atoms → 2⁶⁰ ≈ 10¹⁸ rows (Section 1.7).

#### Classification of formulas

| Kind | Meaning | Truth-table signature | Example |
|---|---|---|---|
| **Tautology** (valid) `⊨ A` | true under every valuation | last column all T | `P ∨ ¬P` |
| **Contradiction** (unsatisfiable) | false under every valuation | last column all F | `P ∧ ¬P` |
| **Contingent** | true under some, false under some | mixed | `P → Q` |
| **Satisfiable** | true under at least one valuation | at least one T | tautologies and contingent ones |
| **Falsifiable** | false under at least one valuation | at least one F | contradictions and contingent ones |

Relationships you should be able to recite:

- A is a tautology ⇔ `¬A` is a contradiction.
- A is satisfiable ⇔ `¬A` is falsifiable ⇔ A is **not** a contradiction.
- A is valid ⇔ A is not falsifiable.

#### Semantic relations between formulas

| Relation | Notation | Meaning |
|---|---|---|
| Entailment | `Γ ⊨ A` | every valuation that makes **all** of Γ true makes A true |
| Equivalence | `A ≡ B` | same value under every valuation (⇔ `⊨ A ↔ B`) |
| Consistency (satisfiability) of a set | Γ has a **model** | some valuation makes **every** member of Γ true |
| Inconsistency | Γ has no model | e.g. `{P, ¬P}`; `{P → Q, P, ¬Q}` |
| Independence | neither `Γ ⊨ A` nor `Γ ⊨ ¬A` | Γ leaves A open |

A valuation that makes Γ true is called a **model** of Γ (written `v ⊨ Γ`). **Entailment** is "truth-preservation in all models".

**Important consequences (be able to prove each):**

1. `Γ ⊨ A` and Γ is inconsistent: holds vacuously (explosion).
2. If `⊨ A` then `Γ ⊨ A` for any Γ (a tautology follows from anything).
3. **Monotonicity:** if `Γ ⊨ A` and `Γ ⊆ Δ`, then `Δ ⊨ A`. (More premises never hurt.)
4. **Cut/transitivity:** if `Γ ⊨ A` and `Γ, A ⊨ B` then `Γ ⊨ B`.
5. `A ≡ B` iff `A ⊨ B` and `B ⊨ A`.

#### Four methods to decide validity

| Method | Idea | Best for |
|---|---|---|
| **Full truth table** | check all 2ⁿ rows | n ≤ 4, or a sanity check |
| **Short truth table** (falsification search) | assume the formula is **false** and try to force valuations; if forcing leads to contradiction, it is valid | most hand work |
| **Algebraic** | transform with equivalence laws until ⊤ | when laws are handy |
| **Refutation** (F1) | `Γ ⊨ A` iff `Γ ∪ {¬A}` unsatisfiable; try to build a model | automation; Chapter 7 |

**Short truth table demonstration.** Is `((P → Q) ∧ (Q → R)) → (P → R)` a tautology? Try to make it **false**:

- An implication is false only if antecedent T and consequent F: need `(P → Q) ∧ (Q → R)` = T and `P → R` = F.
- `P → R` = F forces `P = T` and `R = F`.
- `P → Q` = T with `P = T` forces `Q = T`.
- `Q → R` with `Q = T`, `R = F` is F, but we needed it T. **Contradiction.**
- So no valuation falsifies it: it is a tautology. ∎

If the forcing had **not** collided, the surviving valuation would be a **countermodel**, a concrete falsifying world.

**Complexity note.** Deciding satisfiability (SAT) is **NP-complete** (Cook-Levin, 1971); deciding validity is **coNP-complete**. All known algorithms are exponential in the worst case, yet modern SAT solvers routinely handle millions of variables on structured problems. Propositional logic is **decidable** (the truth table is an algorithm), unlike predicate logic (Chapter 6).

#### Proving an equivalence *without* a table (semantic argument template)

*Claim:* `¬(A ∧ B) ≡ ¬A ∨ ¬B`.
*Proof.* Let `v` be an arbitrary valuation. Then

`⟦¬(A ∧ B)⟧ᵥ = T`
⇔ `⟦A ∧ B⟧ᵥ = F` (def. of ¬)
⇔ not both `⟦A⟧ᵥ = T` and `⟦B⟧ᵥ = T` (def. of ∧)
⇔ `⟦A⟧ᵥ = F` or `⟦B⟧ᵥ = F`
⇔ `⟦¬A⟧ᵥ = T` or `⟦¬B⟧ᵥ = T` (def. of ¬)
⇔ `⟦¬A ∨ ¬B⟧ᵥ = T` (def. of ∨).
Since `v` was arbitrary, the formulas are equivalent. ∎

The pattern is: **take an arbitrary valuation, unfold definitions, chain of ⇔**. This is your first taste of a *proof about logic*, which prepares you for Chapter 6.

### 1.8.5 All truth functions

A **truth function** (Boolean function) of n arguments is any rule giving T or F for each of the 2ⁿ combinations of inputs. The number of different n-ary truth functions is

**2^(2ⁿ)**: n = 0 → 2 (the constants ⊤, ⊥); n = 1 → 4; n = 2 → **16**; n = 3 → 256; n = 4 → 65 536.

#### The 4 unary functions

| A | identity | negation ¬A | constant ⊤ | constant ⊥ |
|---|---|---|---|---|
| T | T | F | T | F |
| F | F | T | T | F |

#### The 16 binary functions

Patterns list the output for rows `(A,B)` = TT, TF, FT, FF in that order.

| # | Pattern | Name | Formula | Notation |
|---|---|---|---|---|
| 0 | F F F F | contradiction (constant false) | `⊥` | ⊥ |
| 1 | F F F T | NOR (joint denial) | `¬(A ∨ B)` | A ↓ B |
| 2 | F F T F | converse nonimplication | `¬A ∧ B` | A ↚ B |
| 3 | F F T T | negation of A | `¬A` | ¬A |
| 4 | F T F F | nonimplication (A but not B) | `A ∧ ¬B` | A ↛ B |
| 5 | F T F T | negation of B | `¬B` | ¬B |
| 6 | F T T F | exclusive or (XOR) | `(A ∨ B) ∧ ¬(A ∧ B)` | A ⊕ B |
| 7 | F T T T | NAND (alternative denial) | `¬(A ∧ B)` | A ↑ B |
| 8 | T F F F | conjunction | `A ∧ B` | A ∧ B |
| 9 | T F F T | biconditional (XNOR) | `(A → B) ∧ (B → A)` | A ↔ B |
| 10 | T F T F | projection onto B | `B` | B |
| 11 | T F T T | conditional | `¬A ∨ B` | A → B |
| 12 | T T F F | projection onto A | `A` | A |
| 13 | T T F T | converse conditional | `A ∨ ¬B` | A ← B |
| 14 | T T T F | disjunction | `A ∨ B` | A ∨ B |
| 15 | T T T T | tautology (constant true) | `⊤` | ⊤ |

**Observations.**

- Only functions 8, 14, 11 (and 9, 6, 7, 1) are conventionally used as binary connectives. Functions 0, 3, 5, 10, 12, 15 do not really depend on both inputs.
- Pairs of **duals/negations**: 8↔7 (∧, NAND), 14↔1 (∨, NOR), 9↔6 (↔, ⊕), 11↔4 (→, ↛), 13↔2.
- **Commutative:** 1, 6, 7, 8, 9, 14. **Not commutative:** 11, 13, 4, 2.
- → is function 11. Every other implication-like function is a flip or negation of it.

A **ternary** example: *if-then-else* `ITE(A, B, C) ≡ (A ∧ B) ∨ (¬A ∧ C)`: "if A then B else C". *Majority*: `MAJ(A,B,C) ≡ (A∧B) ∨ (A∧C) ∨ (B∧C)`.

### 1.8.6 The complete table of laws, with names

Below, `A, B, C` are arbitrary formulas. Each line is an equivalence `≡` (and thus also a tautology after replacing ≡ by ↔).

#### Laws for ∧, ∨, ¬ (Boolean algebra)

| Name | Law |
|---|---|
| Idempotence | `A ∧ A ≡ A`;  `A ∨ A ≡ A` |
| Commutativity | `A ∧ B ≡ B ∧ A`;  `A ∨ B ≡ B ∨ A` |
| Associativity | `(A ∧ B) ∧ C ≡ A ∧ (B ∧ C)`;  `(A ∨ B) ∨ C ≡ A ∨ (B ∨ C)` |
| Distributivity | `A ∧ (B ∨ C) ≡ (A ∧ B) ∨ (A ∧ C)`;  `A ∨ (B ∧ C) ≡ (A ∨ B) ∧ (A ∨ C)` |
| Absorption | `A ∧ (A ∨ B) ≡ A`;  `A ∨ (A ∧ B) ≡ A` |
| Identity | `A ∧ ⊤ ≡ A`;  `A ∨ ⊥ ≡ A` |
| Domination (annihilation) | `A ∨ ⊤ ≡ ⊤`;  `A ∧ ⊥ ≡ ⊥` |
| Complement | `A ∨ ¬A ≡ ⊤` (excluded middle);  `A ∧ ¬A ≡ ⊥` (non-contradiction) |
| Double negation | `¬¬A ≡ A` |
| De Morgan | `¬(A ∧ B) ≡ ¬A ∨ ¬B`;  `¬(A ∨ B) ≡ ¬A ∧ ¬B` |
| Constants and negation | `¬⊤ ≡ ⊥`;  `¬⊥ ≡ ⊤` |

#### Laws for →

| Name | Law |
|---|---|
| Material implication | `A → B ≡ ¬A ∨ B` |
| Negated implication | `¬(A → B) ≡ A ∧ ¬B` |
| Contraposition | `A → B ≡ ¬B → ¬A` |
| Exportation / importation | `(A ∧ B) → C ≡ A → (B → C)` |
| Permutation of premises | `A → (B → C) ≡ B → (A → C)` |
| Distribution over ∧ in consequent | `A → (B ∧ C) ≡ (A → B) ∧ (A → C)` |
| Distribution over ∨ in consequent | `A → (B ∨ C) ≡ (A → B) ∨ (A → C)` |
| Cases in antecedent | `(A ∨ B) → C ≡ (A → C) ∧ (B → C)` |
| Antecedent conjunction | `(A ∧ B) → C ≡ (A → C) ∨ (B → C)` |
| Reflexivity | `A → A ≡ ⊤` |
| Trivial antecedents/consequents | `⊤ → A ≡ A`;  `A → ⊤ ≡ ⊤`;  `⊥ → A ≡ ⊤`;  `A → ⊥ ≡ ¬A` |
| Self-reference | `A → ¬A ≡ ¬A`;  `¬A → A ≡ A` |
| Consequentia mirabilis (Clavius) | `(¬A → A) → A` is a tautology |
| Peirce's law | `((A → B) → A) → A` is a tautology |

#### Laws for ↔ and ⊕

| Name | Law |
|---|---|
| Definition | `A ↔ B ≡ (A → B) ∧ (B → A)  ≡  (A ∧ B) ∨ (¬A ∧ ¬B)` |
| Commutativity | `A ↔ B ≡ B ↔ A` |
| Associativity | `(A ↔ B) ↔ C ≡ A ↔ (B ↔ C)` |
| Reflexivity | `A ↔ A ≡ ⊤` |
| Contrary | `A ↔ ¬A ≡ ⊥` |
| Negation | `¬(A ↔ B) ≡ A ↔ ¬B ≡ ¬A ↔ B ≡ A ⊕ B` |
| With constants | `A ↔ ⊤ ≡ A`;  `A ↔ ⊥ ≡ ¬A` |
| XOR | `A ⊕ B ≡ (A ∨ B) ∧ ¬(A ∧ B)`; also commutative, associative, `A ⊕ A ≡ ⊥` |

#### Things that are **not** valid (common false laws)

| False "law" | Counterexample (valuation making them differ) |
|---|---|
| `A → B ≡ B → A` (converse) | A = T, B = F |
| `A → B ≡ ¬A → ¬B` (inverse) | A = F, B = T |
| `(A → B) → C ≡ A → (B → C)` (→ is not associative) | A = F, C = F (left: (T) → F = F; right: F → … = T) |
| `¬(A ∧ B) ≡ ¬A ∧ ¬B` | A = T, B = F |
| `¬(A ∨ B) ≡ ¬A ∨ ¬B` | A = T, B = F |
| `A → (B ∨ C) ≡ (A → B) ∧ (A → C)` | A = T, B = T, C = F |
| `(A ∨ B) → C ≡ (A → C) ∨ (B → C)` | A = T, B = F, C = F |
| `A ∨ B, A ⊨ ¬B` ("affirming a disjunct") | A = B = T (for inclusive or) |

#### Using the laws: a derivation by equational reasoning

*Prove absorption* `A ∨ (A ∧ B) ≡ A`:

```
      A ∨ (A ∧ B)
  ≡     { identity: A ≡ A ∧ ⊤ }
      (A ∧ ⊤) ∨ (A ∧ B)
  ≡     { distributivity, factoring out A }
      A ∧ (⊤ ∨ B)
  ≡     { domination: ⊤ ∨ B ≡ ⊤ }
      A ∧ ⊤
  ≡     { identity }
      A
```

#### Two meta-theorems that make laws usable

**Replacement theorem.** If `B ≡ B′`, then replacing an occurrence of `B` inside a formula `C` by `B′` gives a formula equivalent to `C`. (Equivalent subformulas are interchangeable. This is what justifies chains of ≡.)

**Substitution theorem.** If `A` is a tautology and you replace **every** occurrence of an atom `p` in `A` **uniformly** by any formula `B`, the result is still a tautology. (So `p ∨ ¬p` being valid yields `(Q ∧ R) ∨ ¬(Q ∧ R)` being valid.)

Care: *uniform* is essential. Replacing only one of two occurrences of `p` in `p → p` by `¬p` gives `¬p → p`, which is not valid.

This is why laws are written with **metavariables** A, B, C: each is a **schema** with infinitely many instances.

### 1.8.7 Normal forms in complete detail

#### Vocabulary

- **Literal:** an atom `p` or a negated atom `¬p`.
- **Clause:** a disjunction of literals: `p ∨ ¬q ∨ r`. (A single literal is a clause; the empty disjunction is ⊥, called the **empty clause**.)
- **Term** (or *cube*, *conjunctive clause*): a conjunction of literals.
- **NNF:** negation only on atoms; connectives only ∧, ∨ (and ¬ at the atoms).
- **CNF:** a conjunction of clauses.  **DNF:** a disjunction of terms.
- **Canonical (full) forms:** every clause/term mentions **every** atom exactly once.

Every formula is equivalent to a CNF and to a DNF.

#### Reading a DNF/CNF off a truth table (canonical forms)

*Canonical DNF:* take every row where the formula is **T**; write the term that is true *only* on that row (atom if T, negated atom if F); OR them together.
*Canonical CNF:* take every row where the formula is **F**; write the clause that is false *only* on that row (atom if F, negated atom if T); AND them together.

**Example.** Majority of three, `MAJ(P,Q,R)` = "at least two true":

| P | Q | R | MAJ |
|---|---|---|---|
| T | T | T | **T** |
| T | T | F | **T** |
| T | F | T | **T** |
| T | F | F | F |
| F | T | T | **T** |
| F | T | F | F |
| F | F | T | F |
| F | F | F | F |

- Canonical DNF (4 true rows):
  `(P∧Q∧R) ∨ (P∧Q∧¬R) ∨ (P∧¬Q∧R) ∨ (¬P∧Q∧R)`
- Canonical CNF (4 false rows):
  `(¬P∨Q∨R) ∧ (P∨¬Q∨R) ∧ (P∨Q∨¬R) ∧ (P∨Q∨R)`
- Minimal forms (simplified by laws): DNF `(P∧Q) ∨ (P∧R) ∨ (Q∧R)`; CNF `(P∨Q) ∧ (P∨R) ∧ (Q∨R)`.

This construction proves **functional completeness of {¬, ∧, ∨}**: every truth function (every table) equals its canonical DNF. Two special cases: if there are no T rows the formula is ⊥; if no F rows, ⊤.

#### Conversion algorithm (syntactic), step by step

1. **Eliminate** ↔, ⊕, → :
   `A ↔ B ⟹ (¬A ∨ B) ∧ (¬B ∨ A)`; `A ⊕ B ⟹ (A ∨ B) ∧ (¬A ∨ ¬B)`; `A → B ⟹ ¬A ∨ B`.
2. **Push negations inward** (reach NNF):
   `¬¬A ⟹ A`; `¬(A ∧ B) ⟹ ¬A ∨ ¬B`; `¬(A ∨ B) ⟹ ¬A ∧ ¬B`; `¬⊤ ⟹ ⊥`; `¬⊥ ⟹ ⊤`.
3. **Distribute** ∨ over ∧ to reach CNF (or ∧ over ∨ for DNF):
   `A ∨ (B ∧ C) ⟹ (A ∨ B) ∧ (A ∨ C)`.
4. **Clean up:** remove duplicates, drop clauses containing both `p` and `¬p` (they are tautologies), apply absorption.

**Worked example.** Convert `¬((P ∨ Q) → (P ∧ R))` to CNF.

- Eliminate →: `¬(¬(P ∨ Q) ∨ (P ∧ R))`
- De Morgan: `¬¬(P ∨ Q) ∧ ¬(P ∧ R)`
- Double negation and De Morgan: `(P ∨ Q) ∧ (¬P ∨ ¬R)`

Already in CNF: two clauses `P ∨ Q` and `¬P ∨ ¬R`. ✓.

**Blow-up.** Converting `(a₁ ∧ b₁) ∨ (a₂ ∧ b₂) ∨ ... ∨ (aₙ ∧ bₙ)` to CNF gives 2ⁿ clauses. That is why Tseitin exists.

#### Tseitin transformation (equisatisfiable CNF in linear size)

Introduce a **fresh atom** `xᵢ` for each non-atomic subformula and assert that `xᵢ` is equivalent to it, written as clauses.

**Gate clauses:**

| Definition | Clauses |
|---|---|
| `x ↔ (a ∧ b)` | `(¬x ∨ a) ∧ (¬x ∨ b) ∧ (x ∨ ¬a ∨ ¬b)` |
| `x ↔ (a ∨ b)` | `(¬x ∨ a ∨ b) ∧ (x ∨ ¬a) ∧ (x ∨ ¬b)` |
| `x ↔ ¬a` | `(¬x ∨ ¬a) ∧ (x ∨ a)` |
| `x ↔ (a → b)` | `(¬x ∨ ¬a ∨ b) ∧ (x ∨ a) ∧ (x ∨ ¬b)` |

**Example.** `(P ∧ Q) ∨ R`: name `x₁ ↔ (P ∧ Q)` and `x₂ ↔ (x₁ ∨ R)`, then assert `x₂`:

```
(¬x₁ ∨ P) ∧ (¬x₁ ∨ Q) ∧ (x₁ ∨ ¬P ∨ ¬Q)        -- defines x₁
∧ (¬x₂ ∨ x₁ ∨ R) ∧ (x₂ ∨ ¬x₁) ∧ (x₂ ∨ ¬R)    -- defines x₂
∧ x₂                                            -- assert the whole formula
```

The result is **satisfiable iff** `(P ∧ Q) ∨ R` is satisfiable (equisatisfiable), but it is *not equivalent* (it mentions new atoms) and its size grows only linearly.

#### Why normal forms matter

- **CNF** is the input format of SAT solvers and of resolution provers.
- **DNF** makes satisfiability trivial (a term is satisfiable iff it has no clashing literals) but makes validity hard.
- **CNF** makes validity trivial (check each clause for `p` and `¬p`) but makes satisfiability hard.
- This asymmetry is exactly why SAT is NP-complete.

### 1.8.8 Functional completeness in complete detail

A set of connectives is **functionally complete** (adequate) if every truth function is expressible using only them.

#### Proofs and expressions

- **{¬, ∧, ∨} is complete:** canonical DNF (Section 1.8.7).
- **{¬, ∧} is complete:** `A ∨ B ≡ ¬(¬A ∧ ¬B)` (De Morgan), then use the previous result.
- **{¬, ∨} is complete:** `A ∧ B ≡ ¬(¬A ∨ ¬B)`.
- **{¬, →} is complete:** `A ∨ B ≡ ¬A → B`; `A ∧ B ≡ ¬(A → ¬B)`.
- **{→, ⊥} is complete:** `¬A ≡ A → ⊥`; `A ∨ B ≡ (A → ⊥) → B`; `A ∧ B ≡ (A → (B → ⊥)) → ⊥`.
- **{↑} alone (NAND):** `¬A ≡ A ↑ A`; `A ∧ B ≡ (A ↑ B) ↑ (A ↑ B)`; `A ∨ B ≡ (A ↑ A) ↑ (B ↑ B)`.
- **{↓} alone (NOR):** `¬A ≡ A ↓ A`; `A ∨ B ≡ (A ↓ B) ↓ (A ↓ B)`; `A ∧ B ≡ (A ↓ A) ↓ (B ↓ B)`.

#### Some incomplete sets, and why

| Set | Why incomplete |
|---|---|
| {∧, ∨} | every formula is **monotone** (switching an input from F to T never makes the output go from T to F), but ¬ is not monotone |
| {∧, ∨, →, ↔, ⊤} | every formula is **T when all atoms are T**, but ¬p is F there (Problem 1.9) |
| {⊕, ⊤} (or {⊕, ↔}) | every formula is **affine** (a sum mod 2 of atoms and constants), but ∧ is not |
| {¬} | only expresses p, ¬p, ¬¬p, ... : no binary function |
| {⊥} alone / {⊤} alone | constants only |

**Post's criterion** (Emil Post, 1941): a set of truth functions is complete **iff** it is *not entirely contained in any one* of five classes: functions that preserve F (T₀), preserve T (T₁), are monotone, are self-dual, or are affine. NAND and NOR escape all five. That is a classification theorem you can study later.

#### Why you care

- **Hardware:** every circuit can be built from NAND gates only.
- **Provers:** restricting to few connectives shrinks the number of rules.
- **Proof systems:** minimal systems (like Hilbert's {→, ⊥}) are shorter to analyze.

### 1.8.9 Arguments in propositional logic: valid forms and fallacies

An **argument** is a list of premises `A₁, ..., Aₙ` and a conclusion `C`. It is **valid** iff `A₁, ..., Aₙ ⊨ C`. Validity depends on **form** only.

#### Named valid forms (rules of inference)

| Name | Form | Description |
|---|---|---|
| Modus ponens | `A → B`, `A` ∴ `B` | affirm the antecedent |
| Modus tollens | `A → B`, `¬B` ∴ `¬A` | deny the consequent |
| Hypothetical syllogism | `A → B`, `B → C` ∴ `A → C` | chain implications |
| Disjunctive syllogism | `A ∨ B`, `¬A` ∴ `B` | eliminate one disjunct |
| Addition (∨ intro) | `A` ∴ `A ∨ B` | weaken |
| Simplification (∧ elim) | `A ∧ B` ∴ `A` | |
| Conjunction (∧ intro) | `A`, `B` ∴ `A ∧ B` | |
| Constructive dilemma | `A → C`, `B → D`, `A ∨ B` ∴ `C ∨ D` | |
| Destructive dilemma | `A → C`, `B → D`, `¬C ∨ ¬D` ∴ `¬A ∨ ¬B` | |
| Resolution | `A ∨ B`, `¬A ∨ C` ∴ `B ∨ C` | basis of automated provers |
| Proof by cases | `A → C`, `B → C`, `A ∨ B` ∴ `C` | |
| Reductio ad absurdum | `A → B`, `A → ¬B` ∴ `¬A` | |
| Explosion (ex falso) | `A`, `¬A` ∴ `B` | anything follows from a contradiction |
| Absorption | `A → B` ∴ `A → (A ∧ B)` | |

#### Named fallacies (invalid forms that look valid)

| Name | Form | Counter-valuation |
|---|---|---|
| **Affirming the consequent** | `A → B`, `B` ∴ `A` | A = F, B = T |
| **Denying the antecedent** | `A → B`, `¬A` ∴ `¬B` | A = F, B = T |
| **Affirming a disjunct** | `A ∨ B`, `A` ∴ `¬B` | A = B = T |
| **Illicit conversion** | `A → B` ∴ `B → A` | A = F, B = T |
| **Denying a conjunct** | `¬(A ∧ B)`, `¬A` ∴ `B` | A = B = F |
| **Converting a disjunction** | `A ∨ B` ∴ `A ∧ B` | A = T, B = F |

**Concrete English instances:**

- *Affirming the consequent:* "If it rained, the grass is wet. The grass is wet. So it rained." (A sprinkler could be responsible.)
- *Denying the antecedent:* "If you study, you pass. You didn't study. So you won't pass." (You may be lucky or brilliant.)

**How to test any argument:** (1) formalize premises and conclusion; (2) search for a valuation making all premises T and the conclusion F (short truth table). If one exists, the argument is invalid and that valuation is your counterexample. If none exists, it is valid.

### 1.8.10 Quick-check (with answers)

**Q1.** Which of these are propositions: (a) "Is 7 prime?" (b) "7 is prime." (c) "x > 3." (d) "Every even number greater than 2 is a sum of two primes."
**Q2.** Translate "You may enter only if you have a ticket and are not drunk" with `E`, `T`, `D`.
**Q3.** What are the main connective, the immediate subformulas, and the number of connectives of `¬(P ∨ Q) → (R ↔ ¬S)`?
**Q4.** How many valuations are there for a formula with 7 distinct atoms? How many different 3-ary truth functions exist?
**Q5.** Use the short-truth-table method on `(P → Q) → (¬Q → ¬P)`. Valid?
**Q6.** True or false: (a) `A → B ≡ ¬B → ¬A`; (b) `A → (B → C) ≡ (A → B) → C`; (c) `{P ∨ Q, ¬P} ⊨ Q`; (d) `P ↔ Q ≡ (P ∧ Q) ∨ (¬P ∧ ¬Q)`.
**Q7.** Give canonical DNF for `P ⊕ Q` and canonical CNF for `P → Q`.
**Q8.** Express `A → B` using only NAND.
**Q9.** Why does a conditional with a false antecedent count as true?

**Answers.**
**A1.** (b) and (d). (a) is a question, (c) is an open sentence.
**A2.** `E → (T ∧ ¬D)`. ("Only if" gives the arrow *from* E *to* the conditions.)
**A3.** Main connective: `→`. Immediate subformulas: `¬(P ∨ Q)` and `R ↔ ¬S`. Connectives: ¬, ∨, →, ↔, ¬ = **5**.
**A4.** 2⁷ = 128 valuations. 2^(2³) = 2⁸ = 256 ternary functions.
**A5.** To falsify: need `P → Q` = T and `¬Q → ¬P` = F. The latter forces `¬Q` = T (Q = F) and `¬P` = F (P = T). Then `P → Q` = T → F = F, contradiction. So it is **valid**.
**A6.** (a) True. (b) False (A = F, C = F). (c) True. (d) True.
**A7.** `P ⊕ Q`: true rows TF and FT: `(P ∧ ¬Q) ∨ (¬P ∧ Q)`. `P → Q`: only false row TF: `(¬P ∨ Q)`.
**A8.** `A → B ≡ ¬A ∨ B ≡ A ↑ ¬B ≡ A ↑ (B ↑ B)`. Check: `A ↑ (B ↑ B)` = `¬(A ∧ ¬B)` = `¬A ∨ B` ✓.
**A9.** Because → promises only that "A true and B false" never occurs. If A is false, that situation did not occur, so the promise is not broken. Also, a universal claim "for all n, if n > 2 then ..." must not be refuted by n = 1 (Section 1.3).

## Problems for Chapter 1

**1.1 ★** Use a truth table to show that P → Q, ¬P ∨ Q, ¬(P ∧ ¬Q), and ¬Q → ¬P are all equivalent.

**1.2 ★** State the converse, inverse, and contrapositive of "if a number is divisible by 6, then it is divisible by 3". Which of the four statements are true?

**1.3 ★** Translate into propositional logic, naming your atoms:
- (a) "You can have dessert only if you finish dinner."
- (b) "Unless you hurry, you will miss the train."
- (c) "Passing the exam is necessary but not sufficient for getting the degree."
- (d) "Neither the server nor the backup is responding."

**1.4 ★★** Decide, with justification, whether each entailment holds:
- (a) {P → Q, Q → R, P} ⊨ R
- (b) {P → Q, Q} ⊨ P
- (c) {P ∨ Q, ¬P} ⊨ Q
- (d) {P → Q, ¬P} ⊨ ¬Q

**1.5 ★★** Show that P → (Q → R) ≡ (P ∧ Q) → R using the laws of Section 1.4 (no truth table).

**1.6 ★★** Convert (P ↔ Q) ∨ R to CNF and to DNF.

**1.7 ★★** Using (F1), show {P → Q, Q → R} ⊨ P → R by proving that {P → Q, Q → R, ¬(P → R)} is unsatisfiable.

**1.8 ★★** Show that NAND is functionally complete by expressing ¬P and P ∧ Q using only |.

**1.9 ★★★** Prove that no formula built from atoms using only ∧, ∨, →, ↔ is equivalent to ¬P. (Hint: look at the valuation making every atom true.)

**1.10 ★★★** On an island, knights always tell the truth and knaves always lie. A says "B is a knave." B says "A and I are of the same kind." Who is the knight and who is the knave? Formalize with atoms a = "A is a knight" and b = "B is a knight" and solve algebraically.

---

# Chapter 2. Natural deduction for propositional logic

## 2.1 What is a proof?

A **formal proof** of A from premises Γ (written **Γ ⊢ A**) is a finite sequence of lines. Each line is either a premise, an assumption (temporarily made), or follows from earlier lines by an **inference rule**. The last line is A.

The point is that a proof is a **purely mechanical object**. A computer (or a skeptical friend) can check it line by line without understanding what the formulas mean. This is what makes it trustworthy.

We use **natural deduction** in **Fitch style**: nested sub-proofs, where each sub-proof opens with an **assumption** and ends when we discharge it.

## 2.2 Reading and writing Fitch proofs

```
1.  P → Q              premise
2.  Q → R              premise
3.  |  P               assumption
4.  |  Q               →E 1,3
5.  |  R               →E 2,4
6.  P → R              →I 3-5
```

- The vertical bar `|` marks a **sub-proof**. Everything inside is true only *under the assumption* that opened it.
- A line may use any earlier line **in its own sub-proof or an enclosing one**, never from a closed sub-proof.
- When the sub-proof closes (line 6), the assumption is **discharged**: line 6 does not depend on P any more. It says "if P then R", which depends only on lines 1 and 2.
- Justifications: rule name plus the line numbers it uses. A sub-proof is cited as a range, like `3-5`.

## 2.3 The rules

Each connective has an **introduction** rule (how to *prove* a statement of that form) and an **elimination** rule (how to *use* a statement of that form). This pairing is the heart of natural deduction.

| Connective | Introduction (to prove it) | Elimination (to use it) |
|---|---|---|
| **∧** | **∧I:** from A and B, infer A ∧ B | **∧E:** from A ∧ B, infer A (or infer B) |
| **∨** | **∨I:** from A, infer A ∨ B (or B ∨ A) | **∨E (cases):** from A ∨ B, a sub-proof A ⊢ C, and a sub-proof B ⊢ C, infer C |
| **→** | **→I:** sub-proof assuming A and reaching B; infer A → B | **→E (modus ponens):** from A and A → B, infer B |
| **¬** | **¬I:** sub-proof assuming A and reaching ⊥; infer ¬A | **¬E:** from A and ¬A, infer ⊥ |
| **⊥** | (none) | **⊥E (ex falso):** from ⊥, infer any C |
| **↔** | **↔I:** from A → B and B → A, infer A ↔ B | **↔E:** from A ↔ B and A, infer B (and symmetrically) |
| **Classical** | | **RAA (reductio):** sub-proof assuming ¬A and reaching ⊥; infer A |

**Two rules to treat with respect:**

- **¬I vs. RAA.** They look similar but differ crucially. ¬I *proves a negation* (assume A, reach ⊥, conclude ¬A). RAA *proves any statement* (assume ¬A, reach ⊥, conclude A). RAA is the rule that makes the logic **classical**. Without it you have *intuitionistic logic* (Section 2.7).
- **∨E needs both branches to reach the same conclusion C.** C is chosen by you, usually the current goal.

## 2.4 How to find proofs: the strategy

Two questions, in this order:

**1. What is my goal? Look at its main connective.**

| Goal looks like | First move |
|---|---|
| A → B | Assume A, aim for B (→I) |
| ¬A | Assume A, aim for ⊥ (¬I) |
| A ∧ B | Prove A, prove B separately (∧I) |
| A ∨ B | Try to prove A, or B, then ∨I. If neither is provable directly, use RAA (assume ¬(A ∨ B), derive ⊥) |
| A ↔ B | Prove both directions (↔I) |
| Atom, or nothing else works | Try RAA: assume ¬goal, aim for ⊥ |

**2. What do I have? Look at the main connective of each available line.**

| Available line | What to do with it |
|---|---|
| A ∧ B | Extract A and B (∧E) |
| A → B | If you can prove A, get B. Otherwise remember it for the contradiction |
| A ∨ B | Do case analysis (∨E), usually aiming at your goal |
| ¬A | Useful for ¬E: if you get A anywhere, you get ⊥ |
| ⊥ | You are done: ⊥E gives anything |

**Golden rule:** work **backwards from the goal** and **forwards from the premises**, and meet in the middle. When stuck, ask "what would give me a contradiction?"

## 2.5 Worked examples

### Example 1. Hypothetical syllogism: P → Q, Q → R ⊢ P → R

The goal is an implication, so assume the antecedent.

```
1.  P → Q              premise
2.  Q → R              premise
3.  |  P               assumption
4.  |  Q               →E 1,3
5.  |  R               →E 2,4
6.  P → R              →I 3-5
```

### Example 2. Contrapositive: P → Q ⊢ ¬Q → ¬P

Goal is an implication, so assume ¬Q. Its conclusion ¬P is a negation, so assume P and look for ⊥.

```
1.  P → Q              premise
2.  |  ¬Q              assumption
3.  |  |  P            assumption
4.  |  |  Q            →E 1,3
5.  |  |  ⊥            ¬E 4,2
6.  |  ¬P              ¬I 3-5
7.  ¬Q → ¬P            →I 2-6
```

### Example 3. Disjunctive syllogism: P ∨ Q, ¬P ⊢ Q

We *use* a disjunction, so do cases.

```
1.  P ∨ Q              premise
2.  ¬P                 premise
3.  |  P               assumption (case 1)
4.  |  ⊥               ¬E 3,2
5.  |  Q               ⊥E 4
6.  |  Q               assumption (case 2)
7.  Q                  ∨E 1, 3-5, 6-6
```

Case 1 is impossible (it contradicts ¬P), so ex falso gives Q. Case 2 is trivial.

### Example 4. De Morgan: ¬(P ∨ Q) ⊢ ¬P ∧ ¬Q

Goal is a conjunction, so prove each part. Each part is a negation, so assume and refute.

```
1.  ¬(P ∨ Q)           premise
2.  |  P               assumption
3.  |  P ∨ Q           ∨I 2
4.  |  ⊥               ¬E 3,1
5.  ¬P                 ¬I 2-4
6.  |  Q               assumption
7.  |  P ∨ Q           ∨I 6
8.  |  ⊥               ¬E 7,1
9.  ¬Q                 ¬I 6-8
10. ¬P ∧ ¬Q            ∧I 5,9
```

### Example 5. Law of excluded middle: ⊢ P ∨ ¬P

This is the classic "no obvious first move" proof. The goal is a disjunction, but we can prove neither P nor ¬P. So use RAA: assume the goal is false and derive a contradiction.

```
1.  |  ¬(P ∨ ¬P)       assumption (for RAA)
2.  |  |  P            assumption
3.  |  |  P ∨ ¬P       ∨I 2
4.  |  |  ⊥            ¬E 3,1
5.  |  ¬P               ¬I 2-4
6.  |  P ∨ ¬P          ∨I 5
7.  |  ⊥                ¬E 6,1
8.  P ∨ ¬P              RAA 1-7
```

Read it in words: "Suppose P ∨ ¬P failed. Then P can't hold (it would give P ∨ ¬P), so ¬P holds. But then P ∨ ¬P holds after all. Contradiction."

### Example 6. Peirce's law: ⊢ ((P → Q) → P) → P

Goal is an implication, so assume the antecedent. Then the goal P is an atom with nothing to build it from, so use RAA.

```
1.  |  (P → Q) → P      assumption
2.  |  |  ¬P            assumption (for RAA)
3.  |  |  |  P          assumption
4.  |  |  |  ⊥          ¬E 3,2
5.  |  |  |  Q          ⊥E 4
6.  |  |  P → Q         →I 3-5
7.  |  |  P              →E 1,6
8.  |  |  ⊥              ¬E 7,2
9.  |  P                 RAA 2-8
10. ((P → Q) → P) → P    →I 1-9
```

The key trick is line 5: from the contradiction at line 4 we derive Q (which we don't care about) in order to *manufacture* P → Q.

### Example 7. Distribution: P ∧ (Q ∨ R) ⊢ (P ∧ Q) ∨ (P ∧ R)

```
1.  P ∧ (Q ∨ R)        premise
2.  P                  ∧E 1
3.  Q ∨ R              ∧E 1
4.  |  Q               assumption (case 1)
5.  |  P ∧ Q           ∧I 2,4
6.  |  (P∧Q) ∨ (P∧R)   ∨I 5
7.  |  R               assumption (case 2)
8.  |  P ∧ R           ∧I 2,7
9.  |  (P∧Q) ∨ (P∧R)   ∨I 8
10. (P∧Q) ∨ (P∧R)      ∨E 3, 4-6, 7-9
```

### Example 8. A proof you should try before reading: ¬¬P ⊢ P

This requires RAA (it is *not* provable in intuitionistic logic). Assume ¬P, and combine it with ¬¬P to get ⊥.

```
1.  ¬¬P                premise
2.  |  ¬P              assumption (for RAA)
3.  |  ⊥               ¬E 2,1
4.  P                  RAA 2-3
```

(Here ¬E is applied to ¬P and ¬¬P, treating ¬P as the "A" and ¬¬P as "¬A".)

## 2.6 Useful derived results

Once you have proved these, you may use them as shortcuts (in an exam, prove them first or cite them):

| Name | Statement |
|---|---|
| Modus tollens | P → Q, ¬Q ⊢ ¬P |
| Contraposition | P → Q ⊢ ¬Q → ¬P |
| Disjunctive syllogism | P ∨ Q, ¬P ⊢ Q |
| Hypothetical syllogism | P → Q, Q → R ⊢ P → R |
| Double negation intro | P ⊢ ¬¬P |
| Double negation elim (classical) | ¬¬P ⊢ P |
| Excluded middle (classical) | ⊢ P ∨ ¬P |
| De Morgan | ¬(P ∨ Q) ⊣⊢ ¬P ∧ ¬Q; ¬(P ∧ Q) ⊣⊢ ¬P ∨ ¬Q (the hard direction is classical) |
| Implication as disjunction | P → Q ⊣⊢ ¬P ∨ Q (the direction → to ∨ is classical) |

## 2.7 Classical vs. intuitionistic logic

If you remove RAA (and everything equivalent to it), you get **intuitionistic logic**, in which a proof of A ∨ B must contain a proof of A or a proof of B, and ¬¬A is weaker than A. This is not a mere curiosity:

- **Curry-Howard correspondence.** Intuitionistic proofs *are* programs: a proof of A → B is a function from proofs of A to proofs of B. This is the foundation of Coq, Lean, Agda and typed functional programming.
- It is a good diagnostic: if you can tell which of your proofs used RAA, you understand exactly where "non-constructive" reasoning enters.

Each of these is equivalent (given the other rules): RAA, ¬¬P ⊢ P, excluded middle, Peirce's law.

## 2.8 Common mistakes

1. **Using a line from a closed sub-proof.** After line 6 in Example 1, lines 3-5 are gone.
2. **Forgetting to discharge.** A proof of A → B must end with →I at the outer level.
3. **Confusing ¬I and RAA.** To prove a *negation*, assume the positive statement. To prove a *positive* statement (by contradiction), assume its negation.
4. **Affirming the consequent.** From A → B and B you cannot conclude A.
5. **Applying a rule to a sub-formula.** Rules apply to the *main connective* only. From (P ∧ Q) → R you cannot "extract" P.
6. **Using ∨E with branches that prove different things.** Both branches must end in the same formula.

## 2.9 Chapter 2 in complete detail (the from-zero companion)

Sections 2.1-2.9 introduced natural deduction in Fitch style. This companion (a) explains **what a formal proof system is** and exactly what it means for a proof to be correct, (b) goes through **every rule** with its conditions, typical uses and typical misuses, (c) gives a **proof-search method**, (d) shows **all the other proof formats with their complete rule sets** (Gentzen tree, Lemmon, Hilbert, sequent calculus, tableaux, resolution), and (e) explains **intuitionistic logic and the Curry-Howard correspondence** properly.

### 2.9.1 What is a formal proof system?

Truth tables (semantics) answer: "is this true in all worlds?". A **proof system** (also **calculus**, **deductive system**) answers a different question, purely by **symbol manipulation**: "can this formula be *derived* by following the rules?".

A proof system consists of:

1. A **formal language** (the formulas, Chapter 1).
2. A set of **rules** (and possibly **axioms**): each rule says "if you already have lines of these shapes, you may write a line of that shape".
3. A definition of **derivation** (proof): a finite structure of lines, each justified by a rule.
4. A **derivability relation** `Γ ⊢ A`: "there is a derivation of A from the premises Γ".

**Vocabulary you must keep straight**

| Term | Meaning |
|---|---|
| **Premise** (hypothesis, given) | a formula in Γ, available for the entire proof |
| **Assumption** (supposition) | a formula we *temporarily* suppose inside a subproof; it must later be **discharged** (closed) |
| **Derived line** | a line obtained from earlier lines by a rule |
| **Conclusion** (goal, target) | the formula we want on the last line |
| **Theorem** | a formula derivable from **no** premises: `⊢ A` |
| **Derivable rule** | a rule that can be simulated by a chain of basic rules (e.g. modus tollens) |
| **Admissible rule** | a rule whose addition does not enlarge the set of theorems, though it may not be simulable line-by-line |
| **Sequent** | the pair "premises + conclusion", written `Γ ⊢ A` |

**Why proofs are trustworthy.** Checking a proof requires **no understanding**: for each line, ask "does this line follow from the cited lines by the cited rule?". A computer can do this in a fraction of a second. The *finding* of a proof is hard (in predicate logic it is undecidable in general); the *checking* is trivial. This asymmetry is the foundation of everything in Chapters 7-8.

**Two big questions about any proof system** (answered in Chapter 6):

- **Soundness:** if `Γ ⊢ A` then `Γ ⊨ A`. (Proofs never prove falsehoods.)
- **Completeness:** if `Γ ⊨ A` then `Γ ⊢ A`. (Every truth is provable.)

Every system in this chapter is sound and complete for classical propositional logic.

### 2.9.2 Anatomy of a Fitch proof

A Fitch proof is a vertical list of numbered lines.

```
1 │ A → B                premise
2 │ ┌─ A                 assumption
3 │ │  B                 →E 1, 2
4 │ └──
5 │ A → B                →I 2-3
```

(The textual style `|` used elsewhere in the course is the same thing drawn with plain characters.)

Each line has:

1. a **line number**;
2. a **formula**;
3. a **justification**: a rule name plus the numbers of the lines (or ranges of lines for subproofs) it uses;
4. a **depth** (how many boxes enclose it), shown by the vertical bars.

#### The scope rule (the single most important rule about format)

> **A line may cite an earlier line only if that line is in the same box or in a box that encloses the citing line. A line inside a closed box can never be cited from outside, except the whole box can be cited as a unit by the rule that closes it.**

Picture: boxes are rooms. You can see out (use anything from your own room and the surrounding rooms) but not into closed rooms. The only communication from a closed room is through its "exit door", the discharging rule.

Formal version: let line *m* be in a box *b*. Line *n > m* may cite *m* iff *b* still contains *n* (i.e. *b* has not been closed before *n*).

#### Subproof citations

A rule that discharges an assumption (→I, ¬I, ∨E, RAA) cites a **range** such as `3-5`, meaning "the subproof starting at line 3 and ending at line 5". The subproof's **first line is the assumption**; its **last line is what it concludes**. The range must be a complete, closed subproof, immediately below the line at the same depth.

#### Premise versus assumption: the lines at the top

Premises are written at the top, at depth 0, and are never discharged. Assumptions start boxes at deeper depth and are discharged by the closing rule.

The **conclusion** of the whole proof must be at depth 0 (outside all boxes). A proof that ends inside a box is incomplete.

#### Reiteration

Some books (Barwise-Etchemendy *Language, Proof and Logic*, the Fitch program) require you to **reiterate** (copy) a line into a box before using it there. We do not: scoping already permits using outer lines. If your textbook or checker insists on `Reit`, add a copy line with justification `Reit n`.

### 2.9.3 Every rule in complete detail

Notation: `A, B, C` are any formulas. A box means a subproof. Each rule is given as

- **schema** (what must be present, what you may write),
- **in words**,
- **use it when**,
- **typical misuse**.

#### Conjunction introduction (∧I)

```
m │ A
n │ B
  │ A ∧ B           ∧I m, n
```

*In words:* if you have A and you have B, you may state "A and B". (The lines may be in either order, anywhere above, in scope.)
*Use it when* the goal is a conjunction: prove each half, then glue.
*Misuse:* citing a line that is out of scope; gluing in the wrong order (`B ∧ A` needs its own ∧I).

#### Conjunction elimination (∧E)

```
m │ A ∧ B
  │ A               ∧E m          (left)
  │ B               ∧E m          (right)
```

*In words:* from "A and B", you may take out either part.
*Use it when* a premise is a conjunction. *Always* extract both halves early; it costs nothing.
*Misuse:* applying ∧E to a conjunction that is a **subformula**: from `(A ∧ B) → C` you cannot extract `A`.

#### Disjunction introduction (∨I)

```
m │ A
  │ A ∨ B           ∨I m          (B is any formula whatsoever)
  │ B ∨ A           ∨I m
```

*In words:* if A is established, then "A or anything" is established (weakening).
*Use it when* the goal is a disjunction and you can prove one disjunct. Also for manufacturing the formula needed by ¬E (`P ∨ Q` against `¬(P ∨ Q)`).
*Misuse:* believing it "adds knowledge": it only weakens. Also: ∨I **needs a proved disjunct**; you cannot choose a disjunct you cannot prove.

#### Disjunction elimination (∨E, proof by cases)

```
m │ A ∨ B
  │ ┌─ A                  assumption (case 1)
  │ │  ...
  │ │  C
  │ └──
  │ ┌─ B                  assumption (case 2)
  │ │  ...
  │ │  C
  │ └──
  │ C                      ∨E m, (case-1 range), (case-2 range)
```

*In words:* if A or B holds, and either one alone leads to C, then C holds.
*Use it when* you have a disjunction available and don't know which side holds.
*Conditions:* **both subproofs must end in the same formula C**; the cases must be the two disjuncts of the cited disjunction.
*Misuse:* ending the two cases in different formulas; assuming only one case; forgetting that the conclusion C *escapes* both boxes (that is the whole point).

#### Conditional introduction (→I, conditional proof)

```
  │ ┌─ A                  assumption
  │ │  ...
  │ │  B
  │ └──
  │ A → B                  →I (range)
```

*In words:* to prove "if A then B", suppose A and derive B.
*Use it when* the goal is an implication. It is almost always your first move on such a goal.
*Misuse:* leaving the box open; thinking A is then "true" outside (it is not: it was only supposed).

#### Conditional elimination (→E, modus ponens)

```
m │ A → B
n │ A
  │ B                     →E m, n
```

*In words:* if you know "A implies B" and you know A, you may conclude B.
*Misuse:* **affirming the consequent** (having B and A → B and "concluding" A); applying it with A that is only a part of a larger formula.

#### Negation introduction (¬I)

```
  │ ┌─ A                  assumption
  │ │  ...
  │ │  ⊥
  │ └──
  │ ¬A                     ¬I (range)
```

*In words:* to prove "not A", suppose A and derive a contradiction.
*Use it when* the goal is a negation `¬A`. (Equivalent presentation: define ¬A as A → ⊥ and treat ¬I as →I.)

#### Negation elimination (¬E, contradiction introduction)

```
m │ A
n │ ¬A
  │ ⊥                     ¬E m, n
```

*In words:* a formula and its negation together yield the absurd ⊥.
*Use it when* you want to close a box ending in ⊥. This is the **only** way to produce ⊥ in our system (besides citing an existing ⊥).
*Variants:* some books call this rule "⊥I" or "contradiction introduction" or "¬ elimination"; some conclude "any formula B" directly (see 2.9.4).

#### Falsum elimination (⊥E, ex falso quodlibet)

```
m │ ⊥
  │ C                     ⊥E m          (C is any formula)
```

*In words:* from a contradiction, anything follows ("from falsehood, anything").
*Use it when* you are inside a branch known to be impossible (like case 1 in disjunctive syllogism). Also to "pay off" a box that must end with some target formula: reach ⊥ and then write the target.
*This is not cheating:* the branch it is used in is already contradicting something; the rule just records that.

#### Reductio ad absurdum (RAA, indirect proof; classical only)

```
  │ ┌─ ¬A                 assumption
  │ │  ...
  │ │  ⊥
  │ └──
  │ A                      RAA (range)
```

*In words:* to prove A, suppose it is false and derive a contradiction.
*Use it when* the goal is atomic or a disjunction/existential with no direct route, or when you are stuck.
*Alternative names:* IP (indirect proof), proof by contradiction, ¬¬E, DNE.
*Misuse:* using it to prove a negation (use ¬I there). If the goal is `¬A`, **do not** assume `¬¬A`; assume `A`.

#### Biconditional introduction (↔I)

```
  │ ┌─ A                  assumption
  │ │  ...
  │ │  B
  │ └──
  │ ┌─ B                  assumption
  │ │  ...
  │ │  A
  │ └──
  │ A ↔ B                  ↔I (range 1), (range 2)
```

Or, if you already have the two implications as lines `A → B` and `B → A`, infer `A ↔ B` directly. Two subproofs (one each direction) is the usual practice.

#### Biconditional elimination (↔E)

```
m │ A ↔ B
n │ A
  │ B                     ↔E m, n       (or from B infer A)
```

#### Constants

`⊤I`: ⊤ may be written at any time (no premises needed). `⊤` elimination: nothing useful.

#### Summary table of rules and their discharge behaviour

| Rule | Cites | Opens/closes a box? | Result |
|---|---|---|---|
| ∧I | 2 lines | no | `A ∧ B` |
| ∧E | 1 line | no | a conjunct |
| ∨I | 1 line | no | `A ∨ B` (any B) |
| ∨E | disjunction + 2 ranges | **closes 2 boxes** | `C` |
| →I | 1 range | **closes 1 box** | `A → B` |
| →E | 2 lines | no | `B` |
| ¬I | 1 range | **closes 1 box** | `¬A` |
| ¬E | 2 lines | no | `⊥` |
| ⊥E | 1 line | no | anything |
| RAA | 1 range | **closes 1 box** | `A` |
| ↔I | 2 ranges | **closes 2 boxes** | `A ↔ B` |
| ↔E | 2 lines | no | the other side |

**Rule counting:** every connective has an **I** and an **E**. The rules ∧I, ∧E, ∨I, ∨E, →I, →E, ¬I, ¬E, ⊥E, (↔I, ↔E) form the **intuitionistic** system; **adding RAA** gives the classical one.

### 2.9.4 Rule names in other books (translation table)

Textbooks differ in **names**, not in power. Learn the equivalence once.

| Idea | This course | Other names |
|---|---|---|
| ∧I | ∧I | Conjunction (Conj), Adjunction, `&I`, `∧-intro` |
| ∧E | ∧E | Simplification (Simp), `&E` |
| ∨I | ∨I | Addition (Add), `∨-intro` |
| ∨E | ∨E | Proof by cases, Constructive dilemma (variant), `∨-elim` |
| →I | →I | Conditional proof (CP), Deduction, `⊃I`, `→-intro`, Discharge |
| →E | →E | Modus ponens (MP), Detachment, `MPP`, `⊃E` |
| ¬I | ¬I | Reductio (Lemmon RAA), Negation intro, Proof of negation |
| ¬E | ¬E | Contradiction (Contra), `⊥I`, Negation elim |
| ⊥E | ⊥E | Ex falso (EFQ), Explosion, Absurdity, Exfalso |
| RAA | RAA | Indirect proof (IP), Proof by contradiction, `¬¬E`, DNE, Classical reductio |
| ↔I / ↔E | ↔I / ↔E | `≡I`, `≡E`, Material equivalence |
| Iteration | (not needed) | Reit, R, Repeat |

**Three styles of negation rules** (all equivalent in power once you add classical reasoning):

| Style | Negation rules | Used by |
|---|---|---|
| **Absurdity style** (this course) | ¬I (from A ⊢ ⊥ infer ¬A), ¬E (A, ¬A ⊢ ⊥), ⊥E, RAA | Gentzen NJ/NK, Fitch, Barwise-Etchemendy |
| **Contradiction-closes-anything style** | ¬I as above; ¬E: from A and ¬A infer *any* B; no ⊥ symbol | Kalish-Montague, many intro books |
| **Double-negation style** | ¬I as above; add DN: `¬¬A ⊢ A` as a rule; no RAA | Copi, Lemmon (via DN rule) |

#### How RAA, DNE, LEM, and Peirce relate

Over the intuitionistic rules, adding any **one** of the following gives classical logic: RAA; double-negation elimination `¬¬A ⊢ A`; excluded middle `⊢ A ∨ ¬A`; Peirce's law `⊢ ((A → B) → A) → A`; `⊢ (¬A → A) → A` (consequentia mirabilis). Each of these five gives full classical logic. Careful with a famous look-alike: adding Dummett's axiom `⊢ (A → B) ∨ (B → A)` gives only the intermediate Gödel-Dummett logic, **not** full classical logic.

### 2.9.5 Finding proofs: a complete procedure

You have two "directions" of work, to be interleaved:

- **Backward (goal-directed):** look at the goal; pick the rule that would introduce it; set up the subgoal(s).
- **Forward (premise-directed):** look at what is available; use elimination rules to unpack it.

#### The loop (try in this priority order)

1. **Unpack everything safe** (forward): from every conjunction available, take both halves (∧E). Apply →E / ↔E wherever the needed antecedent is **already** available. Use ⊥E if you reach ⊥ and need the goal.
2. **Check the goal's main connective** (backward):
   - `A → B`: assume A, aim for B.
   - `¬A`: assume A, aim for ⊥.
   - `A ∧ B`: two subgoals.
   - `A ↔ B`: two boxes.
   - `A ∨ B`: if one disjunct is derivable, ∨I. Otherwise go to 4.
   - `⊥`: find a formula and its negation (¬E).
   - atom: go to 3.
3. **Use disjunctions** (cases): if a disjunction `A ∨ B` is available, plan ∨E aiming at the *current goal* in each case.
4. **RAA:** assume the negation of the goal and aim for ⊥. When you do this you gain a new available line (the assumption), and the new goal is ⊥. To reach ⊥ you need a formula *and* its negation: look at the negations and implications you have.
5. **Repeat** inside each new box.

The loop always terminates for propositional logic (the search space is finite); for predicate logic it need not.

#### Checklist when stuck

- Is every premise unpacked?
- Is there an implication whose antecedent I can prove?
- Is there a negation `¬X` such that I could prove `X`? Then I get ⊥.
- Is there a disjunction I have not split?
- Have I tried RAA?

#### Narrated example 1: ⊢ (P → Q) → ((¬P → Q) → Q) (reasoning by cases on P)

*Thinking aloud.* Goal is an implication: assume `P → Q`. New goal `(¬P → Q) → Q`: also an implication, assume `¬P → Q`. New goal `Q`: an atom, nothing to unpack except two implications whose antecedents (`P`, `¬P`) I don't have. Use RAA: assume `¬Q`, aim for ⊥. Now: from `P → Q` and `¬Q` I expect `¬P` (modus tollens: assume P, get Q, contradiction). Then `¬P → Q` gives Q, which clashes with `¬Q`.

```
1.  |  P → Q                         assumption
2.  |  |  ¬P → Q                     assumption
3.  |  |  |  ¬Q                      assumption (for RAA)
4.  |  |  |  |  P                    assumption (for ¬I)
5.  |  |  |  |  Q                    →E 1,4
6.  |  |  |  |  ⊥                    ¬E 5,3
7.  |  |  |  ¬P                      ¬I 4-6
8.  |  |  |  Q                       →E 2,7
9.  |  |  |  ⊥                       ¬E 8,3
10. |  |  Q                          RAA 3-9
11. |  (¬P → Q) → Q                  →I 2-10
12. (P → Q) → ((¬P → Q) → Q)         →I 1-11
```

Informally: "either P or not P; whichever holds, Q." The proof avoids quoting LEM; RAA does the same work.

#### Narrated example 2: ¬(P ∧ Q) ⊢ P → ¬Q (no RAA needed)

*Thinking aloud.* Goal is an implication: assume P. New goal `¬Q`: a negation, assume Q and look for ⊥. Now I hold P and Q, so P ∧ Q, which clashes with the premise.

```
1.  ¬(P ∧ Q)            premise
2.  |  P                assumption
3.  |  |  Q             assumption
4.  |  |  P ∧ Q         ∧I 2,3
5.  |  |  ⊥             ¬E 4,1
6.  |  ¬Q               ¬I 3-5
7.  P → ¬Q              →I 2-6
```

This one is intuitionistically valid (no RAA). Its converse direction is also valid; compare `¬(P ∧ Q) ⊢ ¬P ∨ ¬Q`, which needs classical logic.

#### Reading someone else's proof (checking)

For each line, ask: (1) which rule? (2) are the cited lines in scope? (3) do the cited lines have exactly the shapes the rule demands? (4) if a box closed, was the right range cited? (5) does the last line, at depth 0, equal the goal, and do all premises used appear in the premise list? If all yes, the proof is correct.

### 2.9.6 Derived rules: tools that save time

You can prove once, then reuse (an allowed abbreviation; the full proof is the abbreviation expanded).

| Derived rule | Premises → conclusion | Proved by |
|---|---|---|
| Modus tollens (MT) | `A → B`, `¬B` ⊢ `¬A` | ¬I: assume A, →E, ¬E |
| Hypothetical syllogism (HS) | `A → B`, `B → C` ⊢ `A → C` | →I, →E twice |
| Disjunctive syllogism (DS) | `A ∨ B`, `¬A` ⊢ `B` | ∨E with ⊥E in case 1 |
| Double negation intro (DNI) | `A` ⊢ `¬¬A` | ¬I: assume ¬A, ¬E |
| Double negation elim (DNE) | `¬¬A` ⊢ `A` | RAA |
| Excluded middle (LEM) | ⊢ `A ∨ ¬A` | RAA (Example 5) |
| Contraposition | `A → B` ⊢ `¬B → ¬A` | →I, ¬I |
| Reverse contraposition | `¬B → ¬A` ⊢ `A → B` | classical (RAA) |
| Explosion | `A`, `¬A` ⊢ `B` | ¬E, ⊥E |
| Commutation | `A ∧ B` ⊢ `B ∧ A`; `A ∨ B` ⊢ `B ∨ A` | ∧E, ∧I; ∨E, ∨I |
| De Morgan 1 | `¬(A ∨ B)` ⊣⊢ `¬A ∧ ¬B` | intuitionistically valid |
| De Morgan 2 | `¬A ∨ ¬B` ⊢ `¬(A ∧ B)` | intuitionistically valid |
| De Morgan 2 (converse) | `¬(A ∧ B)` ⊢ `¬A ∨ ¬B` | classical only |
| Implication to disjunction | `A → B` ⊢ `¬A ∨ B` | classical only |
| Disjunction to implication | `¬A ∨ B` ⊢ `A → B` | intuitionistically valid |
| Resolution | `A ∨ B`, `¬A ∨ C` ⊢ `B ∨ C` | ∨E (nested) |
| Cut | `Γ ⊢ A` and `Γ, A ⊢ B` gives `Γ ⊢ B` | plug the first proof in for assumption A |
| Weakening | `Γ ⊢ A` gives `Γ, B ⊢ A` | extra premises are ignored |

### 2.9.7 The other proof formats, with their complete rule sets

(Z5.3 showed one example in each format. Here are the **rules**.)

#### Format A: Natural deduction in Gentzen's tree style (NJ / NK)

In tree style an inference rule is drawn as
```
  premise₁   premise₂   ...
  ─────────────────────── rule name
         conclusion
```
Assumptions appear as leaves; those discharged are bracketed and labelled with a number, which is repeated at the rule that discharges them. Rules (⟨A⟩ means "A may be discharged here"):

```
 A   B               A ∧ B              A ∧ B
 ───── ∧I            ───── ∧E₁          ───── ∧E₂
 A ∧ B                 A                  B

   A                   B               A ∨ B   ⟨A⟩..C   ⟨B⟩..C
 ───── ∨I₁          ───── ∨I₂          ──────────────────────── ∨E
 A ∨ B              A ∨ B                          C

 ⟨A⟩..B             A   A → B           ⟨A⟩..⊥              ⊥
 ─────── →I         ───────── →E        ─────── ¬I          ─── ⊥E
 A → B                  B                 ¬A                 C

 A   ¬A             ⟨¬A⟩..⊥
 ────── ¬E          ─────── RAA (NK only)
   ⊥                   A
```

**Full example: contrapositive in tree style** (`P → Q ⊢ ¬Q → ¬P`)

```
                 [P]¹   P → Q
                 ──────────── →E
     [¬Q]²              Q
     ───────────────────── ¬E
                ⊥
              ─────── ¬I¹
                ¬P
          ────────────── →I²
             ¬Q → ¬P
```

Gentzen's insight (1934): this tree form displays *exactly* the dependency structure: what each conclusion rests on.

#### Format B: Lemmon style (numbered lines with assumption sets)

Each line has the shape `{assumption-line-numbers}  (line)  formula  justification`. Rules:

| Rule | Effect on assumption set |
|---|---|
| **A** (assumption) | `{n} (n) A  A`: depends only on itself |
| **MPP** (modus ponens) | union of the assumption sets of the two cited lines |
| **MTT** (modus tollens) | union of the two cited sets |
| **DN** | same set as the cited line |
| **CP** (conditional proof) | from line (m) assumption A, and line (n) B: conclude `A → B`; set = set of (n) **minus** m |
| **∧I** | union of the two sets |
| **∧E** | same set |
| **∨I** | same set |
| **∨E** | from `A ∨ B`, and subderivations from A to C and B to C: union of the sets, minus the two assumptions |
| **RAA** | from assumption A deriving `B ∧ ¬B` (or ⊥): conclude `¬A`, set = (set of contradiction line) minus the assumption |

**Example (contrapositive, Lemmon):** `P → Q ⊢ ¬Q → ¬P`

```
{1}        (1)  P → Q         A
{2}        (2)  ¬Q            A
{3}        (3)  P             A
{1,3}      (4)  Q             1,3 MPP
{1,2,3}    (5)  Q ∧ ¬Q        4,2 ∧I
{1,2}      (6)  ¬P            3,5 RAA
{1}        (7)  ¬Q → ¬P       2,6 CP
```

The final line depends only on line 1 (the premise): exactly what we expect. A line with an **empty** assumption set `{}` is a **theorem**.

#### Format C: Hilbert systems (axioms + modus ponens)

A Hilbert system has many **axiom schemes** and a very small set of rules (typically just MP). For classical logic with primitives `→` and `¬` (Łukasiewicz's system):

- **L1:** `A → (B → A)`
- **L2:** `(A → (B → C)) → ((A → B) → (A → C))`
- **L3:** `(¬A → ¬B) → (B → A)`
- **Rule MP:** from `A` and `A → B`, infer `B`.

A **derivation** from premises Γ is a finite list where every line is an axiom instance, a premise, or follows by MP.

**Warm-up: derive `A → A`** (this takes five lines and shows why Hilbert systems are laborious):

```
1. (A → ((A → A) → A)) → ((A → (A → A)) → (A → A))     L2
2. A → ((A → A) → A)                                     L1
3. (A → (A → A)) → (A → A)                               MP 2,1
4. A → (A → A)                                           L1
5. A → A                                                 MP 4,3
```

**Deduction theorem.** If `Γ, A ⊢ B` then `Γ ⊢ A → B`. *Proof idea:* take a derivation of B from Γ, A; show by induction on the line number that `Γ ⊢ A → (line)` holds for every line:

- line is an axiom or in Γ: `B`, `B → (A → B)` (L1), `A → B` (MP);
- line is `A` itself: `A → A` (the five-line derivation above);
- line follows by MP from lines `C` and `C → D`: we already have `A → C` and `A → (C → D)`; with L2, `(A → (C → D)) → ((A → C) → (A → D))`, two applications of MP give `A → D`.

The deduction theorem is precisely the Hilbert-system version of →I. Once it is available, proofs become almost as easy as natural deduction.

**Other classical axiomatisations** exist (Frege's six axioms; Mendelson's `(¬B → ¬A) → ((¬B → A) → B)` as third axiom; Hilbert-Ackermann with ∨ and ¬; Meredith's single axiom). All prove the same theorems.

#### Format D: Sequent calculus (Gentzen's LK; LJ for intuitionistic)

A **sequent** `Γ ⇒ Δ` (Γ and Δ are finite lists or multisets of formulas) is read: *"if all formulas of Γ are true, then at least one formula of Δ is true"*. Equivalently `⋀Γ → ⋁Δ`. A derivation is a tree; we usually construct it **bottom-up** (from the goal sequent, decomposing).

**Axioms and logical rules of LK** (premises above the bar, conclusion below; Γ, Δ are the "context"):

```
Axiom:   Γ, A ⇒ A, Δ                    (any formula appearing on both sides)
Bottom:  Γ, ⊥ ⇒ Δ                       Top:   Γ ⇒ ⊤, Δ

 Γ, A, B ⇒ Δ                 Γ ⇒ A, Δ    Γ ⇒ B, Δ
 ─────────────── ∧L          ───────────────────── ∧R
 Γ, A ∧ B ⇒ Δ                    Γ ⇒ A ∧ B, Δ

 Γ, A ⇒ Δ    Γ, B ⇒ Δ          Γ ⇒ A, B, Δ
 ───────────────────── ∨L      ───────────── ∨R
   Γ, A ∨ B ⇒ Δ                Γ ⇒ A ∨ B, Δ

 Γ ⇒ A, Δ    Γ, B ⇒ Δ          Γ, A ⇒ B, Δ
 ───────────────────── →L      ───────────── →R
   Γ, A → B ⇒ Δ                Γ ⇒ A → B, Δ

 Γ ⇒ A, Δ                      Γ, A ⇒ Δ
 ─────────── ¬L                ─────────── ¬R
 Γ, ¬A ⇒ Δ                     Γ ⇒ ¬A, Δ
```

Additional structural rules (hidden when contexts are treated as sets): **weakening**, **contraction**, **exchange**, and **cut**:

```
 Γ ⇒ A, Δ    Γ, A ⇒ Δ
 ───────────────────── Cut
        Γ ⇒ Δ
```

Cut is **eliminable** (Gentzen's *Hauptsatz*, 1934): every provable sequent has a cut-free proof. Cut-free proofs have the **subformula property** (every formula in the proof is a subformula of the end sequent), which makes proof search finite and mechanical in propositional logic.

**LJ (intuitionistic):** the same rules but with **at most one formula on the right** (`Γ ⇒ A` or `Γ ⇒`). That single restriction removes LEM and Peirce.

**Example 1 (excluded middle in LK):** `⇒ P ∨ ¬P`

```
   ───────── Axiom
   P ⇒ P
   ───────── ¬R
   ⇒ P, ¬P
   ────────── ∨R
   ⇒ P ∨ ¬P
```

In LJ this fails: after ∨R we would have to pick one disjunct (`⇒ P` or `⇒ ¬P`), and neither is provable.

**Example 2 (Peirce's law in LK):** `⇒ ((P → Q) → P) → P`

```
 ───────── Axiom
 P ⇒ Q, P
 ──────────── →R              ───────── Axiom
 ⇒ P → Q, P                   P ⇒ P
 ───────────────────────────────────────── →L
          (P → Q) → P ⇒ P
          ──────────────────── →R
          ⇒ ((P → Q) → P) → P
```

(Read bottom-up: `→R` moves the antecedent to the left; `→L` on `(P → Q) → P` gives the left premise `⇒ P → Q, P` and the right premise `P ⇒ P`. The left premise is closed by `→R` and the axiom `P ⇒ Q, P`. Keeping `P` on the right of `⇒` while proving `P → Q` is exactly the classical move that LJ forbids.)

**Reading of rules:** left rules say how to *use* a formula (like elimination rules); right rules say how to *prove* it (like introduction rules). Every sequent-calculus rule **removes a connective as you go upward**, which is why search is so clean.

#### Format E: Analytic tableaux (refutation by branching)

To show `Γ ⊨ A`, start a tree with `Γ ∪ {¬A}` at the root and try to derive a contradiction on every branch. Rules (unsigned version). **α-rules** extend the same branch; **β-rules** split it into two branches.

| Type | Formula on the branch | Add |
|---|---|---|
| α | `¬¬A` | `A` |
| α | `A ∧ B` | `A` and `B` |
| α | `¬(A ∨ B)` | `¬A` and `¬B` |
| α | `¬(A → B)` | `A` and `¬B` |
| β | `A ∨ B` | branch `A` ∣ branch `B` |
| β | `¬(A ∧ B)` | branch `¬A` ∣ branch `¬B` |
| β | `A → B` | branch `¬A` ∣ branch `B` |
| β | `A ↔ B` | branch `A, B` ∣ branch `¬A, ¬B` |
| β | `¬(A ↔ B)` | branch `A, ¬B` ∣ branch `¬A, B` |

A branch is **closed** (marked ✗) if it contains some `X` and `¬X` (or ⊥). A tableau is **closed** if all branches are closed; then `Γ ⊨ A`.
If a branch is **open** and completed (all rules applied), it describes a **countermodel**: set every atom appearing as a positive literal to T, every atom appearing negated to F.

**Example with a countermodel.** Does `P ∨ Q ⊨ P ∧ Q`? Tableau for `{P ∨ Q, ¬(P ∧ Q)}`:

```
 P ∨ Q
 ¬(P ∧ Q)
 ├── P                         (from P ∨ Q)
 │   ├── ¬P   ✗  (P and ¬P)    (from ¬(P ∧ Q))
 │   └── ¬Q   open: P = T, Q = F
 └── Q
     ├── ¬P   open: P = F, Q = T
     └── ¬Q   ✗  (Q and ¬Q)
```

Two open branches, so **no**: the countermodels are P = T, Q = F and P = F, Q = T.

#### Format F: Resolution (clausal refutation)

Work with sets of **clauses** (Section 1.8.7). The single rule:

```
 C₁ ∪ {L}      C₂ ∪ {¬L}
 ─────────────────────────  Resolution
        C₁ ∪ C₂
```

(`L` is a literal; `C₁`, `C₂` are the remaining literals; the resolvent is the union.) A set of clauses is unsatisfiable iff the **empty clause** `{}` can be derived. The method is **refutation-complete**.

**Procedure to prove `Γ ⊨ A`:** (1) convert Γ and ¬A to CNF; (2) collect all clauses; (3) apply resolution until `{}` appears (then entailment holds) or no new clauses can be produced (then there is a countermodel).

**Example:** `P ∨ Q, ¬P ∨ R, ¬Q ∨ R ⊨ R`. Negated goal: `¬R`.

| Step | Clauses resolved | Resolvent |
|---|---|---|
| 1 | `{P, Q}`, `{¬P, R}` on P | `{Q, R}` |
| 2 | `{Q, R}`, `{¬R}` on R | `{Q}` |
| 3 | `{Q}`, `{¬Q, R}` on Q | `{R}` |
| 4 | `{R}`, `{¬R}` on R | `{}` |

Empty clause reached. The entailment holds. (This is the same inference pattern as the derived rule "proof by cases" in 2.9.6.)

#### Comparison of formats: what each makes easy

| Question | Best format |
|---|---|
| "Teach a beginner" | Fitch |
| "Show the exact dependencies" | Gentzen tree / Lemmon |
| "Prove a metatheorem about provability" | Hilbert |
| "Study the structure of proofs; cut elimination" | Sequent calculus |
| "Find a countermodel quickly" | Tableau |
| "Write an automated prover" | Resolution, tableau, or sequent search |
| "Machine-checked, large developments" | Proof assistant (Lean, Coq, Isabelle) |

### 2.9.8 Intuitionistic logic and the Curry-Howard correspondence

#### The idea

Classical logic assumes statements are true or false independently of whether we can find out. **Intuitionistic (constructive) logic** (Brouwer, Heyting) requires that truth means **having a construction**.

**BHK interpretation** (Brouwer-Heyting-Kolmogorov): what counts as a proof of each form:

| Formula | A proof of it is... |
|---|---|
| `A ∧ B` | a pair: a proof of A and a proof of B |
| `A ∨ B` | a proof of A **or** a proof of B, together with a tag saying which |
| `A → B` | a method that turns any proof of A into a proof of B |
| `⊥` | there is no proof of ⊥ |
| `¬A` | a method that turns any proof of A into a proof of ⊥ (i.e. a proof of `A → ⊥`) |
| `∃x A(x)` | a witness `t` together with a proof of `A(t)` |
| `∀x A(x)` | a method that, given any `t`, produces a proof of `A(t)` |

Under BHK, `A ∨ ¬A` is not a general truth: a proof of it would have to decide A, which is impossible for undecided statements (Goldbach, say).

#### What is and is not intuitionistically valid

| Valid in both | Valid classically only |
|---|---|
| `A → ¬¬A` | `¬¬A → A` |
| `¬¬¬A → ¬A` | `A ∨ ¬A` |
| `¬(A ∨ B) ↔ (¬A ∧ ¬B)` | `¬(A ∧ B) → (¬A ∨ ¬B)` |
| `(¬A ∨ B) → (A → B)` | `(A → B) → (¬A ∨ B)` |
| `(A → B) → (¬B → ¬A)` | `(¬B → ¬A) → (A → B)` |
| `¬¬(A ∨ ¬A)` | `((A → B) → A) → A` (Peirce) |
| `¬(A ∧ ¬A)` | `(A → B) ∨ (B → A)` |

**Glivenko's theorem (1929):** for propositional logic, `⊢_classical A` if and only if `⊢_intuitionistic ¬¬A`. So classical truths are intuitionistic truths "in disguise" as double negations. **Gödel-Gentzen negative translation** extends this to predicate logic.

**Disjunction property.** In intuitionistic logic, if `⊢ A ∨ B` then `⊢ A` or `⊢ B`. (Fails classically: `⊢ P ∨ ¬P` but neither disjunct is provable.)

**Kripke semantics** (preview): instead of a single valuation, a set of "stages of knowledge" ordered by growth of information; a formula is true at a stage if we have established it. Truth of `A` is persistent along growth, `¬A` holds when `A` can never become true.

#### The Curry-Howard correspondence

**Propositions are types; proofs are programs.**

| Logic | Type theory / programming |
|---|---|
| proposition `A` | type `A` |
| proof of `A` | a program (term) of type `A` |
| `A ∧ B` | product (pair) type `A × B` |
| `A ∨ B` | sum (tagged union) type `A + B` / `Either A B` |
| `A → B` | function type `A → B` |
| `⊤` | unit type (one value) |
| `⊥` | empty type (no values) |
| `¬A` | `A → ⊥` (a function to the empty type) |
| `∀x:T. A(x)` | dependent function type (Π-type) |
| `∃x:T. A(x)` | dependent pair type (Σ-type) |
| →I (discharge) | λ-abstraction `λx. e` |
| →E (modus ponens) | function application `f x` |
| ∧I / ∧E | pair construction `(a, b)` / projections `fst`, `snd` |
| ∨I / ∨E | injections `inl`, `inr` / `case` expression |
| ⊥E | the empty-case eliminator (`absurd`) |
| normalization of proofs | evaluation of programs |
| a proof of `A` exists | the type `A` is **inhabited** |

**Hypothetical syllogism is function composition.** The proof of `(P → Q) → (Q → R) → (P → R)` is the program

```
λ f. λ g. λ x. g (f x)
```

In Python-like syntax: `def hs(f, g): return lambda x: g(f(x))`. Each step in the Fitch proof corresponds to a step of the program: the assumption `P` is the parameter `x`; `→E 1,3` is the call `f(x)`; `→E 2,4` is the call `g(·)`; `→I 3-5` is the `lambda x`.

**Contraposition:** `λ f. λ nq. λ p. nq (f p)`, of type `(P → Q) → (¬Q → ¬P)`.

**Excluded middle and double-negation elimination have no such program** in general, which is the precise computational content of "not constructively provable". Classical logic corresponds to programs with **continuation operators** (`call/cc`; Griffin 1990), a deep and beautiful link.

**Why this matters for you:** the logic engine you will build (Chapter 8) is a miniature type checker: checking that a proof term has a given type *is* proof checking. Proof assistants (Lean, Coq, Agda) are built on exactly this.

### 2.9.9 Metatheory preview: what can be said about all proofs at once

| Property | Statement | Where proved |
|---|---|---|
| **Soundness** | `Γ ⊢ A` implies `Γ ⊨ A` | induction on proof structure (Chapter 6) |
| **Completeness** | `Γ ⊨ A` implies `Γ ⊢ A` | propositional: Post 1921, Kalmár 1935; first-order: Gödel 1929, Henkin 1949 (Chapter 6) |
| **Deduction theorem** | `Γ, A ⊢ B` iff `Γ ⊢ A → B` | built in to ND; proved for Hilbert systems |
| **Consistency** | not both `Γ ⊢ A` and `Γ ⊢ ¬A` for any A | follows from soundness |
| **Decidability** | there is an algorithm deciding `Γ ⊢ A` | truth tables, tableaux, DPLL (propositional only) |
| **Normalization / cut-elimination** | every proof can be transformed into a "direct" one | Gentzen 1934; Prawitz 1965 |
| **Compactness** | `Γ ⊨ A` implies some finite `Γ₀ ⊆ Γ` has `Γ₀ ⊨ A` | Chapter 6 |

### 2.9.10 Quick-check (with answers)

**Q1.** In a Fitch proof, can you cite line 4 on line 9 if line 4 is inside a box that closed at line 6? What can you do instead?
**Q2.** Which rule would you use to prove each goal first: (a) `P ∧ Q`, (b) `¬P`, (c) `P → Q`, (d) `P ∨ Q` with nothing known, (e) an atom `R` with no obvious route?
**Q3.** True or false: ∨E requires both cases to conclude the same formula.
**Q4.** What is the difference between a premise and an assumption?
**Q5.** What does the sequent `P, Q ⇒ R, S` mean?
**Q6.** Which tableau rule branches: `A ∧ B`, `A ∨ B`, `¬(A → B)`, `A → B`?
**Q7.** Name two classical-only theorems from the table in 2.9.8.
**Q8.** Under Curry-Howard, what is a proof of `A → A`?

**Answers.**
**A1.** No: line 4 is out of scope. Use the *closing rule* of the box (a range citation such as `2-6`), or restructure so the needed line is derived outside the box.
**A2.** (a) ∧I; (b) assume P, aim for ⊥, then ¬I; (c) assume P, aim for Q, then →I; (d) RAA (assume `¬(P ∨ Q)`); (e) RAA (assume `¬R`).
**A3.** True.
**A4.** A premise is given for the whole proof (depth 0, never discharged). An assumption is supposed only temporarily inside a box and is discharged when the box closes.
**A5.** If both P and Q are true, then at least one of R, S is true.
**A6.** `A ∨ B` and `A → B` branch (β-rules); `A ∧ B` and `¬(A → B)` do not (α-rules).
**A7.** E.g. `¬¬A → A`, `A ∨ ¬A`, Peirce's law, `(A → B) → (¬A ∨ B)`, `¬(A ∧ B) → ¬A ∨ ¬B`.
**A8.** The identity function `λx. x`.

## Problems for Chapter 2

**2.1 ★** P ∧ Q ⊢ Q ∧ P

**2.2 ★** P ⊢ ¬¬P

**2.3 ★** P → Q, ¬Q ⊢ ¬P (modus tollens)

**2.4 ★** ⊢ P → (Q → P)

**2.5 ★** P ∨ Q ⊢ Q ∨ P

**2.6 ★★** (P ∧ Q) → R ⊢ P → (Q → R) and the converse (exportation)

**2.7 ★★** ⊢ (P → (Q → R)) → ((P → Q) → (P → R))

**2.8 ★★** (P ∧ Q) ∨ (P ∧ R) ⊢ P ∧ (Q ∨ R) (the converse of Example 7)

**2.9 ★★** ⊢ ¬(P ∧ ¬P)

**2.10 ★★** ¬P ∨ ¬Q ⊢ ¬(P ∧ Q)

**2.11 ★★** ¬P ∨ Q ⊢ P → Q

**2.12 ★★** P ↔ Q, Q ↔ R ⊢ P ↔ R

**2.13 ★★★** P → Q ⊢ ¬P ∨ Q (classical; the goal is a disjunction with no direct route)

**2.14 ★★★** ¬(P ∧ Q) ⊢ ¬P ∨ ¬Q (classical)

**2.15 ★★★** ⊢ (P → Q) ∨ (Q → P)

**2.16 ★★★** (P → Q) → P ⊢ P

**2.17 ★★★** P ∨ Q, ¬P ∨ R ⊢ Q ∨ R (the resolution rule)

**2.18 ★★★ (meta)** For each of 2.1-2.16, decide whether it is provable *without* RAA (intuitionistically). Justify your answers by finding where RAA is essential, or by giving an RAA-free proof.

---

# Chapter 3. Predicate logic: language, translation, semantics

## 3.1 Why propositional logic is not enough

Consider the classic argument:

> All men are mortal. Socrates is a man. Therefore Socrates is mortal.

In propositional logic the three sentences are three unrelated atoms (p, q, r), and r does not follow from p and q. The validity depends on the *internal structure* of the sentences: "all", "is a man", "Socrates". Predicate logic (first-order logic, FOL) exposes that structure by adding **objects, properties, relations, and quantifiers**.

## 3.2 Syntax

A **signature** (vocabulary) consists of:
- **constant symbols** a, b, c, ..., naming particular objects,
- **function symbols** f, g, ... each with an arity (number of arguments),
- **predicate symbols** P, Q, R, ... each with an arity (a 0-ary predicate is a propositional atom).

**Terms** denote objects. **Formulas** state things.

```
t ::= x | c | f(t₁, ..., tₙ)                         (variable, constant, function application)

A ::= P(t₁, ..., tₙ) | t₁ = t₂ | ⊥                   (atomic formulas)
    | ¬A | (A ∧ A) | (A ∨ A) | (A → A) | (A ↔ A)
    | ∀x A | ∃x A
```

**Convention for quantifier scope.** Textbooks differ. In this course, a quantifier's scope extends as far to the right as the parentheses allow, so `∀x P(x) → Q(x)` would mean `∀x (P(x) → Q(x))`. To avoid any ambiguity, **always write the scope in parentheses**.

## 3.3 Free and bound variables

An occurrence of x in a formula is **bound** if it lies inside the scope of a quantifier ∀x or ∃x, and **free** otherwise. A formula with no free variables is a **sentence**. Only sentences are true or false in a structure. A formula with free variables is like an *open expression* ("x > 3"), whose truth depends on what x stands for.

**Example.** In `∀x (P(x, y) → ∃y Q(y, z)) ∧ R(x)`:
- `x` in P(x, y): bound by ∀x.
- `y` in P(x, y): **free** (the ∃y covers only Q(y, z)).
- `y` in Q(y, z): bound by ∃y.
- `z`: free.
- `x` in R(x): **free** (the scope of ∀x ended at the closing parenthesis).

The same *letter* can occur free in one place and bound in another, which is why we talk about *occurrences*.

### Substitution and variable capture

**A[t/x]** means "replace every *free* occurrence of x in A by the term t".

The danger is **capture**: if t contains a variable that becomes bound by a quantifier in A, the meaning changes. For example, let A = ∃y L(x, y) ("x loves someone") and substitute y for x:

- Naive: ∃y L(y, y) — "someone loves themselves". Wrong! The y we inserted was captured by ∃y.
- Correct: rename the bound variable first: ∃y' L(y, y') — "y loves someone".

We say **t is free for x in A** when no free occurrence of x in A lies inside the scope of a quantifier that binds a variable of t. Every proof rule that substitutes requires this (or implicitly renames bound variables). Capture-avoiding substitution is also the most common source of bugs in a logic engine (Chapter 8).

## 3.4 The art of translation

Translating English into logic is a skill, and it is where most "predicate logic confidence" is won or lost.

### The four basic patterns

| English | Logic | Note |
|---|---|---|
| All S are P | **∀x (S(x) → P(x))** | arrow, not ∧ |
| Some S are P | **∃x (S(x) ∧ P(x))** | ∧, not arrow |
| No S is P | ∀x (S(x) → ¬P(x)) ≡ ¬∃x (S(x) ∧ P(x)) | |
| Not all S are P | ∃x (S(x) ∧ ¬P(x)) ≡ ¬∀x (S(x) → P(x)) | |

**The two classic errors:**
- `∀x (S(x) ∧ P(x))` says *everything* is both S and P. (Wrong for "all students are happy": it says everything is a student.)
- `∃x (S(x) → P(x))` is true as soon as *anything* is not an S (the implication is vacuously true there). It says almost nothing.

**Rule of thumb:** ∀ goes with →, ∃ goes with ∧.

### More patterns

| English | Logic |
|---|---|
| Only S are P (nothing but S is P) | ∀x (P(x) → S(x)) |
| Every S that is P is also Q | ∀x ((S(x) ∧ P(x)) → Q(x)) |
| There are at least two P's | ∃x ∃y (P(x) ∧ P(y) ∧ x ≠ y) |
| There is at most one P | ∀x ∀y ((P(x) ∧ P(y)) → x = y) |
| There is exactly one P | ∃x (P(x) ∧ ∀y (P(y) → y = x)), written ∃!x P(x) |
| There are at least three P's | ∃x∃y∃z (P(x) ∧ P(y) ∧ P(z) ∧ x≠y ∧ x≠z ∧ y≠z) |

(Counting needs equality. "x ≠ y" abbreviates ¬(x = y).)

### Quantifier order matters

Let L(x, y) mean "x loves y".

| Sentence | Meaning |
|---|---|
| ∀x ∃y L(x, y) | Everyone loves someone (each person has their own beloved) |
| ∃y ∀x L(x, y) | There is one person whom everybody loves |
| ∀y ∃x L(x, y) | Everyone is loved by someone |
| ∃x ∀y L(x, y) | Someone loves everybody |

The second implies the first, **but not conversely**. In general: **∃∀ implies ∀∃, never the other way.** Same-type quantifiers commute (∀x∀y ≡ ∀y∀x, ∃x∃y ≡ ∃y∃x).

### A worked translation

*"Every student likes some teacher"* with S, T, L as above:

∀x (S(x) → ∃y (T(y) ∧ L(x, y)))

*"Some teacher is liked by every student"*:

∃y (T(y) ∧ ∀x (S(x) → L(x, y)))

These are not equivalent. The second has one teacher for all students, the first allows a different teacher per student.

### Translation checklist

1. Decide the **domain** (what the variables range over) and the **signature**.
2. Find the quantifier words ("every", "some", "no", "only", "exactly") and their *scope*.
3. Pick ∀→ or ∃∧ for each restricted quantifier.
4. Read your formula back into English and compare. Then test it on a small example world.

## 3.5 Semantics: structures and truth

A **structure** (model) M = (D, I) consists of:
- a non-empty **domain** D (the set of objects),
- an **interpretation** I giving each constant a member of D, each n-ary function symbol a function Dⁿ → D, and each n-ary predicate symbol an n-ary relation on D.

A variable **assignment** s maps variables to members of D. Truth is defined by recursion (Tarski):

| Formula | Satisfied in M under s iff... |
|---|---|
| P(t₁,...,tₙ) | the tuple of values of the tᵢ is in the relation I(P) |
| t₁ = t₂ | the two terms denote the same element |
| ¬A, A ∧ B, A ∨ B, A → B | as in propositional logic |
| **∀x A** | A is satisfied under **every** modification of s that sets x to some d ∈ D |
| **∃x A** | A is satisfied under **some** such modification |

For a sentence, the assignment is irrelevant, so we just say M ⊨ A ("A is true in M").

**Intuition.** ∀x A(x) is a (possibly infinite) conjunction A(d₁) ∧ A(d₂) ∧ ..., and ∃x A(x) is a (possibly infinite) disjunction. In a finite domain this is literally true, so you can evaluate by expanding.

**Example.** Let D = {1, 2, 3}, and R = {(1,2), (2,3), (3,1)} (a cycle).
- ∀x ∃y R(x, y): true. 1→2, 2→3, 3→1.
- ∃y ∀x R(x, y): false. For y = 1, R(1,1) fails. For y = 2, R(2,2) fails. For y = 3, R(1,3) fails.
- ∀x ∀y (R(x,y) → ¬R(y,x)): true (no two elements point at each other).

### Validity, satisfiability, entailment

| Concept | Meaning |
|---|---|
| A is **valid** (⊨ A) | true in **every** structure (under every assignment) |
| A is **satisfiable** | true in **some** structure |
| Γ ⊨ A | every structure making all of Γ true makes A true |
| A ≡ B | A ↔ B is valid |

**Non-empty domains.** Standard FOL requires D ≠ ∅. This is why ∀x P(x) → ∃x P(x) is valid and why the drinker paradox (Example 5 of Section 4.3) is a theorem. Free logics drop this requirement.

### Countermodels: how to show something is not valid

To show A is **not valid**, exhibit a structure where A is false. To show Γ ⊭ A, exhibit a structure where Γ is true and A is false. Method:

1. Try a **tiny domain** first ({1} or {1, 2}).
2. Define each predicate by listing which elements (or pairs) satisfy it.
3. **Verify** by expanding the quantifiers over the domain.

**Example.** Show (∃x P(x) ∧ ∃x Q(x)) → ∃x (P(x) ∧ Q(x)) is not valid. Take D = {1, 2}, P = {1}, Q = {2}. Then ∃x P(x) is true (x = 1), ∃x Q(x) is true (x = 2), but no element satisfies both, so the consequent is false.

**Validity cannot be refuted that way for valid formulas**, and, crucially, there is **no algorithm** that decides validity of arbitrary FOL formulas (Church-Turing, Chapter 6). Some formulas have *only infinite* models. For example,

∀x ∃y R(x, y) ∧ ∀x ¬R(x, x) ∧ ∀x ∀y ∀z ((R(x, y) ∧ R(y, z)) → R(x, z))

is satisfiable (take ℕ with <), but no finite structure satisfies it (Problem 3.11). So a countermodel search over finite structures can fail even when countermodels exist.

## 3.6 Quantifier laws

### Negation (De Morgan for quantifiers)

- ¬∀x A ≡ ∃x ¬A
- ¬∃x A ≡ ∀x ¬A

To negate a long quantified statement, **flip every quantifier and negate the matrix**. Example, continuity of f at a:

∀ε>0 ∃δ>0 ∀x (|x − a| < δ → |f(x) − f(a)| < ε)

becomes

∃ε>0 ∀δ>0 ∃x (|x − a| < δ ∧ |f(x) − f(a)| ≥ ε)

(using ¬(A → B) ≡ A ∧ ¬B on the last step).

### Distribution

| Valid equivalences | |
|---|---|
| ∀x (A ∧ B) | ≡ ∀x A ∧ ∀x B |
| ∃x (A ∨ B) | ≡ ∃x A ∨ ∃x B |

| Valid implications (one direction only) | Converse is **not** valid |
|---|---|
| ∀x A ∨ ∀x B → ∀x (A ∨ B) | ∀x (A ∨ B) → ∀x A ∨ ∀x B  (false: D = {1,2}, A = {1}, B = {2}) |
| ∃x (A ∧ B) → ∃x A ∧ ∃x B | ∃x A ∧ ∃x B → ∃x (A ∧ B) |
| ∀x (A → B) → (∀x A → ∀x B) | (∀x A → ∀x B) → ∀x (A → B) |
| ∃x ∀y R → ∀y ∃x R | ∀y ∃x R → ∃x ∀y R |

**Memory aid.** ∀ distributes over ∧, ∃ distributes over ∨. The "wrong" pairings fail because a single witness (or a single element) cannot be asked to serve two different properties.

### Moving quantifiers across a connective

If **x is not free in B**:

| | |
|---|---|
| (∀x A) ∧ B ≡ ∀x (A ∧ B) | (∃x A) ∧ B ≡ ∃x (A ∧ B) |
| (∀x A) ∨ B ≡ ∀x (A ∨ B) | (∃x A) ∨ B ≡ ∃x (A ∨ B) |
| B → ∀x A ≡ ∀x (B → A) | B → ∃x A ≡ ∃x (B → A) |
| **(∀x A) → B ≡ ∃x (A → B)** | **(∃x A) → B ≡ ∀x (A → B)** |

The last row, where the quantifier **flips** when it leaves the antecedent, surprises everyone. Reason: "if everything is P then B" is the same as "there is some counterexample to P, or B", i.e., ∃x (P(x) → B).

## 3.7 Prenex normal form

A formula is in **prenex normal form** if all quantifiers come first: Q₁x₁ ... Qₙxₙ M, where M has no quantifiers. Every formula is equivalent to one in prenex form. Procedure:

1. Eliminate ↔ and →.
2. Rename bound variables apart so no two quantifiers use the same variable.
3. Push negations inward (flipping quantifiers).
4. Pull quantifiers out using the rules of Section 3.6.

**Example.** (∀x P(x)) → (∃y Q(y)).
Using (∀x A) → B ≡ ∃x (A → B): ∃x (P(x) → ∃y Q(y)), then ∃x ∃y (P(x) → Q(y)).

Prenex form is the first step on the way to automated proving (Chapter 7).

## 3.8 Chapter 3 in complete detail (the from-zero companion)

Predicate logic is where most people lose confidence, usually because it was introduced as a pile of symbols without the *picture* behind it. This companion supplies the picture and then builds the formalism slowly: **what each symbol is for, what counts as a well-formed expression and what does not, exactly what free and bound mean, how substitution works step by step, how to translate any English sentence, and how truth in a structure is computed.**

### 3.8.1 The picture: objects, properties, relations, functions

Imagine a world, a collection of **things** (people, numbers, points, sets...). Call the collection the **domain**. We want to say things about the things:

| We want to say | Kind of statement | Logical device |
|---|---|---|
| "Socrates is a man." | a *property* of one object | **unary predicate** `Man(socrates)` |
| "Ann loves Bob." | a *relation* between two objects | **binary predicate** `Loves(ann, bob)` |
| "3 is between 2 and 5." | a relation among three objects | **ternary predicate** `Between(3, 2, 5)` |
| "Bob's father is tall." | an object *given by* another object | **function** `father(bob)`, then `Tall(father(bob))` |
| "Everything is self-identical." | statement about *all* objects | **universal quantifier** |
| "Something is red." | statement about *at least one* object | **existential quantifier** |

Propositional logic cannot see inside "Socrates is a man". Predicate logic can: it splits a sentence into **names** (terms) and **what is said about them** (predicates), and adds **quantifiers** to speak about unnamed objects.

**First-order** means: quantifiers range over **objects** of the domain only, never over properties or relations. (Quantifying over properties, "for every property P...", is *second-order* logic; see 3.8.11.)

### 3.8.2 The ingredients of the language

A first-order language has these kinds of symbols. Learn the table; everything else is a combination of them.

| Category | Role | Typical letters / examples | Arity |
|---|---|---|---|
| **Individual variables** | placeholders for "some object"; can be quantified | `x, y, z, u, v, w, x₁, x₂, ...` | n/a |
| **Individual constants** | fixed names of particular objects | `a, b, c, d, e`; also `0, 1, socrates, ∅, π` | 0 |
| **Function symbols** | build a new object from objects | `f, g, h`; also `+, ·, succ, father, sin` | n ≥ 1 |
| **Predicate (relation) symbols** | say something true or false of objects | `P, Q, R, S`; also `<, ≤, ⊆, Prime, Loves` | n ≥ 0 |
| **Equality** `=` | "is the very same object as" | `=` | 2 |
| **Connectives** | combine formulas | `¬ ∧ ∨ → ↔` (and `⊤ ⊥`) | 1 or 2 |
| **Quantifiers** | speak about all / some objects | `∀`, `∃` | binds a variable |
| **Punctuation** | grouping, argument lists | `( ) ,` | |

Key points:

- **Constants are 0-ary function symbols.** A **propositional atom** is a 0-ary predicate symbol. So propositional logic is the special case of predicate logic with no variables, functions or quantifiers.
- **Arity** = number of arguments. `Loves` has arity 2 (`Loves(x, y)`); `succ` has arity 1; `+` has arity 2 (written infix `x + y`, which is notation for `+(x, y)`).
- **Functions are total:** `f(a)` must denote *some* object for every object a. "The king of France" is not a function symbol on people (it would be undefined). Handle partial functions with predicates (`King(x, y)`) or definite descriptions (3.8.6).
- **Predicates versus functions:** a predicate makes a *sentence* (true/false). A function makes an *object*. `Tall(father(bob))` is a sentence; `father(bob)` is an object, not a sentence.
- Infix notation (`x < y`, `x + y`, `x = y`) is a convenience: `<` is a binary predicate and `+` a binary function.

The collection of non-logical symbols (constants, function symbols, predicate symbols, each with arity) is the **signature** (or **vocabulary**, **language**) `σ`. The logical symbols (connectives, quantifiers, `=`, punctuation, variables) are the same in every language.

**Examples of signatures**

| Subject | Constants | Functions | Predicates |
|---|---|---|---|
| Arithmetic of ℕ | `0, 1` | `+, ·` (binary), `S` (unary successor) | `<` (binary) (and `=`) |
| Groups | `e` | `·` (binary), `⁻¹` (unary) | (only `=`) |
| Graphs | (none) | (none) | `E` (binary edge relation) |
| Sets | (none) | (none) | `∈` (binary) |
| People | `socrates, plato` | `father` (unary) | `Man` (unary), `Loves` (binary) |
| Ordered fields | `0, 1` | `+, ·, −` | `<` |

### 3.8.3 Terms

**Terms** are the expressions that *denote objects*.

**Definition.**
1. Every variable is a term.
2. Every constant is a term.
3. If `f` is an `n`-ary function symbol and `t₁, ..., tₙ` are terms, then `f(t₁, ..., tₙ)` is a term.
4. Nothing else is a term.

**Examples** (signature: constants `0, 1`; functions `S` (1-ary), `+` (2-ary); variables `x, y`):

| Expression | Term? | Notes |
|---|---|---|
| `x` | yes | variable |
| `0` | yes | constant |
| `S(0)` | yes | "the successor of 0", i.e. 1 |
| `S(S(x))` | yes | x + 2 |
| `+(x, S(y))` | yes | written `x + S(y)` |
| `S(0, 1)` | **no** | wrong arity |
| `+(x)` | **no** | wrong arity |
| `<(x, y)` | **no (not a term)** | this is a *formula* (a predicate application) |
| `S(x < y)` | **no** | you cannot put a formula inside a term |

**Ground (closed) terms** contain no variables: `0`, `S(S(0))`, `+(S(0), S(0))`. They denote specific objects once the structure is fixed. **Term tree:** like formula trees; `S(x + y)` is a root `S` whose child is a `+` node with children `x, y`.

**Term substitution:** `t[s/x]` replaces every `x` in `t` by `s`. Example: `(x + S(y))[S(0)/x] = S(0) + S(y)`. For terms there is no capture problem (no binders).

**The Herbrand universe** of a language is the set of all ground terms (it matters in Chapter 7).

### 3.8.4 Formulas

**Atomic formulas** are the smallest statements:

1. `P(t₁, ..., tₙ)` where `P` is an `n`-ary predicate symbol and the `tᵢ` are terms;
2. `t₁ = t₂` for terms `t₁, t₂`;
3. `⊤` and `⊥`.

**Compound formulas:**

4. if `A` is a formula, so is `¬A`;
5. if `A, B` are formulas, so are `(A ∧ B)`, `(A ∨ B)`, `(A → B)`, `(A ↔ B)`;
6. if `A` is a formula and `x` a variable, then `∀x A` and `∃x A` are formulas.

Nothing else is a formula.

**What is NOT a formula (and why).** The most useful way to catch errors is to ask: "is this a *term* (an object) or a *formula* (a statement)? And is each part used in a place that accepts that kind?"

| Expression | Problem |
|---|---|
| `P(Q(x))` where `P`, `Q` are predicates | a predicate application is a *formula*, but arguments must be *terms* |
| `f(x) ∧ P(x)` | `f(x)` is a term (object), not a statement; `∧` needs formulas |
| `x ∨ y` | variables are terms, not formulas |
| `P(x) = Q(x)` | `=` relates terms; this relates formulas (use `↔`) |
| `∀x` | quantifier with nothing in its scope |
| `∀a P(a)` where `a` is a constant | only **variables** can be quantified |
| `∀P P(a)` | quantifies a predicate: second-order, not allowed |
| `∃x P(x) → ∀` | incomplete |
| `P(x, y)` where `P` is unary | wrong arity |
| `1 + 2` | a term, not a sentence (says nothing) |
| `1 + 2 = 3` | **yes**, a formula (`=` between terms) |

**Formula trees** have the same shape as in propositional logic, with two additions: quantifier nodes have one child (the body) and are labelled with the bound variable.

Formula: `∀x (P(x) → ∃y R(x, y))`

```
        ∀x
         │
         →
       /   \
    P(x)    ∃y
             │
           R(x,y)
```

Atomic formulas are the leaves. Main connective of the whole formula: `∀x` (so it is a universal statement).

**Precedence and scope convention in this course.** Negation binds tightest; then `∧`, `∨`, `→`, `↔`. The scope of a quantifier extends as far right as the parentheses allow. So `∀x P(x) → Q(x)` means `∀x (P(x) → Q(x))`. Many other books instead make a quantifier bind only the *next* formula, so the same string means `(∀x P(x)) → Q(x)`: a different statement (with `x` free in `Q(x)`)! **Always write the body of a quantifier in parentheses** and you will never be wrong.

### 3.8.5 Free and bound variables in depth

#### The binding structure

In `∀x A` (or `∃x A`), the quantifier **binds** `x` throughout `A`, the **scope** (or *body*, *matrix*). The variable `x` right after the quantifier is the **binder**. Inside `A`, occurrences of `x` are **bound** (unless captured by an inner quantifier on the same letter); occurrences of other variables are free unless some other quantifier binds them.

#### Computing free variables (definition by recursion)

| Formula | `FV(formula)` |
|---|---|
| `P(t₁, ..., tₙ)` | all variables occurring in `t₁, ..., tₙ` |
| `t₁ = t₂` | variables of `t₁` and `t₂` |
| `⊤, ⊥` | ∅ |
| `¬A` | `FV(A)` |
| `A ∧ B`, `A ∨ B`, `A → B`, `A ↔ B` | `FV(A) ∪ FV(B)` |
| `∀x A`, `∃x A` | `FV(A) \ {x}` |

Example: `FV(∀x (P(x, y) → ∃y Q(y, z)) ∧ R(x))`, with the rule that the quantifier scope extends to the closing bracket:

- `FV(P(x, y)) = {x, y}`
- `FV(Q(y, z)) = {y, z}`, so `FV(∃y Q(y, z)) = {z}`
- `FV(P(x,y) → ∃y Q(y,z)) = {x, y} ∪ {z} = {x, y, z}`
- `FV(∀x (…)) = {y, z}`
- `FV(R(x)) = {x}`
- Total: `{y, z} ∪ {x} = {x, y, z}`. The letter `x` is free (in `R(x)`) even though it is also bound elsewhere in the same formula.

**Terminology**

| Term | Meaning |
|---|---|
| **Sentence** (closed formula) | `FV = ∅`; has a definite truth value in a structure |
| **Open formula** | has free variables; like a predicate "x is even" |
| **Universal closure** `∀*A` | prefix `∀` for each free variable: makes a sentence |
| **Existential closure** | prefix `∃` for each free variable |
| **Free occurrence / bound occurrence** | refer to *positions*, not letters |
| **Vacuous quantifier** | binds a variable not occurring: `∀x P(a)` is equivalent to `P(a)` (given non-empty domain) |

**Meaning of a formula with free variables.** `x > 3` is neither true nor false until `x` is given a value; its truth depends on an **assignment** (3.8.8). In a proof, a free variable is a *placeholder for an arbitrary object*.

#### Renaming bound variables (α-conversion)

The *name* of a bound variable carries no information: `∀x P(x)` and `∀y P(y)` say the same. Two formulas that differ only by a consistent renaming of bound variables are **α-equivalent** and are considered identical. Rules for renaming `∀x A` to `∀z A[z/x]`:

1. `z` must not occur free in `A` (otherwise it would be captured).
2. Replace the binder and every free occurrence of `x` in `A`.

Example: `∀x ∃y L(x, y)` ≡α `∀u ∃v L(u, v)`, but **not** ≡α `∀y ∃y L(y, y)` (that merges two different variables into one).

**Standardizing apart:** rename bound variables so all binders in a formula use different letters and none coincide with a free variable. Do this before pulling quantifiers (prenex), before substituting, and before writing a program.

#### Substitution `A[t/x]`: definition by recursion

`A[t/x]` is "A with every **free** occurrence of x replaced by the term t, with renaming of bound variables where needed to avoid capture".

| Case | Result |
|---|---|
| `P(t₁, ..., tₙ)` | `P(t₁[t/x], ..., tₙ[t/x])` |
| `¬A` | `¬(A[t/x])` |
| `A ∘ B` | `A[t/x] ∘ B[t/x]` |
| `(∀x A)` | `∀x A` (x is not free here: nothing to do); same for `∃x` |
| `(∀y A)`, `y ≠ x`, and (`y ∉ FV(t)` or `x ∉ FV(A)`) | `∀y (A[t/x])` |
| `(∀y A)`, `y ≠ x`, `y ∈ FV(t)` and `x ∈ FV(A)` | pick fresh `z`; `∀z (A[z/y][t/x])` |

Same for `∃`.

**Worked example 1** (no capture): `(∀y R(x, y))[c/x] = ∀y R(c, y)`.

**Worked example 2** (capture, so rename): `(∃y L(x, y))[y/x]`.
`y ∈ FV(t) = {y}` and `x ∈ FV(L(x,y))`, so rename the bound `y` to a fresh `z`: `∃z L(x, z)`; then substitute: `∃z L(y, z)`. Meaning: "y loves someone". The naive result `∃y L(y, y)` ("someone loves themselves") is wrong.

**Worked example 3** (term with function): `(∀y (R(x, y) → ∃x S(x, y)))[f(y)/x]`.

- The binder `∀y` has `y ∈ FV(f(y))` and `x ∈ FV` of the body, so rename `y ↦ z`: `∀z (R(x, z) → ∃x S(x, z))`.
- Substitute `f(y)` for free `x`: `R(f(y), z)`; inside `∃x S(x, z)` the `x` is bound, so unchanged.
- Result: `∀z (R(f(y), z) → ∃x S(x, z))`.

**Worked example 4** (term substitution into an atomic formula): `(P(x, g(x, y)))[h(a)/x] = P(h(a), g(h(a), y))`.

**t is free for x in A** means: substituting `t` for `x` in `A` needs no renaming, i.e. no free `x` of `A` lies in the scope of a quantifier binding a variable of `t`. Proof rules (Chapter 4) often state this as a side condition.

**Notation reminder** (Z4.7): substitution is written many ways: `A[t/x]`, `A(t/x)`, `A[x := t]`, `A[x ↦ t]`. Check the author's convention; some write `[x/t]` with the opposite order.

### 3.8.6 Quantifiers in depth, and the English-to-logic dictionary

#### What ∀ and ∃ really say

- `∀x A(x)`: "**no matter which** object you choose for x, A holds". Think: an infinite conjunction over the domain.
- `∃x A(x)`: "**at least one** object makes A true". Think: an infinite disjunction. "Exists" means "at least one", never "exactly one" (that is `∃!`).

Consequences, all worth memorizing:

1. **Vacuous truth of ∀ over an empty set.** `∀x (Unicorn(x) → Rides(x))` is true if there are no unicorns.
2. **∃ never holds vacuously:** `∃x (Unicorn(x) ∧ Rides(x))` requires a real unicorn.
3. **Restricted quantifiers:** to say "all S are P" you quantify over the *whole domain* and restrict with a condition: `∀x (S(x) → P(x))`. To say "some S is P": `∃x (S(x) ∧ P(x))`. Here is why: `∀x (S(x) ∧ P(x))` would say *everything* is an S, `∃x (S(x) → P(x))` is true whenever *anything* is not an S (a false antecedent makes the implication true).
4. **Quantifier alternation = dependence.** In `∀x ∃y A(x, y)` the `y` may depend on `x`; in `∃y ∀x A(x, y)` the `y` is chosen first and must work for all `x` ("Skolem functions" in Chapter 7 make this explicit: `∀x A(x, f(x))` versus `∀x A(x, c)`).

#### The big dictionary

Let `S`, `P`, `Q` be unary predicates, `a` a constant. (Choose the domain "everything" and use `S(x)` to restrict, or use a **sorted** domain; see below.)

| English | Formula |
|---|---|
| Everything is P | `∀x P(x)` |
| Something is P | `∃x P(x)` |
| Nothing is P | `∀x ¬P(x)` ≡ `¬∃x P(x)` |
| Not everything is P | `¬∀x P(x)` ≡ `∃x ¬P(x)` |
| All S are P; every S is P; each S is P; any S is P | `∀x (S(x) → P(x))` |
| Some S is P; at least one S is P; there is an S which is P; an S is P (specific) | `∃x (S(x) ∧ P(x))` |
| No S is P; not a single S is P; there is no S that is P | `∀x (S(x) → ¬P(x))` ≡ `¬∃x (S(x) ∧ P(x))` |
| Not every S is P; some S is not P | `∃x (S(x) ∧ ¬P(x))` |
| All S are not P (usually meaning "no S is P") | `∀x (S(x) → ¬P(x))` |
| Only S are P; nothing but S is P; P only if S | `∀x (P(x) → S(x))` |
| All and only S are P | `∀x (P(x) ↔ S(x))` |
| Every S that is P is Q | `∀x ((S(x) ∧ P(x)) → Q(x))` |
| Every S is P or Q | `∀x (S(x) → (P(x) ∨ Q(x)))` |
| Every S except a is P | `∀x ((S(x) ∧ x ≠ a) → P(x))` |
| All S other than a are P and a is not | `∀x ((S(x) ∧ x ≠ a) → P(x)) ∧ ¬P(a)` |
| There are at least two P's | `∃x ∃y (P(x) ∧ P(y) ∧ x ≠ y)` |
| There is at most one P | `∀x ∀y ((P(x) ∧ P(y)) → x = y)` |
| There is exactly one P | `∃x (P(x) ∧ ∀y (P(y) → y = x))`, or `∃!x P(x)` |
| There are exactly two P's | `∃x ∃y (P(x) ∧ P(y) ∧ x ≠ y ∧ ∀z (P(z) → (z = x ∨ z = y)))` |
| There are at most n S's | `∀x₁ … ∀xₙ₊₁ ((S(x₁) ∧ … ∧ S(xₙ₊₁)) → ⋁_{i<j} xᵢ = xⱼ)` (among any n+1 S's, two coincide) |
| The S is P (Russell) | `∃x (S(x) ∧ ∀y (S(y) → y = x) ∧ P(x))` |
| a is the only S | `S(a) ∧ ∀x (S(x) → x = a)` |
| The set of S's has a largest | uses an order relation `≤` (see below) |

#### Ambiguities of English

| English | Readings |
|---|---|
| "A dog is a mammal" | generic: `∀x (Dog(x) → Mammal(x))` |
| "A dog is barking outside" | specific: `∃x (Dog(x) ∧ Barking(x))` |
| "Any" | "any S is P" is universal; "if any S is P" is existential in the antecedent: `∃x(S∧P) → R` |
| "If anyone is at home, the light is on" | `∃x H(x) → L`, equivalent to `∀x (H(x) → L)` (the quantifier flip of Section 3.6) |
| "Every farmer who owns a donkey beats it" (donkey sentence) | `∀x ∀y ((F(x) ∧ D(y) ∧ O(x, y)) → B(x, y))` (note ∀ for "a donkey") |
| "Everybody loves somebody" | `∀x ∃y L(x, y)` (usual); `∃y ∀x L(x, y)` is a strained reading |
| "Not all that glitters is gold" | `¬∀x (G(x) → Au(x))` ≡ `∃x (G(x) ∧ ¬Au(x))` |
| "All that glitters is not gold" | ambiguous, avoid |
| "Most S are P", "few", "many", "more than half" | **not expressible** in first-order logic (needs generalized quantifiers) |
| "Finitely many", "infinitely many" | not expressible by a single FO sentence in general (compactness, Chapter 6) |
| "Every even number > 2 is a sum of two primes" | a first-order sentence over arithmetic (Goldbach), 3.8.7 |

#### Definite descriptions (Russell)

"The present king of France is bald" is analyzed (Russell, 1905) as three claims: there is a king, there is at most one, and he is bald:

`∃x (K(x) ∧ ∀y (K(y) → y = x) ∧ B(x))`.

False if there is no king. Its negation depends on **scope**: `¬∃x(K(x) ∧ ∀y(K(y) → y=x) ∧ B(x))` ("it is not true that the king is bald", true when there is no king) versus `∃x(K(x) ∧ ∀y(K(y) → y=x) ∧ ¬B(x))` ("the king is non-bald", false when there is no king). This resolves a classical puzzle about the law of excluded middle.

#### Many-sorted domains and relativization

If your domain contains several *kinds* of things (people and numbers, points and lines), you can:

- use **sorted** variables (`∀p:Person`, `∀n:Nat`), as in many-sorted logic and in Lean/Coq (`∀ p : Person`); or
- stay one-sorted and **relativize**: add unary predicates `Person(x)`, `Nat(x)` and write `∀x (Person(x) → …)`, `∃x (Nat(x) ∧ …)`.

Both are the same logic; the relativization translation is mechanical, and it is exactly the "∀ with →, ∃ with ∧" pattern.

### 3.8.7 Translation workshop

**Method (always follow it).**
1. Fix the **domain** and the **signature**; write the dictionary of symbols.
2. Find the **quantifier words**; decide each one's **restrictor** and **scope**.
3. Build the formula from the **outside in** (main connective first).
4. **Read back** into English, then **test on a small world**.

**Example 1.** Domain: people. `Student(x)`, `Teacher(x)`, `Likes(x, y)`.
*"Every student likes some teacher."* Outer: all students: `∀x (Student(x) → …)`. Inner: some teacher whom x likes: `∃y (Teacher(y) ∧ Likes(x, y))`.
`∀x (Student(x) → ∃y (Teacher(y) ∧ Likes(x, y)))`.

**Example 2.** *"There is a teacher whom every student likes."*
`∃y (Teacher(y) ∧ ∀x (Student(x) → Likes(x, y)))`. Compare with Example 1: the order of the quantifiers changed the meaning.

**Example 3.** *"No student likes every teacher."* Negate "some student likes every teacher": `¬∃x (Student(x) ∧ ∀y (Teacher(y) → Likes(x, y)))`. Equivalent: `∀x (Student(x) → ∃y (Teacher(y) ∧ ¬Likes(x, y)))`.

**Example 4.** *"Everyone loves someone who loves them back."* Domain: people.
`∀x ∃y (Loves(x, y) ∧ Loves(y, x))`.

**Example 5.** *"If someone is a thief, then someone is arrested."* `∃x Thief(x) → ∃y Arrested(y)`.

**Example 6.** Mathematics. Signature `{0, 1, +, ·, <}`, domain ℕ.

| Statement | Formula |
|---|---|
| x is even | `∃y (x = y + y)` |
| x divides y (x ∣ y) | `∃z (y = x · z)` |
| x is prime | `x > 1 ∧ ∀y ∀z (x = y · z → (y = 1 ∨ z = 1))` |
| there are infinitely many primes | `∀n ∃p (p > n ∧ Prime(p))` |
| every number has a successor | `∀x ∃y (y = x + 1)` |
| there is a least element | `∃x ∀y (x ≤ y)` |
| no largest element | `∀x ∃y (x < y)` |
| Goldbach | `∀x ((Even(x) ∧ x > 2) → ∃p ∃q (Prime(p) ∧ Prime(q) ∧ x = p + q))` |

Here `x > 1`, `x ≤ y` are abbreviations (`≤` as `x < y ∨ x = y`), `Even`, `Prime` abbreviations for the formulas above.

**Example 7.** Functions. Signature: a function symbol `f`, equality, domain arbitrary.

| Statement | Formula |
|---|---|
| f is injective (one-to-one) | `∀x ∀y (f(x) = f(y) → x = y)` |
| f is surjective (onto) | `∀y ∃x (f(x) = y)` |
| f is constant | `∃c ∀x (f(x) = c)` |
| f has a fixed point | `∃x (f(x) = x)` |
| f is idempotent | `∀x (f(f(x)) = f(x))` |

**Example 8.** Relations (binary `R`):

| Property | Formula |
|---|---|
| reflexive | `∀x R(x, x)` |
| irreflexive | `∀x ¬R(x, x)` |
| symmetric | `∀x ∀y (R(x, y) → R(y, x))` |
| antisymmetric | `∀x ∀y ((R(x, y) ∧ R(y, x)) → x = y)` |
| transitive | `∀x ∀y ∀z ((R(x, y) ∧ R(y, z)) → R(x, z))` |
| total (connected) | `∀x ∀y (R(x, y) ∨ R(y, x))` |
| serial (every element has a successor) | `∀x ∃y R(x, y)` |
| functional | `∀x ∀y ∀z ((R(x, y) ∧ R(x, z)) → y = z)` |
| dense | `∀x ∀y (R(x, y) → ∃z (R(x, z) ∧ R(z, y)))` |

**Example 9.** Analysis (ε-δ), Section 3.6. Using order and absolute value as symbols, "f is continuous at a": `∀ε (ε > 0 → ∃δ (δ > 0 ∧ ∀x (|x − a| < δ → |f(x) − f(a)| < ε)))`. The pattern of nested restricted quantifiers is `∀ε>0` = `∀ε (ε > 0 → …)`, `∃δ>0` = `∃δ (δ > 0 ∧ …)`.

**Example 10.** Sets. Predicate `∈`. "A ⊆ B": `∀x (x ∈ A → x ∈ B)`. "A = B" (extensionality): `∀x (x ∈ A ↔ x ∈ B)`. "∅" characterized by `∀x ¬(x ∈ ∅)`. "x is in the union of A and B": `x ∈ A ∨ x ∈ B`.

**Common translation errors**

| Error | Why wrong |
|---|---|
| `∀x (S(x) ∧ P(x))` for "all S are P" | says everything is an S |
| `∃x (S(x) → P(x))` for "some S is P" | true if anything is not S |
| `¬∀x P(x)` read as "no x is P" | that is `∀x ¬P(x)` |
| using one variable twice in nested quantifiers by accident: `∀x (S(x) → ∃x P(x))` | inner x shadows the outer x |
| leaving a free variable in what should be a sentence | the statement is then not yet true or false |
| mixing up `∀x∃y` and `∃y∀x` | dependence changes |
| translating "only S are P" as `∀x (S(x) → P(x))` | direction reversed |

### 3.8.8 Semantics in complete detail

#### Structures

A **structure** (model, interpretation) `M` for a signature `σ` consists of:

1. a non-empty set `D` (also written `|M|`, `dom(M)`, `M`'s **domain** or *universe*);
2. for each constant `c`: an element `c^M ∈ D`;
3. for each `n`-ary function symbol `f`: a function `f^M : Dⁿ → D`;
4. for each `n`-ary predicate symbol `P`: a set of `n`-tuples `P^M ⊆ Dⁿ` (the tuples for which `P` holds).

(For `=` we always use true identity on `D`.)

**Example.** Signature `{a, f, P, R}` (constant, unary function, unary predicate, binary predicate). Structure `M`: `D = {1, 2, 3}`; `a^M = 1`; `f^M(1) = 2, f^M(2) = 3, f^M(3) = 3`; `P^M = {1, 2}`; `R^M = {(1,2), (2,3), (3,3)}`.

Many different structures can interpret the same symbols; the **same sentence may be true in one and false in another**. Truth is always *truth in a structure*.

#### Assignments

An **assignment** `s` assigns an element of `D` to each variable. We write `s[x ↦ d]` for the assignment that agrees with `s` except that `x` goes to `d`.

**Value of a term** `⟦t⟧^M_s`:
- `⟦x⟧ = s(x)`; `⟦c⟧ = c^M`; `⟦f(t₁,…,tₙ)⟧ = f^M(⟦t₁⟧, …, ⟦tₙ⟧)`.

In the structure above with `s(x) = 2`: `⟦f(f(x))⟧ = f^M(f^M(2)) = f^M(3) = 3`.

#### Satisfaction (Tarski's definition)

`M, s ⊨ A` ("A is satisfied in M under s") is defined by recursion:

| Formula | `M, s ⊨` it iff |
|---|---|
| `P(t₁, …, tₙ)` | `(⟦t₁⟧, …, ⟦tₙ⟧) ∈ P^M` |
| `t₁ = t₂` | `⟦t₁⟧ = ⟦t₂⟧` |
| `⊤` / `⊥` | always / never |
| `¬A` | not `M, s ⊨ A` |
| `A ∧ B` | both |
| `A ∨ B` | at least one |
| `A → B` | not `M, s ⊨ A`, or `M, s ⊨ B` |
| `A ↔ B` | both or neither |
| `∀x A` | for **every** `d ∈ D`: `M, s[x ↦ d] ⊨ A` |
| `∃x A` | for **some** `d ∈ D`: `M, s[x ↦ d] ⊨ A` |

For a **sentence** the assignment is irrelevant and we write `M ⊨ A` ("A is true in M", "M is a model of A"). For a set of sentences `Γ`: `M ⊨ Γ` if `M ⊨ A` for every `A ∈ Γ`.

**Coincidence lemma.** The truth of `A` under `s` depends only on the values of `s` on `FV(A)`.

#### Fully worked evaluation

Structure `M`: `D = {1, 2, 3}`, `P^M = {1, 2}`, `R^M = {(1,2), (2,3), (3,3)}`.

**(i) `∀x (P(x) → ∃y R(x, y))`.** For each `d ∈ D`:

| x | P(x)? | ∃y R(x, y)? (witness) | `P(x) → ∃y R(x,y)` |
|---|---|---|---|
| 1 | T | T (y = 2) | T |
| 2 | T | T (y = 3) | T |
| 3 | F | T (y = 3) | T (antecedent false) |

All three T, so the sentence is **true** in `M`.

**(ii) `∃y ∀x R(x, y)`.** Try each y:

| y | `∀x R(x, y)`? | counter-x |
|---|---|---|
| 1 | F | x = 1 (R(1,1) ∉ R) |
| 2 | F | x = 2 (R(2,2) ∉ R) |
| 3 | F | R(1,3) ∉ R: x = 1 |

No y works, so the sentence is **false** in `M`.

**(iii) `∀x ∃y R(x, y)`:** x = 1 → y = 2; x = 2 → y = 3; x = 3 → y = 3. **True.** Together with (ii) this shows `∀x ∃y R ⊭ ∃y ∀x R`: `M` is a countermodel.

**(iv) `∀x R(x, x)`:** false (x = 1 fails). **(v) `∃x R(x, x)`:** true (x = 3).

**The expansion trick** (finite domains): replace `∀x A(x)` by `A(1) ∧ A(2) ∧ A(3)` and `∃x A(x)` by `A(1) ∨ A(2) ∨ A(3)`; you get a propositional formula over atoms `P(1), R(1,2), …`.

#### Kinds of sentences and relations

| Concept | Definition |
|---|---|
| **Valid** (logically true) `⊨ A` | true in **every** structure |
| **Satisfiable** | true in **some** structure |
| **Contradictory** | true in **no** structure |
| **Contingent** | true in some, false in others |
| `Γ ⊨ A` | every structure that makes all of `Γ` true makes `A` true |
| `A ≡ B` | `A ↔ B` valid |
| **Model of a theory** | a structure making every axiom true |
| **Elementary equivalence** `M ≡ N` | `M` and `N` satisfy the same sentences |
| **Isomorphism** `M ≅ N` | a bijection preserving all symbols; isomorphic structures satisfy the same sentences |

**Validity is much harder than in propositional logic:** there are infinitely many structures of every infinite size; no truth table exists. Methods: proof (Chapter 4), countermodel search, tableaux/resolution (Chapter 7). By the **Church-Turing theorem**, validity of first-order sentences is **undecidable** (but semi-decidable).

#### Standard theories as lists of sentences

| Theory | Signature | Axioms (sentences) | A model |
|---|---|---|---|
| Equivalence relation | `R` | `∀x R(x,x)`; `∀x∀y(R(x,y)→R(y,x))`; `∀x∀y∀z(R(x,y)∧R(y,z)→R(x,z))` | `=` on any set; "same remainder mod 5" on ℤ |
| Strict partial order | `<` | `∀x ¬(x<x)`; `∀x∀y∀z(x<y∧y<z→x<z)` | `<` on ℕ; ⊊ on sets |
| Group | `e, ·, ⁻¹` | `∀x∀y∀z (x·y)·z = x·(y·z)`; `∀x x·e = x`; `∀x e·x = x`; `∀x x·x⁻¹ = e`; `∀x x⁻¹·x = e` | (ℤ, 0, +, −); nonzero reals under ×; symmetries of a triangle |
| Graph (simple) | `E` | `∀x ¬E(x,x)`; `∀x∀y(E(x,y)→E(y,x))` | a triangle: `D={1,2,3}`, all pairs of distinct elements |
| Dense linear order without endpoints | `<` | strict total order, `∀x∀y(x<y→∃z(x<z∧z<y))`, `∀x∃y(x<y)`, `∀x∃y(y<x)` | (ℚ, <); also (ℝ, <) |
| Peano arithmetic (PA) | `0, S, +, ·` | `∀x S(x)≠0`; `∀x∀y (S(x)=S(y)→x=y)`; `x+0=x`; `x+S(y)=S(x+y)`; `x·0=0`; `x·S(y)=x·y+x`; **induction schema** for every formula `A(x)` | ℕ (standard); nonstandard models exist (Chapter 6) |

#### Which properties can first-order sentences express?

- "The domain has at least `n` elements" — yes (using `=`). "Exactly n" — yes. "Infinite" — by an infinite set of sentences, but not by any single sentence.
- "The graph is connected", "the order is a well-order", "finite": **not** first-order expressible (consequences of compactness and Löwenheim-Skolem, Chapter 6).
- Monadic fragments (only unary predicates) are **decidable** (Löwenheim, 1915): without equality, a satisfiable sentence with `k` unary predicates has a model of size at most `2^k`.

### 3.8.9 Equality in detail

`=` is a **logical** symbol: in every structure it means true identity. Principles ("laws of identity"):

| Law | Statement |
|---|---|
| Reflexivity | `∀x x = x` |
| Symmetry | `∀x∀y (x = y → y = x)` |
| Transitivity | `∀x∀y∀z ((x = y ∧ y = z) → x = z)` |
| Substitutivity (Leibniz) | `x = y → (A(x) → A(y))` for every formula `A` |
| Congruence for functions | `x = y → f(x) = f(y)` |

`≠` abbreviates `¬(… = …)`. Equality is what lets first-order logic **count** ("at least/at most/exactly n") and **define uniqueness** (`∃!`). Without `=`, the sentence `∃x ∃y (P(x) ∧ P(y))` is satisfied by a structure with one P-element (take x = y), so it cannot enforce "two different objects".

**Identity vs equivalence:** `=` says the *same object*; an equivalence relation like "same height" is a different, user-defined predicate. Do not confuse `x = y` (identity) with `A(x) ↔ A(y)` (indiscernibility for a given formula).

### 3.8.10 From formulas to Skolem form (preview)

A formula like `∀x ∃y R(x, y)` asserts that for each x there is a y. We can name the dependency: introduce a **Skolem function** `f` and write `∀x R(x, f(x))`. This preserves satisfiability (but not equivalence) and removes `∃` altogether; it is the key step for automation (Chapter 7). Example:

`∃x ∀y ∃z R(x, y, z)` becomes `∀y R(c, y, g(y))` with `c` a new constant and `g` a new unary function. A witness chosen *before* y is a constant; a witness chosen *after* y is a function of y.

### 3.8.11 First-order logic among other logics

| Logic | Difference from first-order | Consequences |
|---|---|---|
| **Propositional** | no objects, no quantifiers | decidable (SAT, coNP-complete) |
| **First-order (FOL)** | quantify over objects | complete (Gödel), compact, undecidable |
| **Many-sorted FOL** | several domains/sorts | reducible to one-sorted FOL |
| **Second-order** | quantify over sets/relations: `∀X ∃x X(x)` | can express "finite", "well-ordering"; no complete proof system (with standard semantics); no compactness |
| **Higher-order, type theory** | quantify over functions of functions | Lean, Coq; Church's simple type theory |
| **Modal** | operators `□`, `◇`, Kripke worlds | propositional modal logics are mostly decidable |
| **Free logic** | allows empty domain or non-denoting terms | `∀xP(x) → ∃xP(x)` fails |
| **Infinitary** | infinite conjunctions | `L_{ω₁ω}` can express "finite" |

### 3.8.12 Quick-check (with answers)

**Q1.** Classify each as term, formula, or neither: (a) `f(a)`, (b) `P(f(a))`, (c) `f(P(a))`, (d) `∀x (x + 0 = x)`, (e) `∀x + 1`.
**Q2.** Compute `FV` of `∃y (R(x, y) ∧ ∀x S(x, z))`.
**Q3.** Compute `(∀y R(x, y))[y/x]` with renaming.
**Q4.** Translate: (a) "Every dog barks." (b) "Some dog does not bark." (c) "Only dogs bark." (d) "There is exactly one dog." Use `D`, `B`.
**Q5.** In the structure `D = {1, 2}`, `R^M = {(1,1), (1,2)}`, evaluate `∃x ∀y R(x, y)` and `∀x ∃y R(y, x)`.
**Q6.** Why is `∃x (S(x) → P(x))` a poor translation of "some S is P"?
**Q7.** Translate "the only even prime is 2" using `Even`, `Prime`, constant `2`.

**Answers.**
**A1.** (a) term; (b) formula; (c) neither (a formula inside a term); (d) formula (a sentence); (e) neither (incomplete).
**A2.** `FV(R(x,y) ∧ ∀x S(x,z)) = {x, y} ∪ ({x, z} \ {x}) = {x, y, z}`; remove `y` for `∃y`: **`{x, z}`**. (The `x` in `R(x, y)` is free; the `x` in `S(x, z)` is bound.)
**A3.** `y ∈ FV(y)` and `x` is free in the body: rename the bound `y` to `z`: `∀z R(x, z)`, then substitute: **`∀z R(y, z)`**.
**A4.** (a) `∀x (D(x) → B(x))`; (b) `∃x (D(x) ∧ ¬B(x))`; (c) `∀x (B(x) → D(x))`; (d) `∃x (D(x) ∧ ∀y (D(y) → y = x))`.
**A5.** `∃x ∀y R(x, y)`: x = 1: `R(1,1)` and `R(1,2)` both hold. **True.** `∀x ∃y R(y, x)`: x = 1: y = 1 works. x = 2: y = 1 works (`R(1,2)`). **True.**
**A6.** It is true as soon as anything is not an S (false antecedent), so it asserts almost nothing.
**A7.** `Even(2) ∧ Prime(2) ∧ ∀x ((Even(x) ∧ Prime(x)) → x = 2)`.

## Problems for Chapter 3

**3.1 ★** Translate with S(x) = "x is a student", T(x) = "x is a teacher", L(x, y) = "x likes y":
- (a) Every student likes every teacher.
- (b) No student likes every teacher.
- (c) Some student likes no teacher.
- (d) Every teacher is liked by at most one student.

**3.2 ★** In `∀x (P(x, y) → ∃y Q(y, z)) ∧ R(x)` list all free and bound occurrences (variable and position).

**3.3 ★** Compute (a) (∃y L(x, y))[y/x] with proper renaming; (b) (∀x P(x, y))[f(z)/y]; (c) (∀x P(x, y))[f(x)/y].

**3.4 ★★** Translate into FOL with the signature {0, 1, +, ·, <} over the natural numbers:
- (a) "x is even"
- (b) "x is prime"
- (c) "There are infinitely many primes"
- (d) "Every even number greater than 2 is a sum of two primes" (Goldbach, whose truth is unknown!)

**3.5 ★★** Negate and simplify so that ¬ appears only in front of atoms:
- (a) ∀x ∃y (x < y ∧ ∀z (z < y → z ≤ x))
- (b) The ε-δ definition of continuity (Section 3.6, verify the given answer)
- (c) "A sequence (aₙ) converges": ∃L ∀ε>0 ∃N ∀n>N |aₙ − L| < ε

**3.6 ★★** Express in FOL with equality: "at least 3 elements", "exactly 2 elements", "at most 2 elements".

**3.7 ★★** For each, prove valid or give a **countermodel** (small finite structure):
- (a) ∃x ∀y R(x, y) → ∀y ∃x R(x, y)
- (b) ∀y ∃x R(x, y) → ∃x ∀y R(x, y)
- (c) ∀x (P(x) → Q(x)) → (∀x P(x) → ∀x Q(x))
- (d) (∀x P(x) → ∀x Q(x)) → ∀x (P(x) → Q(x))
- (e) ∀x (P(x) ∨ Q(x)) → (∀x P(x) ∨ ∀x Q(x))
- (f) ∃x (P(x) ∧ Q(x)) → (∃x P(x) ∧ ∃x Q(x))
- (g) ∀x P(x) → ∃x P(x)
- (h) ∃x P(x) → ∀x P(x)

**3.8 ★★** Evaluate in the structure D = {1,2,3,4}, R(x,y) ⇔ x < y:
- (a) ∀x ∃y R(x, y)
- (b) ∃x ∀y (x = y ∨ R(x, y))
- (c) ∀x ∀y (R(x, y) → ∃z (R(x, z) ∧ R(z, y)))

**3.9 ★★** Convert to prenex normal form:
- (a) ∀x P(x) ∨ ∀x Q(x)
- (b) ∀x P(x) → ∃y Q(y)
- (c) ¬∀x (P(x) → ∃y R(x, y))

**3.10 ★★** Is ∀x ∃y R(x, y) ∧ ∀x ∀y (R(x,y) → R(y,x)) satisfiable in a finite structure? In a one-element structure? Describe all models with exactly two elements.

**3.11 ★★★** Show that the sentence ∀x ∃y R(x, y) ∧ ∀x ¬R(x, x) ∧ ∀x∀y∀z ((R(x,y) ∧ R(y,z)) → R(x,z)) has no finite model but does have an infinite one. (Hint: in a finite model, follow a chain x₀ R x₁ R x₂ ... and use pigeonhole plus transitivity and irreflexivity.)

**3.12 ★★★** Prove carefully, using the semantic definition (no tricks), that ∃x ∀y R(x, y) ⊨ ∀y ∃x R(x, y), and explain exactly where the argument breaks for the converse.

---

# Chapter 4. Natural deduction for predicate logic

## 4.1 The four quantifier rules

We keep all propositional rules and add rules for ∀, ∃ (and later =). Each follows the same intro/elim pattern.

| Rule | Form | Informal meaning | Side condition |
|---|---|---|---|
| **∀E** | from ∀x A, infer A[t/x] | "It holds for everything, so it holds for t" | t is a term, free for x in A |
| **∃I** | from A[t/x], infer ∃x A | "t is an example, so something has the property" | t is free for x in A |
| **∀I** | open a sub-proof introducing a **fresh name a** (with no assumption about it), derive A[a/x], infer ∀x A | "Let a be arbitrary... so it holds for all" | a is **fresh** (see below) |
| **∃E** | from ∃x A and a sub-proof that assumes A[a/x] for a **fresh name a** and reaches C, infer C | "Let a be such an object... then C" | a is **fresh**, and C does not contain a |

The first two are *easy* (just instantiate or generalize with an explicit term). The last two are *where proofs are won and lost*, because they have conditions on names.

**Format in Fitch notation** for the name-introducing sub-proofs:

```
|  [a]                 (∀I: a is a fresh name, no assumption)
|  ...
|  A(a)
∀x A(x)                ∀I

∃x A(x)
|  [a]  A(a)           (∃E: fresh a with assumption A(a))
|  ...
|  C
C                      ∃E
```

## 4.2 What "fresh" means, and why it matters

A name `a` is **fresh** in a rule if it does not occur in any premise, in any currently open assumption, in the formula ∀x A / ∃x A being used, or (for ∃E) in the conclusion C. In short: **you know nothing about a except what the rule gives you.**

Why this is necessary, and what goes wrong without it:

- **∀I.** To conclude "everything is P" you must have shown P(a) for an *arbitrary* a. If a is "that specific thing I assumed something about", the argument proves nothing general. Bad "proof" of **∃x P(x) ⊢ ∀x P(x)**:

  ```
  1.  ∃x P(x)           premise
  2.  |  [a] P(a)       assumption (∃E)
  3.  |  ∀x P(x)       ∀I 2  ← ILLEGAL: a occurs in the open assumption P(a)
  ```

- **∃E.** When you say "let a be a witness", you may only use that a satisfies A. Bad "proof" of **∀y ∃x R(x, y) ⊢ ∃x ∀y R(x, y)** (the invalid converse):

  ```
  1.  ∀y ∃x R(x, y)     premise
  2.  ∃x R(x, b)        ∀E 1
  3.  |  [a] R(a, b)    assumption (∃E)
  4.  |  ∀y R(a, y)     ∀I 3  ← ILLEGAL: b occurs in the open assumption R(a, b)
  ```

  The witness a depends on b (the "∃ comes after ∀" structure of the premise), and generalizing over b would break that dependence.

The side conditions are exactly what makes ∃∀ ⊢ ∀∃ provable and ∀∃ ⊬ ∃∀. **They are the proof-theoretic shadow of quantifier order.**

## 4.3 Worked examples

### Example 1. ∀x (P(x) → Q(x)), ∀x P(x) ⊢ ∀x Q(x)

Goal is universal, so introduce an arbitrary a.

```
1.  ∀x (P(x) → Q(x))   premise
2.  ∀x P(x)            premise
3.  |  [a]                       (fresh a)
4.  |  P(a) → Q(a)      ∀E 1
5.  |  P(a)             ∀E 2
6.  |  Q(a)             →E 4,5
7.  ∀x Q(x)            ∀I 3-6
```

In words: "Let a be arbitrary. Since all P's are Q's, P(a) → Q(a). Since everything is P, P(a). So Q(a). As a was arbitrary, everything is Q."

### Example 2. ∀x (P(x) → Q(x)), ∃x P(x) ⊢ ∃x Q(x)

We *use* an existential, so introduce a witness.

```
1.  ∀x (P(x) → Q(x))   premise
2.  ∃x P(x)            premise
3.  |  [a]  P(a)        assumption (∃E)
4.  |  P(a) → Q(a)      ∀E 1
5.  |  Q(a)             →E 4,3
6.  |  ∃x Q(x)          ∃I 5
7.  ∃x Q(x)            ∃E 2, 3-6
```

Check the side condition: the conclusion ∃x Q(x) does not contain a. ✔

### Example 3. ∃x ∀y R(x, y) ⊢ ∀y ∃x R(x, y)

Goal is universal: introduce arbitrary b. Then use the premise by naming its witness a.

```
1.  ∃x ∀y R(x, y)      premise
2.  |  [b]                        (fresh b, for ∀I)
3.  |  |  [a]  ∀y R(a, y)        assumption (∃E; a fresh, a ≠ b)
4.  |  |  R(a, b)                ∀E 3
5.  |  |  ∃x R(x, b)             ∃I 4
6.  |  ∃x R(x, b)               ∃E 1, 3-5
7.  ∀y ∃x R(x, y)      ∀I 2-6
```

Order of introduction matters: b is introduced **first**, and a is introduced **inside** b's scope. The ∃E conclusion ∃x R(x, b) mentions b but not a. ✔

### Example 4. ¬∀x P(x) ⊢ ∃x ¬P(x) (classical)

The goal ∃x ¬P(x) cannot be built directly (we have no witness), so use RAA.

```
1.  ¬∀x P(x)           premise
2.  |  ¬∃x ¬P(x)        assumption (for RAA)
3.  |  |  [a]
4.  |  |  |  ¬P(a)       assumption (for RAA)
5.  |  |  |  ∃x ¬P(x)    ∃I 4
6.  |  |  |  ⊥           ¬E 5,2
7.  |  |  P(a)           RAA 4-6
8.  |  ∀x P(x)           ∀I 3-7
9.  |  ⊥                 ¬E 8,1
10. ∃x ¬P(x)            RAA 2-9
```

The other three quantifier-negation laws are easier; do them as Problems 4.6-4.8.

### Example 5. The Drinker Paradox: ⊢ ∃x (D(x) → ∀y D(y))

*"In any non-empty pub there is someone such that, if they are drinking, then everybody is drinking."*

**Informal proof first** (always find the idea before formalizing):

> Case 1: everybody drinks. Then pick *anyone*; the implication holds because its consequent is true.
> Case 2: not everybody drinks. Then somebody is not drinking; pick that person. The implication holds because its antecedent is false.

Case 1 uses non-emptiness of the domain (we need someone to pick). The case split is on a statement and its negation, which is excluded middle, so this proof is classical.

**Formal proof** (via RAA, with the case analysis folded in):

```
1.  |  ¬∃x (D(x) → ∀y D(y))              assumption (for RAA)
2.  |  |  [b]
3.  |  |  |  ¬D(b)                       assumption (for RAA)
4.  |  |  |  |  D(b)                     assumption
5.  |  |  |  |  ⊥                        ¬E 4,3
6.  |  |  |  |  ∀y D(y)                  ⊥E 5
7.  |  |  |  D(b) → ∀y D(y)              →I 4-6
8.  |  |  |  ∃x (D(x) → ∀y D(y))         ∃I 7
9.  |  |  |  ⊥                           ¬E 8,1
10. |  |  D(b)                           RAA 3-9
11. |  ∀y D(y)                           ∀I 2-10
12. |  |  D(c)                           assumption  (c: any name; domain is non-empty)
13. |  |  ∀y D(y)                        reiteration of 11
14. |  D(c) → ∀y D(y)                    →I 12-13
15. |  ∃x (D(x) → ∀y D(y))               ∃I 14
16. |  ⊥                                 ¬E 15,1
17. ∃x (D(x) → ∀y D(y))                  RAA 1-16
```

Lines 2-11 show that the negated goal forces everyone to be a drinker (if some b weren't, b would be the witness). Lines 12-15 then use *any* name c to produce the witness, which is the place where the non-empty domain assumption is used. Using a name without a prior introduction is legitimate precisely because domains are non-empty.

### Example 6. Russell's barber: ⊢ ¬∃x ∀y (R(x, y) ↔ ¬R(y, y))

*R(x, y): "x shaves y". There is no barber who shaves exactly those who do not shave themselves.* (This is the logical core of Russell's paradox and of Cantor's theorem.)

```
1.  |  ∃x ∀y (R(x, y) ↔ ¬R(y, y))       assumption (for ¬I)
2.  |  |  [a]  ∀y (R(a, y) ↔ ¬R(y, y))  assumption (∃E)
3.  |  |  R(a, a) ↔ ¬R(a, a)            ∀E 2
4.  |  |  |  R(a, a)                    assumption
5.  |  |  |  ¬R(a, a)                   ↔E 3,4
6.  |  |  |  ⊥                          ¬E 4,5
7.  |  |  ¬R(a, a)                      ¬I 4-6
8.  |  |  R(a, a)                       ↔E 3,7
9.  |  |  ⊥                             ¬E 8,7
10. |  ⊥                                ∃E 1, 2-9
11. ¬∃x ∀y (R(x, y) ↔ ¬R(y, y))         ¬I 1-10
```

The magic is line 3: plug the barber into his own definition (y := a). No sophisticated idea is needed; the "paradox" is just the observation that P ↔ ¬P is contradictory.

### Example 7. Socrates: ∀x (Man(x) → Mortal(x)), Man(s) ⊢ Mortal(s)

```
1.  ∀x (Man(x) → Mortal(x))   premise
2.  Man(s)                    premise
3.  Man(s) → Mortal(s)        ∀E 1   (instantiate with the constant s)
4.  Mortal(s)                 →E 3,2
```

## 4.4 Equality

Two extra rules:

| Rule | Form |
|---|---|
| **=I** | infer t = t (no premises) |
| **=E** | from s = t and A[s/x], infer A[t/x] (substitute equals for equals) |

**Derived: symmetry.** s = t ⊢ t = s. Take A(x) to be "x = s":

```
1.  s = t              premise
2.  s = s              =I
3.  t = s              =E 1,2   (replace s by t in the first position of line 2, A(x) := x = s)
```

**Derived: transitivity.** s = t, t = u ⊢ s = u. Take A(x) := "s = x":

```
1.  s = t              premise
2.  t = u              premise
3.  s = u              =E 2,1   (A(x) := s = x; from t = u and s = t get s = u)
```

## 4.5 Proof strategy for quantifiers

Extend the table from Chapter 2:

| Goal | Move |
|---|---|
| ∀x A(x) | Introduce arbitrary a (box), prove A(a), apply ∀I |
| ∃x A(x) | Find a **witness term** t, prove A(t), apply ∃I. If no witness is evident, use RAA. |

| Available line | Move |
|---|---|
| ∀x A(x) | Instantiate (∀E) with every term that could help: usually the names already in your proof |
| ∃x A(x) | Name a witness (∃E): start a sub-proof with A(a) for fresh a, reach your goal (which must not mention a) |

**Order of operations.** When a proof needs both ∀I and ∃E, think about which name depends on which. Usually: introduce the ∀I name first, then the ∃E name inside it. If the ∃E must happen first (because the existential premise has nothing to do with the goal's variable), do it first. Always double-check freshness.

## 4.6 Common mistakes

1. **Illegal generalization** (∀I with a name that appears in an open assumption). See Section 4.2.
2. **Letting the ∃E witness escape.** The conclusion of an ∃E must not mention the witness name. If your conclusion does, you went wrong.
3. **Reusing a name.** Introducing "a" twice for two different ∃E steps. Each existential gets its own fresh name.
4. **∃I with a fake witness.** From P(a) you can infer ∃x P(x), yes. But from ∃x P(x) you cannot infer P(a) for a name of your choice. You may only *name* the witness inside ∃E.
5. **Dropping scope.** (∀x P(x)) → Q is not the same as ∀x (P(x) → Q) with Q having x free. Free-variable clashes cause subtle bugs. Rename bound variables apart.
6. **Applying quantifier rules to sub-formulas.** In (∀x P(x)) ∧ Q you may use ∧E first. In (∀x P(x)) → Q you may not instantiate inside the antecedent.

## 4.7 Chapter 4 in complete detail (the from-zero companion)

Chapter 4 added four quantifier rules to the propositional ones. They look small, but they carry all the subtlety of predicate logic. This companion explains **why each rule has the shape it has**, spells out its **exact conditions**, shows it in **every proof format**, walks through **more proofs with the thinking made visible**, displays a **gallery of illegal "proofs"** (the best way to learn the conditions), and gives the **soundness argument** in plain language.

### 4.7.1 The two kinds of names: arbitrary and specific

Everything in this chapter is governed by one distinction.

| | **Specific** name | **Arbitrary** name |
|---|---|---|
| Meaning | refers to a particular, fixed object about which something may already be known | refers to "some object, any object", about which **nothing special** is assumed |
| Examples | `socrates`, `0`, a constant in the premises, a witness named by ∃E | the `a` introduced by ∀I |
| What you may do with it | use whatever is known about it | only things that hold for *every* object |
| Rules that produce it | constants given in the problem | ∀I box |
| Rules that consume it | ∃I, ∀E accept any term | ∀I **generalizes** an arbitrary name |

**The hard rules are the ones that cross the boundary:**

- **∀I** may only generalize an *arbitrary* name.
- **∃E** introduces a name that is specific *within the box* (the witness), but it must not leak out of the box, and it must not be mistaken for an arbitrary name (you cannot later generalize over it).

Everything in 4.2 of the main text is a refinement of this one idea.

### 4.7.2 The four rules, one at a time

Notation: `A(x)` is a formula in which `x` may occur free; `A(t)` abbreviates `A[t/x]`; `t` is a term (variable, constant or function application); `a` is a name used as a constant ("parameter").

#### ∀E: universal elimination (instantiation)

```
m │ ∀x A(x)
  │ A(t)                  ∀E m
```

*In words:* if every object satisfies A, then in particular the object denoted by `t` does.
*Condition:* `t` must be **free for x in A** (no variable of `t` gets captured by a quantifier of A); otherwise rename bound variables first.
*Freedom:* you may instantiate with **any** term, as many times as you like, including terms that contain function symbols: from `∀x P(x)` you may infer `P(a)`, `P(f(a))`, `P(f(f(b)))`.
*Typical use:* unpack a general law at the specific objects relevant to your goal.
*Example:* from `∀x ∀y (x < y → ¬ y < x)` infer, in two steps, `∀y (a < y → ¬ y < a)` and `a < b → ¬ b < a` (instantiate the outer quantifier first, then the inner).
*Misuse:* instantiating **inside** a formula: from `(∀x P(x)) → Q` you cannot get `P(a) → Q`. The main connective is `→`; ∀E applies only when `∀x` is the *main* connective of the line.

#### ∃I: existential introduction (generalization on a witness)

```
m │ A(t)
  │ ∃x A(x)               ∃I m
```

*In words:* if the object `t` satisfies A, then something satisfies A.
*Condition:* `t` free for `x` in `A`.
*A subtlety (choice of abstraction).* The line `A(t)` can be viewed as `A'[t/x]` for **several** different `A'`, depending on which occurrences of `t` you "abstract". From `P(a, a)`:

| You may infer | Because it is `∃x A(x)` with |
|---|---|
| `∃x P(x, x)` | `A(x) = P(x, x)`: both occurrences abstracted |
| `∃x P(x, a)` | `A(x) = P(x, a)`: only the first |
| `∃x P(a, x)` | `A(x) = P(a, x)`: only the second |
| `∃x ∃y P(x, y)` | two applications of ∃I |

*Typical use:* finish a proof whose goal is existential, after you have found a witness.
*Misuse:* from `∃x P(x)` trying to "go back" to `P(a)` for a chosen `a`. ∃I only goes *into* the quantifier. To go out you need ∃E.

#### ∀I: universal introduction (generalization)

```
  │ ┌─ [a]                 a fresh: "let a be arbitrary"
  │ │  ...
  │ │  A(a)
  │ └──
  │ ∀x A(x)                ∀I (range)
```

*In words:* if you have proved A for an arbitrary object a (one about which no assumption was made), then A holds for all objects.
*Condition (eigenvariable condition).* The name `a`:
1. does **not occur in any premise**,
2. does **not occur in any open assumption** (any assumption of a box enclosing the ∀I box),
3. does **not occur in the formula `∀x A(x)`** being derived.

*Typical use:* the universal goal. Open a box with a new name, prove A for that name, close.
*Remark:* in Fitch notation the name-introduction line `[a]` is a sub-proof header that carries **no assumption** (it is not a formula). Some books flag the variable instead ("flag a").

#### ∃E: existential elimination (naming the witness)

```
m │ ∃x A(x)
  │ ┌─ [a]  A(a)           a fresh: "let a be such a witness"
  │ │  ...
  │ │  C
  │ └──
  │ C                      ∃E m, (range)
```

*In words:* if something satisfies A, give it a name `a` (that is a *new* name, not one you've used) and assume A(a); if from that you can conclude C, and C does not mention `a`, then C follows outright.
*Condition (eigenvariable condition).* The name `a`:
1. does **not occur in `∃x A(x)`**,
2. does **not occur in any premise or open assumption outside the box**,
3. does **not occur in the conclusion C**.

*Typical use:* an existential premise (or a line already proved). Always do it as early as you can, because it adds usable facts about the witness.
*Why the box?* Inside the box the name `a` is a specific object; outside, no such name exists. The conclusion C must be something that makes sense without `a`.

#### The pattern: intro/elim and the two kinds of quantifier

| | Introduction (prove it) | Elimination (use it) |
|---|---|---|
| **∀** | ∀I: prove for an *arbitrary* name | ∀E: apply to any term |
| **∃** | ∃I: exhibit *a* term | ∃E: name a *fresh* witness |

Notice the duality: **∀I and ∃E are the "name-introducing" rules with restrictions; ∀E and ∃I are the "name-using" rules with none** (apart from capture-avoidance).

### 4.7.3 The rules in other formats

Here is the same example in each format: **∀x (P(x) → Q(x)), ∀x P(x) ⊢ ∀x Q(x)**, together with the quantifier rules for that format.

#### Natural deduction in Gentzen's tree style

Rules (the bracketed side conditions are the eigenvariable conditions):

```
 ∀x A(x)                        A(a)
 ───────── ∀E                   ───────── ∀I   (a not free in any undischarged
  A(t)                           ∀x A(x)         assumption, nor in ∀x A(x))

  A(t)                          ∃x A(x)    ⟨A(a)⟩..C
 ───────── ∃I                   ───────────────────── ∃E   (a not free in C, in ∃x A(x),
 ∃x A(x)                                  C                  or in other undischarged assumptions)
```

Example:

```
 ∀x(P(x) → Q(x))              ∀x P(x)
 ─────────────── ∀E           ─────── ∀E
  P(a) → Q(a)                   P(a)
 ──────────────────────────────────── →E
                Q(a)
              ────────── ∀I
               ∀x Q(x)
```

Here the free variable `a` is the arbitrary name; it does not occur in either premise (they are closed formulas), so ∀I is legal.

#### Copi / Quine style (UI, UG, EI, EG) with flagging

Many introductory books use four rules with different names:

| Name | This course | Statement |
|---|---|---|
| **UI** (universal instantiation) | ∀E | from `∀x A(x)` infer `A(t)` |
| **EG** (existential generalization) | ∃I | from `A(t)` infer `∃x A(x)` |
| **UG** (universal generalization) | ∀I | from `A(y)` infer `∀x A(x)`, **if** `y` is a variable not free in any premise/assumption and was **not introduced by EI** |
| **EI** (existential instantiation) | ∃E (flat version) | from `∃x A(x)` infer `A(c)` for a **new** constant `c` (not used before anywhere); then restrictions: `c` may not appear in the conclusion, and UG may not later be applied to a variable-name introduced by EI |

The flat "EI" style is the same logic as the boxed ∃E, but the freshness restrictions are enforced by *bookkeeping* (flags) instead of boxes, which makes errors easy to commit. Example:

```
1. ∀x (P(x) → Q(x))      premise
2. ∀x P(x)               premise
3. P(a) → Q(a)           1 UI
4. P(a)                  2 UI
5. Q(a)                  3,4 MP
6. ∀x Q(x)               5 UG   (a is arbitrary: not from a premise, not introduced by EI)
```

#### Lemmon-style quantifier rules

Same as Lemmon's propositional rules, with `UI`, `UG`, `EI`, `EG`, and with the assumption-set convention: `UG` is permitted only if the name does not occur in any assumption that the line depends on; `EI` introduces a new assumption `A(a)`, and the dependency set of the final conclusion replaces that line number by the dependency of the existential premise (this is the Lemmon encoding of ∃E).

#### Hilbert-style (axioms for quantifiers)

Add to the propositional axioms (L1-L3 of 2.9.7):

- **Q1 (instantiation):** `∀x A → A[t/x]`, where `t` is free for `x` in `A`
- **Q2 (distribution):** `∀x (A → B) → (A → ∀x B)`, where `x` is not free in `A`
- **Gen (generalization rule):** from `A` infer `∀x A` (when deriving from premises, only if `x` is not free in any premise used)

Existential quantification is defined: `∃x A := ¬∀x ¬A`.

Example (same theorem): premises `∀x(P(x)→Q(x))`, `∀x P(x)`.

```
1. ∀x (P(x) → Q(x))                    premise
2. ∀x (P(x) → Q(x)) → (P(x) → Q(x))    Q1 (t := x)
3. P(x) → Q(x)                         MP 1,2
4. ∀x P(x)                             premise
5. ∀x P(x) → P(x)                      Q1
6. P(x)                                MP 4,5
7. Q(x)                                MP 6,3
8. ∀x Q(x)                             Gen 7   (x is not free in premises 1 and 4: it is bound there)
```

#### Sequent calculus (LK) quantifier rules

```
 Γ, A(t), ∀x A(x) ⇒ Δ                 Γ ⇒ A(a), Δ
 ───────────────────── ∀L             ────────────── ∀R    (a not free in Γ, Δ, ∀x A(x))
 Γ, ∀x A(x) ⇒ Δ                       Γ ⇒ ∀x A(x), Δ

 Γ, A(a) ⇒ Δ                          Γ ⇒ A(t), ∃x A(x), Δ
 ────────────── ∃L  (a not free       ───────────────────── ∃R
 Γ, ∃x A(x) ⇒ Δ      in Γ, Δ, ∃x A)  Γ ⇒ ∃x A(x), Δ
```

(In ∀L and ∃R the quantified formula is **kept** in the premise because it may need to be instantiated several times.)

Derivation search (read from the goal upward):

```
 (1) ∀x(P(x)→Q(x)), ∀x P(x) ⇒ ∀x Q(x)
 (2) ∀x(P(x)→Q(x)), ∀x P(x) ⇒ Q(a)                           ∀R   (a fresh)
 (3) P(a)→Q(a), ∀x(P(x)→Q(x)), ∀x P(x) ⇒ Q(a)                ∀L   (t := a)
 (4) P(a)→Q(a), ∀x(P(x)→Q(x)), P(a), ∀x P(x) ⇒ Q(a)          ∀L   (t := a)
 (5a) P(a), ... ⇒ P(a), Q(a)    Axiom          (5b) Q(a), P(a), ... ⇒ Q(a)   Axiom
 Step (4) follows from (5a) and (5b) by →L on P(a)→Q(a).
```

#### Analytic tableaux for quantifiers

Two new kinds of rule:

| Type | Formula on the branch | Action |
|---|---|---|
| **γ** (universal type) | `∀x A(x)` or `¬∃x A(x)` | add `A(t)` (or `¬A(t)`) for **any** term `t`; **keep** the formula (may be reused with new terms) |
| **δ** (existential type) | `∃x A(x)` or `¬∀x A(x)` | add `A(a)` (or `¬A(a)`) for a **brand new** constant `a`; the formula is then used up |

Tableau for our example: the root is `∀x (P(x)→Q(x))`, `∀x P(x)`, `¬∀x Q(x)`.

```
 ∀x (P(x) → Q(x))
 ∀x P(x)
 ¬∀x Q(x)
 ¬Q(a)                          (δ on ¬∀x Q(x), a new)
 P(a)                           (γ on ∀x P(x), t := a)
 P(a) → Q(a)                    (γ on ∀x (P(x)→Q(x)), t := a)
   ├── ¬P(a)  ✗  (clashes with P(a))
   └── Q(a)   ✗  (clashes with ¬Q(a))
```

All branches close, so the entailment holds. For formulas needing infinitely many γ-instances the tableau may not terminate (undecidability).

#### Resolution and Skolemization

Resolution works on clauses with no quantifiers: existentials are replaced by Skolem terms and universals are left implicit (Chapter 7). The same example: clauses `{¬P(x), Q(x)}`, `{P(x)}`, and the negated goal Skolemized as `{¬Q(c)}` (`c` a new constant): resolve `{P(x)}` with `{¬P(x), Q(x)}` (unifier `x`) to get `{Q(x)}`; resolve with `{¬Q(c)}` (unifier `x := c`): empty clause.

#### Proof assistants

**Lean 4** (term mode and tactic mode):

```lean
-- term mode: ∀I is "fun a => ...", ∀E is application
example (α : Type) (P Q : α → Prop)
    (h1 : ∀ x, P x → Q x) (h2 : ∀ x, P x) : ∀ x, Q x :=
  fun a => h1 a (h2 a)

-- tactic mode
example (α : Type) (P Q : α → Prop)
    (h1 : ∀ x, P x → Q x) (h2 : ∀ x, P x) : ∀ x, Q x := by
  intro a            -- ∀I: a is the fresh name
  exact h1 a (h2 a)  -- ∀E twice, →E

-- existential: obtain = ∃E, anonymous constructor = ∃I
example (α : Type) (P Q : α → Prop)
    (h1 : ∀ x, P x → Q x) (h2 : ∃ x, P x) : ∃ x, Q x := by
  obtain ⟨a, ha⟩ := h2   -- ∃E: name the witness a with ha : P a
  exact ⟨a, h1 a ha⟩     -- ∃I with witness a
```

**Coq / Rocq:**

```coq
Theorem ex1 : forall (A : Type) (P Q : A -> Prop),
  (forall x, P x -> Q x) -> (forall x, P x) -> forall x, Q x.
Proof.
  intros A P Q h1 h2 a.   (* ∀I: a is fresh *)
  apply h1.               (* goal Q a becomes P a *)
  apply h2.               (* ∀E *)
Qed.

Theorem ex2 : forall (A : Type) (P Q : A -> Prop),
  (forall x, P x -> Q x) -> (exists x, P x) -> exists x, Q x.
Proof.
  intros A P Q h1 h2.
  destruct h2 as [a ha].  (* ∃E *)
  exists a.               (* ∃I *)
  apply h1. exact ha.
Qed.
```

In Lean/Coq the freshness conditions are enforced **automatically by the scoping rules of the language**: `intro a` makes a new variable; you literally cannot refer to it outside its scope. That is the deepest reason why freshness is a *scoping* idea.

#### Correspondence table: the quantifier rules across systems

| Idea | Fitch (this course) | Gentzen NK | Hilbert | Sequent (LK) | Tableau | Lean/Coq |
|---|---|---|---|---|---|---|
| use ∀ | ∀E | ∀E | Q1 + MP | ∀L | γ | application `h t` |
| prove ∃ | ∃I | ∃I | defined via ¬∀¬ | ∃R | (refutation: γ on ¬∃) | `⟨t, proof⟩` / `exists t` |
| prove ∀ | ∀I (box) | ∀I (eigenvariable) | Gen | ∀R | (refutation: δ on ¬∀) | `intro a` |
| use ∃ | ∃E (box) | ∃E (discharge) | derived | ∃L | δ | `obtain ⟨a, h⟩` / `destruct` |

### 4.7.4 Narrated proofs: thinking made visible

**Proof 1.** ∃x (P(x) ∧ Q(x)), ∀x (Q(x) → S(x)) ⊢ ∃x (P(x) ∧ S(x))

*Thinking.* The goal is existential, but I don't know a witness. The premise is existential, so name its witness `a` (∃E) and then my goal's witness will be that same `a`. Inside the box I need `P(a) ∧ S(a)`: `P(a)` comes from the witness; `S(a)` from instantiating the universal premise at `a` and using `Q(a)`.

```
1.  ∃x (P(x) ∧ Q(x))        premise
2.  ∀x (Q(x) → S(x))        premise
3.  |  [a]  P(a) ∧ Q(a)     assumption (∃E)
4.  |  P(a)                  ∧E 3
5.  |  Q(a)                  ∧E 3
6.  |  Q(a) → S(a)           ∀E 2
7.  |  S(a)                  →E 6,5
8.  |  P(a) ∧ S(a)           ∧I 4,7
9.  |  ∃x (P(x) ∧ S(x))      ∃I 8
10. ∃x (P(x) ∧ S(x))        ∃E 1, 3-9
```

*Check:* `a` does not occur in the conclusion `∃x (P(x) ∧ S(x))` (line 10) ✓, nor in the premises ✓.

**Proof 2.** ∀x ∀y (R(x, y) → ¬R(y, x)) ⊢ ∀x ¬R(x, x) (asymmetric implies irreflexive)

*Thinking.* Goal is universal: introduce an arbitrary `a`. Goal inside: `¬R(a, a)`, a negation: assume `R(a, a)` and look for ⊥. The premise, instantiated twice at `a` (both `x` and `y` := `a`), gives `R(a, a) → ¬R(a, a)`, which together with the assumption clashes.

```
1.  ∀x ∀y (R(x, y) → ¬R(y, x))     premise
2.  |  [a]                         (fresh a, for ∀I)
3.  |  ∀y (R(a, y) → ¬R(y, a))     ∀E 1
4.  |  R(a, a) → ¬R(a, a)          ∀E 3
5.  |  |  R(a, a)                  assumption (for ¬I)
6.  |  |  ¬R(a, a)                 →E 4,5
7.  |  |  ⊥                        ¬E 5,6
8.  |  ¬R(a, a)                    ¬I 5-7
9.  ∀x ¬R(x, x)                   ∀I 2-8
```

*Note:* instantiating a universal twice with the same term is perfectly legal and often essential.

**Proof 3.** ⊢ ∀x ∃y (x = y)  (every object equals something; also uses equality)

*Thinking.* Goal is universal: arbitrary `a`. Inside, I need an existential: I have a witness, `a` itself, since `a = a` by reflexivity.

```
1.  |  [a]
2.  |  a = a                  =I
3.  |  ∃y (a = y)             ∃I 2   (abstract the second a)
4.  ∀x ∃y (x = y)            ∀I 1-3
```

*Remark:* no premises, so this is a theorem of first-order logic with equality. Note how the ∃I step needs a witness: the arbitrary name `a` itself serves, which is legitimate because every domain is non-empty (see 4.7.7).

**Proof 4.** ⊢ ∀x (P(x) → P(x)) ∧ (∃x P(x) → ∃y P(y))

*Thinking.* A conjunction of two things; each is easy. Second part: assume `∃x P(x)`; name the witness; re-abstract with a different bound variable.

```
1.  |  [a]
2.  |  |  P(a)                   assumption
3.  |  P(a) → P(a)              →I 2-2
4.  ∀x (P(x) → P(x))           ∀I 1-3
5.  |  ∃x P(x)                 assumption (for →I)
6.  |  |  [b]  P(b)            assumption (∃E)
7.  |  |  ∃y P(y)              ∃I 6
8.  |  ∃y P(y)                 ∃E 5, 6-7
9.  ∃x P(x) → ∃y P(y)          →I 5-8
10. ∀x (P(x) → P(x)) ∧ (∃x P(x) → ∃y P(y))     ∧I 4,9
```

*Observe* the harmless renaming: `∃x P(x)` and `∃y P(y)` are α-equivalent, and the proof just uses ∃E and ∃I to move between them.

**Proof 5 (nesting order).** ∃x ∀y R(x, y), ∀x ∀y (R(x, y) → S(y, x)) ⊢ ∀y ∃x S(y, x)

*Thinking.* Goal universal in `y`: introduce `b`. I need `∃x S(b, x)`. The first premise gives an `x`, say `a`, that relates to every `y`, in particular to `b`: `R(a, b)`. The second premise turns that into `S(b, a)`. I'll introduce `b` first (it comes from the goal), then the witness `a` inside.

```
1.  ∃x ∀y R(x, y)                    premise
2.  ∀x ∀y (R(x, y) → S(y, x))        premise
3.  |  [b]                          (fresh b, for ∀I)
4.  |  |  [a]  ∀y R(a, y)           assumption (∃E)
5.  |  |  R(a, b)                   ∀E 4
6.  |  |  ∀y (R(a, y) → S(y, a))     ∀E 2
7.  |  |  R(a, b) → S(b, a)         ∀E 6
8.  |  |  S(b, a)                   →E 7,5
9.  |  |  ∃x S(b, x)                ∃I 8
10. |  ∃x S(b, x)                   ∃E 1, 4-9
11. ∀y ∃x S(y, x)                   ∀I 3-10
```

*Check:* the ∃E conclusion `∃x S(b, x)` mentions `b`, not `a` ✓; `b` does not occur in the premises ✓ and not in the open assumptions at line 11 ✓. (The nesting could also be reversed, with the ∃E box outside and the ∀I box inside; see the note after the gallery.)

### 4.7.5 A gallery of illegal "proofs" (and why they are illegal)

Each "proof" below *looks* convincing. Learn to find the exact illegal step.

**Gallery 1: "∃x P(x), ∀x (P(x) → Q(x)) ⊢ ∀x Q(x)"** (invalid: some P, and P's are Q's, does not give everything is Q.)

```
1.  ∃x P(x)                 premise
2.  ∀x (P(x) → Q(x))        premise
3.  |  [a]  P(a)            assumption (∃E)
4.  |  P(a) → Q(a)          ∀E 2
5.  |  Q(a)                 →E 4,3
6.  |  ∀x Q(x)              ∀I 5     ← ILLEGAL
7.  ∀x Q(x)                 ∃E 1, 3-6
```

*Error:* at line 6 the name `a` occurs in the **open assumption** `P(a)` (line 3), so `a` is not arbitrary. ∀I needs `a` not to occur in any open assumption.

**Gallery 2: "∀x ∃y x < y ⊢ ∃y ∀x x < y"** (invalid: the converse of ∃∀ ⊢ ∀∃.)

```
1.  ∀x ∃y x < y            premise
2.  |  [b]                 (fresh b)
3.  |  ∃y b < y            ∀E 1
4.  |  |  [c]  b < c       assumption (∃E)
5.  |  |  ∀x (x < c)       ∀I 4     ← ILLEGAL (generalizing b)
6.  |  |  ∃y ∀x (x < y)    ∃I 5
7.  |  ∃y ∀x (x < y)       ∃E 3, 4-6
```

*Error:* to get `∀x (x < c)` from `b < c` we generalize over `b`, but `b` occurs in the open assumption `b < c` (line 4). The witness `c` was chosen *depending on* `b`, so `b` is not arbitrary any more.

**Gallery 3: "∃x P(x), ∃x Q(x) ⊢ ∃x (P(x) ∧ Q(x))"** (invalid.)

```
1.  ∃x P(x)                premise
2.  ∃x Q(x)                premise
3.  |  [a]  P(a)           assumption (∃E on line 1)
4.  |  |  [a]  Q(a)       assumption (∃E on line 2)   ← ILLEGAL: a not fresh (occurs in P(a))
```

*Error:* each existential needs its **own** fresh name. The legal version uses `a` for the first and `b` for the second, and then the conjunction `P(a) ∧ Q(b)` does not yield `∃x (P(x) ∧ Q(x))`; the proof correctly fails.

**Gallery 4: "∃x P(x) ⊢ P(a)"** (invalid.) The "rule" "from ∃x P(x) infer P(a)" for a name `a` of your choice is not a rule: names introduced by ∃E live **inside the box** and cannot escape. The conclusion `P(a)` contains the witness name, so ∃E is blocked (condition 3).

**Gallery 5: "∃E conclusion contains the witness"**

```
1.  ∃x P(x)                premise
2.  |  [a]  P(a)           assumption (∃E)
3.  P(a)                   ∃E 1, 2-2     ← ILLEGAL: conclusion mentions a
```

*Error:* exactly Gallery 4 in a different guise.

**Gallery 6: capture.** "From `∀x ∃y (x ≠ y)` instantiate x := y to get `∃y (y ≠ y)`."

*Error:* `∀E` with `t = y` into a formula where `y` is bound by `∃y` is a **capture**. The term `y` is not free for `x`. The correct instance (after renaming) is `∃z (y ≠ z)`, which is true in any domain with at least two elements; the capture would produce `∃y (y ≠ y)`, always false.

**Gallery 7: applying a rule inside a formula.** From `(∀x P(x)) → Q`, "infer `P(a) → Q`". *Error:* ∀E applies to a line whose **main** connective is the quantifier. Here the main connective is `→`. (In fact the inference is invalid: take a domain where P is true of `a` but not of everything, and Q false.)

**Gallery 8: generalizing over a name from a premise.** "From the premise `P(a)`, infer `∀x P(x)`."

```
1.  P(a)                   premise
2.  ∀x P(x)                ∀I 1     ← ILLEGAL
```

*Error:* `a` occurs in a premise, so it denotes a specific object about which we know something. "Socrates is a man, therefore everything is a man" is the absurd instance. (Compare the legal pattern: the name must be introduced by the ∀I box itself.)

**A note on the order of boxes.** When a proof needs both an ∃E box and a ∀I box (as in Example 3 of Section 4.3), several nestings may be legal. For `∃x ∀y R(x, y) ⊢ ∀y ∃x R(x, y)` you may open the ∀I box for `b` first and the ∃E box for `a` inside it (the book's version), **or** open the ∃E box for `a` first and the ∀I box for `b` inside it: in the second version `b` is fresh (it does not occur in the open assumption `∀y R(a, y)`), and the ∃E conclusion `∀y ∃x R(x, y)` does not mention `a`. What matters is never the order as such but that **every box satisfies its own conditions**. The invalid converse fails in *both* orders, because some condition is violated each time (Gallery 2).

### 4.7.6 Why the rules are sound (the freshness argument in plain words)

Soundness means: if the rule's premises are true in a structure, so is its conclusion. For the "easy" rules this is immediate:

- **∀E:** if all objects satisfy A, the object denoted by `t` does.
- **∃I:** if `t`'s object satisfies A, some object does.

For the two restricted rules we need freshness:

**∀I.** Suppose we have shown `A(a)` from the assumptions (premises and open assumptions) `Γ`, and `a` does not occur in `Γ` or in `∀x A`. Take any structure `M` that satisfies `Γ`. Since `a` does not occur in `Γ`, we may **reinterpret** `a` as any element `d` of the domain without changing whether `Γ` holds. In each such reinterpretation `A(a)` is true (because the derivation is sound for every structure). Hence `A` holds of *every* `d`, which is the truth condition for `∀x A`. **If `a` occurred in `Γ`, we could not reinterpret it freely, and the argument breaks.**

**∃E.** Suppose `∃x A(x)` is true in `M` and `Γ, A(a) ⊢ C` where `a` occurs in neither `Γ`, nor `∃x A`, nor `C`. Because `∃x A` is true, some `d` satisfies `A`. Reinterpret `a` as that `d` (no harm, since `a` does not occur in `Γ`, `∃x A` or `C`). Then `Γ` and `A(a)` are true, so `C` is true. Since `C` does not mention `a`, its truth is unaffected by the reinterpretation: `C` is true in the *original* `M`. **If `C` mentioned `a`, the reinterpretation might change C's truth value.**

The reinterpretation argument is the heart of the soundness theorem for first-order natural deduction (Chapter 6) and is why the conditions are exactly "does not occur in ..." and nothing more or less.

### 4.7.7 Non-empty domains and "names from nowhere"

In standard first-order logic every structure has a non-empty domain. This is *built into the rules*: the following derivation is valid:

```
1.  ∀x P(x)       premise
2.  P(a)          ∀E 1      ← a: any name, even one not mentioned before
3.  ∃x P(x)       ∃I 2
```

If the domain could be empty, `∀x P(x)` would be true (vacuously) and `∃x P(x)` false. By allowing ∀E to instantiate with an arbitrary name, standard FOL builds in non-emptiness (equivalently the validity of `∃x (x = x)`). In **free logic** the rules are restricted: ∀E requires an existence premise `E!t`.

The drinker paradox `⊢ ∃x (D(x) → ∀y D(y))` uses this: the line "pick any name `c`" in Example 5 of Section 4.3 is exactly an application of this convention.

### 4.7.8 Equality rules in detail

| Rule | Schema | Condition |
|---|---|---|
| **=I** (reflexivity) | infer `t = t` (no premises) | any term `t` |
| **=E** (substitution of equals, Leibniz) | from `s = t` and `A(s)`, infer `A(t)` | `A(x)` is any formula; `A(s)`, `A(t)` result from `A(x)` by replacing `x` with `s`, `t` (free for `x`) |

Important: in `=E` you decide **which occurrences** to replace by choosing the formula `A(x)` with the right pattern of holes. Replacing only some occurrences is allowed.

**Derived rules** (prove them once, use freely):

| Derived | Statement | Proof pattern |
|---|---|---|
| Symmetry | `s = t ⊢ t = s` | `A(x) := x = s`; from `s = s` (=I) and `s = t` infer `t = s` |
| Transitivity | `s = t, t = u ⊢ s = u` | `A(x) := s = x` |
| Function congruence | `s = t ⊢ f(s) = f(t)` | `A(x) := f(s) = f(x)`; start from `f(s) = f(s)` (=I) |
| Predicate congruence | `s = t, P(s) ⊢ P(t)` | `A(x) := P(x)` |
| Uniqueness extraction | `∃!x P(x) ⊢ ∃x P(x) ∧ ∀x ∀y ((P(x) ∧ P(y)) → x = y)` | ∃E, then ∀E and =E |

**Worked derivation (function congruence):** `s = t ⊢ f(s) = f(t)`

```
1.  s = t               premise
2.  f(s) = f(s)         =I
3.  f(s) = f(t)         =E 1,2   (A(x) := f(s) = f(x); line 2 is A(s), so from A(s) and s = t infer A(t))
```

**Worked derivation (uniqueness consequence):** ∃x (P(x) ∧ ∀y (P(y) → y = x)) ⊢ ∀u ∀v ((P(u) ∧ P(v)) → u = v).

```
1.  ∃x (P(x) ∧ ∀y (P(y) → y = x))            premise
2.  |  [u]                                   (fresh u, for ∀I)
3.  |  |  [v]                                (fresh v, for ∀I)
4.  |  |  |  [c]  P(c) ∧ ∀y (P(y) → y = c)   assumption (∃E)
5.  |  |  |  |  P(u) ∧ P(v)                  assumption (for →I)
6.  |  |  |  |  ∀y (P(y) → y = c)            ∧E 4
7.  |  |  |  |  P(u)                         ∧E 5
8.  |  |  |  |  P(v)                         ∧E 5
9.  |  |  |  |  P(u) → u = c                 ∀E 6
10. |  |  |  |  P(v) → v = c                 ∀E 6
11. |  |  |  |  u = c                        →E 9,7
12. |  |  |  |  v = c                        →E 10,8
13. |  |  |  |  c = v                        symmetry 12
14. |  |  |  |  u = v                        transitivity 11,13
15. |  |  |  (P(u) ∧ P(v)) → u = v           →I 5-14
16. |  |  (P(u) ∧ P(v)) → u = v              ∃E 1, 4-15
17. |  ∀v ((P(u) ∧ P(v)) → u = v)            ∀I 3-16
18. ∀u ∀v ((P(u) ∧ P(v)) → u = v)            ∀I 2-17
```

(The names `u`, `v` are arbitrary; the witness `c` is introduced inside both. The ∃E conclusion at line 16 does not mention `c`, and `u`, `v` do not occur in the premise.)

### 4.7.9 Strategy reference for quantifier proofs

**Decision table (extends the one in 2.9.5)**

| Situation | Move |
|---|---|
| Goal `∀x A(x)` | open a ∀I box with fresh `a`, aim for `A(a)` |
| Goal `∃x A(x)` | look for a witness `t` among the names/terms in your proof; prove `A(t)`; ∃I. If none is evident: RAA (assume `¬∃x A(x)`, derive `∀x ¬A(x)`, instantiate...) |
| Goal `¬∀x A(x)` | assume `∀x A(x)`, aim for ⊥ (¬I). Instantiate it at useful terms. |
| Goal `¬∃x A(x)` | assume `∃x A(x)`, use ∃E to name the witness, aim for ⊥ |
| Available `∀x A(x)` | instantiate at every relevant term: all constants/names in the proof, and any term your other facts mention |
| Available `∃x A(x)` | ∃E *early*: name the witness; its new facts help everything below |
| Available `¬∀x A(x)` | classical: convert (via RAA) to `∃x ¬A(x)` |
| Available `¬∃x A(x)` | it gives `¬A(t)` for any `t` (prove `∀x ¬A(x)` first, or instantiate when you find `A(t)` to get ⊥) |

**Heuristics**

1. **Prefer to introduce arbitrary names first, witnesses second.** Do the ∀I boxes that the goal demands first, then use ∃E inside. Other nestings are often legal too, but this one makes the freshness conditions easiest to check.
2. **Instantiate universals only at names that exist.** In a proof with names `a, b`, instantiate `∀x ∀y R(x,y)` at all four pairs if needed. Don't invent terms unless required.
3. **A witness for ∃I is usually a name you already have.** Look at the ∃E witness names and ∀I names in scope.
4. **Keep the goal in sight:** when a box's goal is atomic, decide quickly whether you can reach it by →E from instantiated universals.
5. **Write the informal English proof first.** Then transcribe: "Let a be arbitrary" = ∀I box; "let c be such that" = ∃E box; "in particular" = ∀E; "so there exists" = ∃I.

**Dictionary: prose ↔ quantifier rule**

| Prose | Rule |
|---|---|
| "Let `n` be an arbitrary natural number." | start ∀I box |
| "Since this holds for all `x`, it holds for `t`." | ∀E |
| "Hence this holds for every `n`." | close ∀I box |
| "Choose `c` such that ..." / "Let `c` be such that ..." | start ∃E box |
| "Take `t`, then ..." / "For example ..." / "So there is an `x` such that ..." | ∃I |
| "Suppose, for contradiction, that for all `x`..." | RAA / ¬I with ∀ |

### 4.7.10 Quick-check (with answers)

**Q1.** Which of ∀E, ∃I, ∀I, ∃E have a freshness condition? What exactly must be fresh?
**Q2.** From `P(a, a)` list all the existential formulas of the form `∃x …` obtainable by one application of ∃I.
**Q3.** What is wrong with: premise `∀x ∃y L(x, y)`; line 2: `∃y L(y, y)` by ∀E with `t := y`?
**Q4.** In ∃E, which formula must *not* mention the witness name?
**Q5.** In Example 3 (∃x ∀y R ⊢ ∀y ∃x R), could you open the ∃E box first and the ∀I box inside it? Which conditions would you have to check?
**Q6.** Why is ∀x P(x) ⊢ ∃x P(x) valid in standard first-order logic but not in free logic?
**Q7.** Give the Lean tactic that corresponds to ∀I, to ∃E, to ∃I.

**Answers.**
**A1.** ∀I: the new name must not occur in premises, open assumptions, or the conclusion `∀x A`. ∃E: the witness name must not occur in `∃x A`, in other premises/open assumptions, or in the conclusion `C`.
**A2.** `∃x P(x, x)`, `∃x P(x, a)`, `∃x P(a, x)`.
**A3.** The term `y` is captured by `∃y`; the term is not free for `x`. The correct instance (rename first) is `∃z L(y, z)`.
**A4.** The conclusion `C` of the ∃E (and the formulas `∃x A`, premises).
**A5.** Yes. Open ∃E for `a` with assumption `∀y R(a, y)`, then inside it open ∀I for `b`, derive `R(a, b)` and `∃x R(x, b)`, and close with ∀I to get `∀y ∃x R(x, y)`. Conditions to check: `b` is fresh (it does not occur in the open assumption `∀y R(a, y)` or in any premise), and the ∃E conclusion `∀y ∃x R(x, y)` does not mention `a`. Both hold, so this nesting is legal too.
**A6.** In standard FOL, ∀E may instantiate with any name, which presupposes the domain is non-empty. Free logic allows an empty domain (then `∀x P(x)` is vacuously true and `∃x P(x)` false).
**A7.** ∀I: `intro a`. ∃E: `obtain ⟨a, h⟩ := hex` (or `rcases`/`cases`). ∃I: `exact ⟨t, proof⟩` or `refine ⟨t, ?_⟩`.

## Problems for Chapter 4

**4.1 ★** ∀x (P(x) ∧ Q(x)) ⊢ ∀x P(x) ∧ ∀x Q(x), and the converse.

**4.2 ★** ∀x P(x) ⊢ ∃x P(x)

**4.3 ★** ∃x (P(x) ∧ Q(x)) ⊢ ∃x P(x) ∧ ∃x Q(x)

**4.4 ★** ∀x ∀y R(x, y) ⊢ ∀y ∀x R(x, y)

**4.5 ★** ∃x ∃y R(x, y) ⊢ ∃y ∃x R(x, y)

**4.6 ★★** ∀x ¬P(x) ⊢ ¬∃x P(x)

**4.7 ★★** ¬∃x P(x) ⊢ ∀x ¬P(x)

**4.8 ★★** ∃x ¬P(x) ⊢ ¬∀x P(x)

**4.9 ★★** ∀x (P(x) → Q(x)) ⊢ ∀x P(x) → ∀x Q(x)

**4.10 ★★** ∀x P(x) ∨ ∀x Q(x) ⊢ ∀x (P(x) ∨ Q(x))

**4.11 ★★** ∃x (P(x) ∨ Q(x)) ⊢ ∃x P(x) ∨ ∃x Q(x)

**4.12 ★★** (x not free in B) ∀x (P(x) → B) ⊢ ∃x P(x) → B, and the converse

**4.13 ★★** ∀x (P(x) ∨ Q(x)), ¬∃x P(x) ⊢ ∀x Q(x)

**4.14 ★★** ∃x P(x) → ∀y Q(y) ⊢ ∀y (P(y) → Q(y))

**4.15 ★★** s = t, t = u ⊢ s = u, and: ∀x ∀y (x = y → y = x)

**4.16 ★★** ∃x (P(x) ∧ ∀y (P(y) → y = x)) ⊢ ∀x ∀y ((P(x) ∧ P(y)) → x = y) (existence-and-uniqueness implies at-most-one)

**4.17 ★★★** ∀x ∃y R(x, y), ∀x ∀y (R(x, y) → R(y, x)), ∀x ∀y ∀z ((R(x, y) ∧ R(y, z)) → R(x, z)) ⊢ ∀x R(x, x) (symmetric + transitive + serial implies reflexive)

**4.18 ★★★** ⊢ ∃x (P(x) → ∀y P(y)) (the drinker paradox; do it **by cases** on ∀y P(y) first as in the informal proof, then formalize without looking at Example 5)

**4.19 ★★★** ⊢ ¬∃x ∀y (R(x, y) ↔ ¬R(y, y)) (Russell's barber, from a blank page)

**4.20 ★★★** For each "proof" below, find the exact line that violates a rule, and say whether the *conclusion* is actually valid:
- (a) ∃x P(x) ⊢ P(a)  (by "naming the witness a" and then discharging)
- (b) ∀x ∃y R(x, y) ⊢ ∃y ∀x R(x, y)
- (c) ∃x P(x), ∃x Q(x) ⊢ ∃x (P(x) ∧ Q(x)) by using a single witness name for both existentials

---

# Chapter 5. Mathematical proof technique

Formal proofs are a microscope. Real mathematics is written in prose, but every prose proof is a compressed formal proof. This chapter shows the dictionary.

## 5.1 The dictionary: logic to prose

| Formal rule | What you write in prose |
|---|---|
| →I | "Assume A. ... Therefore B." |
| ∀I | "Let x be arbitrary. ..." / "Let ε > 0 be given. ..." |
| ∃I | "Take x = ... (explicit witness)." / "Choose δ = ε/2." |
| ∃E | "Since there exists x with P(x), let a be such an x." |
| ∨E | "We consider two cases. Case 1: ... Case 2: ..." |
| ¬I | "Suppose, for contradiction, that A. ... This is absurd." |
| RAA | "Suppose not. ... Contradiction." |
| ∧I | "We prove A. We prove B. Hence both." |
| ↔I | "(⇒) ... (⇐) ..." |

**The two-step method for any proof.**
1. **Unpack the statement formally** (write it with quantifiers and connectives, even in rough form). The logical form tells you the proof structure, exactly as in Chapters 2 and 4.
2. **Unpack the definitions** of every defined term in the statement. Most "I don't know how to start" moments come from not having done this.

## 5.2 Direct proof

To prove A → B, assume A and derive B.

**Definitions.** An integer n is **even** if ∃k ∈ ℤ (n = 2k), and **odd** if ∃k ∈ ℤ (n = 2k + 1).

**Theorem.** If m and n are even integers, then m + n is even.

*Proof.* Assume m and n are even. By definition, there are integers j, k with m = 2j and n = 2k (this is ∃E twice). Then m + n = 2j + 2k = 2(j + k). Since j + k is an integer, m + n is even (this is ∃I with witness j + k). ∎

Notice how the proof is literally the sequence: →I, ∃E, ∃E, ∃I.

## 5.3 Proof by contrapositive

To prove A → B, prove ¬B → ¬A instead. Use it when ¬B gives you something concrete to work with.

**Theorem.** For an integer n, if n² is even then n is even.

*Proof.* We prove the contrapositive: if n is odd, then n² is odd. Let n = 2k + 1. Then n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1, which is odd. ∎

A direct attempt would start with n² = 2k and get stuck, because you cannot "take a square root" within the integers by algebra alone. The contrapositive turns the hypothesis into something with algebraic content.

## 5.4 Proof by contradiction

To prove A, assume ¬A and derive a contradiction. (To prove ¬A, assume A and derive a contradiction. That is ¬I and is not really "by contradiction" in the classical, RAA sense.)

**Theorem.** √2 is irrational.

*Proof.* Suppose √2 were rational. Then √2 = p/q for integers p, q with q ≠ 0, and we may assume p/q is in lowest terms (gcd(p, q) = 1). Squaring: p² = 2q², so p² is even, hence p is even (by 5.3). Write p = 2r. Then 4r² = 2q², so q² = 2r², so q² is even and hence q is even. Now both p and q are even, contradicting gcd(p, q) = 1. ∎

**Theorem (Euclid).** There are infinitely many primes.

*Proof.* Suppose there were only finitely many primes p₁, ..., pₙ. Consider N = p₁ · p₂ ··· pₙ + 1. N > 1, so N has a prime divisor q. This q must be one of the pᵢ, so q divides the product p₁···pₙ, and since q divides N it also divides N − p₁···pₙ = 1. But no prime divides 1. Contradiction. ∎

**Warning.** Do not use contradiction when a direct or contrapositive proof is as easy. "Proof by contradiction" that merely wraps a direct proof (assume ¬A, derive A directly, "contradiction") is correct but bad style.

## 5.5 Proof by cases

To use A ∨ B (or a statement that is known to split into exhaustive cases), prove the conclusion in each case. Make sure the cases are **exhaustive**. Overlap is fine; gaps are fatal.

**Theorem.** For every integer n, n² mod 4 ∈ {0, 1}.

*Proof.* Case 1: n is even, n = 2k, so n² = 4k² ≡ 0. Case 2: n is odd, n = 2k + 1, so n² = 4k² + 4k + 1 ≡ 1. Every integer is even or odd, so the cases are exhaustive. ∎

**Corollary.** No integer of the form 4k + 3 is a sum of two squares.
*Proof.* A sum of two squares is ≡ 0 + 0, 0 + 1, 1 + 0 or 1 + 1 (mod 4), i.e., 0, 1, or 2, never 3. ∎

## 5.6 Existence, uniqueness, and counterexamples

- **To prove ∃x P(x)**: *constructive* proof exhibits a witness. A *non-constructive* proof (like the drinker paradox) shows existence without naming one.
- **To prove ∃!x P(x)** (exactly one): prove (1) existence and (2) uniqueness: assume P(a) and P(b) and show a = b.
- **To disprove ∀x P(x)**: give a **counterexample**, i.e., prove ∃x ¬P(x). One example does not prove a universal claim, but one counterexample disproves it.
- **To disprove ∃x P(x)**: prove ∀x ¬P(x). Checking examples will not do.

**Example.** The equation 3x + 2 = 11 has exactly one solution. *Existence:* x = 3. *Uniqueness:* if 3a + 2 = 11 and 3b + 2 = 11, then 3a = 3b, so a = b. ∎

## 5.7 Proofs with nested quantifiers (ε-δ style)

The structure of an ε-δ proof is a direct image of the logical form.

**Claim.** lim_{x → 2} (3x + 1) = 7, i.e., ∀ε > 0 ∃δ > 0 ∀x (|x − 2| < δ → |(3x + 1) − 7| < ε).

*Scratch work* (this part is **not** in the final proof): we need |3x − 6| = 3|x − 2| < ε, so |x − 2| < ε/3 suffices. Choose δ = ε/3.

*Proof.*
- Let ε > 0 be arbitrary. *(∀I)*
- Choose δ = ε/3 > 0. *(∃I, with a witness depending on ε)*
- Let x be arbitrary with |x − 2| < δ. *(∀I and →I)*
- Then |(3x + 1) − 7| = 3|x − 2| < 3δ = ε. ∎

Observe the structure: **∀ introduces a name, ∃ provides a witness that may depend on every name introduced before it.** The order ∀ε ∃δ ∀x tells you δ may depend on ε but not on x.

## 5.8 Mathematical induction

Induction proves statements of the form **∀n ∈ ℕ, P(n)**. It is the standard tool for anything defined recursively.

**Principle of (weak) induction.** If
1. **Base case:** P(0) (or P(1)) holds, and
2. **Inductive step:** for every n, P(n) → P(n + 1),

then P(n) holds for all n ≥ the base.

**Why it works.** It is the logical statement ( P(0) ∧ ∀n (P(n) → P(n+1)) ) → ∀n P(n), which is an *axiom* of arithmetic (or a consequence of the well-ordering principle: a smallest counterexample would have a predecessor that is not a counterexample, which is absurd).

**Template.**
1. State precisely the statement P(n).
2. Base case: verify P(base).
3. Inductive step: *Assume P(n) for some arbitrary n ≥ base* (this is the **induction hypothesis**, IH). Prove P(n + 1), and mark clearly **where you use the IH**.
4. Conclude.

### Example 1. 1 + 2 + ··· + n = n(n + 1)/2

*Proof.* P(n): the identity holds.
- **Base.** n = 1: LHS = 1, RHS = 1·2/2 = 1. ✔
- **Step.** Assume P(n). Then 1 + ··· + n + (n + 1) = n(n + 1)/2 + (n + 1) *(by IH)* = (n + 1)(n/2 + 1) = (n + 1)(n + 2)/2, which is P(n + 1). ∎

### Example 2. 1 + 3 + 5 + ··· + (2n − 1) = n²

*Proof.* Base n = 1: 1 = 1². Step: assume P(n). Then the sum up to 2(n + 1) − 1 = 2n + 1 equals n² + (2n + 1) *(IH)* = (n + 1)². ∎

### Example 3. For all n ≥ 1, n < 2ⁿ

*Base.* 1 < 2. *Step.* Assume n < 2ⁿ. Then n + 1 < 2ⁿ + 1 ≤ 2ⁿ + 2ⁿ = 2ⁿ⁺¹ (since 2ⁿ ≥ 1). ∎

### Example 4. 3 divides n³ − n for every integer n ≥ 0

*Base.* n = 0: 0 is divisible by 3. *Step.* (n + 1)³ − (n + 1) = n³ + 3n² + 3n + 1 − n − 1 = (n³ − n) + 3(n² + n). The first term is divisible by 3 by IH, the second obviously. ∎

## 5.9 Strong induction

When P(n + 1) needs not just P(n) but possibly *any* earlier case, use **strong induction**: assume P(k) for **all k < n** and prove P(n). (Base cases are sometimes handled automatically, since for the smallest n the hypothesis is vacuous. Be careful to handle them explicitly when the step needs them.)

**Theorem.** Every integer n ≥ 2 is a product of primes.

*Proof.* Let n ≥ 2 and assume the claim for all k with 2 ≤ k < n. If n is prime, it is a product of one prime. Otherwise n = ab with 2 ≤ a, b < n. By the IH, a and b are products of primes, so n = ab is as well. ∎

**Theorem.** Every integer n ≥ 12 can be written as 4a + 5b with a, b ≥ 0.

*Proof.* Base cases: 12 = 4·3, 13 = 4·2 + 5, 14 = 4 + 5·2, 15 = 5·3. For n ≥ 16, n − 4 ≥ 12, so by strong IH n − 4 = 4a + 5b, hence n = 4(a + 1) + 5b. ∎

Four base cases were needed because the step reaches back four places.

## 5.10 Structural induction

Because formulas are defined inductively (Chapter 1), we can prove properties of **all formulas** by induction on their structure: prove it for atoms (base) and prove that if it holds for A and B then it holds for ¬A, (A ∧ B), etc. (step).

**Theorem.** Let formulas be built from atoms using ¬ and (A ∧ B). Then every formula has the same number of "(" as ")".

*Proof.* *Atoms:* 0 and 0. *¬A:* parentheses are exactly those of A. *(A ∧ B):* one extra "(" and one extra ")" plus those of A and B, which are balanced by IH. ∎

**Theorem.** Let a formula use only atoms and binary connectives, and let it have n binary connective occurrences. Then it has n + 1 atom occurrences.

*Proof.* *Atom:* 0 connectives, 1 atom. *(A ∘ B):* if A has m connectives (m + 1 atoms) and B has k connectives (k + 1 atoms), then (A ∘ B) has m + k + 1 connectives and (m + 1) + (k + 1) = (m + k + 1) + 1 atoms. ∎

Structural induction is also the engine behind **soundness proofs** (induction on derivations, Chapter 6) and the correctness proofs of every recursive algorithm over ASTs you will write in Chapter 8.

## 5.11 Common induction errors

- **Missing base case.** "P(n) → P(n + 1)" without P(base) proves nothing. (Example: "n = n + 1": the inductive step holds, no base case does.)
- **Wrong base.** Starting at 1 for a claim that is also stated for 0.
- **Using the conclusion in the step.** The IH is P(n), not P(n + 1).
- **A step that fails for small n.** The famous "all horses are the same color" fallacy: the step assumes two sets of n horses overlap, which fails for n = 1 → 2.
- **Not declaring what P(n) is.** Always write it out.

## 5.12 Sets and functions: where logic meets mathematics

### Sets

Set equality and inclusion are defined by logic:

- A ⊆ B  :⇔  ∀x (x ∈ A → x ∈ B)
- A = B  :⇔  A ⊆ B ∧ B ⊆ A  (extensionality; the proof structure is ↔I)
- x ∈ A ∩ B ⇔ x ∈ A ∧ x ∈ B,  x ∈ A ∪ B ⇔ x ∈ A ∨ x ∈ B,  x ∈ Aᶜ ⇔ ¬(x ∈ A)

So every set identity is a logical equivalence in disguise.

**Theorem.** A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).

*Proof.* Let x be arbitrary. x ∈ A ∩ (B ∪ C) ⇔ x ∈ A ∧ (x ∈ B ∨ x ∈ C) ⇔ (x ∈ A ∧ x ∈ B) ∨ (x ∈ A ∧ x ∈ C) ⇔ x ∈ (A ∩ B) ∪ (A ∩ C), using distributivity from Chapter 1. ∎

### Functions

Let f: X → Y.

- **Injective** (one-to-one): ∀a ∀b (f(a) = f(b) → a = b)
- **Surjective** (onto): ∀y ∃x (f(x) = y)
- **Bijective:** both.

**Theorem.** If f: X → Y has a left inverse g: Y → X (so g(f(x)) = x for all x), then f is injective.

*Proof.* Let a, b ∈ X be arbitrary and assume f(a) = f(b). Apply g: g(f(a)) = g(f(b)). By the left-inverse property, a = b. ∎

**Theorem.** If g ∘ f is injective, then f is injective.

*Proof.* Let a, b be arbitrary with f(a) = f(b). Then g(f(a)) = g(f(b)), i.e., (g ∘ f)(a) = (g ∘ f)(b). Since g ∘ f is injective, a = b. ∎

**Theorem (Cantor).** There is no surjection from a set A onto its power set 𝒫(A).

*Proof.* Suppose h: A → 𝒫(A) is surjective. Let D = {x ∈ A : x ∉ h(x)}. Since h is surjective, D = h(d) for some d ∈ A. Then d ∈ D ⇔ d ∉ h(d) ⇔ d ∉ D, a contradiction. ∎

This is **exactly Russell's barber** (Chapter 4, Example 6) with R(x, y) := "y ∈ h(x)".

## 5.13 Writing proofs well

- **Start by saying what you assume and what you will prove.**
- **Introduce every variable** ("Let n be an arbitrary integer").
- **Signal structure**: "Case 1", "Suppose for contradiction", "We prove the contrapositive".
- **Finish with the conclusion** and say why it is what was claimed.
- **Separate scratch work from the proof.** The proof should read forward; scratch work is how you found it.
- **Check the logical form once at the end:** every ∀ introduced with an arbitrary element, every ∃ with a witness or by an explicit witness, no assumption smuggled in.

## 5.14 Chapter 5 in complete detail (the from-zero companion)

Chapter 5 gave you the main techniques with a few examples each. This companion is a **proof-writing manual**: it explains what mathematical statements are made of, gives a step-by-step procedure that works for almost any proof, supplies a **skeleton (template) for every technique**, treats **induction in all its forms** with fully worked examples, shows how proofs about **sets, functions and relations** are done mechanically, and finishes with a catalogue of **fallacious proofs** so that you can recognize bad reasoning, including your own.

### 5.14.1 The vocabulary of mathematical texts

| Term | What it is | Role |
|---|---|---|
| **Definition** | an agreement on how a word is used | not provable or refutable; it *fixes* meaning. "Even" means `∃k (n = 2k)`. |
| **Axiom / postulate** | a statement accepted without proof within a theory | the starting points |
| **Theorem** | an important statement that has been proved | the main results |
| **Proposition** | a (usually less central) proved statement | |
| **Lemma** | a proved statement used as a stepping stone | |
| **Corollary** | a statement that follows quickly from a theorem | |
| **Claim** | a statement made inside a proof, then proved | |
| **Conjecture** | a statement believed true, not yet proved | Goldbach, twin primes |
| **Remark / Note / Example** | commentary | |
| **Counterexample** | an instance showing a universal statement false | |

**Anatomy of a theorem.** Every theorem is, logically, `Hypotheses ⇒ Conclusion`, usually with hidden universal quantifiers.

> "The sum of two even integers is even."

Hidden form: `∀m ∈ ℤ ∀n ∈ ℤ ((Even(m) ∧ Even(n)) → Even(m + n))`.

> "If a function is differentiable then it is continuous."

Hidden form: `∀f ((Differentiable(f) → Continuous(f)))`, with more hidden quantifiers inside the definitions (continuity has `∀ε ∃δ ∀x`).

**Always make hidden quantifiers explicit.** "x² ≥ 0" is the statement `∀x ∈ ℝ, x² ≥ 0`; "the equation x² = 2 has a solution" is `∃x ∈ ℝ, x² = 2`. A statement with no stated quantifier on a variable is *usually* universal in a theorem and *usually* existential only when it says "has a", "there is".

**"If", "only if", "if and only if", "iff".**

| Phrase | Logical form |
|---|---|
| "A if B" | `B → A` |
| "A only if B" | `A → B` |
| "A if and only if B" (iff) | `A ↔ B`: prove both `A → B` and `B → A` |
| "A is necessary for B" | `B → A` |
| "A is sufficient for B" | `A → B` |
| "The following are equivalent: (a), (b), (c)" | prove a cycle `(a) → (b) → (c) → (a)` |

### 5.14.2 A procedure that works for (almost) every proof

**Step 0: Read and understand.** Read the statement slowly. Is every word defined? Try a few concrete examples and a few non-examples. Draw a picture if there is one.

**Step 1: Formalize the statement.** Write it with quantifiers and connectives, even roughly. Identify the **hypotheses** (what you may assume) and the **goal** (what you must show).

**Step 2: Unpack the definitions.** Replace each defined term by its definition, both in the hypotheses and in the goal. *Most proofs become routine after this.*

**Step 3: Choose the shape from the goal.** Use the table below.

**Step 4: Scratch work.** Work backwards from the goal and forwards from the hypotheses on scrap paper. Find the key idea (the witness, the case split, the inequality). *Scratch work is not the proof.*

**Step 5: Write the proof forward.** From the assumptions to the conclusion, each sentence justified. Introduce every variable.

**Step 6: Check.** Re-read it as a skeptic. Did every `∀` start with "let ... be arbitrary"? Every `∃` have a witness? Every case covered? Is every use of the induction hypothesis marked? Was an assumption smuggled in?

#### The shape table: goal form ⇒ first move

| The goal looks like | Standard first move | Rule behind it |
|---|---|---|
| `∀x P(x)` | "Let `x` be arbitrary." Prove `P(x)`. | ∀I |
| `∀x ∈ S, P(x)` | "Let `x ∈ S` be arbitrary." | ∀I + →I |
| `∃x P(x)` | Find (construct) a witness `t`; show `P(t)`. Or argue non-constructively. | ∃I |
| `A → B` | "Assume `A`." Prove `B`. (Or contrapositive: assume `¬B`, prove `¬A`.) | →I |
| `A ↔ B` | Prove `A → B` and `B → A` separately. | ↔I |
| `A ∧ B` | Prove `A`. Prove `B`. | ∧I |
| `A ∨ B` | Assume `¬A` and prove `B` (equivalently the reverse). Or cases. | ¬A → B |
| `¬A` | "Suppose `A`." Derive an absurdity. | ¬I |
| `∃!x P(x)` | Existence and uniqueness: show `P(t)` and `P(a) ∧ P(b) → a = b`. | ∃I, ∀I |
| `A = B` (sets) | Show `A ⊆ B` and `B ⊆ A` (double inclusion). | ↔I |
| `A ⊆ B` | "Let `x ∈ A`." Show `x ∈ B`. | ∀I, →I |
| `f` injective | "Assume `f(a) = f(b)`." Show `a = b`. | ∀I, →I |
| `f` surjective | "Let `y ∈ Y`." Exhibit `x` with `f(x) = y`. | ∀I, ∃I |
| `P(n)` for all `n` | induction | |
| Atomic statement, nothing works | proof by contradiction | RAA |

| What you have | Standard first move | Rule behind it |
|---|---|---|
| `∀x P(x)` | instantiate at useful terms | ∀E |
| `∃x P(x)` | "Let `a` be such that `P(a)`." | ∃E |
| `A → B` | when you get `A`, you get `B` | →E |
| `A ∨ B` | split into cases | ∨E |
| `A ∧ B` | use both | ∧E |
| `¬A` | combine with `A` to get ⊥ | ¬E |
| `A ↔ B` | replace one by the other | ↔E |
| `x = y` | substitute | =E |

### 5.14.3 Catalogue of techniques with skeletons

Each skeleton is a fill-in-the-blanks outline. `⟨…⟩` marks what you supply.

#### Direct proof

```
Claim: if ⟨A⟩ then ⟨B⟩.
Proof. Assume ⟨A⟩. By definition, ⟨unpack A⟩.
       ⟨chain of justified steps⟩
       Hence ⟨B⟩. ∎
```

*Example.* If `a ∣ b` and `b ∣ c` then `a ∣ c`. *Proof.* Assume `a ∣ b` and `b ∣ c`. By definition there are integers `j, k` with `b = aj` and `c = bk`. Then `c = (aj)k = a(jk)`, and `jk` is an integer, so `a ∣ c`. ∎

#### Contrapositive

```
Claim: if ⟨A⟩ then ⟨B⟩.
Proof. We prove the contrapositive: if not ⟨B⟩ then not ⟨A⟩.
       Assume not ⟨B⟩. ⟨...⟩ Hence not ⟨A⟩. ∎
```

Use when `¬B` is easier to use than `A`. Typical: statements with "even/odd", "divisible", "irrational".

*Example.* If `n² − 6n + 5` is even, then `n` is odd. *Proof.* Contrapositive: if `n` is even then `n² − 6n + 5` is odd. Let `n = 2k`. Then `n² − 6n + 5 = 4k² − 12k + 5 = 2(2k² − 6k + 2) + 1`, which is odd. ∎

#### Contradiction

```
Claim: ⟨A⟩.
Proof. Suppose, for contradiction, that not ⟨A⟩. 
       ⟨...⟩ derive a statement ⟨C⟩ and also not ⟨C⟩ (or something false).
       This contradiction shows ⟨A⟩. ∎
```

*Example (irrational √2 in the main text); another: there is no largest integer.* Suppose `N` is the largest integer. Then `N + 1` is an integer larger than `N`: contradiction. ∎

Contradiction is the technique for proving **negative** statements ("there is no...", "is irrational", "cannot") and **uniqueness/infinitude** statements. Beware of dressing a direct proof as a contradiction.

#### Cases (exhaustive)

```
Claim: ⟨C⟩ for all x.
Proof. Cases: Case 1: ⟨D₁⟩.  Case 2: ⟨D₂⟩.  (Exhaustive because ⟨D₁ ∨ D₂ holds⟩.)
       Case 1. ⟨...⟩ ⟨C⟩.   Case 2. ⟨...⟩ ⟨C⟩. ∎
```

*Example.* For every real `x`, `|x| ≥ x`. Case `x ≥ 0`: `|x| = x ≥ x`. Case `x < 0`: `|x| = −x > 0 > x`. ∎

**Without loss of generality (WLOG).** If the problem is symmetric (e.g. in `a` and `b`), you may prove the case `a ≤ b` and say "the case `b ≤ a` is identical by symmetry". Use sparingly, and only when the symmetry is genuinely there (swapping the names really gives the same problem).

#### Existence

*Constructive:* give the witness and verify. "There is an integer between 3 and 4.5: take 4."
*Non-constructive:* show that non-existence is impossible. Classic: **there exist irrational `a, b` with `aᵇ` rational.** Consider `√2^√2`. If rational, take `a = b = √2`. If irrational, take `a = √2^√2`, `b = √2`: `aᵇ = (√2^√2)^√2 = √2² = 2`. Either way a pair exists, but the proof does not say which case holds.

#### Uniqueness

```
Claim: there is exactly one x with ⟨P(x)⟩.
Proof. Existence: ⟨exhibit x, check P⟩.
       Uniqueness: Suppose P(a) and P(b). ⟨...⟩ Hence a = b. ∎
```

#### Counterexample

To refute `∀x P(x)`, exhibit one `x` with `¬P(x)`, and *check carefully that it really is a counterexample*. "Every prime is odd" is false: `2` is prime and even.

To refute an implication `A → B`, exhibit a case where `A` holds and `B` fails.

#### Proof of an "if and only if"

```
Claim: ⟨A⟩ iff ⟨B⟩.
Proof. (⇒) Assume ⟨A⟩. ⟨...⟩ Hence ⟨B⟩.
       (⇐) Assume ⟨B⟩. ⟨...⟩ Hence ⟨A⟩. ∎
```

Alternative: a chain of equivalences `A ⇔ A₁ ⇔ A₂ ⇔ B`, each step justified in both directions. Use only when each step is a genuine equivalence.

#### Proof of "the following are equivalent"

For `(a), (b), (c)` prove `(a) ⇒ (b)`, `(b) ⇒ (c)`, `(c) ⇒ (a)`. Three implications instead of six.

#### Pigeonhole principle

If `n + 1` objects are put into `n` boxes, some box holds at least two. (More generally, `m` objects into `n` boxes: some box has at least `⌈m/n⌉`.) In logic: for a function `f : A → B` with `|A| > |B|` (finite), `f` is not injective.

*Example.* Among any 13 people, two share a birth month. (13 people, 12 months.)
*Example (less obvious).* Among any `n + 1` integers there are two whose difference is divisible by `n`: look at their remainders mod `n` (only `n` possible remainders). ∎

#### Extremal principle and minimal counterexample

If a statement is false for some natural numbers, there is a **smallest** counterexample (well-ordering principle). Derive a contradiction by finding an even smaller one.

*Example.* Every integer `n ≥ 2` has a prime divisor. Suppose not, and let `n` be the least counterexample. `n` is not prime (else `n` divides itself), so `n = ab` with `1 < a < n`. By minimality `a` has a prime divisor `p`, which also divides `n`. Contradiction. ∎

#### Infinite descent

A variant: if from a solution in positive integers you can always build a *smaller* solution, there is no solution (an infinite decreasing sequence of positive integers is impossible). Classic: `√2` irrational, via "if `p² = 2q²` with positive integers, then `(2q − p, p − q)` is a smaller solution to `p² = 2q²`".

#### Proof by construction vs proof by existence argument

A construction gives an algorithm for the object; an existence argument only proves it exists. A mathematician's taste favours constructive proofs, and **proof assistants** (Chapter 2.9.8) make the difference visible: constructive proofs are programs.

#### Proof by induction

See 5.14.4.

#### Proof by exhaustion and computer assistance

When the set of cases is finite and small, check each. When large, a computer may do it (four-colour theorem, 1976/2005 formally verified in Coq; Kepler conjecture, formal proof 2014; the "Boolean Pythagorean triples" problem, 2016, with a proof certificate of about 200 terabytes). Such proofs rely on **formal logic engines**, exactly the subject of Chapters 7-8.

### 5.14.4 Induction in complete detail

**The idea.** To prove `∀n ≥ n₀, P(n)` you cannot check infinitely many cases, but you can prove a *ladder*: the first rung (base case) and the step from each rung to the next (inductive step). Climbing is then automatic.

#### The forms of induction

| Form | Statement | Use when |
|---|---|---|
| **Weak (ordinary) induction** | `P(n₀)` and `∀n ≥ n₀ (P(n) → P(n+1))` ⟹ `∀n ≥ n₀ P(n)` | step from `n` to `n+1` uses only `P(n)` |
| **Strong (complete) induction** | `∀n ≥ n₀ ((∀k, n₀ ≤ k < n → P(k)) → P(n))` ⟹ `∀n ≥ n₀ P(n)` | step may use any earlier case; recursive splits (divide into two parts) |
| **Multiple base cases** | prove `P(n₀), …, P(n₀+r−1)`; step from the previous `r` cases | recurrences of order `r` (Fibonacci needs 2) |
| **Induction with a shifted base** | start at any `n₀` | statements true only from `n₀` on |
| **Two-variable induction** | induct on `n` for fixed `m`, then on `m`; or on `m + n` | statements about pairs |
| **Induction on a strengthened statement** | prove a stronger `Q(n)` that implies `P(n)` | when the plain statement's IH is too weak (tiling problem, 5.14) |
| **Structural induction** | base: atoms/leaves; step: each constructor | formulas, trees, lists, programs |
| **Well-founded induction** | induction over any well-founded order (no infinite descending chains) | termination proofs, lexicographic orders |
| **Transfinite induction** | along ordinals | set theory |
| **Induction on derivations** | on the proof tree | soundness (Chapter 6) |
| **Backward ("Cauchy") induction** | prove for infinitely many `n`, then downwards | AM-GM inequality |

#### Why induction is valid

The three statements below are **equivalent** (given the other axioms of the natural numbers):

1. **Weak induction**
2. **Strong induction**
3. **The well-ordering principle**: every non-empty set of natural numbers has a least element.

*Sketch of (3) ⇒ (1):* Suppose the base case and the step hold but `P(n)` fails for some `n`. The set of counterexamples is non-empty, so it has a least element `m`. `m ≠ n₀` (the base case holds), so `m − 1` is not a counterexample, i.e. `P(m − 1)` holds, and the step gives `P(m)`: contradiction. ∎

*Strong ⇒ weak:* trivial (weak is the special case where only `P(n − 1)` is used). *Weak ⇒ strong:* apply weak induction to `Q(n) := ∀k ≤ n P(k)`.

#### The template (write it every time)

```
Claim. For all n ≥ n₀, P(n), where P(n) is the statement ⟨…⟩.
Proof. By induction on n.
  Base case (n = n₀). ⟨verify P(n₀) directly⟩.
  Inductive step. Let n ≥ n₀ and assume P(n) (the induction hypothesis, IH).
       We must show P(n + 1). ⟨…use IH here, say so…⟩ 
  By induction, P(n) holds for all n ≥ n₀. ∎
```

#### Worked examples

**Example A (geometric sum).** For `r ≠ 1` and `n ≥ 0`: `1 + r + r² + ⋯ + rⁿ = (rⁿ⁺¹ − 1)/(r − 1)`.

*Proof.* `P(n)` is that identity. *Base* `n = 0`: LHS = 1, RHS = `(r − 1)/(r − 1) = 1`. ✔
*Step.* Assume `P(n)`. Then `1 + ⋯ + rⁿ + rⁿ⁺¹ = (rⁿ⁺¹ − 1)/(r − 1) + rⁿ⁺¹` *(IH)* `= (rⁿ⁺¹ − 1 + rⁿ⁺¹(r − 1))/(r − 1) = (rⁿ⁺² − 1)/(r − 1)`, which is `P(n + 1)`. ∎

**Example B (an inequality, Bernoulli).** For `x ≥ −1` and `n ≥ 0`: `(1 + x)ⁿ ≥ 1 + nx`.

*Proof.* *Base* `n = 0`: `1 ≥ 1`. *Step.* Assume `(1 + x)ⁿ ≥ 1 + nx`. Since `1 + x ≥ 0`, multiplying by `1 + x` preserves the inequality: `(1 + x)ⁿ⁺¹ ≥ (1 + x)(1 + nx) = 1 + (n + 1)x + nx² ≥ 1 + (n + 1)x`, because `nx² ≥ 0`. ∎ (Note exactly where `x ≥ −1` is used: to multiply an inequality by `1 + x`.)

**Example C (strong induction: binary representation).** Every integer `n ≥ 1` is a sum of **distinct** powers of 2.

*Proof (strong induction).* Let `n ≥ 1` and assume the claim for all `k` with `1 ≤ k < n`. If `n = 1 = 2⁰`, done. If `n > 1`, let `2^j` be the largest power of 2 with `2^j ≤ n`, so `2^j ≤ n < 2^(j+1)`. If `n = 2^j`, done. Otherwise `m = n − 2^j` satisfies `1 ≤ m < 2^j`; by the IH `m` is a sum of distinct powers of 2, each at most `m < 2^j`, hence different from `2^j`. Adding `2^j` gives such a sum for `n`. ∎

**Example D (structural induction: binary trees).** A *full binary tree* is either a single leaf, or a root with two full binary trees as children. Claim: a full binary tree has exactly one more leaf than it has internal nodes.

*Proof.* *Base (single leaf):* 1 leaf, 0 internal nodes: `1 = 0 + 1`. ✔ *Step:* a tree with root `r` and subtrees `T₁, T₂`. By IH `T₁` has `L₁ = I₁ + 1` leaves and `T₂` has `L₂ = I₂ + 1`. The new tree has `L₁ + L₂` leaves and `I₁ + I₂ + 1` internal nodes (the root is internal). Then `L₁ + L₂ = I₁ + I₂ + 2 = (I₁ + I₂ + 1) + 1`. ✔ ∎

**Example E (a recurrence, two base cases).** Let `a₀ = 1`, `a₁ = 2`, and `aₙ₊₂ = 5aₙ₊₁ − 6aₙ`. Compute a few terms: `a₂ = 10 − 6 = 4`, `a₃ = 20 − 12 = 8`, `a₄ = 40 − 24 = 16`. The pattern suggests `aₙ = 2ⁿ`.

*Claim.* `aₙ = 2ⁿ` for all `n ≥ 0`.

*Proof.* Induction with **two** base cases, because the recurrence looks back two places. *Base:* `a₀ = 1 = 2⁰` and `a₁ = 2 = 2¹`. *Step:* let `n ≥ 0` and assume `aₙ = 2ⁿ` and `aₙ₊₁ = 2ⁿ⁺¹` (both are needed). Then `aₙ₊₂ = 5·2ⁿ⁺¹ − 6·2ⁿ = 10·2ⁿ − 6·2ⁿ = 4·2ⁿ = 2ⁿ⁺²`. ✔ ∎

(Lesson: **compute small cases first to guess the formula, and test the guess against the base cases before trying to prove it**. A wrong formula cannot be proved, and trying wastes time. If the base cases had given `a₁ = 3`, the pattern `2ⁿ` would have failed immediately.)

#### Strengthening the induction hypothesis

Sometimes `P(n)` is true but the step cannot be proved because the IH is too weak. The remedy is to prove a *stronger* statement `Q(n)`.

*Example.* Claim: `1 + 1/4 + 1/9 + ⋯ + 1/n² < 2` for all `n ≥ 1`. Trying to prove it directly fails (adding `1/(n+1)²` to something `< 2` need not stay `< 2`). Strengthen to `Q(n)`: the sum is `≤ 2 − 1/n`. *Base:* `1 ≤ 1`. *Step:* sum for `n+1` is `≤ 2 − 1/n + 1/(n+1)²`, and `1/(n+1)² < 1/(n(n+1)) = 1/n − 1/(n+1)`, so the sum is `< 2 − 1/n + 1/n − 1/(n+1) = 2 − 1/(n+1)`. ✔ Hence `Q(n)` for all `n`, and `Q(n)` implies the original claim. ∎

#### Common pitfalls (extended list)

| Pitfall | Example / explanation |
|---|---|
| Missing or false base case | "`n = n + 1`": the step holds (add 1 to both sides) but no base case |
| Wrong base case | claim for `n ≥ 0` but only `n = 1` checked |
| Assuming what you want to prove | using `P(n + 1)` inside the proof of the step |
| Proving the step only for particular `n` | the step must hold for **arbitrary** `n ≥ n₀` |
| Hidden dependence on `n` being large | "all horses have the same colour": step fails at `n = 1` |
| Not enough base cases for strong induction | step reaches back `r` places ⇒ `r` base cases |
| Induction variable confusion | induction on `n` for a statement with two variables; the IH must apply to the **same** other variables or be quantified (`∀m`) |
| Mixing up `n` and `n + 1` indices | check by writing `P(n + 1)` explicitly |
| Using induction when not needed | a direct argument may be simpler |
| Forgetting to say what `P(n)` is | always define it |

### 5.14.5 Proofs about sets, functions and relations

These proofs are **mechanical**: a definition unfolds into a quantified statement and the skeleton from the shape table does the rest.

#### Sets (element-chasing)

```
To prove A ⊆ B:    Let x ∈ A be arbitrary. ⟨…⟩ Hence x ∈ B.
To prove A = B:    Show A ⊆ B and B ⊆ A.
To prove A ∩ B ⊆ C:   Let x ∈ A ∩ B. Then x ∈ A and x ∈ B. ⟨…⟩ x ∈ C.
```

**Example 1.** `(A ∖ B) ∩ B = ∅`. *Proof.* Suppose `x ∈ (A ∖ B) ∩ B`. Then `x ∈ A ∖ B` (so `x ∉ B`) and `x ∈ B`: contradiction. So no such `x` exists. ∎

**Example 2 (De Morgan for sets).** `(A ∩ B)ᶜ = Aᶜ ∪ Bᶜ` (complement in a universe `U`). *Proof.* For arbitrary `x ∈ U`: `x ∈ (A ∩ B)ᶜ ⇔ ¬(x ∈ A ∧ x ∈ B) ⇔ x ∉ A ∨ x ∉ B ⇔ x ∈ Aᶜ ∪ Bᶜ`. ∎ (Set identities are propositional laws applied to membership statements.)

**Example 3 (power set).** If `A ⊆ B` then `𝒫(A) ⊆ 𝒫(B)`. *Proof.* Let `X ∈ 𝒫(A)`; then `X ⊆ A ⊆ B`, so `X ⊆ B` (transitivity of ⊆), i.e. `X ∈ 𝒫(B)`. ∎

**Russell's paradox as a proof.** There is no set `R` with `∀x (x ∈ R ↔ x ∉ x)`. *Proof.* Suppose `R` is such a set. Instantiate `x := R`: `R ∈ R ↔ R ∉ R`. Impossible (`P ↔ ¬P`). ∎ (This is Chapter 4, Example 6 with `R(x, y) := y ∈ x`.)

#### Functions

Let `f : X → Y`, `g : Y → Z`.

| Property | To prove it |
|---|---|
| `f` injective | assume `f(a) = f(b)`, show `a = b` |
| `f` surjective | given `y`, find `x` with `f(x) = y` |
| `f` bijective | both |
| `g ∘ f` injective/surjective | usually: unpack, apply the properties of `f` and `g` in turn |
| `f` has an inverse | show bijective; define `f⁻¹(y)` = the unique `x` with `f(x) = y` |

**Example 4.** If `f : X → Y` and `g : Y → Z` are injective, so is `g ∘ f`. *Proof.* Let `g(f(a)) = g(f(b))`. Since `g` is injective, `f(a) = f(b)`. Since `f` is injective, `a = b`. ∎

**Example 5 (a bijection).** `h : ℝ → ℝ`, `h(x) = 2x + 3` is bijective. *Injective:* `2a + 3 = 2b + 3` ⇒ `a = b`. *Surjective:* given `y`, take `x = (y − 3)/2`; then `h(x) = y`. ∎

**Example 6 (images and preimages).** `f(A ∩ B) ⊆ f(A) ∩ f(B)`, but equality can fail for non-injective `f`. *Proof of ⊆:* if `y ∈ f(A ∩ B)`, then `y = f(x)` with `x ∈ A ∩ B`, so `y ∈ f(A)` and `y ∈ f(B)`. *Counterexample for ⊇:* `f(x) = x²`, `A = {−1}`, `B = {1}`: `f(A ∩ B) = f(∅) = ∅`, but `f(A) ∩ f(B) = {1}`. ∎

#### Relations

**An equivalence relation** is reflexive, symmetric, transitive; to prove `~` is one, prove all three.

**Example 7.** On ℤ define `a ≡ b (mod n)` iff `n ∣ (a − b)`. *Reflexive:* `n ∣ 0`. *Symmetric:* if `n ∣ (a − b)`, then `n ∣ −(a − b) = (b − a)`. *Transitive:* if `n ∣ (a − b)` and `n ∣ (b − c)`, then `n ∣ (a − b) + (b − c) = (a − c)`. ∎

**Equivalence classes partition.** If `~` is an equivalence relation on `S`, then the classes `[a] = {x : x ~ a}` are pairwise disjoint or equal, and cover `S`. *Proof of "disjoint or equal":* suppose `z ∈ [a] ∩ [b]`, so `z ~ a` and `z ~ b`. By symmetry and transitivity, `a ~ b`. Then for any `x ∈ [a]`: `x ~ a ~ b`, so `x ∈ [b]`; similarly `[b] ⊆ [a]`. ∎

### 5.14.6 Proofs about ε-δ and limits (in more detail)

The general shape of an ε-δ limit proof: `lim_{x → a} f(x) = L` means `∀ε > 0 ∃δ > 0 ∀x (0 < |x − a| < δ → |f(x) − L| < ε)`.

```
Proof. Let ε > 0 be given.
       Choose δ = ⟨expression in ε⟩ (found by scratch work). Note δ > 0.
       Let x be such that 0 < |x − a| < δ.
       Then |f(x) − L| = ⟨…⟩ < ε. ∎
```

**Scratch work for `lim_{x → 2} x² = 4`:** `|x² − 4| = |x − 2||x + 2|`. To control `|x + 2|`, first restrict `|x − 2| < 1`, so `1 < x < 3` and `|x + 2| < 5`. Then `|x² − 4| < 5|x − 2|`. We want `< ε`, so ask `|x − 2| < ε/5`. Take `δ = min(1, ε/5)`.

**Proof.** Let `ε > 0`. Put `δ = min(1, ε/5) > 0`. If `0 < |x − 2| < δ`, then `|x − 2| < 1` gives `|x + 2| < 5`, and `|x − 2| < ε/5`, so `|x² − 4| = |x − 2||x + 2| < (ε/5)·5 = ε`. ∎

**Negating the definition (proving a limit does not exist or is not L).** `¬∀ε ∃δ ∀x …` becomes `∃ε > 0 ∀δ > 0 ∃x (0 < |x − a| < δ ∧ |f(x) − L| ≥ ε)`. To use it: **you** pick `ε` (cleverly), then for each `δ` that the adversary names, **you** produce an `x`.

### 5.14.7 Mathematical writing: style and phrases

| Intention | Phrase |
|---|---|
| begin an arbitrary argument | "Let `x` be an arbitrary element of `S`." |
| assume the hypothesis | "Assume (Suppose) that ..." |
| introduce a witness | "Since `∃x P(x)`, choose `a` such that `P(a)`." |
| state what you will prove | "We must show that ..." / "It suffices to show that ..." |
| use a definition | "By definition, ..." |
| a derived fact | "Hence", "Therefore", "Thus", "It follows that" |
| a cause | "Because", "Since" |
| case split | "We distinguish two cases." |
| contradiction | "Suppose, for contradiction, that ... This contradicts ..." |
| contrapositive | "We prove the contrapositive." |
| induction | "We argue by induction on `n`." |
| end | "This completes the proof." / `∎` / `□` |
| caution | avoid "clearly", "obviously", "trivially" unless truly so; they hide gaps |

**Quantifier discipline in prose.** Never use a variable before introducing it. Never reuse a letter for two different objects in the same scope. Say "for every ε > 0 there is δ > 0 such that" with the order intact, because the order of quantifiers is the content.

### 5.14.8 A gallery of bad proofs

Learning to see a false proof is learning logic. For each, find the error before reading the diagnosis.

**1. "1 = 2".** Let `a = b`. Then `a² = ab`, `a² − b² = ab − b²`, `(a + b)(a − b) = b(a − b)`. Cancel `(a − b)`: `a + b = b`; since `a = b`, `2b = b`, so `2 = 1`.
*Error:* dividing by `a − b = 0`. (A false step hides inside an equivalence-looking chain.)

**2. Circular reasoning.** "Claim: `√2` is irrational. Proof: `√2` is not a fraction, hence irrational."
*Error:* assumes the conclusion in other words.

**3. The converse.** "If `n` is even then `n²` is even. Since `n²` is even, `n` is even."
*Error:* uses the converse. (The converse is true here, but needs its own proof, via contrapositive.)

**4. Generalizing from examples.** "`n² + n + 41` is prime for `n = 0, 1, …, 39`, so for all `n`."
*Error:* examples never prove a universal. (For `n = 40`: `40² + 40 + 41 = 1681 = 41²`.)

**5. Illegal ∀I.** "Let `x` be an even integer; `x = 2k`. So every integer is of the form `2k`."
*Error:* the name `x` was assumed even, so it is not arbitrary.

**6. Quantifier swap.** "For every integer `n` there is an integer `m` with `m > n`. So there is an integer `m` with `m > n` for all `n`."
*Error:* `∀∃` turned into `∃∀`.

**7. Illegal use of WLOG.** "To show that `a/b ≥ 1` for all positive reals `a, b`, assume without loss of generality that `a ≥ b`."
*Error:* the statement is not symmetric: swapping `a` and `b` turns it into `b/a ≥ 1`, a different claim (and the original claim is false for `a < b`). WLOG is allowed only when swapping the names gives the *same* statement.

**8. Horse fallacy** (induction): see 5.11.

**9. Hidden assumption.** "Let `x` be a real number. Then `x² ≥ x`." *Error:* false for `0 < x < 1`. (A tacit assumption `x ≥ 1`.)

**10. Equality sign abuse.** "`(−1)(−1) = 1`, so `(−1)(−1) = 1 = √1 = √((−1)(−1)) = √(−1)√(−1) = i·i = −1`."
*Error:* `√(ab) = √a√b` holds only for non-negative `a, b`.

### 5.14.9 Quick-check (with answers)

**Q1.** Write the hidden quantifiers of "If `x > 1` then `x² > x`".
**Q2.** Which technique would you try first for: (a) "if `n²` is divisible by 5 then `n` is divisible by 5"; (b) "there are infinitely many primes of the form `4k + 3`" (hint: like Euclid); (c) "`A ∪ B = B ∪ A`"; (d) "`∑ᵢ₌₁ⁿ i³ = (n(n+1)/2)²`"?
**Q3.** What exactly is wrong with: "Base case `n = 1` ✔. Step: assume `P(n)`. Then `P(n + 1)` because `P(n + 1)` is `P(n)` with `n` replaced by `n + 1`."
**Q4.** What does the proof of an "iff" require?
**Q5.** How many base cases does a strong-induction proof need if the step reaches back to `n − 3`?
**Q6.** Negate: "`f` is injective."
**Q7.** What is a minimal counterexample argument?

**Answers.**
**A1.** `∀x ∈ ℝ (x > 1 → x² > x)`.
**A2.** (a) contrapositive (if `n` is not divisible by 5 then `n²` is not); or cases on the remainder mod 5. (b) contradiction (assume finitely many, consider `4p₁⋯pₙ − 1`). (c) element-chasing, or the commutativity of ∨. (d) induction.
**A3.** It "proves" `P(n + 1)` by renaming, not by argument: the step must actually *derive* `P(n + 1)` from `P(n)` using algebra or reasoning.
**A4.** Both directions, `A → B` and `B → A`, each with its own argument.
**A5.** Three base cases, `n₀`, `n₀ + 1`, `n₀ + 2`. Then every `n ≥ n₀ + 3` has `n − 3 ≥ n₀`, so the step can look back three places. (In general: reaching back `r` places needs `r` base cases, as in the `4a + 5b` example, which needed four.)
**A6.** `∃a ∃b (f(a) = f(b) ∧ a ≠ b)`.
**A7.** Assume the statement fails for some natural number; take the least such; derive a contradiction using the statement's truth for smaller values.

## Problems for Chapter 5

**5.1 ★** Prove: the sum of two odd integers is even.

**5.2 ★** Prove: if n² is odd then n is odd. (Hint: which technique?)

**5.3 ★** Prove: the product of two odd integers is odd.

**5.4 ★★** Prove: if n is an integer and n² is divisible by 3, then n is divisible by 3. Deduce that √3 is irrational.

**5.5 ★★** Prove: if q is a nonzero rational and r is irrational, then q·r is irrational. (Is the same true for q + r? For r + s with both irrational?)

**5.6 ★★** Prove by cases: for all integers n, n(n + 1) is even.

**5.7 ★★** Prove by induction: 1² + 2² + ··· + n² = n(n + 1)(2n + 1)/6.

**5.8 ★★** Prove by induction: for all n ≥ 0, 2ⁿ⁺¹ − 1 = 1 + 2 + 4 + ··· + 2ⁿ.

**5.9 ★★** Prove by induction: for all n ≥ 5, 2ⁿ > n². (Mind the base case!)

**5.10 ★★** Let F₁ = F₂ = 1 and Fₙ₊₂ = Fₙ₊₁ + Fₙ. Prove F₁ + F₂ + ··· + Fₙ = Fₙ₊₂ − 1.

**5.11 ★★** Prove the set identities: (a) A ⊆ B ⇔ A ∩ B = A; (b) (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ.

**5.12 ★★** Prove: if f: X → Y and g: Y → Z are both surjective, then g ∘ f is surjective. And: if f has a right inverse h (f(h(y)) = y for all y), then f is surjective.

**5.13 ★★** Prove: every integer n ≥ 2 has a prime divisor. (Strong induction or well-ordering.)

**5.14 ★★★** Prove: for every n ≥ 1, a 2ⁿ × 2ⁿ chessboard with one square removed can be tiled by L-shaped trominoes. (Induction, and the *strengthened* hypothesis matters: it must hold for *any* removed square.)

**5.15 ★★★** Find the error in this "proof" that all horses have the same color: "Induct on the number of horses. One horse: trivial. Assume any n horses have the same color. Given n + 1 horses, remove one: the remaining n have the same color; remove a different one: those n also have the same color. The two groups overlap, so all n + 1 have the same color."

**5.16 ★★★** Prove using the ε-δ definition: lim_{x → 2} x² = 4. (Hint: restrict δ ≤ 1 first to bound |x + 2|, then choose δ = min(1, ε/5).)

**5.17 ★★★** Prove Cantor's theorem for A = ℕ by constructing the diagonal set explicitly, then explain in one paragraph why the argument is the barber paradox.

---

# Chapter 6. Metatheory: what logic can and cannot do

This chapter is more conceptual. You should be able to **state** each theorem precisely, **explain** why it matters, and **prove** the easy ones. (The big proofs, notably completeness, are in Enderton or Huth-Ryan; sketches are given here.)

## 6.1 Soundness and completeness

Recall: **Γ ⊨ A** (semantic): every model of Γ satisfies A. **Γ ⊢ A** (syntactic): there is a derivation of A from Γ.

| Theorem | Statement | Meaning |
|---|---|---|
| **Soundness** | Γ ⊢ A ⇒ Γ ⊨ A | The proof system proves only truths |
| **Completeness** (Gödel 1929) | Γ ⊨ A ⇒ Γ ⊢ A | The proof system proves *all* truths (of this kind) |

**Soundness proof idea (structural induction on derivations).** Show every rule preserves the property "if all premises are true in M, so is the conclusion". For ∧I: if Γ ⊨ A and Γ ⊨ B, then any model of Γ satisfies both A and B, hence A ∧ B. For →I: use the semantic deduction theorem (F2). For ∀I: the freshness condition is exactly what makes the argument go through, since a name about which nothing is assumed can be reinterpreted as any element. This is why every side condition matters.

**Completeness proof idea (Henkin).** Suppose Γ ⊬ A. Then Γ ∪ {¬A} is *consistent*. Extend it to a *maximal consistent* set that also has "witnesses" for existentials (add new constants c with ∃x B → B[c/x]). Then build a model whose domain is made of the terms themselves. This model satisfies Γ ∪ {¬A}, so Γ ⊭ A.

**Why this is remarkable.** Truth quantifies over *all* structures (a vast, infinite notion). Completeness says that finite, checkable derivations suffice to capture it. For *second-order* logic this fails (no complete proof system).

## 6.2 Consistency, theories, and compactness

- A set Γ is **consistent** if Γ ⊬ ⊥. By soundness and completeness, consistent ⇔ satisfiable.
- A **theory** is a set of sentences closed under consequence. Examples: the theory of groups, Peano Arithmetic (PA), ZFC set theory.

**Compactness theorem.** A set Γ of sentences is satisfiable iff **every finite subset** of Γ is satisfiable.

*Why it follows from completeness:* if Γ were unsatisfiable, then Γ ⊢ ⊥, and the derivation uses only finitely many premises.

**Consequences:**
- *Non-standard models of arithmetic.* Add a new constant c to the language of arithmetic, together with the sentences c > 0, c > 1, c > 2, ... Every finite subset is satisfiable (take c large enough in the standard model), so the whole set is satisfiable. The model contains an "infinite natural number". Hence first-order logic **cannot pin down ℕ**.
- *Finiteness is not expressible in FOL.* There is no sentence (or set of sentences) true exactly in the finite structures (Problem 6.5).

## 6.3 Löwenheim-Skolem

If a countable first-order theory has an infinite model, it has a model of **every** infinite cardinality. In particular, ZFC (if consistent) has a *countable* model, which thinks it contains uncountable sets (the Skolem paradox). FOL cannot distinguish "countable" from "uncountable".

## 6.4 Decidability

| Logic | Is validity decidable? |
|---|---|
| Propositional | **Yes** (truth tables, SAT algorithms; the problem is co-NP-complete) |
| Monadic FOL (only unary predicates) | Yes |
| FOL, Bernays-Schönfinkel fragment (satisfiability of ∃*∀* sentences, no function symbols; validity of the dual ∀*∃* class) | Yes |
| **Full FOL** | **No** (Church-Turing 1936). But validity is **semi-decidable**: a program can enumerate all proofs and halt when it finds one. |

**Semi-decidable** means: if the formula is valid, a prover will eventually find a proof. If it is *not* valid, the prover may run forever. This is why every real prover needs timeouts, and why "the prover didn't answer" never proves invalidity.

The theorem connects to everything above: completeness gives you the enumeration of proofs (hence semi-decidability), and the Church-Turing reduction shows no algorithm can always decide.

## 6.5 Gödel's incompleteness theorems

Do not confuse these with the completeness theorem (different notion of "complete").

- **First incompleteness.** Any consistent, effectively axiomatized theory that can express basic arithmetic (e.g., PA, ZFC) contains a sentence G such that neither G nor ¬G is provable. (G, informally, says "I am not provable.")
- **Second incompleteness.** Such a theory cannot prove its own consistency.

*Not contradictory with completeness:* completeness says "true in all models of T ⇔ provable in T". G is true in *some* models of T and false in others (e.g., non-standard ones), so it is not true in *all* models, so nothing contradicts. What fails is that no first-order theory of arithmetic can make ℕ the *only* model.

## 6.6 Other semantic and syntactic notions worth knowing

- **Herbrand's theorem.** A set of universal sentences has a model iff it has a *Herbrand model*, built from ground terms. It reduces FOL satisfiability to a (possibly infinite) propositional problem and is the theoretical basis for resolution provers.
- **Cut elimination (Gentzen).** In sequent calculus, every proof can be transformed into one without "lemmas" (cuts). This gives consistency proofs and the subformula property.
- **Interpolation (Craig).** If ⊨ A → B, there is an I using only symbols common to A and B with ⊨ A → I and ⊨ I → B. Applications in model checking.

## 6.7 Chapter 6 in complete detail (the from-zero companion)

Chapter 6 states the big theorems about logic. This companion explains **what is being claimed and why it is plausible**, proves the easy parts completely, gives the proof of completeness in checkable steps, builds the **computability background** you need for decidability and Gödel, explains **Gödel's theorems** properly (and the misconceptions around them), and opens the door to **other logics** (modal, many-valued, and more) so that you know where to go after this course.

### 6.7.1 Why study logic *itself*? The two levels again

Until now you have *used* logic: you proved theorems inside a proof system. **Metatheory** (metalogic) proves theorems *about* proof systems and about the languages they describe. The questions:

| Question | Meaning |
|---|---|
| **Soundness** | Can the system prove something false? |
| **Completeness** | Is there something true that the system can't prove? |
| **Consistency** | Can the system prove a contradiction? |
| **Decidability** | Is there an algorithm that, given `A`, tells whether it is provable? |
| **Expressiveness** | What can the language say (and not say)? |
| **Categoricity** | Do the axioms pin down one structure? |
| **Compactness, interpolation, definability** | structural properties of the logic |

#### Vocabulary of theories

| Term | Definition |
|---|---|
| **Theory** `T` | a set of sentences (axioms), often taken closed under consequence |
| **Th(T)** or **Cn(T)** | the deductive closure: all sentences `A` with `T ⊢ A` |
| **Mod(T)** | the class of all structures that satisfy every sentence of `T` |
| **Th(M)** | the complete theory of a structure `M`: all sentences true in `M` |
| **Consistent** | `T ⊬ ⊥` |
| **Complete** (of a theory) | for every sentence `A`: `T ⊢ A` or `T ⊢ ¬A` (do not confuse with *completeness* of a proof system!) |
| **Axiomatizable / recursively axiomatizable** | the axioms can be listed (generated) by an algorithm |
| **Decidable theory** | `{A : T ⊢ A}` is a decidable set |
| **Conservative extension** | `T' ⊇ T` proves no new sentences in the language of `T` |
| **Definitional extension** | adds new symbols with defining axioms (conservative) |
| **Categorical** | all models are isomorphic; **κ-categorical**: all models of cardinality κ are isomorphic |
| **Elementary equivalence** `M ≡ N` | `Th(M) = Th(N)` |
| **Independent sentence** | neither `A` nor `¬A` follows from `T` (e.g. the continuum hypothesis for ZFC) |

**Two different "completenesses".** (1) *Completeness of a proof system* (Gödel 1929): everything valid is provable. (2) *Completeness of a theory*: every sentence is decided. Gödel's *incompleteness* theorems are about sense (2).

### 6.7.2 Soundness proved in full (propositional natural deduction)

**Theorem.** If `Γ ⊢ A` then `Γ ⊨ A`.

*Setup.* A derivation is a sequence of lines. For each line `n` let `Γₙ` be the set of formulas that are open at that line: the premises plus the assumptions of all boxes enclosing line `n`. **Claim (by strong induction on the line number):** for every line `n` with formula `Aₙ`, we have `Γₙ ⊨ Aₙ`.

The theorem follows: at the last line (depth 0) `Γₙ` is the set of premises and `Aₙ` is the conclusion.

*Cases (by the rule justifying line `n`):*

1. **Premise or assumption.** `Aₙ ∈ Γₙ`, so every valuation making `Γₙ` true makes `Aₙ` true. ✔
2. **∧I** from lines `i, j` with `Aₙ = Aᵢ ∧ Aⱼ`. Here `Γᵢ ⊆ Γₙ` and `Γⱼ ⊆ Γₙ` (lines `i`, `j` are visible at `n`). By IH, `Γᵢ ⊨ Aᵢ` and `Γⱼ ⊨ Aⱼ`. A valuation satisfying `Γₙ` satisfies `Γᵢ` and `Γⱼ`, hence `Aᵢ` and `Aⱼ`, hence `Aᵢ ∧ Aⱼ`. ✔ (Uses **monotonicity**: more premises can only help.)
3. **∧E, ∨I, →E, ↔E:** the same style: a valuation satisfying `Γₙ` satisfies the cited lines (by IH), hence the conclusion by the truth table.
4. **→I** from a box `[i … j]` with `Aᵢ = A`, `Aⱼ = B`, `Aₙ = A → B`. In the box `Γⱼ = Γₙ ∪ {A}`, so the IH gives `Γₙ ∪ {A} ⊨ B`. Take `v ⊨ Γₙ`. If `v ⊭ A` then `A → B` is true. If `v ⊨ A` then `v ⊨ Γₙ ∪ {A}`, so `v ⊨ B`. Either way `v ⊨ A → B`. ✔ (This is the semantic deduction theorem F2.)
5. **∨E** from `A ∨ B` and boxes with `A ⊢ C` and `B ⊢ C`: IH gives `Γₙ ⊨ A ∨ B`, `Γₙ ∪ {A} ⊨ C`, `Γₙ ∪ {B} ⊨ C`. Take `v ⊨ Γₙ`. Then `v ⊨ A` or `v ⊨ B`; in either case `v` satisfies `C`. ✔
6. **¬I** from a box with `A ⊢ ⊥`: IH gives `Γₙ ∪ {A} ⊨ ⊥`, so no valuation satisfies `Γₙ ∪ {A}`. Hence every `v ⊨ Γₙ` has `v ⊭ A`, i.e. `v ⊨ ¬A`. ✔
7. **¬E** from lines `A` and `¬A`: the IH gives `Γₙ ⊨ A` and `Γₙ ⊨ ¬A`. A valuation satisfying `Γₙ` would satisfy both `A` and `¬A`, which is impossible; so `Γₙ` has no model, and `Γₙ ⊨ ⊥` holds vacuously. ✔
8. **⊥E** from `⊥`: `Γₙ ⊨ ⊥` means `Γₙ` has no model, so `Γₙ ⊨ C` vacuously. ✔
9. **RAA** from a box `¬A ⊢ ⊥`: `Γₙ ∪ {¬A}` has no model, so every model of `Γₙ` satisfies `A`. ✔ (This is the step that uses classical two-valued semantics.)

∎ This proof is short because the rules are designed to mirror the semantics. For first-order logic the new cases are ∀I and ∃E, handled by the reinterpretation argument of 4.7.6, plus ∀E, ∃I (substitution lemma: `⟦A[t/x]⟧_s = ⟦A⟧_{s[x ↦ ⟦t⟧]}`) and the equality rules.

**Corollary (consistency).** If `Γ` has a model, then `Γ ⊬ ⊥`. (If `Γ ⊢ ⊥`, soundness gives `Γ ⊨ ⊥`, so `Γ` has no model.) This is how one proves, say, that group theory is consistent: exhibit a group.

### 6.7.3 Completeness: the proof in steps

**Theorem (propositional case).** If `Γ ⊨ A` then `Γ ⊢ A`.

It suffices to prove the **model existence lemma**: *every consistent set of formulas is satisfiable.* Indeed, suppose `Γ ⊨ A` but `Γ ⊬ A`. Then `Γ ∪ {¬A}` is consistent (if `Γ, ¬A ⊢ ⊥` then `Γ ⊢ A` by RAA). By the lemma, `Γ ∪ {¬A}` has a model, contradicting `Γ ⊨ A`.

*Proof of the model existence lemma.*

**Step 1 (Lindenbaum's lemma).** Every consistent `Γ` extends to a **maximal consistent set** `Δ`: consistent, and for every formula `B`, either `B ∈ Δ` or `¬B ∈ Δ`.
*Construction.* Enumerate all formulas `B₁, B₂, …`. Put `Δ₀ = Γ`. If `Δₙ ∪ {Bₙ₊₁}` is consistent, let `Δₙ₊₁ = Δₙ ∪ {Bₙ₊₁}`; otherwise `Δₙ₊₁ = Δₙ ∪ {¬Bₙ₊₁}`. This keeps consistency: if both `Δₙ, B ⊢ ⊥` and `Δₙ, ¬B ⊢ ⊥`, then `Δₙ ⊢ ¬B` (¬I) and `Δₙ ⊢ B` (RAA), so `Δₙ ⊢ ⊥`. Let `Δ = ⋃ Δₙ`. It is consistent (a derivation of ⊥ uses only finitely many premises, all in some `Δₙ`).

**Step 2 (properties of maximal consistent sets).** For `Δ` maximal consistent:
- (a) `Δ` is deductively closed: if `Δ ⊢ B` then `B ∈ Δ` (otherwise `¬B ∈ Δ`, and `Δ ⊢ ⊥`).
- (b) `¬B ∈ Δ` iff `B ∉ Δ`.
- (c) `B ∧ C ∈ Δ` iff `B ∈ Δ` and `C ∈ Δ`. (∧I, ∧E, closure.)
- (d) `B ∨ C ∈ Δ` iff `B ∈ Δ` or `C ∈ Δ`. (⇐ by ∨I; ⇒: if neither is in `Δ`, then `¬B, ¬C ∈ Δ`, and ∨E with these gives `Δ ⊢ ⊥`.)
- (e) `B → C ∈ Δ` iff `B ∉ Δ` or `C ∈ Δ`.
Each is a short use of the natural deduction rules.

**Step 3 (the canonical valuation).** Define `v(p) = T` iff `p ∈ Δ`.

**Step 4 (truth lemma).** For every formula `B`: `⟦B⟧ᵥ = T` iff `B ∈ Δ`. *Induction on `B`:* atoms by definition; each connective by (b)-(e) and the truth tables. ∎

Hence `v` satisfies `Δ ⊇ Γ`, and the model existence lemma holds.

#### First-order completeness (Henkin's method; outline)

The same plan, with three additions:

1. **Henkin witnesses.** Add infinitely many new constants `c₁, c₂, …` and, for each formula `∃x B(x)`, an axiom `∃x B(x) → B(cᵢ)` (a "witness axiom"). The extended theory remains consistent (this is where the freshness conditions of ∃E and ∀I are used).
2. **Maximal consistent extension** `Δ`, now also *witnessed*: whenever `∃x B(x) ∈ Δ`, some `B(c) ∈ Δ`.
3. **The term model.** Domain: the set of closed terms (modulo `s ~ t` iff `s = t ∈ Δ`, to handle equality). Interpret each function symbol syntactically and each predicate by `P^M = {(t₁,…,tₙ) : P(t₁,…,tₙ) ∈ Δ}`. The **truth lemma** is proved by induction on formulas; the `∃` case uses the witnesses, the `∀` case uses the maximality.

The resulting structure is a model of `Γ`, countable if the language is countable. This proves **Gödel's completeness theorem** (1929; Henkin's proof 1949).

#### Consequences of the proof method

- **Compactness** (6.7.4) follows because derivations are finite.
- **Löwenheim-Skolem (downward)** follows because the term model is countable.
- **Semi-decidability of validity**: enumerate all finite derivations.

### 6.7.4 Compactness in complete detail

**Theorem (compactness).** A set `Γ` of sentences has a model iff every finite subset of `Γ` has a model.

*Equivalent form:* if `Γ ⊨ A`, then `Γ₀ ⊨ A` for some finite `Γ₀ ⊆ Γ`.

*Proof from completeness.* (⇒) trivial. (⇐) Suppose `Γ` has no model. By completeness `Γ ⊢ ⊥`; the derivation uses finitely many premises `Γ₀`, so `Γ₀ ⊢ ⊥`, so by soundness `Γ₀` has no model. ∎

(There are other proofs: via ultraproducts (Łoś), and for propositional logic via Tychonoff's theorem or the compactness of Cantor space.)

#### Applications, with proofs

**1. Non-standard models of arithmetic.** Let `T = Th(ℕ)` (all true sentences of arithmetic) and add a new constant `c` with axioms `c ≠ 0`, `c ≠ 1`, `c ≠ 2`, … (more precisely `c > n̄` for each numeral). Every finite subset has a model: ℕ itself, with `c` interpreted as a number larger than the finitely many constraints. By compactness the whole set has a model `*ℕ`, which satisfies every first-order truth of ℕ but contains an element `c` greater than all standard numerals. First-order logic **cannot characterize ℕ up to isomorphism**.

**2. Finiteness is not first-order expressible.** Suppose `T` had exactly the finite structures as models (over `=`). Let `λₙ` say "there are at least `n` elements". Every finite subset of `T ∪ {λₙ : n ≥ 1}` has a (large enough finite) model. By compactness `T ∪ {λₙ}` has a model, which is infinite: contradiction with `T` having only finite models. ∎

**3. The de Bruijn-Erdős theorem (an application of *propositional* compactness).** An infinite graph is `k`-colourable iff every finite subgraph is.
*Proof.* For each vertex `v` and colour `i ≤ k` take an atom `p_{v,i}` ("v has colour i"). Clauses: `p_{v,1} ∨ ⋯ ∨ p_{v,k}` (some colour); `¬p_{v,i} ∨ ¬p_{v,j}` for `i ≠ j` (at most one); `¬p_{u,i} ∨ ¬p_{v,i}` for each edge `uv` (adjacent vertices differ). A finite subset of these clauses mentions finitely many vertices, so it is satisfiable if the corresponding finite subgraph is `k`-colourable. By compactness the whole set is satisfiable: a `k`-colouring. ∎

**4. Connectedness is not first-order expressible.** If it were, `φ` = "the graph is connected". Add constants `a, b` and sentences `dist(a, b) > n` for all `n` (each is first-order: "no path of length ≤ n"). Every finite subset is satisfiable in a large connected graph (a long path), so the whole set has a model: a connected graph (by `φ`) with `a, b` at infinite distance: impossible. ∎

**5. Ordering and well-ordering.** "`<` is a well-order" is not first-order expressible: add constants `c₀, c₁, …` with `cₙ₊₁ < cₙ`; any finite subset is satisfiable in ℕ; so there is a model with an infinite descending sequence.

### 6.7.5 Löwenheim-Skolem and categoricity

**Downward L-S.** Every structure for a countable language has a countable *elementary substructure*. In particular, a satisfiable countable theory has a countable model.
**Upward L-S.** If a theory has an infinite model it has models of every larger cardinality (by compactness, adding `κ` many new constants).

**Consequences.**

- **Skolem's paradox.** ZFC (assuming it is consistent) has a countable model, which satisfies "there exists an uncountable set". No contradiction: "uncountable" inside the model means "no bijection with ω *inside the model*"; the model simply lacks the bijection (see Problem 6.8).
- **No first-order theory with an infinite model is categorical** (has exactly one model up to isomorphism): it has non-isomorphic models of different cardinalities.
- Isomorphism type can be pinned down only *within a cardinality*: **κ-categoricity.**

| Theory | Categorical in |
|---|---|
| Pure equality, "infinitely many elements" | every infinite cardinal |
| Dense linear orders without endpoints | ℵ₀ only (Cantor's back-and-forth); (ℚ,<) vs (ℝ,<) differ in size |
| Algebraically closed fields of characteristic 0 | every uncountable cardinal (Steinitz), not ℵ₀ |
| Vector spaces over a fixed field | every cardinality larger than the field's |
| Peano arithmetic | none: non-standard models in every infinite size |

**Łoś-Vaught test.** A theory with no finite models, in a countable language, that is κ-categorical for some infinite κ, is **complete**. Hence dense linear orders without endpoints and algebraically closed fields of characteristic 0 are complete theories, and (since axiomatizable complete theories are decidable) decidable.

**Tarski-Vaught test, elementary substructures, ultraproducts** are the main tools of *model theory*, the study of the relation between theories and their models. A good first book: Chang and Keisler, or Marker, *Model Theory: an Introduction*.

### 6.7.6 Computability background (just enough)

An **algorithm** is a finite, mechanical procedure. A formalization (Turing machines, λ-calculus, recursive functions) gives the **Church-Turing thesis**: every intuitively computable function is computable by a Turing machine.

| Notion | Definition |
|---|---|
| **Decidable** (recursive) set `S` | an algorithm that on input `x` halts and answers yes/no correctly for "x ∈ S?" |
| **Semi-decidable** (r.e., recursively enumerable) set | an algorithm that halts with *yes* exactly when `x ∈ S` (may loop if not) |
| **Co-r.e.** | complement is r.e. |
| **Fact** | `S` is decidable iff both `S` and its complement are r.e. |
| **Halting problem** `K` | the set of (program, input) pairs that halt: r.e. but **not** decidable (Turing 1936) |
| **Reduction** | `S ≤ T` if an algorithm converts instances of `S` into instances of `T` preserving answers; if `T` decidable then so is `S`. Contrapositive: to show `T` undecidable, reduce a known undecidable `S` to it. |

**Why the halting problem is undecidable** (diagonal argument, the same form as Cantor's theorem and Russell's barber). Suppose a program `H(p, x)` decides whether program `p` halts on input `x`. Define `D(p)`: if `H(p, p)` says "halts", loop forever; otherwise halt. Then `D(D)` halts iff `H(D, D)` says "does not halt" iff `D(D)` does not halt. Contradiction. ∎

#### The Church-Turing theorem for first-order logic

**Theorem (Church 1936, Turing 1936).** The set of valid first-order sentences is **not decidable**, though it is r.e.

*Why r.e.:* by completeness every valid sentence has a finite derivation; enumerate all strings, check each for being a derivation (mechanically checkable), and print its last line. *Why not decidable:* one *reduces* the halting problem (or the word problem, or Post's correspondence problem) to validity: for each Turing machine `M` and input `x` one can effectively write a sentence `φ_{M,x}` that is valid iff `M` halts on `x`. A decision procedure for validity would decide halting.

#### Decidable and undecidable theories and fragments

| Theory or fragment | Decidable? | Remark |
|---|---|---|
| Propositional logic | yes | SAT is NP-complete |
| Quantified Boolean formulas (QBF) | yes | PSPACE-complete |
| Monadic first-order logic (unary predicates only) | yes | Löwenheim 1915 |
| Bernays-Schönfinkel-Ramsey class (`∃*∀*` prefix, no function symbols) | yes | satisfiability NEXPTIME-complete |
| Two-variable fragment `FO²` | yes | Mortimer 1975, NEXPTIME-complete |
| Guarded fragment | yes | Andréka-van Benthem-Németi 1998 |
| Presburger arithmetic `(ℕ, +, 0, 1, <)` | yes | Presburger 1929 |
| Real closed fields `(ℝ, +, ·, 0, 1, <)` | yes | Tarski 1951 (quantifier elimination) |
| Theory of dense linear orders | yes | complete theory |
| Theory of algebraically closed fields | yes | Tarski, Robinson |
| Abelian groups | yes | Szmielew 1955 |
| **Full FOL (validity)** | **no** | Church-Turing; r.e. |
| FOL with a single binary relation symbol (no functions) | no | already undecidable: the undecidability of full FOL survives such drastic restriction |
| Arithmetic `(ℕ, +, ·)`, `Th(ℕ)` | no | not even r.e. (Gödel/Tarski) |
| Group theory (all groups) | no | Tarski |
| Finite satisfiability / validity in finite models | no | Trakhtenbrot 1950 (the set of sentences valid in all finite models is not r.e.) |
| Second-order logic validity | no | not even arithmetical |

The map of decidable fragments is the reason why **SMT solvers** (which decide combinations of decidable theories such as linear arithmetic, arrays and bit-vectors) are so useful in practice, even though full first-order logic is undecidable.

### 6.7.7 Gödel's incompleteness theorems, explained

#### The setting

Let `T` be a theory in the language of arithmetic that is (1) **consistent**, (2) **effectively axiomatized** (an algorithm can decide whether a sentence is an axiom), and (3) strong enough to prove basic facts about `+` and `·` (for instance Robinson arithmetic `Q`, a small finite fragment of Peano arithmetic). Examples: PA, ZFC.

#### Ingredient 1: arithmetization (Gödel numbering)

Assign each symbol a number, and each finite string a number, so that syntactic operations become arithmetic operations. One scheme: give the symbols codes `c(¬) = 1`, `c(→) = 2`, `c(∀) = 3`, `c(=) = 4`, `c(0) = 5`, `c(S) = 6`, `c(+) = 7`, `c(·) = 8`, `c(() = 9`, `c()) = 10`, and `c(xᵢ) = 10 + i` for the variables `x₁, x₂, …` (so the variable codes start at 11 and never clash with the other symbols). The code of a string `s₁ s₂ … sₖ` is
`⌜s₁…sₖ⌝ = 2^{c(s₁)} · 3^{c(s₂)} · 5^{c(s₃)} ⋯ pₖ^{c(sₖ)}`
(`pᵢ` the `i`-th prime), and uniqueness of prime factorization makes decoding possible. A derivation is a sequence of formulas, coded likewise. Then relations such as "`x` is the code of a formula", "`x` is the code of a derivation of the formula with code `y`" are **primitive recursive**, hence expressible by arithmetic formulas. In particular there is a formula `Prov_T(y)`, "there exists a code of a derivation of the formula with code `y`", expressing **provability in T**. Write `⌜A⌝` for the numeral denoting the code of `A`.

#### Ingredient 2: the diagonal (fixed-point) lemma

**Lemma.** For every formula `B(y)` with one free variable there is a sentence `G` such that `T ⊢ G ↔ B(⌜G⌝)`.

*Idea.* "Substitute the code of a formula into itself" is an arithmetic operation `d`. Let `A(x)` be the formula `B(d(x))` and let `G` be `A(⌜A⌝)`. Then `G` says `B(d(⌜A⌝))`, and `d(⌜A⌝) = ⌜A(⌜A⌝)⌝ = ⌜G⌝`, so `G ↔ B(⌜G⌝)`. This is the same self-reference trick as the barber, Cantor's diagonal, and the halting problem.

#### The first incompleteness theorem

Apply the lemma to `B(y) := ¬Prov_T(y)`. We get a sentence `G` with `T ⊢ G ↔ ¬Prov_T(⌜G⌝)`: "**G says: I am not provable in T.**"

- If `T ⊢ G`: then `T` proves `Prov_T(⌜G⌝)` (it is true and arithmetical, so `T` proves it) and `¬Prov_T(⌜G⌝)` (from `G`), so `T` is inconsistent. So **if `T` is consistent, `T ⊬ G`.**
- Then `G` is true (it says "I am not provable", and indeed it is not). If also `T ⊬ ¬G`, then `G` is independent. Showing `T ⊬ ¬G` needs `T` to be **ω-consistent** (Gödel's original assumption); Rosser (1936) removed this by a modified sentence "if there is a proof of me, there is a shorter proof of my negation".

**Theorem (Gödel 1931, Rosser 1936).** If `T` is consistent, effectively axiomatized and extends `Q`, there is a sentence `G` with `T ⊬ G` and `T ⊬ ¬G`.

#### The second incompleteness theorem

Let `Con_T := ¬Prov_T(⌜⊥⌝)` ("T is consistent"). The proof of the first theorem can be formalized *inside* `T`, giving `T ⊢ Con_T → G`. If `T ⊢ Con_T` then `T ⊢ G`, contradicting the first theorem. So:

**Theorem.** If `T` is consistent (and satisfies the Hilbert-Bernays-Löb derivability conditions), then `T ⊬ Con_T`.

**Löb's theorem.** If `T ⊢ Prov_T(⌜A⌝) → A` then `T ⊢ A`. (A theory cannot prove "if provable then true" for any sentence unless it already proves the sentence.)

#### Related results

| Theorem | Statement |
|---|---|
| **Tarski's undefinability of truth** | there is no arithmetical formula `True(x)` with `ℕ ⊨ True(⌜A⌝) ↔ A` for all sentences `A` |
| **Church-Turing** | validity of FOL is undecidable (6.7.6) |
| **Halting problem** | undecidable |
| **Gödel + Church** | `Th(ℕ)` is not r.e., not even arithmetical |
| **Rosser** | removes the ω-consistency assumption |
| **Gentzen (1936)** | consistency of PA follows from transfinite induction up to the ordinal `ε₀` (a theory beyond PA can prove `Con(PA)`) |
| **Paris-Harrington (1977)** | a natural combinatorial sentence true in ℕ but unprovable in PA |
| **Goodstein's theorem** | true, but unprovable in PA |

#### Common misconceptions (and the correct statement)

| Misconception | Reality |
|---|---|
| "Gödel showed that some truths are unprovable, so mathematics is unreliable." | For *each fixed* consistent effective theory, some arithmetical truths are unprovable *in that theory*. A stronger theory can prove them (and has its own unprovable truths). |
| "G is neither true nor false." | `G` is true in the standard model ℕ (if `T` is consistent). It is unprovable *in T*. |
| "Incompleteness contradicts completeness." | No: they concern different notions (6.7.1). Completeness: `T ⊨ A ⇒ T ⊢ A`. `G` is not a consequence of `T` (true in ℕ, false in some non-standard models of `T`). |
| "Humans can see the truth of G, so minds are not machines." | We see `G` is true *assuming T is consistent*; we have no proof that our own reasoning is consistent. Not a valid argument for non-mechanism (Lucas-Penrose argument is widely rejected). |
| "Incompleteness only affects exotic theories." | It affects every consistent effective theory that interprets basic arithmetic (PA, ZFC), but not, e.g., Presburger arithmetic or the theory of real closed fields. |
| "Therefore everything is relative." | The theorems are precise mathematical statements with hypotheses. |

### 6.7.8 More metatheorems at a glance

| Theorem | Statement | Why it matters |
|---|---|---|
| **Herbrand's theorem** | `∃`-free universal `S` is unsatisfiable iff some finite set of its ground instances is propositionally unsatisfiable | basis of resolution (Chapter 7) |
| **Skolem normal form** | each formula is equisatisfiable with a universal formula in an expanded language | automated reasoning |
| **Cut-elimination (Gentzen's Hauptsatz)** | every LK proof can be converted into a cut-free proof | consistency, subformula property |
| **Craig interpolation** | if `⊨ A → B` there is `I` in the shared vocabulary with `⊨ A → I`, `⊨ I → B` | modularity, verification |
| **Beth definability** | implicit definability implies explicit definability | |
| **Łoś's theorem** | truth in an ultraproduct = truth in "almost all" factors | compactness; nonstandard analysis |
| **Lindström's theorem** | FOL is the strongest logic satisfying both compactness and downward L-S | characterizes FOL |
| **Gödel's β-function lemma** | finite sequences can be coded in arithmetic | arithmetization |
| **Löb's theorem** | `T ⊢ Prov(⌜A⌝) → A` implies `T ⊢ A` | provability logic |
| **Rice's theorem** | every nontrivial semantic property of programs is undecidable | program analysis |
| **Cook-Levin** | SAT is NP-complete | computational complexity |

### 6.7.9 Other logics: a guided tour

You now know classical first-order logic, the "standard" logic. The rest of logic studies variations and extensions. Here is a map with enough detail to start reading.

#### Intuitionistic and substructural logics

| Logic | Change | Idea |
|---|---|---|
| **Intuitionistic** | drop LEM / RAA | truth = constructibility (2.9.8) |
| **Minimal logic** | also drop ex falso | |
| **Linear logic** (Girard 1987) | drop weakening and contraction | formulas are resources used exactly once: `A ⊸ B`, `A ⊗ B`, `!A` |
| **Relevance logic** | demand that premises are relevant to conclusions | avoids `A → (B → A)` paradoxes |
| **Paraconsistent logic** | no explosion | tolerate contradictions without triviality |

#### Many-valued logics

Allow truth values beyond T and F.

**Kleene's strong three-valued logic K₃** (values T, U ("unknown"), F with order F < U < T): `¬` swaps T and F and fixes U; `∧` is the minimum; `∨` the maximum.

| ∧ | T | U | F |
|---|---|---|---|
| **T** | T | U | F |
| **U** | U | U | F |
| **F** | F | F | F |

`A → B` is defined as `¬A ∨ B`. In K₃ there are no tautologies (set every atom to U). **Łukasiewicz's L₃** differs in `U → U = T`, so `A → A` is valid. **Fuzzy logic** uses values in `[0, 1]` with `∧` = min (or product), `∨` = max, `¬x = 1 − x`. **Belnap's four-valued logic** adds "both" for conflicting information.

#### Modal logic

Add operators `□A` ("necessarily A") and `◇A` ("possibly A", defined `¬□¬A`).

**Kripke semantics.** A **frame** is `(W, R)`: a set `W` of "worlds" and an accessibility relation `R ⊆ W × W`. A **model** adds a valuation `V` saying which atoms are true at which worlds. Truth at a world `w`:

| Formula | `M, w ⊨` it iff |
|---|---|
| `p` | `w ∈ V(p)` |
| `¬A`, `A ∧ B`, … | as usual, at `w` |
| `□A` | `M, u ⊨ A` for **every** `u` with `wRu` |
| `◇A` | `M, u ⊨ A` for **some** `u` with `wRu` |

Axioms and the frame conditions they correspond to:

| Axiom | Name | Valid on a frame iff `R` is... |
|---|---|---|
| `□(A → B) → (□A → □B)` | **K** | (all frames) |
| `□A → A` | **T** | reflexive |
| `□A → □□A` | **4** | transitive |
| `A → □◇A` | **B** | symmetric |
| `◇A → □◇A` | **5** | Euclidean (`wRu ∧ wRv ⇒ uRv`) |
| `□A → ◇A` | **D** | serial (`∀w ∃u wRu`) |
| `□(□A → A) → □A` | **GL** (Löb) | transitive and conversely well-founded |

Standard systems: **K**, **T** (= KT), **S4** (= KT4), **S5** (= KT5; `R` an equivalence relation, "all worlds see each other"). Rule: **necessitation**: if `⊢ A` then `⊢ □A`.

Modal logics embed in first-order logic via the **standard translation** `ST(□A, x) = ∀y (R(x, y) → ST(A, y))`, and live in the decidable "guarded" fragment; that is why they are (mostly) decidable. Applications: epistemic logic (`□` = "agent knows"), deontic logic (`□` = "obligatory"), provability logic (`□` = "provable in PA", logic GL), temporal logic, program logics.

**Temporal logic** (LTL: `X` next, `F` eventually, `G` always, `U` until; CTL adds path quantifiers `A`, `E`): specifications for **model checking** hardware and software. **Dynamic logic**: `[a]A` "after every run of program `a`, `A`". **Hoare logic**: `{P} C {Q}` "if `P` holds before command `C`, `Q` holds after". **Separation logic**: reasoning about pointer programs.

#### Higher-order logic and type theory

**Second-order logic** quantifies over sets/relations. With *full semantics* it can characterize ℕ and ℝ up to isomorphism but has no complete proof system and no compactness. **Higher-order logic** and **type theories** (simple type theory, Martin-Löf type theory, the Calculus of Constructions) underlie Isabelle/HOL, Lean, Coq, Agda. In the Curry-Howard view (2.9.8), proofs are programs and propositions are types.

#### Logics for knowledge representation and computation

| Logic | Used for |
|---|---|
| **Description logics** (`ALC`, `SROIQ`) | ontologies (OWL, semantic web); decidable fragments of FOL |
| **Datalog** | database queries: Horn clauses, no function symbols, always terminating |
| **Answer set programming** | nonmonotonic reasoning, default logic |
| **Non-monotonic logic** | conclusions can be retracted when new information arrives |
| **Probabilistic logic, Markov logic** | uncertainty |
| **Fixed-point logics, finite model theory** | database theory, complexity (descriptive complexity: NP = existential second-order logic, Fagin 1974) |

### 6.7.10 Where to go next (study roadmap)

| Goal | Read |
|---|---|
| A rigorous first course in mathematical logic | Enderton, *A Mathematical Introduction to Logic*; or van Dalen, *Logic and Structure* |
| Proof theory | Troelstra & Schwichtenberg, *Basic Proof Theory*; Negri & von Plato, *Structural Proof Theory* |
| Computability and incompleteness | Boolos, Burgess & Jeffrey, *Computability and Logic*; Smith, *An Introduction to Gödel's Theorems* |
| Model theory | Marker, *Model Theory: An Introduction*; Hodges, *A Shorter Model Theory* |
| Set theory | Jech; Kunen |
| Type theory and formalization | *Software Foundations* (Coq); *Theorem Proving in Lean 4*; *Natural Number Game* |
| Automated reasoning | Harrison, *Handbook of Practical Logic and Automated Reasoning*; Robinson & Voronkov (eds.), *Handbook of Automated Reasoning*; Kroening & Strichman, *Decision Procedures*; Biere et al., *Handbook of Satisfiability* |
| Modal logic | Blackburn, de Rijke & Venema, *Modal Logic* |
| Philosophy of logic | Priest, *Introduction to Non-Classical Logic*; Sider, *Logic for Philosophy* |

### 6.7.11 Quick-check (with answers)

**Q1.** State soundness and completeness in one line each, using `⊢` and `⊨`.
**Q2.** Why does the soundness proof for →I use the *semantic deduction theorem*?
**Q3.** What is a maximal consistent set, and why is it useful?
**Q4.** Show, using compactness, that there is no set of first-order sentences whose models are exactly the **finite** graphs.
**Q5.** Is validity of first-order logic decidable? Semi-decidable? Explain the difference.
**Q6.** Which is true: "`G` is true but unprovable in PA" or "`G` is neither true nor false"?
**Q7.** What does it mean for a modal logic to be "S5"? Which frame condition?
**Q8.** Name two decidable fragments of first-order logic.

**Answers.**
**A1.** Soundness: `Γ ⊢ A ⇒ Γ ⊨ A`. Completeness: `Γ ⊨ A ⇒ Γ ⊢ A`.
**A2.** Because the box for →I has assumption `A` and conclusion `B`; the IH is `Γ ∪ {A} ⊨ B`, and the semantic deduction theorem turns it into `Γ ⊨ A → B`.
**A3.** A consistent set `Δ` such that for every formula, either it or its negation belongs to `Δ`. It is useful because its members define a valuation/structure directly (the truth lemma), which gives completeness.
**A4.** Same pattern as 6.7.4 Application 2: add `λₙ` ("at least n vertices"); each finite subset has a finite model; compactness gives an infinite model of a theory that has only finite models.
**A5.** Not decidable (Church-Turing), but semi-decidable: if a sentence is valid a proof-enumerating program eventually finds a proof; if it is not valid, it may run forever.
**A6.** "True but unprovable in PA" (assuming PA is consistent).
**A7.** S5 = KT5: accessibility is an equivalence relation (reflexive, symmetric, transitive); every world sees every world in its class.
**A8.** E.g., monadic first-order logic; the Bernays-Schönfinkel class; the two-variable fragment; the guarded fragment; Presburger arithmetic (a theory).

## Problems for Chapter 6

**6.1 ★** In your own words, explain the difference between A ⊨ B and A → B being a theorem of a proof system. What do soundness and completeness say about the relation between A ⊨ B, A ⊢ B, and ⊢ A → B?

**6.2 ★** Which of the following are true statements of the *metalanguage* and which are formulas of the object language: (a) P → Q; (b) P ⊨ Q; (c) ⊢ P ∨ ¬P; (d) "P ∨ ¬P is a tautology"; (e) ∀x P(x)?

**6.3 ★★** Prove soundness for the rules ∧E, ∨I, and →E: show that if the premises hold in a model, so does the conclusion.

**6.4 ★★** Explain, using the completeness theorem, why the set of valid FOL sentences is **recursively enumerable**. Then explain why a recursively enumerable set need not be decidable, and which direction a prover can answer reliably.

**6.5 ★★★** Use compactness to prove that there is no set of FOL sentences (over the empty signature plus =) whose models are exactly the finite sets. (Hint: let λₙ say "there are at least n elements" and consider {λₙ : n ≥ 1} together with the supposed theory.)

**6.6 ★★★** Use compactness to show there is a model of the true arithmetic of ℕ containing an element larger than every standard natural number.

**6.7 ★★★** Explain why the freshness condition in ∀I is needed for soundness, by giving an explicit **model and assignment** that refutes the invalid inference "from P(a), infer ∀x P(x)" when a is not fresh.

**6.8 ★★★** (Discussion) The statement "ZFC proves that there are uncountably many reals" and "ZFC has a countable model" both hold. Explain why they are not in conflict.

---

# Chapter 7. Automated reasoning: from formulas to resolution

Chapters 2 and 4 taught you to *find proofs by hand*, with insight. This chapter teaches how a **machine** finds proofs with no insight at all, only systematic search. It is also the theory behind the prover you will build in Chapter 8.

## 7.1 The refutation idea

By (F1) of Chapter 1 (and its first-order version), **Γ ⊨ A iff Γ ∪ {¬A} is unsatisfiable**. So a prover does not try to *build* a proof of A. It negates A, adds it to the premises, and tries to derive a **contradiction** (the empty clause). Pipeline:

```
 premises + ¬goal
        │
        ▼
 1. eliminate ↔, →
 2. negation normal form (NNF)
 3. standardize variables apart
 4. Skolemize (remove ∃)
 5. drop ∀, convert to CNF  ──►  a set of clauses
        │
        ▼
 6. resolution with unification, searching for the empty clause □
        │
        ▼
 □ derived  ⇒  premises ⊨ goal      (otherwise: no answer, or ⊭)
```

## 7.2 Propositional resolution and DPLL

A **clause** is a disjunction of literals, written as a set: {P, ¬Q, R} means P ∨ ¬Q ∨ R. The **empty clause** □ is false (a disjunction with no true disjunct). A set of clauses means their conjunction.

**The resolution rule:**

```
   C ∨ A        D ∨ ¬A
  ─────────────────────        (resolvent: C ∨ D)
         C ∨ D
```

It is sound: if both premises are true, then in the valuation either A is true, so D must be true, or A is false, so C must be true; either way C ∨ D holds. (You proved it in Problem 2.17.) Special cases: modus ponens (C empty: from A and ¬A ∨ D get D), and contradiction (A and ¬A give □).

**Example.** Refute {P ∨ Q, ¬P ∨ R, ¬Q ∨ R, ¬R}:

1. P ∨ Q (given)
2. ¬P ∨ R (given)
3. ¬Q ∨ R (given)
4. ¬R (given)
5. Q ∨ R (resolve 1, 2 on P)
6. R (resolve 5, 3 on Q)
7. □ (resolve 6, 4 on R)

Propositional resolution is **complete for refutation**: if the clause set is unsatisfiable, □ is derivable.

**DPLL** is the classic algorithm behind modern SAT solvers:

```
def dpll(clauses):
    clauses = unit_propagate(clauses)      # a clause {l} forces l; simplify everything
    if [] in clauses: return UNSAT         # empty clause: conflict
    if not clauses:   return SAT           # nothing left to satisfy
    l = choose_literal(clauses)
    return dpll(clauses + [[l]]) or dpll(clauses + [[-l]])    # branch
```

Modern solvers add *conflict-driven clause learning* (CDCL), but the skeleton is this. Tseitin's transformation (Chapter 1) lets you feed any formula into such a solver in linear size.

## 7.3 From first-order formulas to clauses

### Step 1-2: eliminate → and ↔, push negations in (NNF)

Exactly as in propositional logic, plus the quantifier rules ¬∀ ≡ ∃¬ and ¬∃ ≡ ∀¬.

### Step 3: standardize variables apart

Rename bound variables so every quantifier binds a distinct variable. Example: ∀x P(x) ∧ ∃x Q(x) becomes ∀x P(x) ∧ ∃y Q(y).

### Step 4: Skolemization (eliminating ∃)

Replace each existentially quantified variable by a **fresh function symbol applied to the universally quantified variables whose scope it lies in** (a *Skolem function*). If no ∀ encloses it, the function has no arguments, i.e., a *Skolem constant*.

| Before | After |
|---|---|
| ∃x P(x) | P(c) |
| ∀x ∃y R(x, y) | ∀x R(x, f(x)) |
| ∃x ∀y R(x, y) | ∀y R(c, y) |
| ∀x ∃y ∀z ∃w S(x, y, z, w) | ∀x ∀z S(x, f(x), z, g(x, z)) |

The dependency structure is exactly the quantifier-order story from Chapters 3-4: in ∀x ∃y the witness may depend on x (so f(x)), in ∃x ∀y it may not (so c).

**Skolemization preserves satisfiability, not equivalence.** A is satisfiable iff its Skolemized form is, but ∃x P(x) and P(c) are not equivalent (P(c) says more: about a specific, named object). This is exactly why the refutation approach works: we only ever ask "is this set unsatisfiable?".

### Step 5: drop universal quantifiers and convert to CNF

After Skolemization, all remaining quantifiers are ∀ (after pulling them out, which is why variables were standardized apart). Drop them, since free variables in clauses are implicitly universal. Convert the matrix to CNF. Each conjunct becomes a clause. **Variables in different clauses are independent** (they are separately universally quantified), so you may rename them freely.

### Worked example: the negated drinker paradox

We want to prove ∃x (D(x) → ∀y D(y)). Negate it and look for a contradiction.

1. ¬∃x (D(x) → ∀y D(y))
2. Push negation: ∀x ¬(D(x) → ∀y D(y)) ≡ ∀x (D(x) ∧ ¬∀y D(y)) ≡ ∀x (D(x) ∧ ∃y ¬D(y))
3. Skolemize y := f(x): ∀x (D(x) ∧ ¬D(f(x)))
4. Clauses: **C₁ = {D(x)}**,  **C₂ = {¬D(f(x))}**

Resolve C₁ with C₂: unify D(x) with D(f(x′)) (after renaming apart): x ↦ f(x′). Result: □. Proved, in one step.

## 7.4 Unification

To resolve {P(x)} against {¬P(f(a))}, we must make the atoms *equal* by substituting for variables. That is **unification**.

A **substitution** θ maps variables to terms. A **unifier** of terms s and t is θ with sθ = tθ. A **most general unifier (MGU)** is a unifier from which every other unifier can be obtained by further substitution. If a unifier exists, an MGU exists and is unique up to renaming of variables.

**Examples:**

| Terms | Result |
|---|---|
| P(x, f(y)) and P(g(z), w) | MGU {x ↦ g(z), w ↦ f(y)} |
| P(x, x) and P(a, b) | **fails** (x = a, then a = b clash of constants) |
| P(x, f(x)) and P(y, y) | **fails**: y = x, then f(x) = x, and x occurs in f(x) (occurs check) |
| R(x, g(x), y) and R(a, z, f(z)) | MGU {x ↦ a, z ↦ g(a), y ↦ f(g(a))} |

**Robinson's algorithm** (sketch):
1. Start with the set of equations {s = t}.
2. Pick an equation:
   - identical terms: delete it;
   - f(s₁..sₙ) = f(t₁..tₙ): replace by s₁ = t₁, ..., sₙ = tₙ;
   - f(...) = g(...) with f ≠ g (or different arity): **fail**;
   - x = t where x is a variable: if x occurs in t (and t ≠ x), **fail (occurs check)**; otherwise substitute x ↦ t in all remaining equations and record it.
3. Repeat until no equations remain.

**The occurs check matters**: without it x ↦ f(x) would create an infinite term and make the prover unsound. (Prolog famously omits it for speed. A theorem prover must not.)

## 7.5 First-order resolution

**Resolution rule with unification.** Given clauses C ∨ A and D ∨ ¬B, where the two clauses have been **renamed apart** (no shared variables) and A, B unify with MGU θ, derive the **resolvent** (C ∨ D)θ.

**Factoring.** If two literals *of the same sign* in one clause unify with MGU θ, derive the clause with θ applied (and the duplicate merged). Factoring is not optional: without it resolution is incomplete (see Example 3 below).

**Theorem (Robinson 1965).** A set of clauses is unsatisfiable iff □ is derivable by resolution and factoring. (Refutation completeness, proven via Herbrand's theorem and lifting propositional resolution.)

### Example 1. Socrates

Clauses: {¬Man(x), Mortal(x)}, {Man(s)}, {¬Mortal(s)}.
Resolve the first two with x ↦ s: {Mortal(s)}. Resolve with the third: □.

### Example 2. ∃x ∀y R(x, y) ⊨ ∀y ∃x R(x, y)

Premise ∃x∀y R(x, y) → {R(c, y)}. Negated conclusion ¬∀y∃x R(x, y) ≡ ∃y∀x ¬R(x, y) → {¬R(x, d)}. Unify R(c, y) with R(x, d): {x ↦ c, y ↦ d}. Result: □. ✔

### Example 2′. The converse fails: ∀y ∃x R(x, y) ⊭ ∃x ∀y R(x, y)

Premise → {R(f(y), y)}. Negated conclusion ¬∃x∀y R(x, y) ≡ ∀x∃y ¬R(x, y) → {¬R(x, g(x))}. Try to resolve: unify R(f(y), y) with R(x, g(x)): x ↦ f(y), then y = g(x) = g(f(y)), which fails the occurs check. No other resolvents exist, the set is **saturated** without □, so (by refutation completeness) it is satisfiable, and the entailment fails. The occurs check *is* the quantifier-order asymmetry.

### Example 3. Why factoring is needed (Russell's barber)

Refute the barber: ∃x ∀y (R(x, y) ↔ ¬R(y, y)). Skolemize x := a: ∀y (R(a, y) ↔ ¬R(y, y)). Split ↔ into two implications:
- R(a, y) → ¬R(y, y), i.e., clause **C₁ = {¬R(a, y), ¬R(y, y)}**
- ¬R(y, y) → R(a, y), i.e., clause **C₂ = {R(y, y), R(a, y)}**

Binary resolution alone on C₁ and C₂ never produces a clause with fewer than two literals, so it can never reach □. Instead *factor*: in C₁, unify R(a, y) with R(y, y) (that is, y ↦ a), giving {¬R(a, a)}. In C₂, unify likewise, giving {R(a, a)}. Resolve the two unit clauses: □. ∎ (This is the same contradiction as Chapter 4, Example 6, found mechanically.)

## 7.6 Search strategy and why provers can run forever

Resolution is *complete* but the search space is huge. Practical provers use a **given-clause loop**:

```
def prove(clauses, limit):
    passive = priority_queue(clauses)     # unprocessed
    active  = []                          # processed
    while passive and within(limit):
        given = passive.pop_best()        # heuristic: shortest/lightest clause first
        if given == EMPTY: return PROVED
        if subsumed_by_any(given, active): continue      # redundancy elimination
        for c in active:
            for r in resolvents(given, c) + factors(given):
                if r == EMPTY: return PROVED
                if not is_tautology(r): passive.add(r)
        active.append(given)
    return UNKNOWN            # *never* "invalid": FOL is only semi-decidable
```

Key ideas used by real provers (Vampire, E, Prover9):
- **Subsumption:** a clause is redundant if a more general (and no longer) clause already exists, e.g. {P(x)} subsumes {P(a), Q}.
- **Tautology deletion** (clauses containing A and ¬A).
- **Set of support:** only resolve using clauses descending from the negated goal (cuts the search, keeps completeness).
- **Ordered resolution:** only resolve on "maximal" literals under a term ordering.
- **Equality:** treated specially (paramodulation / superposition) instead of adding equality axioms.

**Why can't the prover be made to terminate?** Because FOL validity is undecidable (Chapter 6.4). Resolution may generate infinitely many clauses on a satisfiable set, e.g. {P(a)}, {¬P(x), P(f(x))} saturates only in an infinite model. You can only add *resource limits* and report "unknown".

## 7.7 The Herbrand connection (why it works)

For a set S of clauses, the **Herbrand universe** is the set of ground terms built from its constants and function symbols. **Herbrand's theorem:** S is unsatisfiable iff some *finite* set of **ground instances** of its clauses is propositionally unsatisfiable.

**Example.** S = {P(a)}, {¬P(x), P(f(x))}, {¬P(f(f(a)))}. Ground instances with x := a and x := f(a):
- P(a)
- ¬P(a) ∨ P(f(a))
- ¬P(f(a)) ∨ P(f(f(a)))
- ¬P(f(f(a)))

This propositional set is unsatisfiable: P(a) forces P(f(a)), which forces P(f(f(a))), contradicting the last clause. Early provers (Gilmore, Davis-Putnam) literally enumerated ground instances and called a SAT procedure. Resolution with unification does the same job *lazily*, instantiating only as much as needed.

## 7.9 Chapter 7 in complete detail (the from-zero companion)

Chapter 7 explained how a machine proves theorems. This companion widens the picture: **the landscape of automated reasoning tools**, **SAT solving** step by step (with a tested program), a complete **clause-form conversion** example, **unification** traced by hand, **resolution strategies** and **Prolog**, **SMT solvers**, **finite model finding**, and a full **worked puzzle** (the Dreadbury Mansion mystery) from English to proof. Every worked example in this section was checked with an independent solver (Z3).

### 7.9.1 The landscape of automated reasoning

| Family | Problem solved | Typical tools | Strength |
|---|---|---|---|
| **SAT solvers** | is a propositional CNF satisfiable? | MiniSat, CaDiCaL, Kissat, Glucose | millions of variables on structured instances |
| **SMT solvers** | satisfiability modulo theories (arithmetic, arrays, bit-vectors, strings) with quantifiers | Z3, CVC5, Yices, MathSAT | verification, symbolic execution, planning |
| **Automated theorem provers (ATP) for FOL** | is this first-order conjecture a consequence of the axioms? | Vampire, E, SPASS, Prover9, iProver | resolution/superposition, equational reasoning |
| **Model finders** | find a finite model (countermodel) | Mace4, Paradox, Kodkod/Alloy | complements ATPs |
| **Interactive theorem provers (proof assistants)** | human-guided, machine-checked proofs | Lean, Coq/Rocq, Isabelle, Agda, HOL Light | large formalizations (4-colour theorem, Kepler, Feit-Thompson) |
| **Model checkers** | does a finite-state system satisfy a temporal-logic spec? | SPIN, NuSMV, TLA+/TLC | hardware and protocol verification |
| **Logic programming** | run Horn clauses as programs | Prolog, Datalog, ASP | queries, rules |
| **Hybrids ("hammers")** | proof assistant calls ATP/SMT | Sledgehammer (Isabelle), CoqHammer | automation inside interactive proofs |

All of them are built on the ideas in Chapters 1-7: normal forms, refutation, unification, search with pruning.

**Typical architecture of an ATP:** (1) parse; (2) clausify (7.3); (3) saturation loop with a heuristic *given clause* strategy (7.6); (4) output a proof or "unknown/timeout"; (5) optionally check the proof with an independent checker.

**Landmark results found by automated reasoning:** the *Robbins conjecture* (about a variant of Boolean algebra) proved by the equational prover EQP in 1996; the *Boolean Pythagorean triples problem* resolved by SAT solving in 2016 (the natural numbers can be 2-coloured up to 7824 without a monochromatic Pythagorean triple, but not up to 7825; the proof certificate takes about 200 terabytes); formal proofs of the *four-colour theorem* (Gonthier, Coq, 2005) and the *Kepler conjecture* (Flyspeck, HOL Light and Isabelle, 2014).

### 7.9.2 SAT solving in detail

#### The input format: DIMACS CNF

SAT solvers read this plain-text format. Atoms are numbered `1, 2, 3, …`; a negative number is a negated literal; each clause ends with `0`. Example: the clause set `{P ∨ Q, ¬P ∨ R, ¬Q ∨ R, ¬R}` with `P = 1`, `Q = 2`, `R = 3`:

```
c this line is a comment
p cnf 3 4
1 2 0
-1 3 0
-2 3 0
-3 0
```

(`p cnf 3 4` = 3 variables, 4 clauses.) The solver answers `UNSATISFIABLE` here; a satisfiable instance returns `SATISFIABLE` and a line `v 1 -2 3 0` giving a model.

#### Unit propagation and pure literals

- **Unit propagation (BCP):** if a clause has become a single literal `ℓ`, then `ℓ` must be true. Set it, delete every clause containing `ℓ`, and delete `¬ℓ` from the remaining clauses. This may create new unit clauses; repeat.
- **Pure literal rule:** if a variable occurs only positively (or only negatively) in all remaining clauses, set it to make those clauses true.
- **Conflict:** an empty clause appears. This branch is unsatisfiable.

**Trace 1 (no branching needed).** `{P, Q}`, `{¬P, R}`, `{¬Q, R}`, `{¬R}`.

1. `{¬R}` is a unit: set `R = F`. Remove `¬R` clauses (satisfied); delete `R` from `{¬P, R}` and `{¬Q, R}`: now `{P, Q}`, `{¬P}`, `{¬Q}`.
2. `{¬P}` is a unit: `P = F`. `{P, Q}` becomes `{Q}`; `{¬P}` satisfied.
3. `{Q}` and `{¬Q}` are both units: setting `Q = T` turns `{¬Q}` into the empty clause. **Conflict: UNSAT.**

**Trace 2 (satisfiable, one decision).** `{P, Q}`, `{¬P, Q}`, `{P, ¬Q}`.

1. No unit clauses; no pure literals (P and Q both occur in both polarities). **Decide** `P = T`.
2. `{P, Q}` and `{P, ¬Q}` satisfied. `{¬P, Q}` becomes `{Q}`: a unit.
3. `Q = T`. All clauses satisfied. **SAT**, model `P = Q = T`.

#### The DPLL algorithm (Davis-Putnam-Logemann-Loveland, 1960/62)

```
DPLL(clauses):
    repeat unit propagation until no unit clause remains
    if the empty clause is present:  return UNSAT
    apply the pure-literal rule
    if no clauses remain:           return SAT
    choose a literal l (the "decision")
    return DPLL(clauses ∧ l)  or  DPLL(clauses ∧ ¬l)
```

A complete, **tested** Python implementation (clauses are lists of nonzero integers as in DIMACS; the function returns a model as a dictionary, or `None` if unsatisfiable):

```python
def simplify(clauses, lit):
    """Assume `lit` is true: drop satisfied clauses, shrink the others."""
    out = []
    for c in clauses:
        if lit in c:
            continue                          # clause is satisfied
        out.append([l for l in c if l != -lit])
    return out


def dpll(clauses, assignment=None):
    assignment = dict(assignment or {})
    # 1. unit propagation
    while True:
        unit = next((c[0] for c in clauses if len(c) == 1), None)
        if unit is None:
            break
        assignment[abs(unit)] = unit > 0
        clauses = simplify(clauses, unit)
    if any(len(c) == 0 for c in clauses):     # empty clause: conflict
        return None
    # 2. pure literals
    lits = {l for c in clauses for l in c}
    pure = next((l for l in lits if -l not in lits), None)
    while pure is not None:
        assignment[abs(pure)] = pure > 0
        clauses = simplify(clauses, pure)
        lits = {l for c in clauses for l in c}
        pure = next((l for l in lits if -l not in lits), None)
    if not clauses:                           # everything satisfied
        return assignment
    # 3. branch on some literal
    l = clauses[0][0]
    for choice in (l, -l):
        result = dpll(simplify(clauses, choice), {**assignment, abs(choice): choice > 0})
        if result is not None:
            return result
    return None


P, Q, R = 1, 2, 3
print(dpll([[P, Q], [-P, R], [-Q, R], [-R]]))   # None  (unsatisfiable)
print(dpll([[P, Q], [-P, Q], [P, -Q]]))         # {1: True, 2: True}
```

(This program was checked against brute-force truth tables on 2000 random clause sets; variables absent from the returned dictionary are unconstrained.)

#### Beyond DPLL: conflict-driven clause learning (CDCL)

Modern solvers (MiniSat onwards, 2003-) add:

| Technique | Idea |
|---|---|
| **Implication graph** | record which decisions and clauses forced each assigned literal |
| **Conflict analysis, clause learning** | when a conflict occurs, derive a new clause (a resolvent of the clauses involved) that rules out the whole cause, and add it permanently |
| **Non-chronological backjumping** | jump back to the decision level where the learned clause becomes unit, skipping irrelevant decisions |
| **Decision heuristics (VSIDS)** | prefer variables recently involved in conflicts |
| **Restarts** | periodically restart the search, keeping learned clauses |
| **Two-watched-literal scheme** | make unit propagation fast by watching only two literals per clause |
| **Preprocessing, inprocessing** | subsumption, variable elimination, equivalent-literal substitution |

**The deep fact:** a CDCL run that answers UNSAT *is* a resolution proof: every learned clause is obtained by resolution. Unsatisfiability certificates (DRAT proofs) can be checked independently.

#### Encoding problems as SAT

To solve a problem with a SAT solver, encode it as CNF.

**Example: graph colouring.** Variables `c_{v,i}` ("vertex v has colour i"). Clauses: each vertex has at least one colour; (optional) at most one colour; adjacent vertices do not share a colour. For a triangle with 2 colours the clause set is unsatisfiable (a triangle needs 3 colours).

**Example: "exactly one of x₁, …, xₙ"** needs an at-least-one clause `x₁ ∨ … ∨ xₙ` and pairwise at-most-one clauses `¬xᵢ ∨ ¬xⱼ` for `i < j` (that is `n(n−1)/2` clauses; better encodings use auxiliary variables).

**Example: pigeonhole.** `n + 1` pigeons, `n` holes, `pᵢⱼ` = "pigeon i in hole j". Every pigeon is in some hole; no hole has two pigeons. Unsatisfiable, but **every resolution refutation is exponentially long in `n`** (Haken 1985), so resolution-based solvers struggle on it: an example of a gap between "obvious to a human" and "short in the proof system".

**Other applications:** hardware equivalence checking, bounded model checking of software, planning, test generation, cryptanalysis, scheduling, package dependency solving (your package manager may be using a SAT solver), solving Sudoku.

#### Complexity facts

| Problem | Complexity |
|---|---|
| SAT (CNF, any clause length) | NP-complete (Cook-Levin 1971) |
| 3-SAT | NP-complete |
| **2-SAT** | solvable in linear time (implication graph, strongly connected components) |
| **Horn-SAT** (each clause has at most one positive literal) | solvable in linear time (unit propagation) |
| Tautology checking (validity) | coNP-complete |
| QBF (quantified Boolean formulas) | PSPACE-complete |
| Random 3-SAT with clause/variable ratio `r` | easy for `r` small (almost always SAT) and large (almost always UNSAT); hardest near the **phase transition** `r ≈ 4.27` |

### 7.9.3 Clause-form conversion: a complete worked example

**Problem.** Convert to clauses, showing every step, the sentence
`φ = ∀x ( ∃y R(x, y) → ∃z ( R(z, x) ∧ ∀w ¬S(w, z) ) )`.

1. **Eliminate →:** `∀x ( ¬∃y R(x, y) ∨ ∃z ( R(z, x) ∧ ∀w ¬S(w, z) ) )`.
2. **Push negations in (NNF):** `¬∃y R(x, y)` becomes `∀y ¬R(x, y)`:
   `∀x ( ∀y ¬R(x, y) ∨ ∃z ( R(z, x) ∧ ∀w ¬S(w, z) ) )`.
3. **Standardize variables apart:** all binders already use different letters (`x, y, z, w`). ✔
4. **Skolemize** (outermost first). Existentials: `z` lies inside `∀x` only (the `∀y` and `∀w` do not enclose it: they are in separate subformulas). So `z := f(x)`:
   `∀x ( ∀y ¬R(x, y) ∨ ( R(f(x), x) ∧ ∀w ¬S(w, f(x)) ) )`.
5. **Pull out the universal quantifiers** (prenex): `∀x ∀y ∀w ( ¬R(x, y) ∨ ( R(f(x), x) ∧ ¬S(w, f(x)) ) )`. (Valid because the variables are standardized apart.)
6. **Drop the quantifiers; convert the matrix to CNF** (distribute ∨ over ∧):
   `( ¬R(x, y) ∨ R(f(x), x) ) ∧ ( ¬R(x, y) ∨ ¬S(w, f(x)) )`.
7. **Clauses:**
   `C₁ = { ¬R(x, y), R(f(x), x) }`
   `C₂ = { ¬R(x, y), ¬S(w, f(x)) }`

Reading: C₁ says "if x has an R-successor then f(x) is R-related to x". The Skolem function `f` is the witness `z` chosen as a function of `x`.

**Where students go wrong:**

| Mistake | Correction |
|---|---|
| Skolemizing before pushing negations in | do NNF first, otherwise ∃ and ∀ are swapped incorrectly |
| Using a Skolem constant for an `∃` under a `∀` | the witness may depend on the universals above it: use a function |
| Giving an `∃` too many arguments | only the universal variables **whose scope contains** the `∃` count |
| Reusing a Skolem symbol | each ∃ needs a **fresh** symbol (`f₁, f₂, …`) |
| Forgetting to rename clause variables apart | before resolution, the two clauses must share no variables |
| Treating Skolemization as an equivalence | it is only **equisatisfiable** |

**Structure-preserving (definitional) CNF for first-order formulas.** As in the propositional Tseitin transformation (1.8.7), introduce a fresh predicate symbol for a complex subformula to avoid exponential blow-up when distributing ∨ over ∧.

**Miniscoping** pushes quantifiers inward before Skolemization so that Skolem functions get fewer arguments (simpler terms, easier search).

### 7.9.4 Unification traced by hand

#### Substitutions and their composition

A **substitution** is a finite map `θ = {x₁ ↦ t₁, …, xₙ ↦ tₙ}`; `Eθ` applies it simultaneously to every variable of `E`. The **composition** `θσ` is "first θ, then σ": `E(θσ) = (Eθ)σ`. Example: `θ = {x ↦ f(y)}`, `σ = {y ↦ a}`. Then `θσ = {x ↦ f(a), y ↦ a}`: apply σ to the right-hand sides of θ, then add the bindings of σ for variables not already in θ's domain.

A substitution `θ` is **more general** than `σ` if `σ = θτ` for some `τ`. An **MGU** is more general than every other unifier. For `P(x)` and `P(f(y))`: `{x ↦ f(y)}` is an MGU; `{x ↦ f(a), y ↦ a}` is also a unifier but less general.

#### Robinson's algorithm, with a trace

**Unify** `P(x, g(y), z)` with `P(f(w), g(a), h(x))`.

| Step | Equations (to solve) | Action | Substitution so far |
|---|---|---|---|
| 0 | `x = f(w)`, `g(y) = g(a)`, `z = h(x)` | start | `{}` |
| 1 | pick `x = f(w)`: `x` a variable, `x` not in `f(w)` | bind `x ↦ f(w)`, apply to the rest | `{x ↦ f(w)}` |
| | remaining: `g(y) = g(a)`, `z = h(f(w))` | | |
| 2 | `g(y) = g(a)`: same head symbol | decompose into `y = a` | |
| 3 | `y = a`: bind `y ↦ a` | | `{x ↦ f(w), y ↦ a}` |
| 4 | `z = h(f(w))`: `z` not in the term | bind `z ↦ h(f(w))` | `{x ↦ f(w), y ↦ a, z ↦ h(f(w))}` |

Result: the MGU `θ = {x ↦ f(w), y ↦ a, z ↦ h(f(w))}`. Check: `P(x, g(y), z)θ = P(f(w), g(a), h(f(w)))` and `P(f(w), g(a), h(x))θ = P(f(w), g(a), h(f(w)))` ✔.

**Failure cases:**

| Terms | Why it fails |
|---|---|
| `f(x)` and `g(y)` | clash of function symbols |
| `f(x)` and `f(x, y)` | different arities |
| `a` and `b` (constants) | clash |
| `x` and `f(x)` | **occurs check**: no finite term equals a term containing itself |
| `P(x, x)` and `P(a, b)` | `x ↦ a`, then `a = b` clashes |

#### Related notions

| Notion | Description |
|---|---|
| **Matching** (one-way unification) | find θ with `sθ = t`, instantiating only `s` (used in rewriting, subsumption) |
| **Subsumption** | clause `C` subsumes `D` if `Cθ ⊆ D` for some θ |
| **E-unification** | unification modulo equations (associativity, commutativity, ...) |
| **Higher-order unification** | undecidable in general; used in proof assistants |
| **Complexity** | the naive algorithm may take exponential time (terms as trees); with DAG sharing, unification is linear (Paterson-Wegman) |

### 7.9.5 Resolution strategies, refinements and Prolog

Resolution is **complete** but an uninformed search generates enormous numbers of clauses. Strategies restrict the search while keeping (or deliberately sacrificing) completeness.

| Strategy / refinement | Idea | Complete? |
|---|---|---|
| **Binary resolution + factoring** | basic rule (7.5) | yes |
| **Subsumption** (forward and backward) | delete clauses that are instances of existing ones | yes (with fairness) |
| **Tautology deletion** | delete clauses containing `L` and `¬L` | yes |
| **Set of support (SOS)** | resolve only if one parent descends from the negated goal | yes |
| **Unit resolution** | one parent is a unit clause | complete only for Horn clauses |
| **Input resolution** | one parent is an original clause | complete for Horn |
| **Linear resolution / model elimination** | each step uses the previous resolvent | yes |
| **Hyperresolution** | resolve a "nucleus" with several positive "satellites" at once | yes |
| **Ordered resolution** | resolve only on literals maximal in a term ordering | yes |
| **Paramodulation / superposition** | built-in treatment of equality (rewriting) | yes (superposition: refutationally complete for equational FOL) |
| **Demodulation** | simplify clauses by oriented equations | |
| **Selection functions, saturation** | the modern calculus (Bachmair-Ganzinger) behind Vampire/E | yes |

#### Horn clauses and Prolog

A **Horn clause** has at most one positive literal. Three kinds:

| Kind | Form | Reading |
|---|---|---|
| **Fact** (definite, unit) | `P(t)` | `P(t)` holds |
| **Rule** (definite) | `¬A₁ ∨ ⋯ ∨ ¬Aₙ ∨ B`, i.e. `A₁ ∧ ⋯ ∧ Aₙ → B` | if all `Aᵢ` then `B` |
| **Goal / query** (negative) | `¬A₁ ∨ ⋯ ∨ ¬Aₙ` | to prove `A₁ ∧ ⋯ ∧ Aₙ` |

**Prolog** executes by *SLD resolution*: it resolves the current goal with the first matching program clause (top to bottom), depth-first, with backtracking.

```prolog
parent(tom, bob).
parent(bob, ann).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

?- ancestor(tom, ann).      % true
?- ancestor(tom, W).        % W = bob ; W = ann
```

In Prolog `:-` is `←` (read "if"), the comma is `∧`, and variables begin with a capital. The program above is the logic formulas `parent(tom,bob)`, `parent(bob,ann)`, `∀x∀y (parent(x,y) → ancestor(x,y))`, `∀x∀y∀z (parent(x,z) ∧ ancestor(z,y) → ancestor(x,y))`.

**How Prolog differs from a theorem prover:** (1) Horn clauses only; (2) fixed search order (depth-first, left-to-right), so incomplete: a left-recursive rule can loop forever; (3) usually **no occurs check** (for speed), hence unsound in rare cases; (4) negation as failure (`\+`) is not logical negation; (5) built-in arithmetic and side effects. **Datalog** is the terminating subset (no function symbols), the basis of deductive databases.

### 7.9.6 SMT solvers: first-order logic modulo theories

A **theory** fixes the meaning of some symbols (e.g. `+`, `<`, array `select/store`). An **SMT solver** decides satisfiability of formulas mixing Boolean structure with theory atoms.

**DPLL(T):** a SAT solver handles the Boolean skeleton; when it proposes a full assignment to the theory atoms, a **theory solver** checks consistency (e.g. simplex for linear arithmetic; congruence closure for equality with uninterpreted functions; bit-blasting for bit-vectors) and returns a conflict clause if inconsistent.

| Theory | Example atoms | Decidable? |
|---|---|---|
| Equality + uninterpreted functions (EUF) | `f(a) = b` | yes (congruence closure) |
| Linear integer/real arithmetic (LIA, LRA) | `2x + 3y ≤ 7` | yes |
| Non-linear real arithmetic | `x·y > 1` | yes (but expensive) |
| Non-linear integer arithmetic | `x·y = z` | **no** |
| Arrays | `select(store(a, i, v), i) = v` | yes (quantifier-free) |
| Bit-vectors | `x & y = 0` | yes |
| Strings | `len(s) > 3` | partially |

**SMT-LIB** is the standard input language (prefix notation, like Lisp). Satisfiability:

```
(set-logic QF_LIA)
(declare-const x Int)
(declare-const y Int)
(assert (> x 0))
(assert (< y 0))
(assert (= (+ x y) 0))
(check-sat)          ; sat
(get-model)          ; e.g. x = 1, y = -1
```

**To check validity, assert the negation and look for `unsat`:**

```
(declare-const x Int)
(declare-const y Int)
(assert (not (=> (and (> x 0) (> y 0)) (> (+ x y) 0))))
(check-sat)          ; unsat  => the implication is valid
```

**Quantifiers in SMT** are handled heuristically (E-matching, model-based instantiation), so the solver may answer `unknown`.

### 7.9.7 Finding countermodels: finite model search

Resolution proves entailments; to show a **non-entailment** you need a model. **Model finders** (Mace4, Paradox, Kodkod) search for a finite model by encoding the problem in SAT:

1. Fix a domain size `n`, with domain `{0, …, n−1}`.
2. Create a Boolean variable for each ground atom: for a binary predicate `R`, variables `r_{ij}` for `0 ≤ i, j < n`.
3. Replace `∀x A(x)` by `A(0) ∧ ⋯ ∧ A(n−1)` and `∃x A(x)` by `A(0) ∨ ⋯ ∨ A(n−1)`; replace function symbols by relations with functionality clauses.
4. Hand the resulting propositional formula to a SAT solver; a satisfying assignment *is* a model.
5. If none exists, try `n + 1`. Break symmetries (isomorphic relabellings) to prune the search.

**Example.** To refute `∀y ∃x R(x, y) ⊨ ∃x ∀y R(x, y)`, try `n = 1`: with a single element `0`, `R(0,0)` is either true (then both sentences are true) or false (then the premise is false). So there is no countermodel of size 1. Try `n = 2`: choose `R = {(0,0), (1,1)}`. Premise `∀y ∃x R(x, y)`: for `y = 0` take `x = 0`; for `y = 1` take `x = 1`. ✔. Conclusion `∃x ∀y R(x, y)`: for `x = 0`, `R(0, 1)` fails; for `x = 1`, `R(1, 0)` fails. ✘. So this 2-element structure is a **countermodel**. (Z3 also finds one.)

**Limits.** Finite model search is complete for finite satisfiability but not for sentences that have *only* infinite models (3.5). A prover/model-finder pair running in parallel is a standard combination: either proves or refutes most "small" problems.

### 7.9.8 A complete worked puzzle: the Dreadbury Mansion mystery

This is a classic benchmark (Pelletier's problem 55) that every first-order prover can solve in milliseconds.

> Someone who lives in Dreadbury Mansion killed Aunt Agatha. Agatha, the butler, and Charles live in Dreadbury Mansion, and are the only people who live there. A killer always hates his victim, and is never richer than his victim. Charles hates no one that Aunt Agatha hates. Agatha hates everyone except the butler. The butler hates everyone not richer than Aunt Agatha. The butler hates everyone Agatha hates. No one hates everyone. Agatha is not the butler. **Who killed Agatha?**

#### Step 1: Signature

Constants `a` (Agatha), `b` (butler), `c` (Charles). Unary predicate `Lives(x)`. Binary predicates `Killed(x, y)`, `Hates(x, y)`, `Richer(x, y)`.

#### Step 2: Formalization

| # | English | Formula |
|---|---|---|
| 1 | Someone living there killed Agatha | `∃x (Lives(x) ∧ Killed(x, a))` |
| 2 | Agatha, the butler and Charles live there | `Lives(a) ∧ Lives(b) ∧ Lives(c)` |
| 3 | They are the only residents | `∀x (Lives(x) → (x = a ∨ x = b ∨ x = c))` |
| 4 | A killer hates his victim | `∀x ∀y (Killed(x, y) → Hates(x, y))` |
| 5 | A killer is never richer than the victim | `∀x ∀y (Killed(x, y) → ¬Richer(x, y))` |
| 6 | Charles hates no one Agatha hates | `∀x (Hates(a, x) → ¬Hates(c, x))` |
| 7 | Agatha hates everyone except the butler | `∀x (x ≠ b → Hates(a, x))` |
| 8 | The butler hates everyone not richer than Agatha | `∀x (¬Richer(x, a) → Hates(b, x))` |
| 9 | The butler hates everyone Agatha hates | `∀x (Hates(a, x) → Hates(b, x))` |
| 10 | No one hates everyone | `∀x ∃y ¬Hates(x, y)` |
| 11 | Agatha is not the butler | `a ≠ b` |

**Goal:** `Killed(a, a)`.

#### Step 3: The human proof

By (1), (2), (3) the killer is one of `a`, `b`, `c`.

- **Charles is not the killer.** Suppose `Killed(c, a)`. By (4) `Hates(c, a)`. By (7), since `a ≠ b` (11), `Hates(a, a)`. By (6) with `x := a`: `Hates(a, a) → ¬Hates(c, a)`. So `¬Hates(c, a)`. Contradiction.
- **The butler is not the killer.** Suppose `Killed(b, a)`. By (5) `¬Richer(b, a)`. Take any object `y`. If `y = b`: by (8) (`¬Richer(b, a)` holds) `Hates(b, b)`. If `y ≠ b`: by (7) `Hates(a, y)` and by (9) `Hates(b, y)`. So the butler hates **everybody**, contradicting (10) with `x := b`.
- Hence **Agatha killed herself**. ∎

(Note where (11) is used: in the Charles case. Without it the axioms would not entail the conclusion; Z3 confirms that dropping `a ≠ b` makes the problem satisfiable with a different killer.)

#### Step 4: Give it to a prover (Prover9 syntax)

```
formulas(assumptions).
  exists x (Lives(x) & Killed(x, agatha)).
  Lives(agatha). Lives(butler). Lives(charles).
  all x (Lives(x) -> (x = agatha | x = butler | x = charles)).
  all x all y (Killed(x, y) -> Hates(x, y)).
  all x all y (Killed(x, y) -> -Richer(x, y)).
  all x (Hates(agatha, x) -> -Hates(charles, x)).
  all x (x != butler -> Hates(agatha, x)).
  all x (-Richer(x, agatha) -> Hates(butler, x)).
  all x (Hates(agatha, x) -> Hates(butler, x)).
  all x exists y -Hates(x, y).
  agatha != butler.
end_of_list.

formulas(goals).
  Killed(agatha, agatha).
end_of_list.
```

(In Prover9, `&`, `|`, `->`, `-` are ∧, ∨, →, ¬; `all`/`exists` are quantifiers; identifiers starting with `u`..`z` are variables, the others constants.) The prover negates the goal, clausifies everything (Skolemizing 1 and 10), and finds the refutation almost instantly.

#### Step 5: What the clauses look like

Skolemize (1) with constant `k` and (10) with a function `g`:

```
{Lives(k)}                     {Killed(k, agatha)}
{¬Lives(x), x = agatha, x = butler, x = charles}
{¬Killed(x, y), Hates(x, y)}   {¬Killed(x, y), ¬Richer(x, y)}
{¬Hates(agatha, x), ¬Hates(charles, x)}
{x = butler, Hates(agatha, x)}
{Richer(x, agatha), Hates(butler, x)}
{¬Hates(agatha, x), Hates(butler, x)}
{¬Hates(x, g(x))}              {agatha ≠ butler}
{¬Killed(agatha, agatha)}      (negated goal)
```

Each human case above becomes a short resolution/paramodulation derivation.

### 7.9.9 One more resolution proof: reflexivity from symmetry, transitivity and seriality

Show: `∀x ∀y (R(x,y) → R(y,x))`, `∀x ∀y ∀z ((R(x,y) ∧ R(y,z)) → R(x,z))`, `∀x ∃y R(x,y)` ⊨ `∀x R(x,x)`.

*Clauses.*
`C₁ = {¬R(x, y), R(y, x)}` (symmetry)
`C₂ = {¬R(x, y), ¬R(y, z), R(x, z)}` (transitivity)
`C₃ = {R(x, f(x))}` (seriality, Skolemized)
`C₄ = {¬R(c, c)}` (negated goal: `¬∀x R(x,x)` Skolemized with constant `c`)

*Derivation.*

| Step | Resolve | Unifier | Resolvent |
|---|---|---|---|
| 5 | `C₃` with `C₁` (on `R(x,f(x))` vs `¬R(x′,y′)`) | `x′ ↦ x`, `y′ ↦ f(x)` | `C₅ = {R(f(x), x)}` |
| 6 | `C₃` with `C₂` (first literal) | `x′ ↦ x`, `y′ ↦ f(x)` | `C₆ = {¬R(f(x), z), R(x, z)}` |
| 7 | `C₆` with `C₅′` (a renamed copy `R(f(x′), x′)`) | `z ↦ x′`, `x ↦ x′` | `C₇ = {R(x′, x′)}` |
| 8 | `C₇` with `C₄` | `x′ ↦ c` | `□` |

Reading: from "everything has an R-successor f(x)" and symmetry we get `R(f(x), x)`; transitivity then yields `R(x, x)`, contradicting the negated goal. (Z3 independently confirms the entailment.) Compare with the natural-deduction proof you construct in Problem 4.17: the same idea, a different format.

### 7.9.10 Quick-check (with answers)

**Q1.** What does the DIMACS line `-3 1 0` mean?
**Q2.** Run unit propagation on `{A, B}`, `{¬A}`, `{¬B, C}`. What happens?
**Q3.** Skolemize `∀x ∃y ∀z ∃w S(x, y, z, w)`.
**Q4.** Find an MGU of `Q(f(x), y)` and `Q(z, g(a))`.
**Q5.** Why does Prolog usually omit the occurs check, and what can go wrong?
**Q6.** True or false: a Horn clause set is satisfiable iff unit propagation does not derive the empty clause.
**Q7.** Why must the SAT solver answer for a *validity* question be read as "unsat means valid"?
**Q8.** In the Dreadbury puzzle, which axiom rules out Charles as the killer, and which fact is needed to apply it?

**Answers.**
**A1.** The clause `¬x₃ ∨ x₁`.
**A2.** `{¬A}` is a unit: `A = F`. Then `{A, B}` becomes `{B}`: unit, `B = T`. Then `{¬B, C}` becomes `{C}`: unit, `C = T`. All clauses satisfied: SAT with `A = F, B = T, C = T`.
**A3.** `∀x ∀z S(x, f(x), z, g(x, z))`.
**A4.** `{z ↦ f(x), y ↦ g(a)}`.
**A5.** For speed: checking `x ∈ t` costs time. Without it, `X = f(X)` "succeeds" by creating a cyclic term, so the answer can be unsound (and the program may loop).
**A6.** True: unit propagation is complete for Horn clauses (Horn-SAT is solved by it).
**A7.** Because `Γ ⊨ A` iff `Γ ∪ {¬A}` is unsatisfiable (F1): asserting the negated goal and getting UNSAT means the goal follows.
**A8.** Axiom 6 (Charles hates no one Agatha hates), applied with `x := a`; it needs `Hates(a, a)`, which comes from axiom 7 and `a ≠ b`.

## Problems for Chapter 7

**7.1 ★★** Convert to clause form (show Skolemization):
- (a) ∀x (P(x) → Q(x))
- (b) ∃x ∀y R(x, y)
- (c) ∀x ∃y (P(x) → Q(y)) ∧ ∃x ∀y R(x, y)
- (d) ¬∀x (P(x) → ∃y R(x, y))

**7.2 ★★** Find an MGU or show none exists:
- (a) P(x, f(y)) and P(g(z), w)
- (b) P(x, x) and P(a, b)
- (c) P(x, f(x)) and P(y, y)
- (d) R(x, g(x), y) and R(a, z, f(z))
- (e) Q(f(x), g(y)) and Q(f(h(a)), g(x))

**7.3 ★★** Prove by resolution: ∀x (P(x) → Q(x)), ∀x (Q(x) → R(x)), P(a) ⊨ R(a).

**7.4 ★★** Prove by resolution: ∀x (P(x) → Q(x)), ∃x P(x) ⊨ ∃x Q(x).

**7.5 ★★** Prove the propositional resolution rule is sound: if C ∨ A and D ∨ ¬A are both true under a valuation, so is C ∨ D.

**7.6 ★★★** Show by resolution that ∀y ∃x R(x, y) ⊭ ∃x ∀y R(x, y), i.e., show that the clause set saturates with no empty clause, and say which unification step fails.

**7.7 ★★★** Prove the drinker paradox ∃x (D(x) → ∀y D(y)) by resolution from scratch. Then prove Russell's barber, observing where factoring is needed.

**7.8 ★★★** Explain why Skolemization preserves satisfiability but not equivalence. Give an explicit example of a formula φ with φ_Sk ⊭ φ or φ ⊭ φ_Sk, and a model-theoretic sketch of why φ satisfiable ⇒ φ_Sk satisfiable.

**7.9 ★★★** Consider the clause set {P(a)}, {¬P(x), P(f(x))}, {¬P(f(f(f(a))))}. Using Herbrand's theorem, list a finite set of ground instances that is propositionally unsatisfiable. How many instances of the second clause are needed? Then refute the set by first-order resolution and compare how many steps each approach takes.

---

# Chapter 8. Project: build your own logic engine

Building the engine is not a side activity: it is the most efficient way to *test* your understanding. You cannot implement ∀-introduction without understanding freshness, or capture-avoiding substitution without understanding free and bound variables.

## 8.1 Goal and scope

**Goal:** a program in which you can state a theorem in predicate logic and either (a) **check** a proof you wrote step by step, (b) build a proof **interactively** with goal-directed tactics, or (c) ask the machine to **find** a proof automatically, or a countermodel.

**Recommended languages:** any language with algebraic data types and pattern matching.
- *Python 3.10+* with dataclasses and `match` is the fastest for prototyping.
- *Java 21* (sealed interfaces, records, pattern-matching switch) gives you a typed and compiler-checked AST. Kotlin, Scala, Rust, Haskell, OCaml are also excellent.
- Go works too but lacks sum types, so the AST code is more verbose.

I recommend prototyping the whole stack in Python first, then (optionally) rewriting the **kernel** (the proof checker) in a typed language.

## 8.2 Architecture

```
   ┌──────────────────────────── UI / CLI / web ─────────────────────────────┐
   │                                                                          │
   │  Tactics layer (intro, apply, cases, exists, ...)      Automated prover  │
   │            │                                    (NNF → Skolem → CNF →     │
   │            ▼                                     unification → resolution)│
   │   Proof objects (Fitch-style derivations)                    │           │
   │            │                                                 │           │
   │            ▼                                                 ▼           │
   │   ┌────────────────────────────────────┐        ┌──────────────────────┐ │
   │   │   KERNEL: proof checker (small,    │        │  Semantics:           │ │
   │   │   trusted, ~300 lines)             │        │  finite models,       │ │
   │   └────────────────────────────────────┘        │  countermodel finder  │ │
   │            │                                    └──────────────────────┘ │
   │            ▼                                                 │           │
   │   Core: AST, parser/printer, free vars, substitution, alpha-equivalence ◄┘ │
   └──────────────────────────────────────────────────────────────────────────┘
```

**The LCF principle.** Only the kernel can create "theorems". Everything above it (tactics, automation) may be buggy or heuristic, but if it ever produces a proof, the kernel re-checks it. This is the architecture of Lean, Coq/Rocq and Isabelle, and it is why you can trust their output.

## 8.3 Milestones

Each milestone ends with tests. **Do not move on until the tests pass.**

### M1. Syntax: AST, parser, pretty-printer
- Define terms and formulas (Section 8.4).
- Concrete syntax suggestion (ASCII, easy to type):
  `~A`, `A & B`, `A | B`, `A -> B`, `A <-> B`, `forall x. A`, `exists x. A`, `s = t`, `P(x, f(y))`.
- Use **precedence climbing** or a Pratt parser. Implication is right-associative. Quantifiers extend as far right as possible.
- **Tests:** `parse(pretty(f)) == f` for random formulas (property-based testing with `hypothesis`); precedence cases like `a & b | c`, `p -> q -> r`.

### M2. Core operations: free variables, substitution, alpha-equivalence
- `free_vars(f)`, `bound_vars(f)`.
- **Capture-avoiding substitution** `subst(f, x, t)`.
- `alpha_eq(f, g)`: equality up to renaming of bound variables.
- **Tests:** the classic capture case (∃y L(x, y))[y/x] must return a formula alpha-equivalent to ∃y′ L(y, y′), never ∃y L(y, y). Substitution lemmas: if x ∉ FV(f) then `subst(f, x, t) == f`.

### M3. Semantics: model evaluator and countermodel finder
- A finite structure: domain `{0..n-1}`, interpretations for constants, functions (tables), predicates (sets of tuples).
- `eval(formula, structure, assignment)` by recursion on the formula, expanding quantifiers over the domain.
- **Countermodel finder:** for n = 1, 2, 3, ..., enumerate all structures over the formula's signature (feasible for small signatures), check premises true and conclusion false.
- **Tests:** reproduce every claim of Problems 3.7 and 3.8 mechanically: (b), (d), (e), (h) have countermodels; (a), (c), (f), (g) do not (up to size n you test).

### M4. Propositional engine
- Truth table evaluator, tautology and satisfiability check by brute force.
- Convert to NNF and CNF; Tseitin variant.
- DPLL solver on CNF.
- **Tests:** on random formulas with ≤ 8 atoms, DPLL agrees with brute force, CNF conversion preserves equivalence.

### M5. Proof checker (the kernel)
This is the heart of the project. See Section 8.5 for design.
- Parse Fitch-style proofs (use the same layout as this course, so every worked example is a test case).
- Check every rule, including scope of sub-proofs and the **freshness conditions** of ∀I and ∃E.
- **Tests (critical):**
  - *accept* every worked proof in Chapters 2 and 4;
  - *reject* the "bad" proofs of Section 4.2 and Problem 4.20, with an error message naming the violated condition;
  - *reject* proofs that use lines from closed sub-proofs, wrong line references, mismatched formulas, ∨E with branches that end in different formulas.

### M6. Tactics and interactive mode (proof assistant)
- State: a list of **goals**, each = (context of hypotheses, target formula).
- Tactics transform goals and *emit proof fragments*: `intro` (→I, ∀I), `split` (∧I), `left`/`right` (∨I), `apply` (→E, ∀E), `cases` (∨E, ∃E), `exists t` (∃I), `by_contra` (RAA), `exact h`, `contradiction`.
- When all goals are closed, assemble the final Fitch proof and hand it to the kernel for checking.
- **Tests:** re-prove the worked examples by tactic scripts and check that the generated proofs pass the kernel.

### M7. Automated FOL prover (resolution)
- NNF, standardization of variables, Skolemization, CNF, clause set (Chapter 7).
- Unification with occurs check.
- Binary resolution + factoring in a given-clause loop, with subsumption, tautology deletion, and a time/clause limit.
- **Tests:** Socrates, ∃∀ ⊨ ∀∃ (proved), ∀∃ ⊭ ∃∀ (saturates), drinker, barber, and the classic **Pelletier problems** (75 small FOL problems used to benchmark provers, graded in difficulty).
- **Soundness cross-check:** if the prover proves φ, the model finder (M3) must find no countermodel; if the model finder finds a countermodel, the prover must not prove φ.

### M8. Equality, proof output, and cross-checking
- Equality via axioms (reflexivity, symmetry, transitivity, congruence) at first, later paramodulation.
- Make the prover emit a **resolution proof log**. Optional advanced goal: translate it into a kernel-checkable natural deduction proof (hard, but a rewarding research-flavoured exercise).
- Compare against **Z3** (`pip install z3-solver`), **Prover9**, **Vampire**, or **E**. Import problems from the **TPTP** library (the standard format for first-order benchmark problems).

### M9. Usability and polish
- Better error messages ("∀I: name `a` occurs in open assumption at line 3").
- A web or terminal UI that renders proofs in Fitch style, a problem library with the exercises of this course, and export to Lean 4 or LaTeX.

## 8.4 Core data structures (Python)

```python
from __future__ import annotations
from dataclasses import dataclass
from itertools import count

# ---------- Terms ----------
@dataclass(frozen=True)
class Var:
    name: str

@dataclass(frozen=True)
class Fn:                      # constants are Fn with no arguments
    name: str
    args: tuple = ()

# ---------- Formulas ----------
@dataclass(frozen=True)
class Pred:
    name: str
    args: tuple = ()

@dataclass(frozen=True)
class Not:     f: object
@dataclass(frozen=True)
class And:     l: object; r: object
@dataclass(frozen=True)
class Or:      l: object; r: object
@dataclass(frozen=True)
class Implies: l: object; r: object
@dataclass(frozen=True)
class Iff:     l: object; r: object
@dataclass(frozen=True)
class Forall:  var: str; body: object
@dataclass(frozen=True)
class Exists:  var: str; body: object
@dataclass(frozen=True)
class Eq:      l: object; r: object
@dataclass(frozen=True)
class Bottom:  pass
```

**Free variables:**

```python
def free_vars(x) -> set[str]:
    match x:
        case Var(n):                       return {n}
        case Fn(_, args) | Pred(_, args):  return set().union(*map(free_vars, args))
        case Eq(l, r) | And(l, r) | Or(l, r) | Implies(l, r) | Iff(l, r):
            return free_vars(l) | free_vars(r)
        case Not(f):                       return free_vars(f)
        case Forall(v, b) | Exists(v, b):  return free_vars(b) - {v}
        case Bottom():                     return set()
```

**Capture-avoiding substitution** `x[t/v]` (the single most bug-prone function in the project):

```python
_fresh = count()
def fresh(base: str) -> str:
    return f"{base}_{next(_fresh)}"

def subst(x, v: str, t):
    match x:
        case Var(n):          return t if n == v else x
        case Fn(f, args):     return Fn(f, tuple(subst(a, v, t) for a in args))
        case Pred(p, args):   return Pred(p, tuple(subst(a, v, t) for a in args))
        case Eq(l, r):        return Eq(subst(l, v, t), subst(r, v, t))
        case Not(f):          return Not(subst(f, v, t))
        case And(l, r):       return And(subst(l, v, t), subst(r, v, t))
        case Or(l, r):        return Or(subst(l, v, t), subst(r, v, t))
        case Implies(l, r):   return Implies(subst(l, v, t), subst(r, v, t))
        case Iff(l, r):       return Iff(subst(l, v, t), subst(r, v, t))
        case Bottom():        return x
        case Forall(n, body) | Exists(n, body):
            ctor = type(x)
            if n == v:                                  # v is bound here: nothing to replace
                return x
            if n in free_vars(t) and v in free_vars(body):
                n2 = fresh(n)                           # rename the bound variable to avoid capture
                body = subst(body, n, Var(n2))
                n = n2
            return ctor(n, subst(body, v, t))
```

**Unification** (works for terms and atoms, since both have `.name` and `.args`; the substitution is kept in *triangular* form, so apply it with `walk` recursively):

```python
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

def apply(s, t):
    t = walk(t, s)
    if isinstance(t, Var):
        return t
    return type(t)(t.name, tuple(apply(s, a) for a in t.args))
```

**Resolution** (clauses are frozensets of `(positive?, atom)` literals):

```python
_ids = count()

def rename_apart(clause):
    suffix = f"#{next(_ids)}"            # globally unique, so repeated renaming never clashes
    def rt(t):
        if isinstance(t, Var):
            return Var(t.name + suffix)
        return type(t)(t.name, tuple(rt(a) for a in t.args))
    return frozenset((sign, rt(atom)) for sign, atom in clause)

def resolvents(c1, c2):
    c2 = rename_apart(c2)
    for (s1, a1) in c1:
        for (s2, a2) in c2:
            if s1 != s2:
                theta = unify(a1, a2)
                if theta is not None:
                    rest = (c1 - {(s1, a1)}) | (c2 - {(s2, a2)})
                    yield frozenset((s, apply(theta, a)) for s, a in rest)

def factors(c):
    lits = list(c)
    for i, (s1, a1) in enumerate(lits):
        for (s2, a2) in lits[i + 1:]:
            if s1 == s2:
                theta = unify(a1, a2)
                if theta is not None:
                    yield frozenset((s, apply(theta, a)) for s, a in c)
```

(A real implementation adds subsumption, tautology checks, variable normalization to keep clause sets finite up to renaming, and resource limits.)

**Java 21 alternative** for the AST:

```java
sealed interface Formula permits Pred, Not, And, Or, Implies, Iff, Forall, Exists, Eq, Bottom {}
record Pred(String name, List<Term> args) implements Formula {}
record Not(Formula f) implements Formula {}
record And(Formula l, Formula r) implements Formula {}
// ...
record Forall(String var, Formula body) implements Formula {}
```
with `switch` pattern matching giving you exhaustiveness checking from the compiler. If you forget a case when writing `subst`, it will not compile.

## 8.5 Designing the proof checker (the kernel)

**Representation.** A proof is a tree of **blocks**. A block has an optional *opening* (an assumption formula, or a fresh-name introduction, or both for ∃E) and a list of *items*, each of which is a line or a nested block. A line is `(formula, rule, references)`.

**Scope rule.** When checking a line, the lines it may cite are exactly those in the same block or in enclosing blocks, appearing earlier. A *block* may be cited as a whole (a range) by →I, ¬I, RAA, ∨E, ∀I, ∃E. Implement this with a stack of scopes as you traverse the proof.

**Per-rule check = pattern match + side condition.** Each rule is a small function `check_rule(line, cited_lines) -> None | error`. For example:

```text
→E:    cited lines: φ and ψ.  Require ψ == Implies(φ, line.formula)         (modulo alpha-equivalence)
→I:    cited block: opens with assumption φ, last line ψ.  Require line.formula == Implies(φ, ψ)
∨E:    cited: line (φ ∨ ψ), block opening φ ending χ, block opening ψ ending χ'.
       Require χ == χ' == line.formula
∀E:    cited: ∀x φ.   Require line.formula == subst(φ, x, t) for some term t that is free for x in φ.
       (Simplest: try t = every term occurring in the conclusion; or require the user to give t.)
∃I:    cited: φ[t/x].  Require line.formula == ∃x φ for some t. (Ask the user for t, or search.)
∀I:    cited block: opens with fresh name a (no assumption), ends with φ(a).
       Require line.formula == ∀x ψ where ψ[a/x] == φ(a), and
         a does not occur in: any premise, any assumption of an ENCLOSING open block, or ∀x ψ.
∃E:    cited: ∃x ψ at line i; block opening ψ[a/x] with name a, ending χ.
       Require line.formula == χ, and
         a does not occur in: ∃x ψ, χ, any premise, any assumption of an enclosing open block.
RAA:   cited block: opens with ¬φ, ends ⊥.  Require line.formula == φ.
```

**The side conditions are the most valuable lines of code in the project.** Write them, test them with the bad proofs of Section 4.2, and you will never again confuse a legal ∀I with an illegal one.

**Comparing formulas.** Use `alpha_eq`, not `==`, wherever formulas are matched (a substitution may rename bound variables).

**Error reporting.** Return structured errors: line number, rule, which condition failed. Good error messages are what turn the checker into a teaching tool.

## 8.6 Testing strategy

- **Golden tests:** every worked proof in this course (as Fitch text) must be accepted. Every "bad proof" must be rejected for the *right reason*.
- **Property-based tests** (`hypothesis`, QuickCheck, jqwik): parse/print round-trip, CNF equivalence, substitution laws, DPLL agrees with brute force.
- **Differential tests:** compare your prover/model finder to Z3 on random small formulas. Any disagreement is a bug somewhere (and finding which side is wrong teaches a lot).
- **Soundness cross-check:** as in M7.
- **Benchmarks:** Pelletier's 75 problems; TPTP problems from the PUZ (puzzles) and SYN (syntactic) domains.

## 8.7 Extensions

- Sequent calculus and **tableaux** provers (an alternative to resolution that is easier to turn into readable proofs).
- A small **dependently typed** kernel (Curry-Howard in practice): implement the simply-typed λ-calculus, then Π-types.
- **SMT-style** theory reasoning: congruence closure for equality, then linear arithmetic.
- **Modal and temporal logic** model checker (LTL/CTL), useful for verifying real systems.
- A **Lean 4** exporter, or a verified kernel in Lean itself.

## 8.8 Chapter 8 in complete detail: the starter kit

Sections 8.1–8.7 describe *what* to build. This section hands you a **working, tested reference implementation** of the hardest milestones, so that you can read real code, break it on purpose, and then write your own better version. It is deliberately small (one Python file, no dependencies) and deliberately incomplete: tactics, paramodulation and a user interface are left as your exercises.

The two files are:

- `logic_engine_starter.py` — the engine (about 1,500 lines including comments and blank lines).
- `test_starter.py` — 2,520 automated checks. Run it with `python3 test_starter.py`; it should end with `all 2520 checks passed`.

Both ship alongside this document. Requirement: Python 3.10 or newer, because the code uses `match` statements (structural pattern matching).

### 8.8.1 What is inside, milestone by milestone

| Milestone | Functions you will find | What it demonstrates |
| --- | --- | --- |
| M1 Syntax | `parse`, `pretty`, `tokenize`, the dataclasses `Var Fn Pred Not And Or Implies Iff Forall Exists Eq Bottom` | Recursive-descent parsing with precedence; an immutable AST; `parse(pretty(f)) == f` |
| M2 Substitution | `free_vars`, `subst`, `fresh_var`, `alpha_eq` | Capture-avoiding substitution; equality up to renaming of bound variables |
| M3 Semantics | `Structure`, `holds`, `signature`, `structures`, `find_countermodel` | Tarski's definition executed literally over finite domains; refuting invalid arguments |
| M4 Propositional | `truth_table`, `is_tautology`, `elim_arrows`, `nnf`, `nnf_to_clauses`, `tseitin`, `dpll`, `sat` | The whole SAT pipeline, from formula to model |
| M5 Kernel | `check_proof`, `ProofError` | A Fitch proof checker with scoping and freshness conditions |
| M7 Prover | `clausify`, `skolemize`, `unify`, `resolvents`, `factors`, `subsumes`, `prove` | Resolution refutation with a given-clause loop |

Milestones M6 (tactics), M8 (equality by paramodulation) and M9 (user interface) are *not* implemented. `prove` can handle equality only by adding explicit equality axioms (`with_equality=True`), which is slow and incomplete in practice — that weakness is the motivation for M8.

### 8.8.2 The input language

The parser accepts ASCII and Unicode interchangeably.

| Meaning | ASCII | Unicode also accepted |
| --- | --- | --- |
| not | `~P` | `¬P` |
| and | `P & Q` | `P ∧ Q` |
| or | `P \| Q` | `P ∨ Q` |
| implies | `P -> Q` | `P → Q`, `P ⇒ Q` |
| iff | `P <-> Q` | `P ↔ Q`, `P ⇔ Q` |
| false | `false` | `⊥` |
| for all | `forall x. P(x)` | `∀x P(x)` |
| exists | `exists x. P(x)` | `∃x P(x)` |
| equals, not equals | `a = b`, `a != b` | `a ≠ b` |

Two conventions you must know, because they decide how input is read:

1. **Variables versus constants.** An identifier that starts with one of the letters `u v w x y z` is a *variable*. Every other identifier (`a`, `socrates`, `f`, `P`) is a constant, function or predicate symbol. This mirrors the usual textbook convention (Section Z4.8) and keeps the grammar simple.
2. **Quantifier scope.** `forall x. A` (with a dot) extends *as far right as possible*. `∀x A` (no dot) binds tightly, like `~`. So `forall x. P(x) -> Q(x)` is `∀x (P(x) → Q(x))`, while `∀x P(x) → Q` is `(∀x P(x)) → Q`.

Precedence from loosest to tightest: `<->`, then `->` (right-associative), then `|`, then `&`, then `~` and quantifiers.

### 8.8.3 Using it from the command line

```text
$ python3 logic_engine_starter.py parse 'forall x. P(x) -> exists y. R(x,y)'
forall x. P(x) -> (exists y. R(x, y))
Forall(var='x', body=Implies(l=Pred(name='P', ...), r=Exists(var='y', ...)))
```

The pretty-printer adds parentheses around the inner quantifier. That is harmless and safe: printing never has to guess how far a quantifier reaches.

```text
$ python3 logic_engine_starter.py prove 'forall x. (H(x) -> M(x))' 'H(socrates)' '|-' 'M(socrates)'
proved
  1. {~H(x_0), M(x_0)}                             input
  2. {H(socrates)}                                 input
  3. {M(socrates)}                                 resolve
  4. {~M(socrates)}                                input
  5. []                                            resolve
```

Read this as a resolution proof (Section 7.9.9). Lines 1, 2 and 4 are the clauses of the premises and of the *negated* goal. Line 3 resolves lines 1 and 2 (unifier `x_0 ↦ socrates`). Line 5 resolves 3 and 4 and produces the empty clause `[]`: a contradiction, so the argument is valid.

```text
$ python3 logic_engine_starter.py countermodel 'exists x. P(x)' '|-' 'forall x. P(x)'
D = [0, 1]; P = [(1,)]
```

A two-element world where something is `P` (element 1) but not everything is. This is exactly the semantic refutation you learned in Chapter 3.

```text
$ python3 logic_engine_starter.py prove 'forall x. exists y. R(x,y)' '|-' 'exists y. forall x. R(x,y)'
saturated
```

This is the classic invalid quantifier swap. The prover returns `saturated`: it ran out of new clauses without finding the empty clause. For a *finite, saturated* clause set that means the set is satisfiable, i.e. the argument is invalid. The prover never says "invalid" outright, because in general first-order validity is only semi-decidable (Section 6.7.6); `limit` means "I gave up", which tells you nothing.

### 8.8.4 Walking through the proof checker (the kernel)

`check_proof(text, goal=None)` returns a **list of error messages**; an empty list means the proof is accepted. This is the LCF idea in miniature: everything else in your engine (tactics, automation) may be clever and buggy, but nothing counts as a theorem until this small, simple function accepts it.

**Proof format.** One line per step:

```text
1. P -> Q  premise
2. Q -> R  premise
3. | P  assumption
4. | Q  ->E 1,3
5. | R  ->E 2,4
6. P -> R  ->I 3-5
```

- A leading number, then `|` bars showing the depth of box nesting, then the formula, then **two or more spaces**, then the rule and its line references.
- `m-n` cites a whole box (a *subproof*). A single number cites a line.
- A line `[a]` on its own opens a **∀I box** with a fresh name `a` and no assumption. `[a] A(a)  assumption` opens an **∃E box**.
- Everything after `;` is a comment.

Rule names (ASCII or Unicode): `premise assumption &I &E |I |E ->I ->E ~I ~E falseE RAA <->I <->E forallE forallI existsI existsE =I =E Reit`.

**What the kernel checks, rule by rule.** For propositional rules it checks that the cited lines have exactly the required shapes, e.g. `->E` needs `A -> B` and `A`, concluding `B`. Formulas are compared *up to alpha-equivalence*, so `forall x. P(x)` and `forall y. P(y)` are the same.

For quantifier rules it adds the side conditions that make first-order logic sound:

- **∀E / ∃I** — the conclusion (resp. premise) must be an *instance* of the quantified formula, checked with capture-avoiding `subst`.
- **∀I** — the box must open with a *fresh name* `a`; the last line must be the body with `a` in place of the variable; and `a` must not occur in the conclusion.
- **∃E** — same freshness, plus: the box assumption must be the body with `a` for the variable; the box must end with the conclusion; `a` must not occur in the conclusion *or in the existential formula itself*.
- **Freshness at creation** (checked once per box): the name must not occur in any premise, nor in the assumption of any enclosing open box, and must not already be used by an enclosing box. That last condition is what rejects the classic cheat of "reusing the witness name" for two different existentials.
- **Names are not variables.** A fresh name may not start with `u v w x y z`, because those spell variables in the input language.

**Four proofs the test-suite checks.**

1. Hypothetical syllogism (above) — accepted.
2. The same proof with `->E 1,4` in line 5 — rejected, with the message `line 5 (impE): need A -> B and A, concluding B`.
3. A ∀I proof of `∀x Q(x)` from `∀x (P(x) → Q(x))` and `∀x P(x)` — accepted.
4. A "proof" of `∀x P(x)` from the single premise `P(a)` that opens a ∀I box with the name `a` — rejected, because `a` occurs in a premise. This is the mechanical form of the warning "you cannot generalise from a particular".

```text
1. exists x. P(x)  premise
2. exists x. Q(x)  premise
3. | [a] P(a)  assumption
4. | | [a] Q(a)  assumption         <- REJECTED: name 'a' already introduced by the enclosing box
5. | | P(a) & Q(a)  &I 3,4
...
```

This is the invalid inference `∃x P(x), ∃x Q(x) ⊢ ∃x (P(x) ∧ Q(x))`. A naive checker would accept it; yours must not.

### 8.8.5 Walking through the prover

`prove(premises, goal)` does the textbook pipeline of Sections 7.9.3–7.9.5:

1. `elim_arrows` removes `->` and `<->`.
2. `nnf` pushes negations inward (De Morgan, quantifier duality).
3. `standardize_apart` gives every quantifier its own variable name (`x_0`, `x_1`, …).
4. `skolemize` replaces each `∃y` by a fresh Skolem term `sk1(x1,…,xk)` over the enclosing universal variables.
5. `drop_universals` forgets the `∀` prefix (all remaining variables are implicitly universal).
6. `nnf_to_clauses` distributes `|` over `&` to get clauses: frozensets of `(sign, atom)`.
7. The **given-clause loop**: pick the lightest unprocessed clause; discard it if an active clause subsumes it; resolve it against every active clause and itself; add factors; delete tautologies and duplicates (compared after renaming variables canonically). Stop when the empty clause appears (`proved`), when nothing is left (`saturated`), or when resources run out (`limit`).

Three engineering details worth studying, because they are where beginners' provers go wrong:

- **Renaming apart.** Before resolving, one clause is given a fresh set of variable names (`rename_apart`). Forget this and `P(x)` will fail to unify with `~P(f(x))` even though the two `x`s are unrelated.
- **The occurs check.** `unify(x, f(x))` must fail. Without the check you get infinite terms and unsound "proofs".
- **Weight limit.** Without a cap on clause size, even a trivial equality problem makes terms like `f(f(f(…)))` grow forever. The cap (`max_weight=60`) makes the search incomplete, so when any clause is discarded the final status is `limit`, never `saturated`.

### 8.8.6 Testing strategy (copy it)

`test_starter.py` uses four kinds of test; every engine should:

| Kind | Example in the file | Why it catches bugs |
| --- | --- | --- |
| Unit tests with known answers | `P \| Q & R` parses as `P \| (Q & R)` | Locks in conventions |
| Round-trip properties | `parse(pretty(f)) == f` on 300 random formulas | Catches printer/parser disagreements |
| Oracle comparison | `sat(f)` (Tseitin+DPLL) versus brute-force truth tables on 300 random formulas | A slow, obviously correct implementation checks the fast one |
| Negative tests | the unsound proofs listed in 8.8.4 *must be rejected* | A checker that accepts everything passes every positive test |
| Cross-checks between components | if `prove` says valid, `find_countermodel` must find nothing | Components agree or one is wrong |

### 8.8.7 Exercises for the starter kit

1. **Read first.** Without running anything, predict what `pretty(parse("~(P & Q) -> R | S"))` prints. Then run it.
2. **Break the occurs check.** Delete the occurs check from `unify`, then run `unify(Var("x"), Fn("f", (Var("x"),)))`. What happens, and which test in the file would you write to catch it?
3. **Break renaming.** Comment out `rename_apart` in `resolvents`. Find a small problem that `prove` solved before and now fails or misbehaves.
4. **Add a rule.** Add the derived rule `MT` (modus tollens: from `A -> B` and `~B` conclude `~A`) to the kernel as a *primitive*, then explain why you would rather add it as a *derived* rule that expands into primitive steps.
5. **Add `Reit`-free scoping.** The kernel allows a line to cite any earlier line in an enclosing box. Write a test proving that citing a line inside a *closed* box is rejected.
6. **Better output.** Write `explain(proof_text)` that, for each accepted line, prints an English sentence such as "Line 4: from lines 1 and 3 by modus ponens, Q."
7. **Countermodel quality.** `find_countermodel` enumerates every structure of size `n`. For `n = 3` and a binary predicate this is 512 structures; for `n = 4` it is 65,536. Estimate the count for one binary predicate and one binary function at `n = 3`, then explain why you would switch to a SAT-based search (Section 7.9.7).
8. **Tactics (M6).** Write a function `intro(goal)` that, given a goal `A -> B`, returns the new assumption `A` and new goal `B`. Then write `apply_rule(goal, hyps)` for `->E`, and use them to implement a tiny interactive prover on top of the kernel.
9. **Equality (M8).** Implement a *demodulation* step: given a unit equation `l = r` and a clause containing an instance of `l`, replace it by the instance of `r`. Show it solves `a = b, P(a) ⊢ P(b)` without equality axioms.
10. **Stress test.** Generate random Horn problems, solve them with `prove`, and compare against a simple forward-chaining implementation. Any disagreement is a bug.

### 8.8.8 Quick-check

1. Why does the kernel compare formulas up to alpha-equivalence rather than with `==`? *(Because renaming a bound variable does not change meaning; `∀x P(x)` and `∀y P(y)` are the same formula and a proof should not fail because of the bound variable's spelling.)*
2. What does the status `saturated` tell you, and why can `prove` never say "invalid"? *(That no empty clause can be derived, so premises plus negated goal are satisfiable and the argument is invalid — but only when no clauses were discarded. First-order validity is semi-decidable, so a general procedure may simply run forever; "limit" is not evidence of invalidity.)*
3. Name two reasons the freshness conditions exist. *(Without them, ∀I would generalise from a particular object and ∃E would let a witness name leak out of its box; both make the system unsound.)*
4. Why do we test that bad proofs are rejected? *(A kernel that accepts everything passes all positive tests; only negative tests show it actually checks something.)*
5. What would you change so that `prove` can solve `f(f(x)) = x, f(f(f(a))) = b ⊢ f(a) = b`? *(Replace equality axioms by a rule built into the calculus — paramodulation/superposition with term orderings — Milestone M8.)*

---

# Chapter 9. Beyond the basics, resources, and a 12-week plan

## 9.1 Where to go next

| Topic | What it is | Why it matters | Prerequisites |
|---|---|---|---|
| **Computability** | Turing machines, halting problem, Rice's theorem, reductions | Explains *why* FOL is undecidable and why verification is hard | Ch. 5-6 |
| **Gödel's theorems (in depth)** | Arithmetization, representability, the fixed-point lemma | The limits of formal systems | Computability |
| **Model theory** | Types, elementary equivalence, ultraproducts, Łoś, quantifier elimination | What first-order theories can and cannot say; applications to algebra | Ch. 3, 6 |
| **Set theory** | ZFC axioms, ordinals, cardinals, the axiom of choice, independence of CH | The foundation of mathematics | Ch. 5 |
| **Proof theory** | Sequent calculus, cut elimination, normalization | Structure of proofs; basis of proof assistants | Ch. 2, 4 |
| **Type theory / Curry-Howard** | λ-calculus, simple types, dependent types, Martin-Löf type theory | Programs are proofs. Lean, Coq/Rocq, Agda | Ch. 2, 4 |
| **Proof assistants** | Lean 4, Rocq, Isabelle | Machine-checked mathematics and verified software | Ch. 4, 5 |
| **SAT / SMT** | CDCL, DPLL(T), theory solvers (arithmetic, arrays, bitvectors) | Industrial verification, symbolic execution, planning | Ch. 1, 7 |
| **Modal and temporal logic** | Kripke semantics; LTL, CTL; model checking | Specifying and verifying concurrent and distributed systems (TLA+) | Ch. 3 |
| **Program verification** | Hoare logic, weakest preconditions, separation logic | Proving programs correct | Ch. 4 |
| **Logic programming / Datalog** | Horn clauses, SLD resolution, Prolog, Datalog | Queries, rules engines, program analysis | Ch. 7 |
| **Description logics / ontologies** | Decidable fragments of FOL (OWL) | Knowledge graphs, semantic web | Ch. 3 |
| **Higher-order logic** | Quantification over predicates and functions | Isabelle/HOL, formalized mathematics | Ch. 3-4 |
| **Intuitionistic and linear logic** | Constructive reasoning; resource-sensitive logic | Type systems (Rust's ownership has linear-logic roots) | Ch. 2 |

**A natural next sequence** after this course: *computability → Gödel's theorems → model theory or type theory (depending on whether you lean toward mathematics or programming languages)*. Since you want to build engines, **Lean 4 + type theory** is the path that most directly reuses your project.

## 9.2 Resources

**Textbooks (roughly in order of use):**
- Daniel Velleman, *How to Prove It*: the best bridge from truth tables to proofs.
- Huth and Ryan, *Logic in Computer Science*: natural deduction, program verification, model checking, written for software engineers.
- Genesereth and Kao, *Introduction to Logic* (free online, Stanford): clear, includes Herbrand and resolution.
- Open Logic Project, *Sets, Logic, Computation* (free online): rigorous and modular.
- Herbert Enderton, *A Mathematical Introduction to Logic*: the classic for metatheory (completeness, compactness, incompleteness).
- Chiswell and Hodges, *Mathematical Logic*: natural deduction with full metatheory.
- John Harrison, *Handbook of Practical Logic and Automated Reasoning*: implement everything (in OCaml); closest to your project.
- Chang and Lee, *Symbolic Logic and Mechanical Theorem Proving*: classic on resolution and Herbrand.
- Peter Smith, *An Introduction to Gödel's Theorems* (and his free *Teach Yourself Logic* guide).
- Benjamin Pierce et al., *Software Foundations* (free): logic and proofs in Rocq/Coq, programming-flavoured.
- Jeremy Avigad et al., *Logic and Proof* and *Mathematics in Lean* (free): the Lean 4 route.

**Interactive tools:**
- **Lean 4** and the *Natural Number Game*: proof checking with instant feedback.
- **Carnap.io** and **Logitext**: natural deduction / sequent proofs in the browser.
- **Z3** (and its Python API), **Prover9/Mace4**, **Vampire**, **E**: provers and model finders to compare with your engine.
- **TPTP** (tptp.org): library of benchmark problems.

## 9.3 The 12-week plan

Assumes 6-8 hours per week. Each week: 2-3 hours reading and worked examples, 2-3 hours problems, 2 hours project. **Redo one old proof each week** from a blank page.

| Week | Theory | Problems | Project milestone |
|---|---|---|---|
| 1 | Ch. 0-1: foundations, implication, normal forms | 1.1-1.10 | M1 start: AST, parser |
| 2 | Ch. 2.1-2.5: Fitch proofs, rules, strategy | 2.1-2.8 | M1 finish: pretty-printer, round-trip tests |
| 3 | Ch. 2.6-2.9: derived rules, classical vs. intuitionistic | 2.9-2.18 | M4: truth tables, CNF, DPLL |
| 4 | Ch. 3.1-3.4: syntax, free/bound, translation | 3.1-3.6 | M2: free vars, substitution, alpha-eq |
| 5 | Ch. 3.5-3.8: semantics, countermodels, laws, prenex | 3.7-3.12 | M3: model evaluator, countermodel search |
| 6 | Ch. 4.1-4.4: quantifier rules, freshness, worked proofs | 4.1-4.9 | M5 start: checker for propositional rules |
| 7 | Ch. 4.5-4.7: strategy, equality, mistakes | 4.10-4.20 | M5: quantifier rules, side conditions, tests |
| 8 | Ch. 5.1-5.7: informal proof techniques | 5.1-5.6 | M5 polish; start M6 (tactics) |
| 9 | Ch. 5.8-5.13: induction (weak, strong, structural), sets, functions | 5.7-5.17 | M6: tactic layer |
| 10 | Ch. 6: soundness, completeness, compactness, undecidability | 6.1-6.8 | M7 start: NNF, Skolemization, CNF |
| 11 | Ch. 7: unification, resolution | 7.1-7.9 | M7: resolution prover, Pelletier problems |
| 12 | Review; redo the hardest problems; choose next topic | Error-log review | M8/M9: equality, cross-checks, polish |

**Readiness checkpoints** (be honest with yourself):

- **After week 3**, you should be able to prove 2.1-2.12 without hints, and 2.13-2.16 with at most one hint each. If not, repeat Ch. 2.
- **After week 7**, you should be able to prove 4.1-4.14 unaided, explain *why* the converse of 4.14-style arguments fails, and reproduce Examples 3, 5, 6 of Chapter 4 from memory.
- **After week 9**, you should be able to write a complete, correct induction proof for a new identity and find the flaw in a faulty induction.
- **After week 11**, you should be able to Skolemize any formula and run resolution by hand on a 4-5 clause problem.

If you meet these, you have mastered the *basics of logic and proofs* in the sense you asked for, and you are ready for the topics in 9.1.

## 9.4 Pace for the Complete Edition (starting from absolute zero)

The 12-week plan above assumes you read only the core sections of each chapter. The Complete Edition adds **Part Zero** (Chapters Z1–Z5) and a **"complete detail" companion** at the end of every chapter's numbered sections (1.8, 2.9, 3.8, 4.7, 5.14, 6.7, 7.9, 8.8). Here is how to fold them in.

| Stage | Read | Notes |
|---|---|---|
| Before week 1 (3–5 days) | Z1, Z2, Z3 | Reasoning, mathematical language, sets, functions, relations, sequences, trees. Do the quick-checks. Skip nothing if any word is unfamiliar. |
| Before week 1 (1–2 days) | Z4 (skim), Z5 (skim) | Treat the Symbol Atlas as a reference; read it fully once, then come back whenever a sign puzzles you. Z5 shows the same logic in other notations; skim it now, study it when you meet those formats. |
| Weeks 1–2 | Ch. 0–1, then 1.8 | Read the companion after the core sections, then do the problems. |
| Weeks 3–4 | Ch. 2, then 2.9 | The companion has the full rule tables, the proof-search procedure and the other proof formats. |
| Weeks 5–6 | Ch. 3, then 3.8 | Do the translation workshop in 3.8.7 on paper. |
| Weeks 7–8 | Ch. 4, then 4.7 | Study the gallery of illegal proofs in 4.7.5 until you can state the violated condition at a glance. |
| Weeks 9–10 | Ch. 5, then 5.14 | Induction in complete detail (5.14.4) is the most reusable material in the book. |
| Weeks 11–12 | Ch. 6, 7, then 6.7, 7.9 | Metatheory and automated reasoning; run the SAT and unification traces by hand. |
| Weeks 13–16 | Ch. 8, then 8.8 | Run the starter kit, read its tests, do the exercises, then extend it. |

Use Appendix D (glossary) whenever a term is unfamiliar and Appendix E when you need to type a symbol or write a formula in some tool's syntax. Total: about 16 weeks at 6–8 hours per week if you start from zero; fewer if you already know the Part Zero material.

---

# Appendix A. Rule cheat sheet

## A.1 Natural deduction: propositional rules

| Rule | Premises | Conclusion |
|---|---|---|
| ∧I | A, B | A ∧ B |
| ∧E | A ∧ B | A  (or B) |
| ∨I | A | A ∨ B  (or B ∨ A) |
| ∨E | A ∨ B; sub-proof A ⊢ C; sub-proof B ⊢ C | C |
| →I | sub-proof A ⊢ B | A → B |
| →E | A, A → B | B |
| ¬I | sub-proof A ⊢ ⊥ | ¬A |
| ¬E | A, ¬A | ⊥ |
| ⊥E | ⊥ | any C |
| ↔I | A → B, B → A | A ↔ B |
| ↔E | A ↔ B, A  (or B) | B  (or A) |
| RAA (classical) | sub-proof ¬A ⊢ ⊥ | A |

## A.2 Quantifier and equality rules

| Rule | Premises | Conclusion | Side condition |
|---|---|---|---|
| ∀E | ∀x A | A[t/x] | t free for x in A |
| ∃I | A[t/x] | ∃x A | t free for x in A |
| ∀I | sub-proof (fresh a) ⊢ A[a/x] | ∀x A | a does not occur in any premise, any open assumption, or ∀x A |
| ∃E | ∃x A; sub-proof (fresh a, assume A[a/x]) ⊢ C | C | a does not occur in ∃x A, C, any premise, or any other open assumption |
| =I | (none) | t = t | |
| =E | s = t, A[s/x] | A[t/x] | |

## A.3 Proof-finding strategy at a glance

| Goal | Move |
|---|---|
| A → B | assume A, prove B |
| ¬A | assume A, derive ⊥ |
| A ∧ B | prove both |
| A ∨ B | prove one disjunct; else RAA |
| A ↔ B | prove both directions |
| ∀x A | fresh a, prove A(a) |
| ∃x A | find a witness t, prove A(t); else RAA |
| anything stuck | RAA: assume the negation, derive ⊥ |

| Have | Move |
|---|---|
| A ∧ B | ∧E |
| A → B | →E when you have A |
| A ∨ B | cases (∨E) |
| ¬A | combine with A to get ⊥ |
| ∀x A | ∀E with useful terms |
| ∃x A | ∃E with a fresh witness name |
| ⊥ | ⊥E: anything |

## A.4 Translation patterns

| English | Logic |
|---|---|
| All S are P | ∀x (S(x) → P(x)) |
| Some S are P | ∃x (S(x) ∧ P(x)) |
| No S is P | ∀x (S(x) → ¬P(x)) |
| Not all S are P | ∃x (S(x) ∧ ¬P(x)) |
| Only S are P | ∀x (P(x) → S(x)) |
| At most one P | ∀x∀y ((P(x) ∧ P(y)) → x = y) |
| Exactly one P | ∃x (P(x) ∧ ∀y (P(y) → y = x)) |

## A.5 Key equivalences

- ¬∀x A ≡ ∃x ¬A;  ¬∃x A ≡ ∀x ¬A
- ∀x (A ∧ B) ≡ ∀x A ∧ ∀x B;  ∃x (A ∨ B) ≡ ∃x A ∨ ∃x B
- (x not free in B)  (∀x A) → B ≡ ∃x (A → B);  (∃x A) → B ≡ ∀x (A → B)
- ∃x ∀y R ⊨ ∀y ∃x R, **never** the converse

## A.6 Symbol glossary

| Symbol | Reads | Level |
|---|---|---|
| ¬, ∧, ∨, →, ↔ | not, and, or, implies, iff | object language |
| ⊤, ⊥ | true, false (absurdity) | object language |
| ∀, ∃, ∃! | for all, there exists, there exists exactly one | object language |
| ⊨ | semantically entails / is valid | metalanguage |
| ⊢ | proves / is derivable from | metalanguage |
| ≡ | is logically equivalent to | metalanguage |
| ⊣⊢ | is provably equivalent to | metalanguage |
| A[t/x] | A with t substituted for free x | metalanguage |
| ∎ | end of proof | prose |

---

# Appendix B. Common mistakes catalog

Use this as a checklist when reviewing your own work.

## Propositional logic and proofs
1. Reading "A only if B" as B → A. (It is A → B.)
2. Affirming the consequent: from A → B and B, concluding A.
3. Denying the antecedent: from A → B and ¬A, concluding ¬B.
4. Treating P → Q as false when P is false.
5. Confusing the **converse** with the **contrapositive**.
6. Proving a negation by assuming the negation (¬I needs you to assume the *positive* statement).
7. Using RAA to prove a statement but forgetting that you must assume the **negation** of the goal.
8. Using a line from a closed sub-proof.
9. Forgetting to discharge an assumption.
10. Applying a rule to a sub-formula instead of the main connective.
11. ∨E with branches that end in different formulas.

## Predicate logic
12. Translating "All S are P" with ∧, or "Some S are P" with →.
13. Swapping quantifier order: ∀∃ and ∃∀ are different, and only ∃∀ ⇒ ∀∃.
14. Forgetting that ∀x (A → B) is not equivalent to ∀x A → ∀x B.
15. Moving a quantifier out of an antecedent without flipping it.
16. Variable capture in substitution.
17. Assuming a domain is non-empty when working in a free logic, or forgetting it when working in standard FOL.
18. Illegal ∀I: generalizing over a name that occurs in an open assumption or premise.
19. Letting the ∃E witness escape into the conclusion.
20. Reusing one witness name for two different existentials.
21. Concluding P(a) from ∃x P(x) with a name of your own choosing.
22. Proving ∀x P(x) by checking examples. (Examples prove ∃, and counterexamples disprove ∀.)

## Informal mathematical proofs
23. Starting without unpacking the definitions.
24. Assuming what is to be proved (circular reasoning).
25. Using the same letter for two different objects.
26. Introducing a variable "arbitrary" and then silently assuming a special property of it ("WLOG" without justification).
27. Proof by contradiction where no contradiction is derived, or the contradiction is with something not assumed.
28. Missing cases in a case analysis.
29. Induction: no base case, wrong base case, an inductive step that uses P(n + 1), or a step that fails for small n.
30. Induction hypothesis not strong enough: you may need to **strengthen the claim** (tromino problem).

## Metatheory
31. Confusing ⊨ with ⊢ (before soundness/completeness are invoked).
32. Confusing Gödel's *completeness* theorem (about FOL provability) with the *incompleteness* theorems.
33. Believing a prover's timeout means the formula is invalid.

## Engineering the logic engine
34. Substitution that does not rename bound variables.
35. Unification without occurs check.
36. Forgetting to rename clauses apart before resolution.
37. Resolution without factoring.
38. Comparing formulas with `==` instead of alpha-equivalence.
39. A checker that verifies the final formula but not scope or freshness conditions.
40. Skolemizing with Skolem constants where Skolem **functions** of the enclosing universals are needed.

---

# Appendix C. Hints and solutions

**How to use:** read the hint, close the file, and try again. Read the full solution only after a real attempt. Where a solution is only a sketch, you should be able to expand it into a full formal or informal proof; if you cannot, that is exactly the thing to practice.

---

## Chapter 1

**1.1** Rows (P,Q) = TT, TF, FT, FF. P → Q: T F T T. ¬P ∨ Q: T F T T. P ∧ ¬Q: F T F F, so ¬(P ∧ ¬Q): T F T T. ¬Q → ¬P: T F T T. All four columns agree.

**1.2** Original: true. Converse ("if divisible by 3 then by 6"): **false** (3). Inverse ("if not divisible by 6 then not divisible by 3"): **false** (3 again). Contrapositive ("if not divisible by 3 then not divisible by 6"): **true**. As expected, the original and its contrapositive are equivalent, and the converse and inverse are equivalent to each other.

**1.3**
- (a) D → F (D = "you have dessert", F = "you finish dinner").
- (b) ¬H → M (H = "you hurry", M = "you miss the train"); equivalently H ∨ M.
- (c) (G → X) ∧ ¬(X → G), where X = "passes the exam", G = "gets the degree". Equivalent to (G → X) ∧ X ∧ ¬G.
- (d) ¬S ∧ ¬B.

**1.4** (a) Yes (modus ponens twice). (b) **No**: P = F, Q = T makes both premises true and P false (affirming the consequent). (c) Yes (disjunctive syllogism). (d) **No**: P = F, Q = T makes P → Q true, ¬P true, and ¬Q false.

**1.5** P → (Q → R) ≡ ¬P ∨ (¬Q ∨ R) ≡ (¬P ∨ ¬Q) ∨ R ≡ ¬(P ∧ Q) ∨ R ≡ (P ∧ Q) → R. (Steps: implication as disjunction twice, associativity, De Morgan, implication as disjunction.)

**1.6** P ↔ Q ≡ (¬P ∨ Q) ∧ (¬Q ∨ P).
CNF: (¬P ∨ Q ∨ R) ∧ (P ∨ ¬Q ∨ R). DNF: (P ∧ Q) ∨ (¬P ∧ ¬Q) ∨ R.

**1.7** Suppose all three hold. ¬(P → R) forces P true and R false. Then P → Q gives Q true, and Q → R gives R true. Contradiction with R false. So the set is unsatisfiable, and by (F1) the entailment holds.

**1.8** ¬P ≡ P | P. P ∧ Q ≡ ¬(P | Q) ≡ (P | Q) | (P | Q). Since {¬, ∧} is complete, so is NAND.

**1.9** Let v⊤ make every atom true. By structural induction, every formula built from atoms with ∧, ∨, →, ↔ is true under v⊤ (each connective maps T, T to T). But ¬P is false under v⊤. So no such formula is equivalent to ¬P.

**1.10** Let a = "A is a knight", b = "B is a knight". A's statement is ¬b; a person is a knight iff their statement is true, so a ↔ ¬b. B's statement is (a ↔ b), so b ↔ (a ↔ b). If b were true, then a ↔ b would have to be true, so a is true; but then a ↔ ¬b is T ↔ F, false. So b is false. Then (a ↔ b) must be false, so a ≠ b, so a is true. Check a ↔ ¬b: T ↔ T ✔. **A is the knight, B is the knave.**

---

## Chapter 2

*(Fitch notation as in Chapter 2. "Reit" means reiteration of an earlier line into a sub-proof.)*

**2.1** ∧E (get Q), ∧E (get P), ∧I.

**2.2** P ⊢ ¬¬P: assume ¬P; ¬E with P gives ⊥; ¬I gives ¬¬P.

**2.3** Assume P; →E gives Q; ¬E with ¬Q gives ⊥; ¬I gives ¬P.

**2.4** ⊢ P → (Q → P):
```
1.  |  P               assumption
2.  |  |  Q            assumption
3.  |  |  P            reit 1
4.  |  Q → P           →I 2-3
5.  P → (Q → P)        →I 1-4
```

**2.5** ∨E on P ∨ Q: case P → ∨I gives Q ∨ P; case Q → ∨I gives Q ∨ P.

**2.6** (P ∧ Q) → R ⊢ P → (Q → R): assume P, assume Q, ∧I, →E, →I, →I. Converse: assume P ∧ Q, ∧E twice, →E with P gives Q → R, →E with Q gives R, →I.

**2.7** Assume (1) P → (Q → R), (2) P → Q, (3) P. →E 2,3: Q. →E 1,3: Q → R. →E: R. Discharge 3, 2, 1 with →I three times.

**2.8** ∨E on the premise. Case P ∧ Q: ∧E gives P and Q; ∨I gives Q ∨ R; ∧I gives P ∧ (Q ∨ R). Case P ∧ R: symmetric.

**2.9** Assume P ∧ ¬P; ∧E twice; ¬E gives ⊥; ¬I gives ¬(P ∧ ¬P).
```
1.  |  P ∧ ¬P          assumption
2.  |  P               ∧E 1
3.  |  ¬P              ∧E 1
4.  |  ⊥               ¬E 2,3
5.  ¬(P ∧ ¬P)          ¬I 1-4
```

**2.10** Assume P ∧ Q. ∨E on ¬P ∨ ¬Q with goal ⊥: case ¬P: ∧E gives P; ¬E gives ⊥. Case ¬Q: ∧E gives Q; ¬E gives ⊥. So ⊥. Discharge with ¬I.

**2.11** Assume P. ∨E on ¬P ∨ Q with goal Q: case ¬P: ¬E with P gives ⊥, ⊥E gives Q. Case Q: Q. So Q. →I.

**2.12** ↔I needs P → R and R → P. For P → R: assume P; ↔E with P ↔ Q gives Q; ↔E with Q ↔ R gives R. For R → P: assume R; ↔E (the other direction) with Q ↔ R gives Q, then with P ↔ Q gives P.

**2.13**

```
1.  P → Q              premise
2.  P ∨ ¬P             LEM (Example 5)
3.  |  P               assumption
4.  |  Q               →E 1,3
5.  |  ¬P ∨ Q          ∨I 4
6.  |  ¬P              assumption
7.  |  ¬P ∨ Q          ∨I 6
8.  ¬P ∨ Q             ∨E 2, 3-5, 6-7
```

**2.14**

```
1.  ¬(P ∧ Q)           premise
2.  P ∨ ¬P             LEM
3.  |  P               assumption
4.  |  |  Q            assumption
5.  |  |  P ∧ Q       ∧I 3,4
6.  |  |  ⊥           ¬E 5,1
7.  |  ¬Q              ¬I 4-6
8.  |  ¬P ∨ ¬Q        ∨I 7
9.  |  ¬P              assumption
10. |  ¬P ∨ ¬Q        ∨I 9
11. ¬P ∨ ¬Q            ∨E 2, 3-8, 9-10
```

**2.15**

```
1.  P ∨ ¬P                         LEM
2.  |  P                          assumption
3.  |  |  Q                       assumption
4.  |  |  P                       reit 2
5.  |  Q → P                      →I 3-4
6.  |  (P → Q) ∨ (Q → P)          ∨I 5
7.  |  ¬P                         assumption
8.  |  |  P                       assumption
9.  |  |  ⊥                       ¬E 8,7
10. |  |  Q                       ⊥E 9
11. |  P → Q                      →I 8-10
12. |  (P → Q) ∨ (Q → P)          ∨I 11
13. (P → Q) ∨ (Q → P)             ∨E 1, 2-6, 7-12
```
(Intuition: for any two statements, one implies the other. Surprising, but it is a consequence of classical truth values: either P is true, so everything implies it, or P is false, so it implies everything.)

**2.16** Assume ¬P (for RAA). Assume P; ¬E gives ⊥; ⊥E gives Q; →I gives P → Q. →E with the premise gives P. ¬E with ¬P gives ⊥. RAA gives P.

**2.17** ∨E on P ∨ Q with goal Q ∨ R. Case P: ∨E on ¬P ∨ R: sub-case ¬P gives ⊥ (with P) then Q ∨ R by ⊥E; sub-case R gives Q ∨ R by ∨I. Case Q: ∨I gives Q ∨ R.

**2.18** *Provable intuitionistically (no RAA, no LEM needed):* 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.10, 2.11, 2.12, 2.17. Check: none of the proofs above uses RAA or LEM.
*Not provable intuitionistically:* 2.13 (P → Q ⊢ ¬P ∨ Q), 2.14 (De Morgan, hard direction), 2.15 ((P → Q) ∨ (Q → P)), 2.16 (Peirce's law). Each of our proofs uses LEM or RAA, and they genuinely require it. A rigorous proof of *unprovability* needs Kripke semantics or Heyting algebras (a good topic to learn later). (Example 8 of Chapter 2, ¬¬P ⊢ P, is likewise classical only.)

---

## Chapter 3

**3.1**
- (a) ∀x (S(x) → ∀y (T(y) → L(x, y)))
- (b) ¬∃x (S(x) ∧ ∀y (T(y) → L(x, y))), equivalently ∀x (S(x) → ∃y (T(y) ∧ ¬L(x, y)))
- (c) ∃x (S(x) ∧ ∀y (T(y) → ¬L(x, y)))
- (d) ∀y (T(y) → ∀x ∀z ((S(x) ∧ S(z) ∧ L(x, y) ∧ L(z, y)) → x = z))

**3.2** Binding occurrences: x in P(x, y) (bound by ∀x), y in Q(y, z) (bound by ∃y). Free: y in P(x, y), z in Q(y, z), x in R(x). (The quantifier symbols themselves are binders, not occurrences in this sense.)

**3.3** (a) ∃y′ L(y, y′). (b) ∀x P(x, f(z)). (c) ∀x′ P(x′, f(x)): the bound x must be renamed, otherwise the x in f(x) would be captured.

**3.4**
- (a) Even(x) := ∃y (y + y = x).
- (b) Prime(x) := 1 < x ∧ ∀y ∀z (y · z = x → (y = x ∨ z = x)).
- (c) ∀n ∃p (n < p ∧ Prime(p)).
- (d) ∀x ((Even(x) ∧ 1 + 1 < x) → ∃p ∃q (Prime(p) ∧ Prime(q) ∧ p + q = x)).

**3.5**
- (a) ∃x ∀y (¬(x < y) ∨ ∃z (z < y ∧ ¬(z ≤ x))). In words: some x has no immediate successor.
- (b) As given in 3.6: ∃ε>0 ∀δ>0 ∃x (|x − a| < δ ∧ |f(x) − f(a)| ≥ ε). ✔
- (c) ∀L ∃ε>0 ∀N ∃n>N |aₙ − L| ≥ ε. (No number L is a limit.)

**3.6** At least 3: ∃x∃y∃z (x≠y ∧ x≠z ∧ y≠z). Exactly 2: ∃x∃y (x ≠ y ∧ ∀z (z = x ∨ z = y)). At most 2: ∀x∀y∀z (x = y ∨ x = z ∨ y = z).

**3.7**
- (a) **Valid** (Chapter 4, Example 3).
- (b) **Invalid.** D = {1, 2}, R = {(1,2), (2,1)}. Each element is R-related *from* someone, but no single element is related from everyone.
- (c) **Valid** (Problem 4.9).
- (d) **Invalid.** D = {1, 2}, P = {1}, Q = ∅. ∀x P is false so the antecedent holds, but x = 1 is a counterexample to P → Q.
- (e) **Invalid.** D = {1, 2}, P = {1}, Q = {2}.
- (f) **Valid** (Problem 4.3).
- (g) **Valid** (non-empty domain; Problem 4.2).
- (h) **Invalid.** D = {1, 2}, P = {1}.

**3.8** (a) False (element 4 has no larger element). (b) True (take x = 1). (c) False (take x = 1, y = 2: nothing lies strictly between).

**3.9**
- (a) ∀x ∀y (P(x) ∨ Q(y)) (rename the second quantified variable to y first).
- (b) ∃x ∃y (P(x) → Q(y)).
- (c) ¬∀x (P(x) → ∃y R(x, y)) ≡ ∃x (P(x) ∧ ¬∃y R(x, y)) ≡ ∃x (P(x) ∧ ∀y ¬R(x, y)) ≡ ∃x ∀y (P(x) ∧ ¬R(x, y)).

**3.10** Yes: satisfiable in finite structures. One-element model: R = {(1,1)}. The sentence says "R is symmetric, and every element has an R-neighbour". For D = {1, 2}, let a = [R(1,1)], b = [R(2,2)], c = [R(1,2) and R(2,1)] (symmetry forces both together). Element 1 needs a or c, and element 2 needs b or c. If c is true, a and b are free: 4 models. If c is false, both a and b must be true: 1 model. **Total: 5 models.**

**3.11** *Infinite model:* (ℕ, <). *No finite model:* in a finite model with n elements, seriality lets us build x₀ R x₁ R x₂ ... R x_n (n + 1 terms). By pigeonhole xᵢ = xⱼ for some i < j. Applying transitivity along the chain gives R(xᵢ, xⱼ), i.e., R(xᵢ, xᵢ), contradicting irreflexivity.

**3.12** Let M ⊨ ∃x ∀y R(x, y): there is d ∈ D such that for every e ∈ D, (d, e) ∈ R. To show M ⊨ ∀y ∃x R(x, y), take any e ∈ D. Then x := d witnesses ∃x R(x, e), since (d, e) ∈ R. As e was arbitrary, done. For the converse, ∀y ∃x R(x, y) provides for each e *some* d_e, and d_e may vary with e; nothing forces one d to work for all e. Countermodel: D = {1, 2}, R = {(1,2), (2,1)}.

---

## Chapter 4

**4.1** (⇒) For ∀x P: open [a], ∀E on the premise gives P(a) ∧ Q(a), ∧E gives P(a), ∀I. Same for ∀x Q. ∧I. (⇐) Open [a], ∀E on both conjuncts of the premise, ∧I, ∀I.

**4.2** ∀E with *any* name c gives P(c) (this is where non-emptiness enters); ∃I gives ∃x P(x).

**4.3** ∃E with fresh a: P(a) ∧ Q(a); ∧E gives P(a), Q(a); ∃I gives ∃x P(x) and ∃x Q(x); ∧I. The conclusion contains no a. ✔

**4.4** Open [b]; inside it open [a]; ∀E on ∀x ∀y R(x, y) with a gives ∀y R(a, y); ∀E with b gives R(a, b); close [a] with ∀I: ∀x R(x, b); close [b] with ∀I: ∀y ∀x R(x, y).

**4.5** ∃E on ∃x ∃y R(x, y) with a: assume ∃y R(a, y); ∃E with b: assume R(a, b); ∃I gives ∃x R(x, b); ∃I gives ∃y ∃x R(x, y). That formula mentions neither a nor b, so both ∃E steps are legal.

**4.6** Assume ∃x P(x). ∃E with fresh a: P(a). ∀E on the premise: ¬P(a). ¬E: ⊥. ∃E exports ⊥ (no a in ⊥). ¬I gives ¬∃x P(x).

**4.7** Open [a]. Assume P(a). ∃I gives ∃x P(x). ¬E with the premise gives ⊥. ¬I gives ¬P(a). Close [a] with ∀I.

**4.8** Assume ∀x P(x). ∃E on the premise with a: ¬P(a). ∀E gives P(a). ¬E gives ⊥. Export ⊥ from ∃E. ¬I gives ¬∀x P(x).

**4.9** Assume ∀x P(x). Open [a]: ∀E on both hypotheses gives P(a) → Q(a) and P(a); →E gives Q(a). ∀I. →I.

**4.10** ∨E on the premise. Each case: open [a], ∀E, ∨I, ∀I. Both branches conclude ∀x (P(x) ∨ Q(x)).

**4.11** ∃E with a: P(a) ∨ Q(a). ∨E: case P(a): ∃I gives ∃x P(x), then ∨I gives ∃x P(x) ∨ ∃x Q(x); case Q(a): symmetric. The conclusion has no a.

**4.12** (⇒) Assume ∃x P(x). ∃E with a: P(a). ∀E on the premise: P(a) → B. →E: B. B does not contain a (x not free in B, a fresh), so ∃E exports B. →I. (⇐) Assume the premise ∃x P(x) → B. Open [a]. Assume P(a). ∃I gives ∃x P(x). →E gives B. →I gives P(a) → B. ∀I.

**4.13** Open [a]. ∀E: P(a) ∨ Q(a). ∨E with goal Q(a): case P(a): ∃I gives ∃x P(x), ¬E with the premise ¬∃x P(x) gives ⊥, ⊥E gives Q(a). Case Q(a): trivial. ∀I.

**4.14** Open [a]. Assume P(a). ∃I gives ∃x P(x). →E on the premise gives ∀y Q(y). ∀E with a gives Q(a). →I gives P(a) → Q(a). ∀I.

**4.15** s = t, t = u ⊢ s = u: by =E with A(x) := s = x (Chapter 4, Section 4.4). For ∀x ∀y (x = y → y = x): open [a], [b]; assume a = b; =I gives a = a; =E with A(x) := x = a gives b = a; →I; ∀I twice.

**4.16** ∃E with a name c: assume P(c) ∧ ∀y (P(y) → y = c). Open [a], [b]; assume P(a) ∧ P(b). ∀E on the second conjunct: P(a) → a = c, P(b) → b = c; →E: a = c, b = c. Symmetry on b = c gives c = b; transitivity: a = b. →I; ∀I; ∀I. Export the universal conclusion from ∃E (it does not contain c).

**4.17** Open [a]. ∀E on the first premise: ∃y R(a, y). ∃E with b: R(a, b). Symmetry (∀E twice, →E): R(b, a). Transitivity with R(a, b), R(b, a): R(a, a). This conclusion has no b, so ∃E exports it. ∀I.

**4.18** *Informal first:* either ∀y D(y) or not. Case 1: ∀y D(y): for any name c, D(c) → ∀y D(y) holds because the consequent is a premise; ∃I. Case 2: ¬∀y D(y): by Example 4, ∃x ¬D(x); ∃E with a: ¬D(a); then D(a) → ∀y D(y) (assume D(a), ¬E gives ⊥, ⊥E gives ∀y D(y)); ∃I gives the goal; ∃E exports it. Combine the two cases with ∨E applied to the LEM instance ∀y D(y) ∨ ¬∀y D(y). Formal version: Example 5 (via RAA) or the one built from this outline.

**4.19** Example 6 of Chapter 4.

**4.20**
- (a) The "proof" opens ∃E with P(a) and then concludes P(a). But in ∃E the conclusion C **must not contain the witness name a**. The conclusion ∃x P(x) ⊢ P(a) is **invalid** (D = {1, 2}, P = {1}, a ↦ 2).
- (b) After opening [b] and obtaining R(b, a) via ∃E on ∃y R(b, y), the "proof" tries to generalize ∀x R(x, a) using ∀I on b. This is illegal: b occurs in the open assumption R(b, a) (and a was chosen depending on b). The conclusion is **invalid** (countermodel of 3.7(b)).
- (c) The second ∃E assumes Q(a) with the *same* a as the first witness. For ∃E the name must be fresh, and a already occurs in the open assumption P(a). The conclusion is **invalid** (D = {1, 2}, P = {1}, Q = {2}).

---

## Chapter 5

**5.1** Let m = 2j + 1, n = 2k + 1. Then m + n = 2(j + k + 1), even.

**5.2** Contrapositive: if n is even, then n² is even. n = 2k gives n² = 2(2k²).

**5.3** (2j + 1)(2k + 1) = 4jk + 2j + 2k + 1 = 2(2jk + j + k) + 1.

**5.4** Contrapositive: if 3 ∤ n, then n = 3k ± 1, so n² = 9k² ± 6k + 1 = 3(3k² ± 2k) + 1, not divisible by 3. For √3: suppose √3 = p/q in lowest terms. Then p² = 3q², so 3 | p² and hence 3 | p, p = 3r. Then 9r² = 3q², so q² = 3r², 3 | q² and 3 | q, contradicting lowest terms.

**5.5** If qr = s were rational, then r = s/q would be rational (q ≠ 0): contradiction. For q + r the same trick works (r = s − q). For r + s with both irrational, no: √2 + (−√2) = 0 is rational. (Likewise √2 · √2 = 2.)

**5.6** Case n even: n = 2k, so n(n + 1) = 2k(n + 1) is even. Case n odd: n + 1 is even, n + 1 = 2k, so n(n + 1) = 2nk is even. Exhaustive.

**5.7** Base n = 1: 1 = 1·2·3/6. Step: n(n+1)(2n+1)/6 + (n+1)² = (n+1)[n(2n+1) + 6(n+1)]/6 = (n+1)(2n² + 7n + 6)/6 = (n+1)(n+2)(2n+3)/6.

**5.8** Base n = 0: 2¹ − 1 = 1. Step: 2ⁿ⁺² − 1 = 2·2ⁿ⁺¹ − 1 = (2ⁿ⁺¹ − 1) + 2ⁿ⁺¹ = (1 + 2 + ... + 2ⁿ) + 2ⁿ⁺¹.

**5.9** Base n = 5: 32 > 25. (It fails for n = 3, 4: 8 < 9 and 16 = 16.) Step: assume 2ⁿ > n² with n ≥ 5. Then 2ⁿ⁺¹ > 2n² = n² + n² ≥ n² + 2n + 1 = (n + 1)², using n² ≥ 2n + 1 for n ≥ 3.

**5.10** Base n = 1: F₁ = 1 = F₃ − 1 = 2 − 1. Step: F₁ + ... + Fₙ + Fₙ₊₁ = (Fₙ₊₂ − 1) + Fₙ₊₁ = Fₙ₊₃ − 1.

**5.11** (a) (⇒) Assume A ⊆ B. A ∩ B ⊆ A is trivial. If x ∈ A then x ∈ B, so x ∈ A ∩ B. (⇐) Assume A ∩ B = A. If x ∈ A then x ∈ A ∩ B, so x ∈ B. (b) x ∈ (A ∪ B)ᶜ ⇔ ¬(x ∈ A ∨ x ∈ B) ⇔ x ∉ A ∧ x ∉ B ⇔ x ∈ Aᶜ ∩ Bᶜ (De Morgan).

**5.12** Let z ∈ Z. g is surjective, so g(y) = z for some y. f is surjective, so f(x) = y for some x. Then (g ∘ f)(x) = z. For the right inverse: given y ∈ Y, take x := h(y); then f(x) = f(h(y)) = y.

**5.13** Strong induction on n ≥ 2. If n is prime, n divides itself. Otherwise n = ab with 1 < a < n; by the IH a has a prime divisor p, and p divides a, hence n.

**5.14** Claim P(n): for **every** choice of removed square, the 2ⁿ × 2ⁿ board can be tiled. Base n = 1: a 2×2 board minus one square is exactly one L-tromino. Step: split the 2ⁿ⁺¹ board into four 2ⁿ quadrants. The removed square lies in one quadrant. Place one L-tromino at the centre covering one square from each of the other three quadrants. Now each quadrant has exactly one "missing" square, so the IH tiles each. (The strengthening "for every choice" is essential.)

**5.15** The step "the two groups overlap" fails for n = 1: with 2 horses, the two groups of 1 horse are disjoint. So P(1) → P(2) is false and the induction collapses (P(n) → P(n + 1) holds for n ≥ 2, but the chain never starts).

**5.16** Let ε > 0 and δ = min(1, ε/5). Suppose |x − 2| < δ. Then |x − 2| < 1, so 1 < x < 3 and |x + 2| < 5. Hence |x² − 4| = |x − 2||x + 2| < δ · 5 ≤ ε.

**5.17** Suppose f: ℕ → 𝒫(ℕ). Let D = {n ∈ ℕ : n ∉ f(n)}. For each n, n ∈ D ⇔ n ∉ f(n), so D ≠ f(n) (they differ on the element n). Hence D is not in the range of f, so f is not surjective. *Barber connection:* read "n ∈ f(m)" as "m shaves n". D is the set of people shaved by the "barber" who shaves exactly those who do not shave themselves; if D = f(d) then d would shave himself iff he does not.

---

## Chapter 6

**6.1** A ⊨ B is a *semantic* statement about all models. "⊢ A → B" is a *syntactic* statement: a derivation exists. By the deduction theorem, A ⊢ B iff ⊢ A → B. By soundness and completeness, A ⊢ B iff A ⊨ B. So all three are equivalent, but they are different *definitions*, and the equivalence is a theorem (not a triviality).

**6.2** Object language: (a) P → Q, (e) ∀x P(x). Metalanguage: (b) P ⊨ Q, (c) ⊢ P ∨ ¬P, (d) the English sentence about tautologies.

**6.3** ∧E: if M ⊨ A ∧ B then, by the truth condition for ∧, M ⊨ A (and M ⊨ B). ∨I: if M ⊨ A then M ⊨ A ∨ B. →E: if M ⊨ A and M ⊨ A → B then M ⊨ B, since a true implication with a true antecedent has a true consequent.

**6.4** By completeness, valid = provable. Proofs are finite strings over a finite alphabet and can be checked mechanically. Enumerate all strings in order, check each, and output those that are proofs; every valid sentence eventually appears. So the set is recursively enumerable. But an r.e. set need not be decidable: to decide non-membership you would need to know when to stop searching. (By Church-Turing, validity is undecidable.) A prover can reliably answer "valid" (it eventually halts with a proof), but it cannot reliably answer "invalid".

**6.5** Suppose a theory T has exactly the finite structures as models. Let λₙ say "at least n elements" and Γ = T ∪ {λₙ : n ≥ 1}. Any finite subset of Γ mentions only λ₁, ..., λₖ, and is satisfied by a finite structure of size k (which satisfies T). By compactness, Γ has a model. This model satisfies every λₙ so is infinite, yet satisfies T, so it should be finite. Contradiction.

**6.6** Let T = Th(ℕ) be the set of all sentences true in ℕ, and add a new constant c and sentences c > n̄ for every numeral n̄. Any finite subset is satisfied in ℕ by interpreting c as a large enough number. By compactness the whole set has a model; it satisfies all true arithmetic, and contains an element c larger than every standard natural number.

**6.7** Take D = {1, 2}, P = {1}, and interpret the constant a as 1. Then P(a) is true but ∀x P(x) is false. The inference is invalid because the premise says something about the specific object a. In the soundness proof for ∀I, freshness lets you *re-interpret* a as any element without affecting the open assumptions, so A(a) must hold for every element, giving ∀x A(x).

**6.8** Cardinality is not absolute. "Uncountable" inside a model means "no bijection with ℕ *exists as an element of that model*". The countable model (as seen from outside) simply lacks the bijections that would reveal the sets as countable. This is the Skolem paradox: a relativity of first-order notions, not a contradiction.

---

## Chapter 7

**7.1**
- (a) {¬P(x), Q(x)}.
- (b) {R(c, y)} (Skolem constant c).
- (c) ∀x ∃y (P(x) → Q(y)) becomes ∀x (P(x) → Q(f(x))): clause {¬P(x), Q(f(x))}. And ∃x ∀y R(x, y) becomes {R(c, y)}. Two clauses.
- (d) ¬∀x (P(x) → ∃y R(x, y)) ≡ ∃x (P(x) ∧ ∀y ¬R(x, y)). Skolemize x := c: two unit clauses {P(c)} and {¬R(c, y)}.

**7.2**
- (a) {x ↦ g(z), w ↦ f(y)}.
- (b) None: x = a and x = b would force a = b, a clash.
- (c) None: y = x, then f(x) = x fails the occurs check.
- (d) {x ↦ a, z ↦ g(a), y ↦ f(g(a))}.
- (e) {x ↦ h(a), y ↦ h(a)}: f(x) = f(h(a)) gives x = h(a); g(y) = g(x) gives y = x = h(a).

**7.3** Clauses: 1. {¬P(x), Q(x)}; 2. {¬Q(x), R(x)}; 3. {P(a)}; 4. {¬R(a)}. Resolve 1, 3 (x ↦ a): {Q(a)}. Resolve with 2 (x ↦ a): {R(a)}. Resolve with 4: □.

**7.4** Premises: {¬P(x), Q(x)}, {P(c)} (Skolem constant c). Negated conclusion ¬∃x Q(x) ≡ ∀x ¬Q(x): {¬Q(x)}. Resolve {¬P(x), Q(x)} with {P(c)}: {Q(c)}. Resolve with {¬Q(x)}: □.

**7.5** Suppose C ∨ A and D ∨ ¬A are true under valuation v. If A is true under v, then ¬A is false, so D must be true, hence C ∨ D is true. If A is false, then C must be true, so C ∨ D is true.

**7.6** See Example 2′ in Chapter 7. The clause set is {R(f(y), y)} and {¬R(x, g(x))}. The only candidate resolution unifies R(f(y), y) with R(x, g(x)): x ↦ f(y), then y must equal g(f(y)), which fails the occurs check. No resolvent exists and no factors exist, so the set saturates without □, hence is satisfiable, and the entailment fails.

**7.7** *Drinker:* Example in Section 7.3. *Barber:* Example 3 in Section 7.5. Factoring is needed because each clause C₁ and C₂ contains two *unifiable* literals of the same sign, and binary resolution alone cannot reduce the number of literals.

**7.8** If φ is satisfiable, say M ⊨ φ. For ∃y inside the scope of ∀x₁..xₙ, define the Skolem function f_M(d₁..dₙ) := some witness for y, which exists by the semantic truth of ∃. Interpret f this way (choice). Then M extended with f satisfies φ_Sk. Conversely φ_Sk ⊨ φ, because from the Skolem witnesses you get ∃. But **φ ⊭ φ_Sk** (e.g., φ = ∃x P(x); φ_Sk = P(c); in D = {1, 2}, P = {1}, c ↦ 2, φ is true and φ_Sk false). So Skolemization is *equisatisfiable* but not *equivalent*.

**7.9** Instances of the second clause for x := a, f(a), f(f(a)); in total **3 instances** are needed: P(a); ¬P(a) ∨ P(f(a)); ¬P(f(a)) ∨ P(f(f(a))); ¬P(f(f(a))) ∨ P(f(f(f(a)))); ¬P(f(f(f(a)))). That is propositionally unsatisfiable. First-order resolution: resolve {P(a)} with the second clause (x ↦ a): {P(f(a))}; again: {P(f(f(a)))}; again: {P(f(f(f(a))))}; resolve with the goal: □. Four resolution steps in both approaches, but the first-order version never had to guess the instances: unification found them.

---

*End of the course. Send me your solutions to any problem (formal proofs line by line, informal proofs in prose, or code from the project) and I will check them, point out the exact line where something goes wrong, and suggest the next problem.*

---

# Appendix D. Glossary of logic terms (A–Z)

Short definitions, in plain words, with a pointer to where the idea is developed. Symbols are in Section Z4 and Appendix A.6; tool syntax is in Appendix E. When a term has two common names, both are listed and cross-referenced. "Prop." means propositional logic, "FOL" first-order (predicate) logic.

## A

**Absurdity** — see *Contradiction* and *Falsum*.

**Alpha-conversion (α-conversion)** — renaming a bound variable (and every occurrence it binds) without changing meaning: `∀x P(x)` and `∀y P(y)` are α-equivalent. Capture must be avoided. (Z1, 3.8.5)

**Antecedent** — the "if" part `A` of a conditional `A → B`. See *Consequent*.

**Argument** — a list of premises together with a conclusion. It is *valid* when the conclusion is true in every situation where all premises are true. (1.8.9)

**Arity** — the number of arguments a function or predicate symbol takes. `P(x)` has arity 1, `R(x, y)` arity 2; a symbol of arity 0 is a constant (function) or a proposition letter (predicate). (3.8.2)

**Assignment (valuation)** — in prop. logic, a choice of true/false for every proposition letter; in FOL, a map from variables to domain elements, written `s`, with `s[x↦d]` for "the same except `x` goes to `d`". (1.8.4, 3.8.8)

**Assumption** — a statement temporarily supposed true inside a subproof; it is *discharged* when the subproof closes (for example by `→I`). Not the same as a premise. (2.9.2)

**Atom, atomic formula** — a formula with no connective or quantifier: a proposition letter `P`, a predicate applied to terms `R(a, f(x))`, or an equation `s = t`. (1.8.3, 3.8.4)

**Axiom** — a formula accepted without proof inside a given system or theory. In Hilbert-style systems the axioms are schemas such as `A → (B → A)`. (2.9.7, 3.8.8)

**Axiom schema** — a template that yields infinitely many axioms, one for each way of filling in its metavariables. Induction in Peano arithmetic is a schema. (2.9.7, 6.7.1)

## B

**Biconditional** — `A ↔ B`: true exactly when `A` and `B` have the same truth value. Read "if and only if" (iff). (1.8.2)

**Bound variable** — an occurrence of a variable inside the scope of a quantifier that names it. Opposite of *free*. (3.8.5)

**Box** — in Fitch notation, the indented block that holds a subproof. Lines inside are visible only inside it. (2.9.2)

**BHK interpretation** — Brouwer–Heyting–Kolmogorov: the constructive reading of connectives as operations on proofs ("a proof of `A → B` is a method turning proofs of `A` into proofs of `B`"). (2.9.8)

## C

**Calculus** — a formal system of rules for manipulating formulas; "sequent calculus", "natural deduction", "tableau calculus". (2.9.1)

**Canonical form** — a unique-up-to-order normal form of a Boolean function: full DNF (one term per true row) or full CNF (one clause per false row). (1.8.7)

**Capture** — the error where substituting a term puts one of its free variables under a quantifier that binds the same name, changing the meaning. Avoided by α-conversion. (3.8.5)

**Categorical (theory)** — has exactly one model up to isomorphism. First-order theories with infinite models are never categorical, but may be categorical *in a cardinality*. (6.7.5)

**Clause** — a disjunction of literals, often written as a set: `{P, ¬Q, R}`. The empty clause `[]` is false. (1.8.7, 7.9.5)

**Closed formula** — see *Sentence*.

**CNF (conjunctive normal form)** — a conjunction of clauses (an AND of ORs of literals). Input format of SAT solvers. (1.8.7)

**Compactness theorem** — a set of FOL sentences has a model iff every finite subset has one. Consequences: non-standard models, no first-order definition of "finite". (6.7.4)

**Completeness** — *of a system:* every semantically valid formula is provable (`⊨ A` implies `⊢ A`). Gödel 1929 for FOL. Not to be confused with *negation-completeness* of a theory (which fails by Gödel's first theorem for arithmetic). (6.7.3)

**Conclusion** — the statement an argument or proof aims to establish.

**Conditional** — `A → B`; false only when `A` is true and `B` false. Also called *material implication* or *material conditional*. (1.8.2)

**Congruence** — an equivalence relation compatible with the function symbols; the basis of the equality axioms. (4.7.8)

**Conjunction** — `A ∧ B`, "and"; true when both are. `A` and `B` are *conjuncts*. (1.8.2)

**Connective** — a symbol combining formulas into a bigger formula: `¬ ∧ ∨ → ↔` (and `⊥ ⊤` as 0-ary connectives). (1.8.2)

**Consequence (semantic)** — `Γ ⊨ A`: every model of all of `Γ` is a model of `A`. (1.8.9, 3.8.8)

**Consequence (syntactic)** — `Γ ⊢ A`: there is a proof of `A` from `Γ`. (2.9.1)

**Consequent** — the "then" part `B` of `A → B`.

**Consistent** — a set `Γ` is consistent if `Γ ⊬ ⊥`: nothing contradictory can be proved from it. A set with a model is consistent (soundness); the converse is completeness. (6.7.3)

**Constant** — a function symbol of arity 0; names one particular object. (3.8.2)

**Constructive logic** — see *Intuitionistic logic*.

**Contingent** — true in some situations and false in others (neither a tautology nor a contradiction). (1.8.4)

**Contradiction** — a formula false in every situation (e.g. `P ∧ ¬P`); also the act of deriving `⊥`. (1.8.4)

**Contraposition, contrapositive** — `¬B → ¬A` is the contrapositive of `A → B`; the two are equivalent. Not the same as the *converse* `B → A`. (1.8.6)

**Converse** — `B → A` for the conditional `A → B`. Not equivalent. (1.8.6)

**Counterexample** — a situation that makes all premises true and the conclusion false; proves invalidity. (1.8.9)

**Countermodel** — a model (structure) serving as a counterexample in FOL. (3.8.8, 8.8.3)

**Curry–Howard correspondence** — propositions are types, proofs are programs: `A → B` is a function type, `A ∧ B` a pair type, `A ∨ B` a sum type. (2.9.8)

**Cut** — a proof step that introduces and then eliminates a lemma; *cut-elimination* (Gentzen) shows it is dispensable in sequent calculus. (2.9.7)

## D

**Decidable** — there is an algorithm that always halts with the right yes/no answer. Prop. validity is decidable; FOL validity is not (Church–Turing). (6.7.6)

**Deduction theorem** — if `Γ, A ⊢ B` then `Γ ⊢ A → B`; the metatheorem behind `→I`. (2.9.7)

**Definite description** — a phrase "the unique `x` such that …", formalised as `∃x (P(x) ∧ ∀y (P(y) → y = x))` (Russell) or with the symbol `ιx`. (3.8.6)

**De Morgan's laws** — `¬(A ∧ B) ≡ ¬A ∨ ¬B`, `¬(A ∨ B) ≡ ¬A ∧ ¬B`; and for quantifiers `¬∀x A ≡ ∃x ¬A`, `¬∃x A ≡ ∀x ¬A`. (1.8.6)

**Derivation** — see *Proof*.

**Derived rule** — a rule whose use can always be replaced by a fixed sequence of primitive rules. (2.9.6)

**Disjunction** — `A ∨ B`, inclusive "or"; false only when both are false. (1.8.2)

**Discharge** — closing an assumption: after `→I` the assumed `A` no longer counts as an open premise. (2.9.2)

**Disjunctive syllogism** — from `A ∨ B` and `¬A` infer `B`. (1.8.9)

**DNF (disjunctive normal form)** — an OR of ANDs of literals. (1.8.7)

**Domain (universe, domain of discourse)** — the non-empty set of objects the quantifiers range over in a structure. (3.8.8)

**Double negation** — `¬¬A ≡ A` classically; only `A → ¬¬A` holds intuitionistically. (1.8.6, 2.9.8)

**DPLL, CDCL** — complete backtracking SAT algorithms based on unit propagation (DPLL) and conflict-driven clause learning (CDCL). (7.9.2)

## E

**Eigenvariable** — the fresh variable or name in `∀I`/`∃E` (Gentzen's term). See *Fresh name*. (4.7.1)

**Elementary equivalence** — two structures satisfy the same first-order sentences. Isomorphic structures are elementarily equivalent; the converse fails. (6.7.5)

**Entailment** — see *Consequence*.

**Equivalence (logical)** — `A ≡ B`: `A ↔ B` is a tautology/valid; they have the same truth value in every model. (1.8.4)

**Equisatisfiable** — one formula is satisfiable iff the other is; weaker than equivalence. Skolemization and Tseitin produce equisatisfiable results. (7.9.3)

**Ex falso quodlibet (explosion)** — from a contradiction anything follows: `⊥ ⊢ A`. Rule `⊥E`. (2.9.3)

**Excluded middle** — `A ∨ ¬A`; classically valid, rejected by intuitionists. (2.9.8)

**Existential quantifier** — `∃x A`: some element of the domain satisfies `A`. (3.8.6)

**Extensionality** — objects are equal when they have the same members/values; for sets, `A = B` iff same elements. (Z3)

## F

**Factoring** — in resolution, unifying and merging two literals of the same clause. (7.9.5)

**Falsum, absurdum (⊥)** — the constant "false". (2.9.3)

**Finitary / finitistic** — using only finite, constructive reasoning (Hilbert's program).

**First-order logic** — logic whose quantifiers range over individuals (not over predicates or sets). Also *predicate logic*, *quantification theory*, *FOL*. (Ch. 3)

**Fitch system** — natural deduction written with indented boxes for subproofs. (2.9.2)

**Formal language** — the set of well-formed formulas over a fixed alphabet and grammar. (1.8.3)

**Formal system** — a language plus axioms and/or rules plus a notion of proof. (2.9.1)

**Formula (well-formed formula, wff)** — a string built by the grammar's formation rules. (1.8.3, 3.8.4)

**Free variable** — an occurrence not bound by any quantifier; a formula with free variables is *open*. (3.8.5)

**Fresh name** — a constant (or variable) that occurs nowhere else in the proof's relevant context; required by `∀I` and `∃E`. (4.7.1)

**Function symbol** — a symbol that forms terms: `f(x)`, `+`. (3.8.2)

**Functional completeness** — a set of connectives able to express every truth function, e.g. `{¬, ∧}`, `{NAND}`. (1.8.8)

## G

**Gentzen systems** — natural deduction (NJ/NK) and sequent calculi (LJ/LK), both by Gerhard Gentzen (1935). (2.9.7)

**Gödel numbering** — assigning each formula/proof a natural number so arithmetic can talk about syntax. (6.7.7)

**Gödel's theorems** — *Completeness* (1929) and *Incompleteness* (1931; two theorems). (6.7.3, 6.7.7)

## H

**Herbrand universe/theorem** — the set of ground terms; a set of clauses is unsatisfiable iff some finite set of its ground instances is propositionally unsatisfiable. Basis of automated provers. (7.9.5)

**Hilbert system** — a proof system with many axiom schemas and (usually) modus ponens as the only rule. (2.9.7)

**Horn clause** — a clause with at most one positive literal; the logic of Prolog. Horn satisfiability is decidable in linear time (prop. case). (7.9.5)

**Hypothetical syllogism** — from `A → B` and `B → C` infer `A → C`. (1.8.9)

## I

**Identity** — see *Equality*.

**Implication** — the connective `→`; also the relation "A implies B", meaning `A → B` is valid. (1.8.2)

**Inconsistent** — proves `⊥`; the opposite of consistent.

**Independence** — a statement is independent of a theory if neither it nor its negation is provable (e.g. the continuum hypothesis in ZFC). (6.7.7)

**Induction** — proving a statement for all naturals (or all objects built by a recursive definition) via a base case and an inductive step. (5.14.4)

**Inference rule** — a pattern "from these formulas (premises) conclude that formula". (2.9.1)

**Instance** — the result of substituting terms for variables: `P(a)` is an instance of `∀x P(x)`. (3.8.5)

**Interpretation** — see *Structure*.

**Intuitionistic logic** — logic without excluded middle and double-negation elimination; "provable" means "constructively demonstrated". (2.9.8)

**Invalid** — an argument/formula that has a counterexample.

**Isomorphism** — a bijection between structures preserving all functions and relations. (6.7.5)

## K

**Kripke semantics** — models for modal and intuitionistic logic: sets of "worlds" with an accessibility relation. (6.7.9)

## L

**Lemma** — a helper theorem proved on the way to a larger result.

**Literal** — an atom or a negated atom: `P`, `¬P`. (1.8.7)

**Logical consequence** — see *Consequence*.

**Logical constant** — a symbol whose meaning is fixed by the logic: connectives, quantifiers, (usually) equality.

**Löwenheim–Skolem theorems** — a first-order theory with an infinite model has models of every infinite cardinality (upward) and a countable one (downward). (6.7.5)

## M

**Many-valued logic** — logic with more than two truth values (Łukasiewicz, Kleene, fuzzy). (6.7.9)

**Material implication** — see *Conditional*. "Material" means truth-functional, defined purely by truth values.

**Metalanguage / object language** — the language we use to talk *about* a logic versus the logic's own language. `⊢` and `⊨` live in the metalanguage. (Z4.3)

**Metatheorem, metatheory** — a theorem *about* a system (soundness, completeness, compactness). (Ch. 6)

**Model** — a structure in which a given sentence/set of sentences is true. `M ⊨ A`. (3.8.8)

**Modal logic** — logic with `□` ("necessarily") and `◇` ("possibly"). (6.7.9)

**Modus ponens (MP, →E)** — from `A → B` and `A` infer `B`. (2.9.3)

**Modus tollens (MT)** — from `A → B` and `¬B` infer `¬A`. (1.8.9)

## N

**Natural deduction** — proof systems with introduction and elimination rules for every connective, designed to mirror human reasoning. (Ch. 2)

**Necessary / sufficient condition** — in `A → B`, `A` is *sufficient* for `B` and `B` is *necessary* for `A`. (1.8.2)

**Negation** — `¬A`, "not". (1.8.2)

**NNF (negation normal form)** — negations apply only to atoms. (1.8.7)

**Non-standard model** — a model of true arithmetic containing "infinite" numbers; exists by compactness. (6.7.4)

**Normal form** — a restricted syntactic shape every formula can be converted to: NNF, CNF, DNF, prenex, Skolem. (1.8.7, 7.9.3)

## O

**Omega-consistency** — a strengthening of consistency used in Gödel's original first theorem.

**Open formula** — contains free variables; neither true nor false until the variables are assigned. (3.8.5)

## P

**Paradoxes of material implication** — `B ⊢ A → B` and `¬A ⊢ A → B` are valid though they sound odd in English. (1.8.9)

**Peano arithmetic (PA)** — the first-order theory of the natural numbers with an induction schema. (3.8.8)

**Peirce's law** — `((A → B) → A) → A`: classically valid, equivalent to excluded middle, intuitionistically unprovable. (1.8.6)

**Predicate** — a symbol for a property (arity 1) or relation (arity ≥ 2); applied to terms it yields an atomic formula. (3.8.2)

**Premise** — a formula given as true at the start of a proof or argument.

**Prenex normal form** — all quantifiers at the front, followed by a quantifier-free matrix. (7.9.3)

**Proof** — a finite, rule-governed sequence/tree of formulas ending in the conclusion, each step justified. (2.9.1)

**Proof by cases** — `∨E`: if `A ∨ B`, and `C` follows from `A` and also from `B`, then `C`. (2.9.3)

**Proof by contradiction** — assume `¬A`, derive `⊥`, conclude `A` (RAA). Distinguish from *proof of negation* (assume `A`, derive `⊥`, conclude `¬A`; fine intuitionistically). (5.14.3)

**Proposition** — a statement that is definitely true or false. In formal logic, a formula of prop. logic. (1.8.1)

**Propositional logic (sentential logic, Boolean logic)** — the logic of connectives alone. (Ch. 1)

## Q

**Quantifier** — `∀` or `∃`; binds a variable. (3.8.6)

**Quantifier scope** — the sub-formula a quantifier governs. (3.8.5, Z5.1.1)

## R

**RAA (reductio ad absurdum)** — see *Proof by contradiction*.

**Refutation** — a proof that a set of formulas is unsatisfiable; resolution is a refutation method. (7.9.5)

**Relation** — a set of tuples; the semantic value of a predicate symbol. (Z3)

**Resolution** — an inference rule on clauses: from `C ∨ L` and `D ∨ ¬L` infer `C ∨ D`; refutation-complete. (7.9.5)

**Rule of inference** — see *Inference rule*.

## S

**SAT problem** — decide whether a prop. formula (usually CNF) is satisfiable; NP-complete (Cook–Levin). (7.9.2)

**Satisfiable** — true under at least one assignment/model. (1.8.4)

**Schema** — see *Axiom schema*.

**Scope** — see *Quantifier scope*.

**Semantics** — the study of meaning/truth of formulas: valuations, structures. (1.8.4, 3.8.8)

**Sentence** — a formula with no free variables; the only kind with a definite truth value in a structure. Also *closed formula*. (3.8.5)

**Sequent** — `Γ ⊢ Δ`: from the assumptions listed in `Γ`, at least one of `Δ` follows. (2.9.7)

**Signature (vocabulary, language)** — the list of constant, function and predicate symbols with arities. (3.8.2)

**Skolemization** — eliminating `∃` by introducing fresh function symbols (Skolem functions) of the preceding universal variables. (7.9.3)

**SMT** — satisfiability modulo theories: SAT combined with arithmetic, arrays, etc. (7.9.6)

**Soundness** — *of a system:* everything provable is valid (`⊢ A` implies `⊨ A`). *Of an argument* (everyday sense): valid with true premises. (6.7.2)

**Structure** — a domain plus an interpretation of each symbol of a signature; also *model* (when it satisfies given sentences) or *interpretation*. (3.8.8)

**Substitution** — replacing free occurrences of a variable by a term: `A[t/x]`. Also a map from variables to terms in unification. (3.8.5, 7.9.4)

**Syllogism** — a three-line argument with two premises, in Aristotle's logic, e.g. Barbara: all M are P, all S are M, so all S are P. (Z1)

**Syntax** — the study of the *form* of formulas and proofs, apart from meaning. (1.8.3)

## T

**Tableau (truth tree)** — a refutation method that breaks formulas apart along branches; a closed tableau refutes. (2.9.7)

**Tarski's definition of truth** — truth of a formula in a structure by recursion on its structure. (3.8.8)

**Tautology** — true under every assignment (prop.). The FOL analogue is *validity*. (1.8.4)

**Term** — an expression naming an object: variable, constant, or function applied to terms. (3.8.3)

**Theory** — a set of sentences closed under consequence (or its axiomatisation). (3.8.8)

**Theorem** — a statement with a proof; in a formal system, a formula derivable from the axioms. (2.9.1)

**Truth function** — a function from truth values to truth values; there are `2^(2^n)` of them with `n` inputs. (1.8.5)

**Truth table** — a listing of a formula's value under every assignment. (1.8.4)

**Tseitin transformation** — converts any prop. formula into an equisatisfiable CNF of linear size by naming sub-formulas. (7.9.3)

**Turing machine** — the standard formal model of computation behind decidability results. (6.7.6)

## U

**Unification** — finding a substitution that makes two terms/atoms identical; the most general such is the *mgu*. (7.9.4)

**Uniqueness quantifier `∃!`** — "exactly one": `∃x (P(x) ∧ ∀y (P(y) → y = x))`. (3.8.6)

**Universal closure** — prefixing `∀` for every free variable, turning a formula into a sentence. (3.8.5)

**Universal quantifier** — `∀x A`: every element of the domain satisfies `A`. (3.8.6)

**Unsatisfiable** — no model/assignment makes it true. (1.8.4)

## V

**Valid, validity** — *of a formula:* true in every structure (FOL) or assignment (prop.). *Of an argument:* conclusion true whenever premises are. (1.8.4, 1.8.9)

**Valuation** — see *Assignment*.

**Variable** — a placeholder ranging over the domain; either free or bound. (3.8.2)

## W–Z

**Well-formed formula (wff)** — see *Formula*.

**Well-ordering principle** — every non-empty set of naturals has a least element; equivalent to induction. (5.14.4)

**Witness** — an object shown to satisfy an existential statement. (4.7.1)

**Zermelo–Fraenkel set theory (ZF, ZFC)** — the standard first-order theory in which most mathematics is formalised; ZFC adds the axiom of choice. (6.7.7)

---

# Appendix E. Typing symbols and tool syntax: a cheat sheet

This appendix answers the practical questions: *How do I type `∀`? How do I write the same formula for Prover9, Z3, Lean or LaTeX? What does the input file for a SAT solver look like?* Prover installation is not covered, only what you write once you have one. Where a tool was run while preparing this book (Z3 via Python and SMT-LIB), the snippet is marked **tested**; the others follow the tools' documented syntax and you should expect to adjust minor details for your version.

## E.1 Typing logic symbols

**Method 1: copy and paste.** Every symbol in this book can be pasted from here: `¬ ∧ ∨ → ↔ ⊥ ⊤ ∀ ∃ ⊢ ⊨ ≡ ∈ ∉ ⊆ ∪ ∩ ∅ ≠ ≤ ≥ ⇒ ⇔ □ ◇ ∴ ∎ ℕ ℤ ℚ ℝ λ`.

**Method 2: operating-system shortcuts by code point.** Each symbol has a Unicode *code point* (a hexadecimal number). Typical entry methods:

| System | How to enter a code point such as U+2200 |
| --- | --- |
| Linux (GTK apps, many terminals) | Ctrl+Shift+U, type `2200`, press Space or Enter |
| macOS | Enable "Unicode Hex Input" keyboard, hold Option, type `2200` |
| Windows | Hold Alt, type `+2200` on the numeric pad (needs the registry setting "EnableHexNumpad"), or use Win+. (emoji/symbol panel) and search |
| Any system | Use the Character Map / Character Viewer / Emoji & Symbols picker |

**Method 3: editor abbreviations** (fastest if you write a lot). In Lean's editor mode, in Emacs/TeX input mode, and in VS Code with a LaTeX-abbreviation extension, you type a backslash name and the symbol appears. The Lean/TeX names below work in Lean 4's VS Code and Emacs modes.

| Symbol | Name | Unicode | LaTeX | Lean abbreviation | ASCII in this book |
| --- | --- | --- | --- | --- | --- |
| ¬ | negation | U+00AC | `\neg` (`\lnot`) | `\not`, `\neg` | `~` |
| ∧ | and | U+2227 | `\land` (`\wedge`) | `\and` | `&` |
| ∨ | or | U+2228 | `\lor` (`\vee`) | `\or` | `\|` |
| → | implies | U+2192 | `\to` (`\rightarrow`) | `\to`, `\r` | `->` |
| ↔ | iff | U+2194 | `\leftrightarrow` | `\iff`, `\lr` | `<->` |
| ⊥ | falsum | U+22A5 | `\bot` | `\bot` | `false` |
| ⊤ | verum | U+22A4 | `\top` | `\top` | `true` |
| ∀ | for all | U+2200 | `\forall` | `\forall`, `\all` | `forall` |
| ∃ | exists | U+2203 | `\exists` | `\exists`, `\ex` | `exists` |
| ⊢ | proves | U+22A2 | `\vdash` | `\vdash` | `\|-` |
| ⊨ | models | U+22A8 | `\models` (`\vDash`) | `\models` | `\|=` |
| ≡ | equivalent | U+2261 | `\equiv` | `\==` | `==` |
| = | equals | U+003D | `=` | `=` | `=` |
| ≠ | not equal | U+2260 | `\neq` (`\ne`) | `\ne` | `!=` |
| ∈ | element of | U+2208 | `\in` | `\in` | `in` |
| ∉ | not element | U+2209 | `\notin` | `\notin` | `not in` |
| ⊆ | subset | U+2286 | `\subseteq` | `\sub=`, `\subseteq` | `subseteq` |
| ∪ | union | U+222A | `\cup` | `\cup`, `\union` | `union` |
| ∩ | intersection | U+2229 | `\cap` | `\cap`, `\inter` | `inter` |
| ∅ | empty set | U+2205 | `\emptyset` (`\varnothing`) | `\empty` | `{}` |
| ≤ | at most | U+2264 | `\le` (`\leq`) | `\le` | `<=` |
| ⇒ | double arrow | U+21D2 | `\Rightarrow` | `\=>` | `=>` |
| ⇔ | double iff | U+21D4 | `\Leftrightarrow` | `\<=>` | `<=>` |
| □ | box (necessarily) | U+25A1 | `\Box` | `\box` | `[]` |
| ◇ | diamond (possibly) | U+25C7 | `\Diamond` | `\di` | `<>` |
| ∴ | therefore | U+2234 | `\therefore` | `\therefore` | `therefore` |
| ∎ | end of proof | U+220E | `\qed` / `\blacksquare` | `\qed` | `QED` |
| ℕ ℤ ℚ ℝ | number sets | U+2115 U+2124 U+211A U+211D | `\mathbb{N}` etc. | `\N \Z \Q \R` | `N Z Q R` |
| λ | lambda | U+03BB | `\lambda` | `\lam`, `\fun` | `fun` |

Subscripts and superscripts: `x₁` is U+2081; type `x\_1` in Lean. In LaTeX write `x_1`, `x^2`.

## E.2 LaTeX in practice

Minimal document with a proof environment:

```latex
\documentclass{article}
\usepackage{amsmath, amssymb, amsthm}
\newtheorem{theorem}{Theorem}
\begin{document}

\begin{theorem}
For all sets $A, B$: $A \cap B \subseteq A$.
\end{theorem}
\begin{proof}
Let $x \in A \cap B$. Then $x \in A$ and $x \in B$; in particular $x \in A$.
\end{proof}

A formula: $\forall x\,\bigl(P(x) \to \exists y\, R(x,y)\bigr)$.

A derivation line: $P \to Q,\; Q \to R \vdash P \to R$.

\[
\frac{A \to B \quad A}{B}\ {\to}E
\]
\end{document}
```

Notes: `\,` inserts a thin space after a quantifier; `\bigl( … \bigr)` makes brackets taller; `\frac{top}{bottom}` draws an inference-rule bar; `{\to}E` stops LaTeX treating `\to` as a binary relation with spaces. For Fitch boxes, packages such as `fitch` (or `logicproof`) draw the vertical rules.

## E.3 One formula in every syntax

The formula: *for every x, if P(x) holds then there exists y with R(x, y)*.

| Syntax | Writing it |
| --- | --- |
| Math (Unicode) | `∀x (P(x) → ∃y R(x, y))` |
| This book's ASCII (and the Chapter 8 starter) | `forall x. P(x) -> exists y. R(x, y)` |
| LaTeX | `\forall x\,(P(x) \to \exists y\, R(x,y))` |
| TPTP (FOF) | `![X]: (p(X) => ?[Y]: r(X,Y))` |
| Prover9 / Mace4 | `all x (P(x) -> exists y R(x,y)).` |
| SMT-LIB | `(forall ((x D)) (=> (P x) (exists ((y D)) (R x y))))` |
| Z3 Python | `ForAll([x], Implies(P(x), Exists([y], R(x, y))))` |
| Lean 4 | `∀ x, P x → ∃ y, R x y` |
| Coq / Rocq | `forall x, P x -> exists y, R x y` |
| Isabelle/HOL | `∀x. P x ⟶ (∃y. R x y)` |
| Prolog | not expressible directly (Horn clauses only); a rule such as `q(X) :- p(X).` |
| Polish notation | `ΠxCPxΣyRxy` (Π = for all, Σ = exists, C = implies) |

## E.4 The connectives in every syntax

| Meaning | TPTP | Prover9 | SMT-LIB | Z3 Python | Lean 4 | Coq |
| --- | --- | --- | --- | --- | --- | --- |
| not | `~A` | `-A` | `(not A)` | `Not(A)` | `¬A` | `~A` |
| and | `A & B` | `A & B` | `(and A B)` | `And(A, B)` | `A ∧ B` | `A /\ B` |
| or | `A \| B` | `A \| B` | `(or A B)` | `Or(A, B)` | `A ∨ B` | `A \/ B` |
| implies | `A => B` | `A -> B` | `(=> A B)` | `Implies(A, B)` | `A → B` | `A -> B` |
| iff | `A <=> B` | `A <-> B` | `(= A B)` | `A == B` (Bool) | `A ↔ B` | `A <-> B` |
| for all | `![X]: A` | `all x A` | `(forall ((x S)) A)` | `ForAll([x], A)` | `∀ x, A` | `forall x, A` |
| exists | `?[X]: A` | `exists x A` | `(exists ((x S)) A)` | `Exists([x], A)` | `∃ x, A` | `exists x, A` |
| equals | `a = b` | `a = b` | `(= a b)` | `a == b` | `a = b` | `a = b` |
| not equal | `a != b` | `a != b` | `(distinct a b)` | `a != b` | `a ≠ b` | `a <> b` |
| false / true | `$false` / `$true` | `$F` / `$T` | `false` / `true` | `BoolVal(False)` | `False` / `True` | `False` / `True` |

Two warnings: in Prover9, symbols beginning with `u` through `z` are variables by default (the same convention as Chapter 8's starter kit); in TPTP, variables start with an upper-case letter and predicates/functions with lower-case.

## E.5 Z3 from Python (tested)

Install with `pip install z3-solver`. To check whether an argument is valid, assert the premises and the *negated* conclusion, and ask for satisfiability: `unsat` means valid.

```python
from z3 import *

D = DeclareSort('D')                  # a domain with no further structure
P = Function('P', D, BoolSort())      # a unary predicate
Q = Function('Q', D, BoolSort())
x = Const('x', D)
a = Const('a', D)

s = Solver()
s.add(ForAll([x], Implies(P(x), Q(x))), P(a))   # premises
s.add(Not(Q(a)))                                # negated conclusion
print(s.check())                                # unsat  => the argument is valid
```

Output: `unsat`. An invalid argument yields a countermodel:

```python
s2 = Solver()
s2.add(Exists([x], P(x)), Not(ForAll([x], P(x))))
print(s2.check())     # sat
print(s2.model())     # for example: [P = [D!val!1 -> False, else -> True]]
```

Output: `sat`, followed by a model in which `P` holds of some element but not another. For propositional tautologies, Z3's helper `prove(formula)` prints `proved` or a counterexample:

```python
p, q = Bools('p q')
prove(Implies(And(Implies(p, q), p), q))     # prints: proved
```

## E.6 SMT-LIB (tested)

The same argument as a stand-alone file `argument.smt2`, runnable with any SMT solver (`z3 argument.smt2`, `cvc5 argument.smt2`):

```text
(declare-sort D 0)
(declare-fun P (D) Bool)
(declare-fun Q (D) Bool)
(declare-const a D)
(assert (forall ((x D)) (=> (P x) (Q x))))
(assert (P a))
(assert (not (Q a)))
(check-sat)
```

Output: `unsat`. Reading rules: everything is a parenthesised prefix expression `(function arg1 arg2 …)`; `declare-sort`, `declare-fun`, `declare-const` introduce vocabulary; `assert` adds a fact; `check-sat` asks for `sat`, `unsat` or `unknown`; add `(get-model)` after a `sat` answer to see the model. Arithmetic uses sort `Int` or `Real` and operators `+ - * <= <`.

## E.7 DIMACS CNF for SAT solvers

A SAT solver reads clauses of integers: variable `n` means atom number `n`, `-n` its negation, and `0` ends a clause. The header gives the number of variables and clauses.

```text
c (P or Q) and (not P or Q) and (P or not Q)   with P = 1, Q = 2
p cnf 2 3
1 2 0
-1 2 0
1 -2 0
```

This is satisfiable (take `P = Q = true`). Add the clause `-1 -2 0` and update the header to `p cnf 2 4` to make it unsatisfiable. Lines starting with `c` are comments. The chapter 8 starter's `dpll` takes the same clauses as lists, e.g. `dpll([[1, 2], [-1, 2], [1, -2]])`.

## E.8 TPTP and Prover9 files

**TPTP** (`.p` file; run with `eprover --auto socrates.p` or `vampire socrates.p`):

```text
fof(all_men_mortal, axiom, ![X]: (man(X) => mortal(X))).
fof(socrates_man,  axiom, man(socrates)).
fof(goal, conjecture, mortal(socrates)).
```

**Prover9** (`prover9 -f socrates.in`):

```text
formulas(assumptions).
  all x (man(x) -> mortal(x)).
  man(socrates).
end_of_list.

formulas(goals).
  mortal(socrates).
end_of_list.
```

To search for a countermodel instead, use **Mace4** on the same input with the goal that you suspect is false. If a clause set is satisfiable, a refutation prover such as these may run forever without answer; that is the semi-decidability of Section 6.7.6, not a bug.

## E.9 Lean 4 cheat sheet

A first proof, in tactic style (each `·` marks a case; hover in the editor to see the goal):

```lean
theorem hyp_syllogism (P Q R : Prop) (h1 : P → Q) (h2 : Q → R) : P → R := by
  intro hp
  apply h2
  apply h1
  exact hp

theorem and_comm' (P Q : Prop) : P ∧ Q → Q ∧ P := by
  intro ⟨hp, hq⟩
  exact ⟨hq, hp⟩

theorem exists_mono (P Q : Nat → Prop) (h : ∀ x, P x → Q x) :
    (∃ x, P x) → ∃ x, Q x := by
  intro ⟨a, ha⟩
  exact ⟨a, h a ha⟩
```

Which tactic does which proof rule?

| Goal or hypothesis | Tactic | Natural-deduction rule |
| --- | --- | --- |
| goal `A → B` | `intro h` | →I |
| goal `∀ x, A x` | `intro a` | ∀I (fresh `a`) |
| goal `A ∧ B` | `constructor` (then two goals) or `exact ⟨ha, hb⟩` | ∧I |
| goal `A ∨ B` | `left` / `right` | ∨I |
| goal `∃ x, A x` | `exact ⟨t, h⟩` or `use t` | ∃I |
| goal `¬A` | `intro h` (h : A, goal False) | ¬I |
| goal `False` from `A` and `¬A` | `exact h2 h1` | ¬E |
| any goal from `False` | `exfalso` or `contradiction` | ⊥E |
| goal `A`, by contradiction | `by_contra h` | RAA (classical) |
| hypothesis `h : A ∧ B` | `obtain ⟨ha, hb⟩ := h` | ∧E |
| hypothesis `h : A ∨ B` | `rcases h with ha \| hb` | ∨E |
| hypothesis `h : ∃ x, A x` | `obtain ⟨a, ha⟩ := h` | ∃E |
| hypothesis `h : ∀ x, A x` | `have := h t` | ∀E |
| hypothesis `h : A → B`, have `ha : A` | `have := h ha` | →E |
| equation `h : a = b` | `rw [h]` | =E |
| induction on `n : Nat` | `induction n with \| zero => … \| succ k ih => …` | induction |
| arithmetic and cleanup | `omega`, `simp`, `decide`, `linarith` (Mathlib) | — |

## E.10 Coq / Rocq cheat sheet

```text
Theorem hyp_syllogism : forall P Q R : Prop, (P -> Q) -> (Q -> R) -> P -> R.
Proof.
  intros P Q R h1 h2 hp.
  apply h2. apply h1. exact hp.
Qed.
```

| Goal or hypothesis | Tactic | Rule |
| --- | --- | --- |
| goal `A -> B` or `forall x, A x` | `intro` / `intros` | →I, ∀I |
| goal `A /\ B` | `split` | ∧I |
| goal `A \/ B` | `left` / `right` | ∨I |
| goal `exists x, A x` | `exists t` | ∃I |
| hypothesis `h : A /\ B` | `destruct h as [ha hb]` | ∧E |
| hypothesis `h : A \/ B` | `destruct h as [ha \| hb]` | ∨E |
| hypothesis `h : exists x, A x` | `destruct h as [a ha]` | ∃E |
| hypothesis `h : A -> B` | `apply h` (backward) or `specialize (h ha)` | →E |
| `False` anywhere | `contradiction` or `exfalso` | ⊥E |
| equation | `rewrite h`, `reflexivity` | =E, =I |
| induction | `induction n as [\| k ih]` | induction |
| automation | `auto`, `tauto`, `lia` (arithmetic), `firstorder` | — |

Classical reasoning (excluded middle, RAA) needs `Require Import Classical.` and the lemma `classic`; Coq's default logic is intuitionistic, matching Section 2.9.8.

## E.11 Prolog (Horn clauses in practice)

```text
mortal(X) :- man(X).      % for all X: man(X) implies mortal(X)
man(socrates).
?- mortal(socrates).      % query; the system answers: true.
```

`:-` reads "if", a comma means "and", and each clause ends with a period. Variables start with a capital letter. Prolog proves a goal by *SLD resolution* (Section 7.9.5). It cannot express `∨` in the conclusion or an unrestricted `∃` in the premises, which is why it is not a general first-order prover.

## E.12 Choosing a tool

| Your goal | Use |
| --- | --- |
| Check a propositional formula or build a CNF for a solver | The Chapter 8 starter (`sat`, `tseitin`), or a SAT solver with DIMACS input |
| Decide arithmetic, arrays, bit-vectors, "find me a counterexample" | Z3 or cvc5 (SMT-LIB) |
| Prove a pure first-order statement automatically | Vampire, E (TPTP), Prover9 |
| Find a small finite countermodel | Mace4, Z3 `model()`, the starter's `find_countermodel` |
| Write proofs checked by a tiny trusted kernel | Lean 4, Coq/Rocq, Isabelle |
| Learn proof construction interactively with Fitch boxes | A Fitch-style checker (the Chapter 8 starter's `check_proof`, or a textbook's web checker) |
| Logic programming and deductive databases | Prolog, Datalog |
