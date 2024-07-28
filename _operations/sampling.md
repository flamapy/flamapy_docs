---
title: Sampling
layout: default
parent: Operations
grand_parent: flamapy as framework
nav_order: 6

flamapy_sat: true
flamapy_bdd: true
flamapy_fm: false
cmd: false
facade: false
python: true
rest: false
---
## Sampling
**Description**: 
Generates a sample set of valid configurations from the feature model, providing a representative subset for analysis.

**Application**: 
Useful for performance testing, validation, and analysis without the need to process all possible configurations.

**Example**: 
Generating a sample set of valid smartphone configurations for testing purposes.

---
## Code Examples

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("BDDSampling", "path/to/feature/model")
print(result)
```
### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation required to get to the fm metamodel
feature_model = dm.use_transformation_t2m(model_path, 'fm')
# Manually call a M2M transformation to BDD
bdd_model = dm.use_transformation_m2m(feature_model, "bdd")
# Get the operation
operation = dm.get_operation(bdd_model, 'BDDSampling')
# Execute the operation
operation.execute(bdd_model)
# Get and print the result
result = operation.get_result()
print(result)
```
