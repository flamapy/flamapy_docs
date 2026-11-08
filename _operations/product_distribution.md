---
title: Product distribution
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/product_distribution

flamapy_sat: false
flamapy_bdd: true
flamapy_fm: false
flamapy_z3: false
flamapy_diagnosis: false
flamapy_sharpsat: false
flamapy_sdd: false
flamapy_dnnf: false
cmd: true
facade: true
python: true
rest: true
---

# Product distribution

**Description**: 
Analyzes the distribution of configurations within the feature model, identifying how features are grouped across valid configurations.

**Application**: 
Useful for understanding the variety and commonality of configurations generated from the feature model, aiding in product planning and strategy.

**Example**: 
Evaluating the distribution of various car models generated from a car feature model.

---
## Code Examples

### Command line usage
```bash
flamapy product_distribution "path/to/feature/model"
```

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
result = fm.product_distribution()
print(result)
```

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
feature_model = dm.use_transformation_t2m("path/to/feature/model", 'fm')
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

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `product_distribution(self)`

**Default backend**: bdd

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| bdd_metamodel | yes | 1000 |

<!-- END GENERATED -->
