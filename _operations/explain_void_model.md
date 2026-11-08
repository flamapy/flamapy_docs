---
title: Explain void model
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/explain_void_model

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

# Explain void model

**Description**:
Explains why the feature model is void (encodes no valid configuration): a minimal set of relationships/cross-tree constraints that is already unsatisfiable (a QuickXPlain minimal conflict), in human-readable form.

**Application**:
Debugs a void feature model (one with no valid configuration) by pointing at a minimal set of relationships and constraints that contradict each other.

**Example**:
If `eCommerce` requires `Server` through a mandatory relationship and a constraint states `Server => !eCommerce`, those two are returned.

---
## Code Examples

### Command line usage
```bash
flamapy explain_void_model "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
result = fm.explain_void_model()
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("PySATExplainVoidModel", "path/to/feature/model")
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
operation = dm.get_operation(sat_model, 'PySATExplainVoidModel')
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `explain_void_model(self)`

**Default backend**: pysat_diagnosis

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_diagnosis_metamodel | yes | — |

<!-- END GENERATED -->
