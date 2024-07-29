---
title: DIMACS Reader
layout: default
parent: Transformations
grand_parent: flamapy as framework
permalink: /framework/transformations/dimacs_reader
nav_order: 10
metamodel: flamapy_sat
type: text_to_model
---

# DIMACS Reader

This transformation reads a DIMACS file, a standard format for SAT solver input, and converts it into a PySAT model representation.

---
## Code Examples

```python
from flamapy.metamodels.pysat_metamodel.transformations.dimacs_reader import DIMACSReader

# Load the DIMACS file and convert it into a PySAT model
pysat_model = DIMACSReader('path/to/model.dimacs').transform()

print(pysat_model)
```
