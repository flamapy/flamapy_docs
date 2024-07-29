---
title: Average Branching Factor
layout: default
parent: Operations
grand_parent: flamapy as framework
permalink: /framework/operations/average_branching_factor
nav_order: 1

flamapy_sat: false
flampy_bdd: false
flamapy_fm: true
cmd: true
facade: true
python: true
rest: true
---

## Average Branching Factor

**Description**: 
This calculates the average number of child features per parent feature in the feature model. It provides insight into the complexity of the model.

**Application**: 
Helps in understanding the model's structure and identifying areas with high complexity.

**Example**: 
If a feature model has 10 parent features with a total of 30 child features, the average branching factor is 3.


---
## Code Examples

### Command line usage
```bash
flamapy average_branching_factor "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flama_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Identify atomic sets
avbf = fm.average_branching_factor()
print(avbf)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result=dm.use_operation_from_file("FMAverageBranchingFactor","path/to/feature/model")
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
result = dm.use_operation(feature_model,'FMAverageBranchingFactor').get_result()
print(result)
```
