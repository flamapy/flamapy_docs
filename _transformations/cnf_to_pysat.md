---
title: CNF to PySAT
layout: default
parent: Transformations
grand_parent: Flamapy as framework
permalink: /framework/transformations/cnf_to_pysat
nav_order: 9
metamodel: flamapy_sat
type: text_to_model
---

# CNF to PySAT

This transformation reads a CNF (Conjunctive Normal Form) file and converts it into a PySAT model representation. CNF is a standard format for Boolean formulas used in SAT solvers.

---
## Code Examples

```python
from flamapy.metamodels.pysat_metamodel.transformations.cnf_to_pysat import CNFReader

# Load the CNF file and convert it into a PySAT model
pysat_model = CNFReader('path/to/model.cnf').transform()

print(pysat_model)
```
