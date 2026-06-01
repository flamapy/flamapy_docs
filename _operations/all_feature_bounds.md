---
title: All Feature Bounds
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/all_feature_bounds
nav_order: 25

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

# All Feature Bounds

**Description**:
Returns the value bounds for all typed attribute features (Integer, Real, String) in the model. Each entry maps a feature name to a dictionary with `min`, `max`, and `bounded` keys. Requires the Z3 metamodel plugin (`flamapy-z3`).

**Application**:
Useful for understanding the numerical or string ranges that typed feature attributes can take across all valid configurations, aiding in constraint analysis and model validation.

**Example**:
Obtaining the minimum and maximum price bounds of all typed attributes in a configurable product model.

---
## Code Examples

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model (must contain typed attributes)
fm = FLAMAFeatureModel("path/to/feature/model")
result = fm.all_feature_bounds()
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
operation = dm.get_operation(z3_model, 'Z3AllFeatureBounds')
# Execute the operation
operation.execute(z3_model)
# Get and print the result
result = operation.get_result()
print(result)
```
