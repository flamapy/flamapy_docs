---
title: Minimum configuration
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/minimum_configuration

flamapy_sat: true
flamapy_bdd: false
flamapy_fm: false
flamapy_z3: false
flamapy_diagnosis: false
flamapy_sharpsat: false
flamapy_sdd: false
flamapy_dnnf: false
cmd: true
facade: true
python: true
rest: true
---

# Minimum configuration

**Description**:
Returns a valid configuration with the fewest selected features (the minimum working configuration).

**Application**:
Finds the leanest valid product, e.g. a baseline product or the smallest deployment of a configurable system.

**Example**:
In an online-shop product line, the minimum configuration contains only the mandatory features plus one child of each required group.

---
## Code Examples

### Command line usage
```bash
flamapy minimum_configuration "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
result = fm.minimum_configuration()
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("PySATMinimumConfiguration", "path/to/feature/model")
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
# Manually call a M2M transformation to PySAT
sat_model = dm.use_transformation_m2m(feature_model, "pysat")
# Get the operation
operation = dm.get_operation(sat_model, 'PySATMinimumConfiguration')
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `minimum_configuration(self, backend: Optional[str] = None, *, allow_approximate: Optional[bool] = None)`

**Default backend**: sat (selectable via `backend=`)

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_metamodel | yes | — |

<!-- END GENERATED -->
