---
title: Feature Bounds
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/feature_bounds
nav_order: 26

flamapy_sat: false
flamapy_bdd: false
flamapy_fm: false
flamapy_z3: true
flamapy_diagnosis: false
cmd: false
facade: true
python: true
rest: false
---

# Feature Bounds

**Description**:
Returns the value bounds for a specific typed attribute feature. The result dictionary contains `min`, `max`, and `bounded` keys indicating the range of values the feature can take across all valid configurations. Requires the Z3 metamodel plugin (`flamapy-z3`).

**Application**:
Useful for targeted constraint analysis when you need to inspect the range of a particular attribute feature without computing bounds for all features.

**Example**:
Finding the minimum and maximum allowed price of a specific component feature in a configurable product model.

---
## Code Examples

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model (must contain typed attributes)
fm = FLAMAFeatureModel("path/to/feature/model")
# Replace "feature_name" with the actual attribute feature name
result = fm.feature_bounds("feature_name")
print(result)
```

### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation
feature_model = dm.use_transformation_t2m("path/to/feature/model", 'fm')
# Manually call a M2M transformation to Z3
z3_model = dm.use_transformation_m2m(feature_model, "z3")
# Get the operation
operation = dm.get_operation(z3_model, 'Z3FeatureBounds')
operation.set_variable_name("feature_name")
# Execute the operation
operation.execute(z3_model)
# Get and print the result
result = operation.get_result()
print(result)
```
