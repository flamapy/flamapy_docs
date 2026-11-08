---
title: Number of Configurations
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/number_of_configurations
nav_order: 1

flamapy_sat: true
flamapy_bdd: true
flamapy_fm: false
flamapy_z3: true
flamapy_diagnosis: false
flamapy_sharpsat: true
flamapy_sdd: true
flamapy_dnnf: true
cmd: true
facade: true
python: true
rest: true
---

# Number of Configurations

**Description**: 
Returns the total number of valid configurations represented by the feature model.

**Application**: 
Provides a measure of the variability and complexity of the product line.

**Example**: 
Counting the total number of valid product variants that can be derived from the feature model.


---
## Code Examples

### Command line usage
```bash
flamapy configurations_number "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Pass backend="sat" | "bdd" | "z3" to choose the analysis plugin (use "sat" to force pysat in WASM environments)
configurations = fm.configurations_number() 
print(configurations)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
# Use BDDConfigurationsNumber, Z3ConfigurationsNumber, SDDConfigurationsNumber or DDNNFConfigurationsNumber (needs the d4 compiler) for an exact count with other solvers,
# or SharpSATConfigurationsNumber for an approximate count on very large models
result = dm.use_operation_from_file("PySATConfigurationsNumber","path/to/feature/model")
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
operation = dm.get_operation(sat_model,'PySATConfigurationsNumber')
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```
In the case of willing to use BDD solving techniques
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation 
# required to get to the fm metamodel
feature_model = dm.use_transformation_t2m("path/to/feature/model",'fm') 
# Manually call a M2M transformation to BDD
bdd_model = dm.use_transformation_m2m(feature_model,"bdd")
# Get the operation
operation = dm.get_operation(bdd_model,'BDDConfigurationsNumber')
# Execute the operation
operation.execute(bdd_model)
# Get and print the result
result = operation.get_result()
print(result)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `configurations_number(self, backend: Optional[str] = None, *, allow_approximate: Optional[bool] = None)`

**Default backend**: bdd (selectable via `backend=`)

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| z3_metamodel | yes | 30 |
| sdd_metamodel | yes | 2000 |
| sharpsat_metamodel | approximate | 2000 |
| pysat_metamodel | yes | 30 |
| dnnf_metamodel | yes | — |
| bdd_metamodel | yes | 1000 |

<!-- END GENERATED -->
