---
title: Language Level
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/language_level
nav_order: 29

flamapy_sat: false
flamapy_bdd: false
flamapy_fm: true
flamapy_z3: false
flamapy_diagnosis: false
cmd: true
facade: true
python: true
rest: false
---

# Language Level

This operation reports the UVL **language level** a feature model uses, i.e. which subset
of the [Universal Variability Language](https://universal-variability-language.github.io/)
is required to express it (for example *Boolean*, *Arithmetic*, *Type*, or the group/feature
cardinality levels). It is a structural operation computed directly on the feature model,
without a backend solver.

---
## Code Examples

```python
from flamapy.metamodels.fm_metamodel.transformations import UVLReader
from flamapy.metamodels.fm_metamodel.operations import FMLanguageLevel

feature_model = UVLReader('model.uvl').transform()
levels = FMLanguageLevel().execute(feature_model).get_result()
print(levels)
```

Using the Python facade:

```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel

result = FLAMAFeatureModel('model.uvl').language_level()
```
