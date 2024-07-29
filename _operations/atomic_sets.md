---
title: Atomic Sets
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/atomic_sets
nav_order: 1

flamapy_sat: false
flamapy_bdd: false
flamapy_fm: true
cmd: true
facade: true
python: true
rest: true
---

# Atomic Sets

**Description**: 
This operation identifies atomic sets in a feature model. An atomic set is a group of features that always appear together across all configurations of the model. These sets help in simplifying and reducing the complexity of the model by grouping features that behave as a single unit.

**Application**: 
Useful for preprocessing feature models to make subsequent analyses more efficient.

**Example**: 
In a feature model where features A and B are always selected together, they form an atomic set.

---
## Code Examples

### Command line usage
```bash
flamapy atomic_sets "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flama_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Identify atomic sets
result = fm.atomic_sets()
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result=dm.use_operation_from_file("AtomicSets","path/to/feature/model")
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
result = dm.use_operation(feature_model,'FMAtomicSets').get_result()
print(result)
```


