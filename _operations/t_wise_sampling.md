---
title: T wise sampling
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/t_wise_sampling

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

# T wise sampling
**Description**:
Returns a t-wise (combinatorial) sample: a set of valid configurations that covers every satisfiable combination of ``t`` feature selections (pairwise for ``t = 2``).

TODO: application and example prose.

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `t_wise_sampling(self, t: int = 2, backend: Optional[str] = None)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `t` | int | no | 2 |

**Default backend**: sat (selectable via `backend=`)

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_metamodel | yes | — |

<!-- END GENERATED -->
