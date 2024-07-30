---
title: Variability
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/variability
nav_order: 8

flamapy_sat: false
flamapy_bdd: true
flamapy_fm: false
cmd: false
facade: false
python: true
rest: false
---

# Variability
**Description**: 
Measures the variability of a feature model by analyzing the presence and absence of features across all valid configurations.

**Application**: 
Useful for understanding the diversity within a product line, helping to identify stable versus variable features.

**Example**: 
Evaluating the variability of features in a home automation system to identify which features are common and which are optional.

---
## Code Examples

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("BDDVariability", "path/to/feature/model")
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
operation = dm.get_operation(bdd_model, 'BDDVariability')
# Execute the operation
operation.execute(bdd_model)
# Get and print the result
result = operation.get_result()
print(result)
```
