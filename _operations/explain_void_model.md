---
title: Explain void model
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/explain_void_model

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

# Explain void model
**Description**:
Explains why the feature model is void (encodes no valid configuration): a minimal set of relationships/cross-tree constraints that is already unsatisfiable (a QuickXPlain minimal conflict), in human-readable form.

TODO: application and example prose.

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `explain_void_model(self)`

**Default backend**: pysat_diagnosis

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_diagnosis_metamodel | yes | — |

<!-- END GENERATED -->
