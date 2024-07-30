---
title: Dead Features
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/deaf_features
nav_order: 1

flamapy_sat: true
flampy_bdd: true
flamapy_fm: false
cmd: true
facade: true
python: true
rest: true
---

# Dead Features

**Description**: 
Identifies features that cannot be included in any valid product configuration due to constraints and dependencies in the model. These are typically indicative of errors in the feature model.

**Application**: 
Helps in debugging and ensuring the correctness of the feature model.

***Example***: 
A feature that is excluded by all other features or cannot be selected due to contradictory constraints.

---
## Code Examples

### Command line usage
```bash
flamapy dead_features "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# This method could be called with the param  with_sat: bool = True if you want to force pysat (useful for WASM enviroments) 
result = fm.dead_features() 
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
# Use BDDConfigurations if you want to rely on BDD solver
result=dm.use_operation_from_file("PySATDeadFeatures","path/to/feature/model")
print(result)
```
### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation 
# required to get to the fm metamodel
feature_model = dm.use_transformation_t2m(model_path,'fm') 
# Manuelly call a M2M transformation to Pysat
sat_model = dm.use_transformation_m2m(feature_model,"pysat")
# Get the operation
operation = dm.get_operation(sat_model,'PySATDeadFeatures')
# Execute the operation
operation.execute(self.sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```
