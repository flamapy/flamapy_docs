---
title: Feature explanation
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/feature_explanation

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

# Feature explanation

**Description**:
Explains why a feature is forced (selected or deselected) by the current configuration: returns the minimal set of decisions responsible.

**Application**:
Supports interactive configurators: when a feature becomes selected or deselected automatically, explains which of the user's decisions caused it.

**Example**:
After selecting `CreditCard`, the feature `HIGH` security is forced; the explanation points at the decisions that imply it.

---
## Code Examples

### Command line usage
```bash
flamapy feature_explanation "path/to/feature/model" "path/to/configuration" "FeatureName"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
result = fm.feature_explanation("path/to/configuration", "FeatureName")
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
operation = dm.get_operation(sat_model, 'PySATFeatureExplanation')
# Set the configuration and the forced feature to explain
operation.set_configuration(configuration)
operation.set_feature("FeatureName")
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `feature_explanation(self, configuration_path: str, feature_name: str)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `configuration_path` | str | yes | — |
| `feature_name` | str | yes | — |

**Default backend**: pysat_diagnosis

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_diagnosis_metamodel | yes | — |

<!-- END GENERATED -->
