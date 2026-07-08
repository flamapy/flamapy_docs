---
title: Configuration conflict
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/configuration_conflict

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

# Configuration conflict
**Description**:
Returns a minimal subset of the configuration decisions that is inconsistent with the feature model — the conflict explaining why the (partial) configuration cannot be completed.

TODO: application and example prose.

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `configuration_conflict(self, configuration_path: str)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `configuration_path` | str | yes | — |

**Default backend**: pysat_diagnosis

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_diagnosis_metamodel | yes | — |

<!-- END GENERATED -->
