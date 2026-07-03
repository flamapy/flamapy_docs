---
layout: default
title: CNF encodings (Tseytin)
parent: Flamapy as framework
permalink: /framework/cnf_encodings
nav_order: 4
---

# CNF encodings: distributive and Tseytin
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Why this matters

When a feature model is analysed with a SAT backend, its cross-tree constraints are translated
into Conjunctive Normal Form (CNF) before being handed to the solver. {% include flamapy.html %}
stores each constraint as an Abstract Syntax Tree (`AST`, in
`flamapy.core.models.ast`) and offers two ways to turn that tree into clauses:

- **Distributive** (the default): repeatedly applies the distributive law. It is simple and returns
  clauses over the constraint's own variables, but its size can grow **exponentially** for formulas
  such as long `XOR` chains or wide equivalences.
- **Tseytin**: the [Tseytin transformation](https://en.wikipedia.org/wiki/Tseytin_transformation)
  introduces one auxiliary variable per logical gate, producing an **equisatisfiable** CNF whose size
  is **linear** in the formula.

For example, the distributive CNF of a 5-variable `XOR` chain already expands to thousands of clauses,
while the Tseytin encoding of the same constraint stays in the low tens.

{: .note }
> Tseytin is a **framework-only, opt-in** feature. It is **not** exposed through the Python facade
> (`FLAMAFeatureModel`) or the CLI; the default encoding everywhere remains the distributive one.

## Semantics: model-count preserving

The encoding uses **full biconditional gates** (`gate ⇔ subformula`). As a consequence every model of the
original constraint extends to **exactly one** model of the encoded formula. Once the auxiliary variables
are projected out, results that depend on counting or enumerating configurations
(`ConfigurationsNumber`, `Configurations`, `Sampling`) are **unchanged**. The auxiliary variables are
registered as solver variables but kept **out of the feature set**, so they never appear in
configurations, feature lists or counts.

## Using it from the AST

```python
from flamapy.core.models.ast import AST, ASTOperation, Node

ast = AST.create_binary_operation(ASTOperation.XOR, Node('A'), Node('B'))

# Default distributive CNF
clauses = ast.get_clauses()                       # method='distributive'

# Tseytin CNF (clauses may contain auxiliary variables)
clauses = ast.get_clauses(method='tseytin')

# When you also need the auxiliary variable names (e.g. to register them yourself)
clauses, aux_names = ast.get_clauses_with_aux(method='tseytin')
```

## Using it from the transformations

The SAT-oriented transformations accept a `cnf_method` argument. Pass `'tseytin'` to encode the
cross-tree constraints with the Tseytin transformation:

```python
from flamapy.metamodels.fm_metamodel.transformations import UVLReader
from flamapy.metamodels.pysat_metamodel.transformations import FmToPysat

fm = UVLReader('model.uvl').transform()

# Default (distributive)
sat_model = FmToPysat(fm).transform()

# Opt in to Tseytin
sat_model = FmToPysat(fm, cnf_method='tseytin').transform()
```

The same `cnf_method='tseytin'` option is available on:

- `FmToPysat` (`flamapy-sat`) and `FmToDiagPysat` (`flamapy-sat` diagnosis metamodel).
- `FmToZ3` (`flamapy-z3`) — see the caveat below.

## Z3 caveat: propositional constraints only

Z3 is an SMT solver and already clausifies internally, so Tseytin brings **no performance benefit** there;
`FmToZ3(fm, cnf_method='tseytin')` is provided only for cross-backend uniformity and experimentation.
It is applied **only** to purely propositional boolean constraints. Any constraint involving arithmetic,
comparison, aggregation or typed (Integer/Real/String) features automatically **falls back** to the direct
Z3 translation.

## When to use which

- Keep the **default distributive** encoding for typical models — it is simplest and adds no auxiliary
  variables.
- Switch to **Tseytin** when a model contains constraints that make the distributive expansion explode
  (long `XOR`/`⇔` chains, deeply nested disjunctions of conjunctions) and the SAT translation becomes slow
  or memory-hungry.
