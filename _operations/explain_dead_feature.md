---
title: Explain dead feature
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/explain_dead_feature

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

# Explain dead feature
**Description**:
Explains why a feature is dead (appears in no valid configuration): a minimal set of relationships/cross-tree constraints that forbids selecting it (a QuickXPlain minimal conflict of the model plus "feature = true"), in human-readable form.

TODO: application and example prose.

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `explain_dead_feature(self, feature_name: str)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `feature_name` | str | yes | — |

**Default backend**: pysat_diagnosis

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_diagnosis_metamodel | yes | — |

<!-- END GENERATED -->
