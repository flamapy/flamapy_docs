---
title: Configuration repair
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/configuration_repair

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

# Configuration repair

**Description**:
Returns a minimal subset of the configuration decisions to retract in order to restore consistency with the feature model — how to repair an over-constrained configuration.

**Application**:
Suggests how to fix an over-constrained configuration: the minimal set of decisions to retract so that the remaining ones can be completed into a valid product.

**Example**:
A configuration that selects both `LOW` storage and `Backup` can be repaired by retracting one of the two decisions.

---
## Code Examples

### Command line usage
```bash
flamapy configuration_repair "path/to/feature/model" "path/to/configuration"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Returns the decisions to retract as (feature, value) pairs
result = fm.configuration_repair("path/to/configuration")
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("PySATConfigurationRepair",
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
operation = dm.get_operation(sat_model, 'PySATConfigurationRepair')
# Set the configuration to repair
operation.set_configuration(configuration)
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `configuration_repair(self, configuration_path: str)`

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
