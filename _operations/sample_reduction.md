---
title: Sample reduction
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/sample_reduction

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

# Sample reduction
**Description**:
Reduces a configuration suite to a (greedily) minimal subset that preserves exactly the t-wise coverage the full suite already achieves.

TODO: application and example prose.

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `sample_reduction(self, configurations: Any, t: int = 2)`

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
