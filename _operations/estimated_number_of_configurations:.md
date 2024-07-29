---
title: Estimated Number of Configurations
layout: default
parent: Operations
grand_parent: flamapy as framework
permalink: /framework/operations/estimated_number_of_configurations
nav_order: 1

flamapy_sat: false
flampy_bdd: false
flamapy_fm: true
cmd: true
facade: true
python: true
rest: true
---

# Estimated number of configurations
**Description**: 
Provides an estimate of the total number of different configurations that can be produced from a feature model by considering all possible combinations of features.

**Application**: 
Useful for assessing the variability and potential complexity of the product line.

**Example**: 
A feature model with numerous optional and alternative features will have a high estimated number of configurations.


---
## Code Examples

### Command line usage
```bash
flamapy estimated_number_of_configurations "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flama_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Identify atomic sets
operation = fm.estimated_number_of_configurations()
print(operation)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result=dm.use_operation_from_file("FMEstimatedConfigurationsNumber","path/to/feature/model")
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
# Call the operation, no automatic transformations will be needed
result = dm.use_operation(feature_model,'FMEstimatedConfigurationsNumber').get_result()
print(result)
```