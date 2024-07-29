---
title: Core Features
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/core_features
nav_order: 1

flamapy_sat: true
flampy_bdd: true
flamapy_fm: true
cmd: true
facade: true
python: true
rest: true
---

# Core Features

**Description**: 
Identifies features that are present in all valid configurations of the feature model. These are mandatory features that cannot be excluded.

**Application**: 
Helps in defining the essential components of all configurations in the product line.

**Example**: 
In a mobile phone feature model, features like 'Call Functionality' might be core features as they are necessary in all phones.


---
## Code Examples

### Command line usage
```bash
flamapy core_features "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flama_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# This method could be called with the param  with_sat: bool = True if you want to force pysat (useful for WASM enviroments) 
result = fm.core_features() 
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
# Use BDDConfigurations if you want to rely on BDD solver
result=dm.use_operation_from_file("PySATCoreFeatures","path/to/feature/model")
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
operation = dm.get_operation(sat_model,'PySATCoreFeatures')
# Execute the operation
operation.execute(self.sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```
