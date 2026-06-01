---
title: Attribute Optimization
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/attribute_optimization
nav_order: 27

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

# Attribute Optimization

**Description**:
Returns the configurations that optimize one or more numerical attributes (Integer or Real). The optimization is based on the sum of the attribute values across all selected features. When a single attribute is given it returns all optimal configurations; when several attributes are given it returns the Pareto front of non-dominated configurations. Requires the Z3 metamodel plugin (`flamapy-z3`).

**Application**:
Useful for decision support in product lines with quantitative attributes — for example finding the cheapest, fastest, or most balanced valid configurations.

**Example**:
Finding the configurations of a car model that minimise total price while maximising total performance.

---
## Code Examples

### Python flamapy framework usage
```python
from flamapy.core.discover import DiscoverMetamodels
from flamapy.metamodels.z3_metamodel.operations.interfaces import OptimizationGoal
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation
feature_model = dm.use_transformation_t2m("path/to/feature/model", 'fm')
# Manually call a M2M transformation to Z3
z3_model = dm.use_transformation_m2m(feature_model, "z3")
# Get the operation
operation = dm.get_operation(z3_model, 'Z3AttributeOptimization')
# Provide the attributes to optimize and the goal for each one
operation.set_attributes({"price": OptimizationGoal.MINIMIZE})
# Execute the operation
operation.execute(z3_model)
# Get and print the result
result = operation.get_result()
print(result)
```
