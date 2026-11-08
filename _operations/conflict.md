---
title: Conflict
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/conflict

flamapy_sat: false
flamapy_bdd: false
flamapy_fm: false
flamapy_z3: false
flamapy_diagnosis: true
flamapy_sharpsat: false
flamapy_sdd: false
flamapy_dnnf: false
cmd: true
facade: true
python: true
rest: true
---

# Conflict
**Description**: 
Identifies conflicts within the feature model by detecting combinations of features that cannot coexist due to constraints.

**Application**: 
Useful for debugging and ensuring the consistency of feature models by identifying conflicting feature combinations that violate constraints.

**Example**: 
Detecting conflicts in a car feature model where certain features like 'Sunroof' and 'Convertible' cannot be selected together.

---
## Code Examples

### Command line usage
```bash
flamapy conflict "path/to/feature/model" "path/to/configuration" --test_case_path "path/to/test_case"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
result = fm.conflict("path/to/configuration", "path/to/test_case")
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Conflict detection requires a configuration; pass it with configuration_file.
# The test case can only be set with the ADVANCED usage below.
# Transformations will be automatically executed.
result = dm.use_operation_from_file(
    "PySATConflict",
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
# Read the configuration and the test case to analyse
configuration = dm.use_transformation_t2m("path/to/configuration", "configuration")
test_case = dm.use_transformation_t2m("path/to/test_case", "configuration")
# Get the operation and set the configuration and test case
operation = dm.get_operation(sat_model, 'PySATConflict')
operation.set_configuration(configuration)
operation.set_test_case(test_case)
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `conflict(self, configuration_path: str, test_case_path: str = None, max_conflicts: int = None)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `configuration_path` | str | yes | — |
| `test_case_path` | str | no | None |
| `max_conflicts` | int | no | None |

**Default backend**: pysat_diagnosis

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_diagnosis_metamodel | yes | — |

<!-- END GENERATED -->
