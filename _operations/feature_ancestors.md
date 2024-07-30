---
title: Feature Ancestors
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/feature_ancestors
nav_order: 1

flamapy_sat: false
flampy_bdd: false
flamapy_fm: true
cmd: true
facade: true
python: true
rest: true
---

# Feature ancestors

**Description**: 
Identifies all ancestor features of a given feature in the feature model. Ancestors are features that are hierarchically above the given feature.

**Application**: 
Helps in understanding the hierarchical structure and dependencies of features.

**Example**: 
For a given feature, listing all parent features up to the root.

---
## Code Examples

### Command line usage
```bash
flamapy feature_ancestors "path/to/feature/model" "FeatureName"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Identify atomic sets
operation = fm.feature_ancestors("FeatureName")
print(operation)
```

### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation 
# required to get to the fm metamodel
feature_model = dm.use_transformation_t2m(model_path,'fm') 
# Get the operation, no automatic transformations will be needed
operation = dm.get_operation(feature_model,'FMFeatureAncestors')
# Set the feature in which we want to get the ancestors
operation.set_feature(feature_model.get_feature_by_name("feature_name"))
# Execute the operation and get the results
operation.execute(feature_model)
result = operation.get_result()
print(result)
```