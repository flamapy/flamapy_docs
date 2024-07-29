---
title: Unique Features
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/unique_features
nav_order: 7

flamapy_sat: false
flamapy_bdd: true
flamapy_fm: false
cmd: true
facade: true
python: true
rest: true
---

# Unique Features
**Description**: 
Identifies features that are unique to specific configurations, highlighting features that differentiate configurations.

**Application**: 
Useful for identifying differentiating features in a product line, aiding in marketing and product development.

**Example**: 
Finding features that are unique to high-end smartphone models within a product line.

---
## Code Examples

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("BDDUniqueFeatures", "path/to/feature/model")
print(result)
```
### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation required to get to the fm metamodel
feature_model = dm.use_transformation_t2m(model_path, 'fm')
# Manually call a M2M transformation to BDD
bdd_model = dm.use_transformation_m2m(feature_model, "bdd")
# Get the operation
operation = dm.get_operation(bdd_model, 'BDDUniqueFeatures')
# Execute the operation
operation.execute(bdd_model)
# Get and print the result
result = operation.get_result()
print(result)
```
