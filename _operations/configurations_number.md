---
title: Number of Configurations
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/number_of_configurations
nav_order: 1

flamapy_sat: true
flampy_bdd: true
flamapy_fm: false
cmd: true
facade: true
python: true
rest: true
---

# Number of Configurations

**Description**: 
Returns the total number of valid configurations represented by the feature model.

**Application**: 
Provides a measure of the variability and complexity of the product line.

**Example**: 
Counting the total number of valid product variants that can be derived from the feature model.


---
## Code Examples

### Command line usage
```bash
flamapy configurations_number "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# This method could be called with the param  with_sat: bool = True if you want to force pysat (useful for WASM enviroments) 
configurations = fm.configurations_number() 
print(configurations)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
# Use BDDConfigurations if you want to rely on BDD solver
result=dm.use_operation_from_file("PySATConfigurationsNumber","path/to/feature/model")
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
operation = dm.get_operation(sat_model,'PySATConfigurationsNumber')
# Execute the operation
operation.execute(self.sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```
In the case of willing to use BDD solving techniques
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation 
# required to get to the fm metamodel
feature_model = dm.use_transformation_t2m(model_path,'fm') 
# Manuelly call a M2M transformation to BDD
bdd_model = dm.use_transformation_m2m(feature_model,"BDD")
# Get the operation
operation = dm.get_operation(sat_model,'BDDConfigurationsNumber')
# Execute the operation
operation.execute(self.bdd_model)
# Get and print the result
result = operation.get_result()
print(result)
```
