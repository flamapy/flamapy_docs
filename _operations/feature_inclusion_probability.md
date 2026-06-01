---
title: Feature Inclusion Probability
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/feature_inclusion_probability
nav_order: 2

flamapy_sat: false
flamapy_bdd: true
flamapy_fm: false
flamapy_z3: false
flamapy_diagnosis: false
cmd: false
facade: true
python: true
rest: false
---

# Feature Inclusion Probability
**Description**: 
Calculates the probability of each feature being included in a valid configuration.

**Application**: 
Useful for understanding the likelihood of feature presence across all valid configurations, aiding in feature prioritization and decision-making.

**Example**: 
Determining the probability of the 'GPS' feature being included in all valid configurations of a car model feature set.

---
## Code Examples

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
result = fm.feature_inclusion_probability()
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("BDDFeatureInclusionProbability", "path/to/feature/model")
print(result)
```
### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation required to get to the fm metamodel
feature_model = dm.use_transformation_t2m("path/to/feature/model", 'fm')
# Manually call a M2M transformation to BDD
bdd_model = dm.use_transformation_m2m(feature_model, "bdd")
# Get the operation
operation = dm.get_operation(bdd_model, 'BDDFeatureInclusionProbability')
# Execute the operation
operation.execute(bdd_model)
# Get and print the result
result = operation.get_result()
print(result)
```
