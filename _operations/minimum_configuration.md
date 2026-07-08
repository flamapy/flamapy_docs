---
title: Minimum configuration
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/minimum_configuration

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

# Minimum configuration
**Description**:
Returns a valid configuration with the fewest selected features (the minimum working configuration).

TODO: application and example prose.

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `minimum_configuration(self, backend: Optional[str] = None)`

**Default backend**: sat (selectable via `backend=`)

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_metamodel | yes | — |

<!-- END GENERATED -->
