---
title: Minimal corrections
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/minimal_corrections

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

# Minimal corrections
**Description**:
Returns the minimal corrections for a void feature model: each correction is a minimal set of relationships/cross-tree constraints whose removal makes the model satisfiable (FastDiag diagnoses enumerated via HSDAG), in human-readable form.

TODO: application and example prose.

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `minimal_corrections(self, max_corrections: int = None)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `max_corrections` | int | no | None |

**Default backend**: pysat_diagnosis

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_diagnosis_metamodel | yes | — |

<!-- END GENERATED -->
