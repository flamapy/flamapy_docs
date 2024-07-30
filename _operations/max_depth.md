---
title: Max Depth
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/max_depth
nav_order: 1

flamapy_sat: false
flampy_bdd: false
flamapy_fm: true
cmd: true
facade: true
python: true
rest: true
---

# Max depth

**Description**: 
This operation finds the maximum depth of the feature tree in the model, indicating the longest path from the root to a leaf.

**Application**: 
Helps in understanding the hierarchical structure and complexity of the feature model.

**Example**: 
In a feature model with multiple levels of features, the longest path from the root to a leaf feature determines the maximum depth.
---
## Code Examples

### Command line usage
```bash
flamapy max_depth "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Identify atomic sets
operation = fm.max_depth()
print(operation)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result=dm.use_operation_from_file("FMMaxDepthTree","path/to/feature/model")
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
result = dm.use_operation(feature_model,'FMMaxDepthTree').get_result()
print(result)
```
