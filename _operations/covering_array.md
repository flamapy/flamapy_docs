---
title: Covering array
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/covering_array

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

# Covering array
**Description**:
Returns a t-wise covering array: a set of valid configurations covering every satisfiable combination of ``t`` feature selections (pairwise for ``t = 2``).

TODO: application and example prose.

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `covering_array(self, t: int = 2, seed: int = None)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `t` | int | no | 2 |
| `seed` | int | no | None |

**Default backend**: sat

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_metamodel | yes | — |

<!-- END GENERATED -->
