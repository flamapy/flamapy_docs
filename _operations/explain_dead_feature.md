---
title: Explain dead feature
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/explain_dead_feature

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

# Explain dead feature

**Description**:
Explains why a feature is dead (appears in no valid configuration): a minimal set of relationships/cross-tree constraints that forbids selecting it (a QuickXPlain minimal conflict of the model plus "feature = true"), in human-readable form.

**Application**:
Debugs a feature model: once a dead feature is found, shows which relationships and cross-tree constraints make it impossible to select.

**Example**:
If `D` is an alternative child of a feature that requires `B`, and a constraint states `D excludes B`, the explanation returns that relationship and constraint.

---
## Code Examples

### Command line usage
```bash
flamapy explain_dead_feature "path/to/feature/model" "FeatureName"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
result = fm.explain_dead_feature("FeatureName")
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
# Get the operation
operation = dm.get_operation(sat_model, 'PySATExplainDeadFeature')
# Set the dead feature to explain
operation.set_feature("FeatureName")
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `explain_dead_feature(self, feature_name: str)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `feature_name` | str | yes | — |

**Default backend**: pysat_diagnosis

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_diagnosis_metamodel | yes | — |

<!-- END GENERATED -->
