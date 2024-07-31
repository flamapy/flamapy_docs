---
title: Diagnosis
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/diagnosis
nav_order: 11

flamapy_sat: true
flamapy_bdd: false
flamapy_fm: false
cmd: false
facade: false
python: true
rest: false
---

# Diagnosis
**Description**: 
Analyzes the feature model to identify and explain inconsistencies or errors, providing insights into potential fixes.

**Application**: 
Useful for debugging and improving the reliability of feature models by diagnosing issues and suggesting corrective actions.

**Example**: 
Diagnosing a feature model of a software application to identify and resolve conflicting constraints or dependencies.

---
## Code Examples

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("PySATDiagnosis", "path/to/feature/model")
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
operation = dm.get_operation(sat_model, 'PySATDiagnosis')
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```
