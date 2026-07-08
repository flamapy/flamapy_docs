---
title: Explain false optional
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/explain_false_optional

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

# Explain false optional
**Description**:
Explains why a feature is false-optional (declared optional but present in every valid configuration that includes its parent): a minimal set of relationships/cross-tree constraints that forbids deselecting it while its parent is selected (a QuickXPlain minimal conflict of the model plus "parent = true, feature = false"), in human-readable form.

TODO: application and example prose.

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `explain_false_optional(self, feature_name: str)`

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
