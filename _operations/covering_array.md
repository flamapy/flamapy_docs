---
title: Covering array
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/covering_array

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

# Covering array

**Description**:
Returns a t-wise covering array: a set of valid configurations covering every satisfiable combination of ``t`` feature selections (pairwise for ``t = 2``).

**Application**:
Generates a small set of products to test so that every valid combination of `t` feature selections is exercised at least once (combinatorial interaction testing).

**Example**:
For the pairwise case (`t = 2`) a model with hundreds of configurations can be covered with around ten of them.

---
## Code Examples

### Command line usage
```bash
flamapy covering_array "path/to/feature/model" --t 2 --seed 42
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Pairwise covering array; the seed makes the result reproducible
result = fm.covering_array(t=2, seed=42)
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("PySATCoveringArray", "path/to/feature/model")
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
operation = dm.get_operation(sat_model, 'PySATCoveringArray')
# Set the interaction strength and the random seed
operation.set_t(2)
operation.set_seed(42)
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `covering_array(self, t: int = 2, seed: int = None)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `t` | int | no | 2 |
| `seed` | int | no | None |

**Default backend**: sat

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_metamodel | yes | — |

<!-- END GENERATED -->
