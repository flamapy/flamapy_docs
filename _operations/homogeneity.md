---
title: Homogeneity
layout: default
parent: Operations
grand_parent: flamapy as framework
permalink: /framework/operations/homogeneity
nav_order: 3

flamapy_sat: false
flamapy_bdd: true
flamapy_fm: false
cmd: false
facade: false
python: true
rest: false
---
## Homogeneity
**Description**: 
Measures the uniformity of feature distributions across all valid configurations.

**Application**: 
Useful for assessing whether certain features are consistently included or excluded in configurations, indicating stability or variability within the product line.

**Example**: 
Evaluating if certain features are consistently present in all configurations of a software product line.

---
## Code Examples

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("BDDHomogeneity", "path/to/feature/model")
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
operation = dm.get_operation(bdd_model, 'BDDHomogeneity')
# Execute the operation
operation.execute(bdd_model)
# Get and print the result
result = operation.get_result()
print(result)
```
