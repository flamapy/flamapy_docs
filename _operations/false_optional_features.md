---
title: False Optional Features
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/false_optional_features
nav_order: 1

flamapy_sat: true
flampy_bdd: true
flamapy_fm: false
cmd: true
facade: true
python: true
rest: true
---

# False optional features
**Description**: 
Identifies features that appear to be optional but, due to constraints and dependencies in the feature model, must be included in every valid product configuration. These features are typically indicative of modeling errors.

**Application**: 
Helps in debugging feature models to ensure that the optional features behave as intended.

**Example**: 
A feature that is marked as optional but is required by every product configuration due to a constraint with other mandatory features.


---
## Code Examples

### Command line usage
```bash
flamapy false_optional_features "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# This method could be called with the param  with_sat: bool = True if you want to force pysat (useful for WASM enviroments) 
result = fm.false_optional_features() 
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
# Use BDDConfigurations if you want to rely on BDD solver
result = dm.use_operation_from_file("PySATFalseOptionalFeatures","path/to/feature/model")
print(result)
```
### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation 
# required to get to the fm metamodel
feature_model = dm.use_transformation_t2m("path/to/feature/model",'fm') 
# Manually call a M2M transformation to Pysat
sat_model = dm.use_transformation_m2m(feature_model,"pysat")
# Get the operation
operation = dm.get_operation(sat_model,'PySATFalseOptionalFeatures')
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```
