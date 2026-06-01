---
title: Configurations With N Features
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/configurations_with_n_features
nav_order: 24

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

# Configurations With N Features

**Description**:
Returns all valid configurations that have exactly N features selected. This is a slice of the product distribution at a specific size.

**Application**:
Useful when you want to enumerate or analyse only the configurations of a specific size, for example to test products with a fixed number of active features.

**Example**:
Finding all valid smartphone configurations that activate exactly 5 features.

---
## Code Examples

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Replace 5 with the desired number of features
result = fm.configurations_with_n_features(n=5)
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation
feature_model = dm.use_transformation_t2m("path/to/feature/model", 'fm')
# Manually call a M2M transformation to BDD
bdd_model = dm.use_transformation_m2m(feature_model, "bdd")
# Get the operation
operation = dm.get_operation(bdd_model, 'BDDConfigurationsWithNFeatures')
operation.set_n_features(5)
# Execute the operation
operation.execute(bdd_model)
# Get and print the result
result = list(operation.get_result())
print(result)
```
