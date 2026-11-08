---
title: Minimal corrections
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/minimal_corrections

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

# Minimal corrections

**Description**:
Returns the minimal corrections for a void feature model: each correction is a minimal set of relationships/cross-tree constraints whose removal makes the model satisfiable (FastDiag diagnoses enumerated via HSDAG), in human-readable form.

**Application**:
Repairs a void feature model: each correction is a minimal set of relationships and constraints whose removal makes the model satisfiable again.

**Example**:
For a model where `eCommerce` requires `Server` but a constraint forbids it, the corrections are removing that constraint, or removing the relationship.

---
## Code Examples

### Command line usage
```bash
flamapy minimal_corrections "path/to/feature/model" --max_corrections 5
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# max_corrections bounds how many corrections are enumerated
result = fm.minimal_corrections(max_corrections=5)
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("PySATMinimalCorrections", "path/to/feature/model")
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
operation = dm.get_operation(sat_model, 'PySATMinimalCorrections')
# Bound the number of corrections to enumerate
operation.set_max_corrections(5)
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `minimal_corrections(self, max_corrections: int = None)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `max_corrections` | int | no | None |

**Default backend**: pysat_diagnosis

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_diagnosis_metamodel | yes | — |

<!-- END GENERATED -->
