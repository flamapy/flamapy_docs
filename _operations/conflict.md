---
title: Conflict
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/conflict

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

# Conflict
**Description**:
Returns a list of conflict sets: minimal subsets of the model constraints that are inconsistent with the given configuration.

TODO: application and example prose.

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `conflict(self, configuration_path: str, test_case_path: str = None, max_conflicts: int = None)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `configuration_path` | str | yes | — |
| `test_case_path` | str | no | None |
| `max_conflicts` | int | no | None |

**Default backend**: pysat_diagnosis

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_diagnosis_metamodel | yes | — |

<!-- END GENERATED -->
