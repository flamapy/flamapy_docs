---
title: Explain false optional
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/explain_false_optional

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

# Explain false optional

**Description**:
Explains why a feature is false-optional (declared optional but present in every valid configuration that includes its parent): a minimal set of relationships/cross-tree constraints that forbids deselecting it while its parent is selected (a QuickXPlain minimal conflict of the model plus "parent = true, feature = false"), in human-readable form.

**Application**:
Debugs a feature model: shows which relationships and cross-tree constraints force a feature declared optional to be always selected with its parent.

**Example**:
If the only alternative to `E` is a dead feature, `E` becomes false-optional; the explanation returns the relationships and constraints responsible.

---
## Code Examples

### Command line usage
```bash
flamapy explain_false_optional "path/to/feature/model" "FeatureName"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
result = fm.explain_false_optional("FeatureName")
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
operation = dm.get_operation(sat_model, 'PySATExplainFalseOptional')
# Set the false-optional feature to explain
operation.set_feature("FeatureName")
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `explain_false_optional(self, feature_name: str)`

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
