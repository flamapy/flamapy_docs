---
title: DIMACS Writer
layout: default
parent: Transformations
grand_parent: flamapy as framework
nav_order: 11
metamodel: flamapy_pysat
type: model_to_text
---

## DIMACS Writer

This transformation serializes a PySAT model representation into a DIMACS file, which can be used as input for various SAT solvers.

### Code Examples

```python
from flamapy.metamodels.pysat_metamodel.transformations.dimacs_writer import DIMACSWriter

# Save the PySAT model to a DIMACS file
DIMACSWriter(path='path/to/save/model.dimacs', source_model=pysat_model).transform()
```

