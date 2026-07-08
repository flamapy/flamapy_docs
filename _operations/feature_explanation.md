---
title: Feature explanation
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/feature_explanation

flamapy_sat: false
flamapy_bdd: false
flamapy_fm: false
flamapy_z3: false
flamapy_diagnosis: true
cmd: true
facade: true
python: true
rest: true
---

# Feature explanation
**Description**:
Explains why a feature is forced (selected or deselected) by the current configuration: returns the minimal set of decisions responsible.

TODO: application and example prose.

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `feature_explanation(self, configuration_path: str, feature_name: str)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `configuration_path` | str | yes | — |
| `feature_name` | str | yes | — |

**Default backend**: pysat_diagnosis

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_diagnosis_metamodel | yes | — |

<!-- END GENERATED -->
