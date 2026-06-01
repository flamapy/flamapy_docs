---
title: Backbone
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/backbone
nav_order: 22

flamapy_sat: true
flamapy_bdd: false
flamapy_fm: false
flamapy_z3: false
flamapy_diagnosis: false
cmd: false
facade: true
python: true
rest: false
---

# Backbone

**Description**:
Returns the backbone of the feature model: the set of features that must always be selected (core features) and those that must never be selected (dead features) across all valid configurations, grouped under `core` and `dead` keys.

**Application**:
Provides a compact summary of the rigid parts of a product line in a single call, useful for model quality assessment.

**Example**:
Obtaining all features that are mandatory or impossible in a smartphone product line model.

---
## Code Examples

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Returns {'core': [...], 'dead': [...]}
result = fm.backbone()
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("PySATBackbone", "path/to/feature/model")
print(result)
```
### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation
feature_model = dm.use_transformation_t2m("path/to/feature/model", 'fm')
# Manually call a M2M transformation to PySAT
sat_model = dm.use_transformation_m2m(feature_model, "pysat")
# Get the operation
operation = dm.get_operation(sat_model, 'PySATBackbone')
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```
