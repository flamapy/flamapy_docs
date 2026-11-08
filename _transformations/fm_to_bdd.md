---
title: FM to BDD
layout: default
parent: Transformations
grand_parent: Flamapy as framework
permalink: /framework/transformations/fm_to_bdd
nav_order: 2
metamodel: flamapy_bdd
type: model_to_model
---

# FM to BDD

This transformation converts a feature model into a Binary Decision Diagram (BDD) representation. BDDs are efficient for representing and manipulating logical functions, making them ideal for feature model analysis.

{% include flamapy.html %} relies on file extensions to identify the required transformation. Ensure you specify the correct file extension for this transformation.

---
## Code Examples

```python
from flamapy.metamodels.fm_metamodel.transformations.featureide_reader import FeatureIDEReader
from flamapy.metamodels.bdd_metamodel.transformations.fm_to_bdd import FmToBDD

# Load the feature model from a FeatureIDE file
feature_model = FeatureIDEReader('path/to/feature/model.xml').transform()

# Transform the feature model into a BDD representation
bdd_model = FmToBDD(feature_model).transform()

print(bdd_model)
```

---
## Building large BDDs

The size of a BDD, and the cost of building it, depend on the order of its variables.
`FmToBDD` builds the BDD clause by clause over a feature-tree variable order. With `dd`
built against CUDD it also reorders variables dynamically. A native builder (Logic2BDD on
CUDD, by D. Fernández-Amorós, UNED) is in preparation and not part of 2.9. These options can
be passed to `FmToBDD(...)` or set with environment variables:

| Option | Environment variable | Values (default first) |
|--------|----------------------|------------------------|
| `builder` | `FLAMAPY_BDD_BUILDER` | `python`; `native` and `auto` are experimental |
| `var_order` | `FLAMAPY_BDD_VAR_ORDER` | `tree`, `force`, `model` |
| `build` | `FLAMAPY_BDD_BUILD` | `incremental`, `monolithic` (Python builder) |
| `clause_order` | `FLAMAPY_BDD_CLAUSE_ORDER` | `minspan`, `minmax`, `model` (Python builder) |
| `reorder` | `FLAMAPY_BDD_REORDER` | `auto`, `1`, `0` (Python builder) |

```python
bdd_model = FmToBDD(feature_model, builder="python", var_order="force").transform()
```

The options change how the BDD is built, never the configurations it represents.
