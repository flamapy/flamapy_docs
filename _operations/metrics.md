---
title: Metrics
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/metrics
nav_order: 20

flamapy_sat: true
flamapy_bdd: true
flamapy_fm: true
flamapy_z3: false
flamapy_diagnosis: false
cmd: false
facade: true
python: true
rest: false
---

# Metrics

**Description**:
Returns a collection of structural metrics for the feature model, such as number of features, constraints, relations, abstract and concrete features, leaf features, and complexity indicators.

**Application**:
Useful for getting a quick overview of the size and complexity of a feature model, comparing models, or feeding metrics into analysis pipelines.

**Example**:
Obtaining the number of features and constraints in a software product line feature model.

---
## Code Examples

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
result = fm.metrics()
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("FMMetrics", "path/to/feature/model")
print(result)
```
### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation
feature_model = dm.use_transformation_t2m("path/to/feature/model", 'fm')
# Get the operation
operation = dm.get_operation(feature_model, 'FMMetrics')
# Execute the operation
operation.execute(feature_model)
# Get and print the result
result = operation.get_result()
print(result)
```
