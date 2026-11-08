---
title: Generate random feature model
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/generate_random_feature_model

flamapy_sat: false
flamapy_bdd: false
flamapy_fm: true
flamapy_z3: false
flamapy_diagnosis: false
flamapy_sharpsat: false
flamapy_sdd: false
flamapy_dnnf: false
cmd: false
facade: true
python: true
rest: true
---

# Generate random feature model

**Description**:
Generates a random synthetic feature model and returns it as a FeatureModel.

**Application**:
Produces synthetic feature models for benchmarking analysis operations or testing tools, with a controlled size, number of constraints and language level.

**Example**:
A reproducible 20-feature model with up to 5 cross-tree constraints, generated from a fixed seed and written to UVL.

---
## Code Examples

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Static method: no input model is needed
model = FLAMAFeatureModel.generate_random_feature_model(
    num_features=20, max_constraints=5, seed=42)
print(model)
```

### Python flamapy framework usage
```python
from flamapy.metamodels.fm_metamodel.operations import GenerateRandomFeatureModel
from flamapy.metamodels.fm_metamodel.transformations import UVLWriter
# Configure the generator
operation = GenerateRandomFeatureModel()
operation.set_num_features(20)
operation.set_max_constraints(5)
operation.set_seed(42)
# Other options: set_void(True) and set_language_level('boolean' | 'arithmetic' | 'type')
# Producer operation: it takes no input model
model = operation.execute().get_result()
# Save it as UVL
UVLWriter(path="random_model.uvl", source_model=model).transform()
print(model)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `generate_random_feature_model(num_features: int = 10, max_constraints: int = 3, seed: int = 0, void: bool = False, language_level: str = 'boolean')`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `num_features` | int | no | 10 |
| `max_constraints` | int | no | 3 |
| `seed` | int | no | 0 |
| `void` | bool | no | False |
| `language_level` | str | no | 'boolean' |

**Default backend**: none (runs on the feature model)

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| fm_metamodel | yes | — |

<!-- END GENERATED -->
