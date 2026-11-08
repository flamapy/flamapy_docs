---
title: T-wise sampling
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/t_wise_sampling

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

# T-wise sampling

**Description**:
Returns a t-wise (combinatorial) sample: a set of valid configurations that covers every satisfiable combination of ``t`` feature selections (pairwise for ``t = 2``).

**Application**:
Generates a sample of products for combinatorial interaction testing, covering every valid combination of `t` feature selections.

**Example**:
With `t = 2` (pairwise), every valid pair of feature selections such as `PayPal` selected and `Backup` deselected appears in at least one product.

---
## Code Examples

### Command line usage
```bash
flamapy t_wise_sampling "path/to/feature/model" --t 2
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
result = fm.t_wise_sampling(t=2)
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("PySATTWiseSampling", "path/to/feature/model")
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
operation = dm.get_operation(sat_model, 'PySATTWiseSampling')
# Set the interaction strength
operation.set_t(2)
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `t_wise_sampling(self, t: int = 2, backend: Optional[str] = None, *, allow_approximate: Optional[bool] = None)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `t` | int | no | 2 |

**Default backend**: sat (selectable via `backend=`)

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_metamodel | yes | — |

<!-- END GENERATED -->
