---
title: Satisfiable
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/satisfiable
nav_order: 1

flamapy_sat: true
flamapy_bdd: true
flamapy_fm: false
flamapy_z3: true
flamapy_diagnosis: false
flamapy_sharpsat: false
flamapy_sdd: true
flamapy_dnnf: true
cmd: true
facade: true
python: true
rest: true
---

# Satisfiable
**Description**: 
Checks whether a given model is valid according to the constraints defined in the feature model.

**Application**: 
Ensures that there is at least a combination of features that can form a valid product.

**Example**: 
Validating a feature model to see if there are violated constraints.

---
## Code Examples

### Command line usage
```bash
flamapy satisfiable "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Pass backend="sat" | "bdd" | "z3" to choose the analysis plugin (use "sat" to force pysat in WASM environments)
result = fm.satisfiable() 
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
# Use BDDSatisfiable, Z3Satisfiable, SDDSatisfiable or DDNNFSatisfiable (needs the d4 compiler) to rely on other solvers
result = dm.use_operation_from_file("PySATSatisfiable","path/to/feature/model")
print(result)
```
### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation 
# required to get to the fm metamodel
feature_model = dm.use_transformation_t2m("path/to/feature/model",'fm') 
# Manually call a M2M transformation to Pysat
sat_model = dm.use_transformation_m2m(feature_model,"pysat")
# Get the operation
operation = dm.get_operation(sat_model,'PySATSatisfiable')
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `satisfiable(self, backend: Optional[str] = None, *, allow_approximate: Optional[bool] = None)`

**Default backend**: sat (selectable via `backend=`)

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| z3_metamodel | yes | — |
| sdd_metamodel | yes | 2000 |
| pysat_metamodel | yes | — |
| dnnf_metamodel | yes | — |
| bdd_metamodel | yes | 1000 |

<!-- END GENERATED -->
