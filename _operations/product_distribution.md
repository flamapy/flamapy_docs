---
title: Product Distribution
layout: default
parent: Operations
grand_parent: flamapy as framework
permalink: /framework/operations/product_distribution
nav_order: 5

flamapy_sat: false
flamapy_bdd: true
flamapy_fm: false
cmd: false
facade: false
python: true
rest: false
---
## Product Distribution
**Description**: 
Analyzes the distribution of configurations within the feature model, identifying how features are grouped across valid configurations.

**Application**: 
Useful for understanding the variety and commonality of products generated from the feature model, aiding in product planning and strategy.

**Example**: 
Evaluating the distribution of various car models generated from a car feature model.

---
## Code Examples

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("BDDProductDistribution", "path/to/feature/model")
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
operation = dm.get_operation(bdd_model, 'BDDProductDistribution')
# Execute the operation
operation.execute(bdd_model)
# Get and print the result
result = operation.get_result()
print(result)
```
