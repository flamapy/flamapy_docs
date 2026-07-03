---
title: Generate Random Attribute
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/generate_random_attribute
nav_order: 30

flamapy_sat: false
flamapy_bdd: false
flamapy_fm: true
flamapy_z3: false
flamapy_diagnosis: false
cmd: false
facade: true
python: true
rest: false
---

# Generate Random Attribute

This operation augments a feature model with a **randomly generated numeric attribute**
attached to its features. It is useful for creating attributed feature models on which to
exercise attribute-based analyses (for example optimization or feature bounds) when the
original model has no attributes.

---
## Code Examples

```python
from flamapy.metamodels.fm_metamodel.transformations import UVLReader
from flamapy.metamodels.fm_metamodel.operations import GenerateRandomAttribute

feature_model = UVLReader('model.uvl').transform()
model_with_attribute = GenerateRandomAttribute().execute(feature_model).get_result()
```

Or, more simply, through the facade (values are drawn from the ``[min_value, max_value]`` range):

```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel

fm = FLAMAFeatureModel('model.uvl')
model_with_attribute = fm.generate_random_attribute('cost', min_value=0, max_value=100)
```
