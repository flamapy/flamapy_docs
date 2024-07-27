---
title: Leaf Features
layout: default
parent: Operations
grand_parent: flamapy as framework
nav_order: 1

flamapy_sat: false
flampy_bdd: false
flamapy_fm: true
cmd: true
facade: true
python: true
rest: true
---
## Leaf features

**Description**: 
Identifies all leaf features in the feature model. Leaf features are those that do not have any child features and represent the most specific options in a product line.

**Application**: 
Useful for identifying the end features that define the specific details of a product.

**Example**: 
Listing features at the bottom of the hierarchy that do not branch into further sub-features.

---
## Code Examples

### Command line usage
```bash
flamapy leaf_features "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flama_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Identify atomic sets
operation = fm.leaf_features()
print(operation)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result=dm.use_operation_from_file("FMLeafFeatures","path/to/feature/model")
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
result = dm.use_operation(feature_model,'FMLeafFeatures').get_result()
print(result)
```
