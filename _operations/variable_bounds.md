---
title: Variable Bounds
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/variable_bounds
nav_order: 28

flamapy_sat: false
flamapy_bdd: false
flamapy_fm: false
flamapy_z3: true
flamapy_diagnosis: false
cmd: false
facade: false
python: true
rest: false
---

# Variable Bounds

**Description**:
Computes the effective bounds for a single typed feature: minimum and maximum values for numeric features (Integer, Real), and minimum and maximum length for String features. It handles unbounded ranges (±infinity) and reports `UNSAT` when the model has no valid configuration. This is a more thorough variant of [Feature Bounds]({{ '/framework/operations/feature_bounds' | relative_url }}) for complex typed attributes. Requires the Z3 metamodel plugin (`flamapy-z3`).

**Application**:
Useful for in-depth analysis of the admissible range of a specific attribute, including string-length analysis and detection of unbounded or unsatisfiable attributes.

**Example**:
Determining the minimum and maximum allowed length of a configurable identifier string in a product model.

---
## Code Examples

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation
feature_model = dm.use_transformation_t2m("path/to/feature/model", 'fm')
# Manually call a M2M transformation to Z3
z3_model = dm.use_transformation_m2m(feature_model, "z3")
# Get the operation
operation = dm.get_operation(z3_model, 'Z3VariableBounds')
operation.set_variable_name("feature_name")
# Execute the operation
operation.execute(z3_model)
# Get and print the result
result = operation.get_result()
print(result)
```
