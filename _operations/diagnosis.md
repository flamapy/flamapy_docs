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
flamapy_z3: false
flamapy_diagnosis: true
cmd: false
facade: true
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

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
result = fm.diagnosis("path/to/configuration", "path/to/test_case")
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Diagnosis requires a configuration; pass it with configuration_file.
# Transformations will be automatically executed.
result = dm.use_operation_from_file(
    "PySATDiagnosis",
    "path/to/feature/model",
    configuration_file="path/to/configuration",
)
print(result)
```
### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation required to get to the fm metamodel
feature_model = dm.use_transformation_t2m("path/to/feature/model", 'fm')
# Manually call a M2M transformation to the diagnosis metamodel
sat_model = dm.use_transformation_m2m(feature_model, "pysat_diagnosis")
# Read the configuration and the test case to diagnose
configuration = dm.use_transformation_t2m("path/to/configuration", "configuration")
test_case = dm.use_transformation_t2m("path/to/test_case", "configuration")
# Get the operation and set the configuration and test case
operation = dm.get_operation(sat_model, 'PySATDiagnosis')
operation.set_configuration(configuration)
operation.set_test_case(test_case)
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```
