---
title: Configuration repair
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/configuration_repair

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

# Configuration repair
**Description**:
Returns a minimal subset of the configuration decisions to retract in order to restore consistency with the feature model — how to repair an over-constrained configuration.

TODO: application and example prose.

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `configuration_repair(self, configuration_path: str)`

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
