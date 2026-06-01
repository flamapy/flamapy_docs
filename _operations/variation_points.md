---
title: Variation Points
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/variation_points
nav_order: 21

flamapy_sat: false
flamapy_bdd: false
flamapy_fm: true
flamapy_z3: false
flamapy_diagnosis: false
cmd: false
facade: true
python: true
rest: false
---

# Variation Points

**Description**:
Returns the variation points of the feature model. A variation point is a feature that has at least one non-mandatory child relation, representing a decision point in the model. The result maps each variation point name to the list of its variant (non-mandatory) feature names.

**Application**:
Useful for understanding the configurable parts of a product line and which features participate in variability decisions.

**Example**:
Identifying which features in a car model act as selection points (e.g., Engine type offering Diesel, Petrol, or Electric as variants).

---
## Code Examples

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
result = fm.variation_points()
print(result)
```

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
result = dm.use_operation_from_file("FMVariationPoints", "path/to/feature/model")
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
operation = dm.get_operation(feature_model, 'FMVariationPoints')
# Execute the operation
operation.execute(feature_model)
# Get and print the result
result = operation.get_result()
print(result)
```
