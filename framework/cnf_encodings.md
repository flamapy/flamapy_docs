---
layout: default
title: CNF encodings (auto, distributive, Tseytin)
parent: Flamapy as framework
permalink: /framework/cnf_encodings
nav_order: 4
---

# CNF encodings: auto, distributive and Tseytin
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

- **Distributive**: repeatedly applies the distributive law. It is simple and returns clauses over the
  constraint's own variables, but its size can grow **exponentially** for formulas such as long `XOR`
  chains or wide equivalences.
- **Tseytin**: the [Tseytin transformation](https://en.wikipedia.org/wiki/Tseytin_transformation)
  introduces one auxiliary variable per logical gate, producing an **equisatisfiable** CNF whose size
  is **linear** in the formula.
- **Auto** (the default since 2.9): decides **per constraint**. A constraint is expanded distributively
  unless that expansion would be larger than its Tseytin encoding (the clause count is computed without
  building it), in which case that constraint alone gets auxiliary variables.

For example, the distributive CNF of a 5-variable `XOR` chain already expands to thousands of clauses,
while the Tseytin encoding of the same constraint stays in the low tens.

{: .note }
> `auto` is the default of every CNF consumer (`FmToPysat`, `FmToDiagPysat`, `FmToSDD`, `FmToSharpSAT`,
> `FmToDDNNF`), so it is what the Python facade and the CLI use. On typical models it produces exactly the
> distributive clauses: on the 1,538 models of the SoSyM benchmark it introduces auxiliary variables in
> 129 (eCos and Linux style models with disjunctions of conjunctions), where it yields 12% fewer clauses
> than the expansion, encodes 2.5 times faster and answers every operation identically. The two models
> whose expansion never finished now encode in under a second.

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

The SAT-oriented transformations accept a `cnf_method` argument: `'auto'` (the default),
`'distributive'` or `'tseytin'`:

```python
from flamapy.metamodels.fm_metamodel.transformations import UVLReader
from flamapy.metamodels.pysat_metamodel.transformations import FmToPysat

fm = UVLReader('model.uvl').transform()

# Default (auto: distributive unless a constraint's expansion blows up)
sat_model = FmToPysat(fm).transform()
sat_model.cnf_method           # 'auto'
sat_model.auxiliary_variables  # empty on typical models

# Force one encoding for every constraint
sat_model = FmToPysat(fm, cnf_method='distributive').transform()
sat_model = FmToPysat(fm, cnf_method='tseytin').transform()
```

The same `cnf_method` option is available on:

- `FmToPysat` (`flamapy-sat`) and `FmToDiagPysat` (`flamapy-sat` diagnosis metamodel).
- `FmToSDD` (`flamapy-sdd`), `FmToSharpSAT` (`flamapy-sharpsat`) and `FmToDDNNF` (`flamapy-dnnf`), which
  build their compilers from the same `ClauseSet`.
- `FmToZ3` (`flamapy-z3`) — see the caveat below; its default is its own direct translation.

## Z3 caveat: propositional constraints only

Z3 is an SMT solver and already clausifies internally, so Tseytin brings **no performance benefit** there;
`FmToZ3(fm, cnf_method='tseytin')` is provided only for cross-backend uniformity and experimentation.
It is applied **only** to purely propositional boolean constraints. Any constraint involving arithmetic,
comparison, aggregation or typed (Integer/Real/String) features automatically **falls back** to the direct
Z3 translation.

## When to use which

- Keep the **default `auto`**: it is the distributive encoding wherever that is small, and only the
  constraints that would explode (long `XOR`/`⇔` chains, deeply nested disjunctions of conjunctions) get
  auxiliary variables.
- Force **`distributive`** when you need a CNF over the feature variables only (for example to convert it
  back with `PysatToFM`, which refuses auxiliary variables, or to feed a tool that does not project them
  out; `DimacsWriter` counts them in the header and names only the features); the SAT translation of some
  large models may then become slow or memory-hungry.
- Force **`tseytin`** to experiment with a linear-size encoding for every constraint; on the benchmark
  models it doubles the clause count and slows SAT queries by about 1.7–2x, which is why `auto` only
  applies it where it pays off.
