---
title: Satisfiable Configuration
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/satisfiable_configuration
nav_order: 1

flamapy_sat: true
flampy_bdd: false
flamapy_fm: false
cmd: true
facade: true
python: true
rest: true
---

# Satisfiable configuration
**Description**: 
Checks if there exists at least one valid configuration that satisfies a given set of selected and deselected features.

**Application**: 
Useful for validating partial configurations and ensuring they can be completed into full valid configurations.

**Example**: 
Verifying if a partial configuration with a selected set of features can lead to a valid product without any constraint violations.

---
## Code Examples

### Command line usage
```bash
flamapy satisfiable_configuration "path/to/feature/model" "path/to/configuration"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Identify atomic sets
operation = fm.satisfiable_configuration(('path/to/configuration'))
print(operation)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed; 
result=dm.use_operation_from_file(operation_name="PySATSatisfiableConfiguration",
                                  file="path/to/feature/model", 
                                  configuration_file='path/to/configuration')
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
# Get the configuration representation using the transformation 
# required to get to the configuration metamodel
configuration = dm.use_transformation_t2m('path/to/configuration','configuration')
# Manuelly call a M2M transformation to Pysat
sat_model = dm.use_transformation_m2m(feature_model,"pysat")
# Get the operation
operation = dm.get_operation(sat_model,'PySATSatisfiableConfiguration')
# Set the configuration within the operation
operation.set_configuration(configuration)
# Execute the operation
operation.execute(self.sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```