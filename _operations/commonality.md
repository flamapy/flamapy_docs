---
title: Commonality
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/commonality
nav_order: 1

flamapy_sat: true
flampy_bdd: true
flamapy_fm: false
cmd: true
facade: true
python: true
rest: true
---

# Commonality

**Description**: 
Measures how often a feature appears in the configurations of a product line, usually expressed as a percentage. Features with high commonality are core features.

**Application**: 
Useful for identifying the most important features that are common across all configurations.

**Example**: If a feature appears in 80 out of 100 possible product configurations, its commonality is 80%.

---
## Code Examples

### Command line usage
```bash
flamapy commonality "path/to/feature/model" "path/to/configuration"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Commonality
commonality = fm.commonality(("path/to/configuration"))
print(commonality)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed; 
result=dm.use_operation_from_file(operation_name="PySATCommonality",
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
operation = dm.get_operation(sat_model,'PySATCommonality')
# Set the configuration within the operation
operation.set_configuration(configuration)
# Execute the operation
operation.execute(self.sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```