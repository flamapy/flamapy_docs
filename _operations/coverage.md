---
title: Coverage
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/coverage

flamapy_sat: true
flamapy_bdd: false
flamapy_fm: false
flamapy_z3: false
flamapy_diagnosis: false
cmd: true
facade: true
python: true
rest: true
---

# Coverage
**Description**:
Measures the t-wise coverage of a configuration suite: the fraction of all satisfiable combinations of ``t`` feature selections that are covered by at least one of the given configurations (1.0 = full coverage).

TODO: application and example prose.

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `coverage(self, configurations: Any, t: int = 2)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `configurations` | Any | yes | — |
| `t` | int | no | 2 |

**Default backend**: sat

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_metamodel | yes | — |

<!-- END GENERATED -->
