---
title: Count Leafs
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/count_leafs
nav_order: 1

flamapy_sat: false
flampy_bdd: false
flamapy_fm: true
cmd: true
facade: true
python: true
rest: true
---

# Count leafs

**Description**: 
This operation counts the number of leaf features in a feature model. Leaf features are those that do not have any children.

**Application**: 
Useful for identifying the most specific options in a product line.

**Example**: 
In a feature model, features at the bottom of the hierarchy without any sub-features are counted as leaf features.

---
## Code Examples

### Command line usage
```bash
flamapy count_leafs "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Identify atomic sets
operation = fm.count_leafs()
print(operation)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("FMCountLeafs","path/to/feature/model")
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
# Call the operation, no automatic transformations will be needed
result = dm.use_operation(feature_model,'FMCountLeafs').get_result()
print(result)
```


