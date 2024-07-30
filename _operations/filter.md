---
title: Filter
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/filter
nav_order: 1

flamapy_sat: true
flampy_bdd: false
flamapy_fm: false
cmd: true
facade: true
python: true
rest: true
---

# Filter
**Description**: 
This operation filters and selects a subset of configurations based on specified criteria. It helps in narrowing down the possible configurations to those that meet certain requirements.

**Application**: 
Useful for customizing and generating specific product configurations.

**Example**: 
Filtering configurations to include only those that support a high-resolution screen and GPS.

---
## Code Examples

### Command line usage
```bash
flamapy filter "path/to/feature/model" "path/to/configuration"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Filter
operation = fm.filter(("path/to/configuration"))
print(operation)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed; 
result = dm.use_operation_from_file(operation_name="PySATFilter",
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
feature_model = dm.use_transformation_t2m("path/to/feature/model",'fm') 
# Get the configuration representation using the transformation 
# required to get to the configuration metamodel
configuration = dm.use_transformation_t2m('path/to/configuration','configuration')
# Manually call a M2M transformation to Pysat
sat_model = dm.use_transformation_m2m(feature_model,"pysat")
# Get the operation
operation = dm.get_operation(sat_model,'PySATFilter')
# Set the configuration within the operation
operation.set_configuration(configuration)
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```