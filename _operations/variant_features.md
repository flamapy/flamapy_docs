---
title: Variant Features
layout: default
parent: Operations
grand_parent: flamapy as framework
permalink: /framework/operations/variant_features
nav_order: 9

flamapy_sat: false
flamapy_bdd: true
flamapy_fm: false
cmd: false
facade: false
python: true
rest: false
---

# Variant Features
**Description**: 
Identifies variant features in the feature model, highlighting features that change across different configurations.

**Application**: 
Useful for understanding which features vary between different configurations, aiding in customization and variability management.

**Example**: 
Identifying variant features in a product line of laptops to determine which features are customizable for customers.

---
## Code Examples

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("BDDVariantFeatures", "path/to/feature/model")
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
operation = dm.get_operation(bdd_model, 'BDDVariantFeatures')
# Execute the operation
operation.execute(bdd_model)
# Get and print the result
result = operation.get_result()
print(result)
```
