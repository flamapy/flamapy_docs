---
title: Metrics
layout: default
parent: Operations
grand_parent: flamapy as framework
permalink: /framework/operations/metrics
nav_order: 4

flamapy_sat: true
flamapy_bdd: true
flamapy_fm: true
cmd: false
facade: false
python: true
rest: false
---
## Metrics
**Description**: 
Calculates various metrics for a given feature model using BDDs, SATs or basic fm operations, including the number of configurations, commonality, and variability.

**Application**: 
Provides comprehensive metrics to analyze and evaluate the feature model's structure and properties.

**Example**: 
Generating metrics to understand the overall complexity and commonality of features in a product line.

---
## Code Examples

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed. 
# This is if only BDD metrics are desired
result = dm.use_operation_from_file("BDDMetrics", "path/to/feature/model")
# Call the operation. Transformations will be automatically executed. 
# This is if allmetrics are desired
result = dm.use_operation_from_file("Metrics", "path/to/feature/model")
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
operation = dm.get_operation(bdd_model, 'BDDMetrics')
# Execute the operation
operation.execute(bdd_model)
# Get and print the result
result = operation.get_result()
print(result)
```
