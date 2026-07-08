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
cmd: true
facade: true
python: true
rest: true
---

# Generate random feature model
**Description**:
Generates a random synthetic feature model and returns it as a FeatureModel.

TODO: application and example prose.

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
