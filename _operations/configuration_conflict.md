---
title: Configuration conflict
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/configuration_conflict

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

# Configuration conflict

**Description**:
Returns a minimal subset of the configuration decisions that is inconsistent with the feature model — the conflict explaining why the (partial) configuration cannot be completed.

**Application**:
Explains to a user why the choices they made cannot be completed into a valid product, pointing at the minimal set of their own decisions that clash.

**Example**:
In an online-shop product line where `LOW` storage excludes `Backup`, a user who selected both gets back those two decisions as the conflict.

---
## Code Examples

### Command line usage
```bash
flamapy configuration_conflict "path/to/feature/model" "path/to/configuration"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Returns the conflicting decisions as (feature, value) pairs
result = fm.configuration_conflict("path/to/configuration")
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("PySATConfigurationConflict",
                                    "path/to/feature/model",
                                    configuration_file="path/to/configuration")
print(result)
```

### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation
# required to get to the fm metamodel
feature_model = dm.use_transformation_t2m("path/to/feature/model", 'fm')
# Manually call a M2M transformation to the diagnosis metamodel
sat_model = dm.use_transformation_m2m(feature_model, "pysat_diagnosis")
# Read the configuration using the transformation
# required to get to the configuration metamodel
configuration = dm.use_transformation_t2m("path/to/configuration", "configuration")
# Get the operation
operation = dm.get_operation(sat_model, 'PySATConfigurationConflict')
# Set the configuration to analyse
operation.set_configuration(configuration)
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `configuration_conflict(self, configuration_path: str)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `configuration_path` | str | yes | — |

**Default backend**: pysat_diagnosis

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_diagnosis_metamodel | yes | — |

<!-- END GENERATED -->
