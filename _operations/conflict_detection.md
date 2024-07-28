### Conflict Detection
---
title: Conflict Detection
layout: default
parent: Operations
grand_parent: flamapy as framework
nav_order: 10

flamapy_sat: true
flamapy_bdd: false
flamapy_fm: false
cmd: true
facade: true
python: true
rest: true
---
## Conflict Detection
**Description**: 
Identifies conflicts within the feature model by detecting combinations of features that cannot coexist due to constraints.

**Application**: 
Useful for debugging and ensuring the consistency of feature models by identifying conflicting feature combinations that violate constraints.

**Example**: 
Detecting conflicts in a car feature model where certain features like 'Sunroof' and 'Convertible' cannot be selected together.

---
## Code Examples

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("PySATConflictDetection", "path/to/feature/model")
print(result)
```
### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation required to get to the fm metamodel
feature_model = dm.use_transformation_t2m(model_path, 'fm')
# Manually call a M2M transformation to Pysat
sat_model = dm.use_transformation_m2m(feature_model, "pysat_diagnosis")
# Get the operation
operation = dm.get_operation(sat_model, 'PySATConflictDetection')
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```
