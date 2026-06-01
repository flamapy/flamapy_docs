---
title: Pure Optional Features
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/pure_optional_features
nav_order: 23

flamapy_sat: false
flamapy_bdd: true
flamapy_fm: false
flamapy_z3: false
flamapy_diagnosis: false
cmd: false
facade: true
python: true
rest: false
---

# Pure Optional Features

**Description**:
Returns the features with a feature inclusion probability of exactly 0.5, meaning they appear in exactly half of all valid configurations. These are the most unconstrained optional features — neither preferred nor avoided by the model's constraints.

**Application**:
Useful for identifying features that are freely optional without any structural bias, which can inform testing strategies and configuration design.

**Example**:
Finding features in a home automation product line that are included in exactly half of all valid products.

---
## Code Examples

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
result = fm.pure_optional_features()
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("BDDPureOptionalFeatures", "path/to/feature/model")
print(result)
```
### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation
feature_model = dm.use_transformation_t2m("path/to/feature/model", 'fm')
# Manually call a M2M transformation to BDD
bdd_model = dm.use_transformation_m2m(feature_model, "bdd")
# Get the operation
operation = dm.get_operation(bdd_model, 'BDDPureOptionalFeatures')
# Execute the operation
operation.execute(bdd_model)
# Get and print the result
result = operation.get_result()
print(result)
```
