---
title: DDDMP Writer
layout: default
parent: Transformations
grand_parent: Flamapy as framework
permalink: /framework/transformations/dddmp_writer
nav_order: 5
metamodel: flamapy_bdd
type: model_to_text
---

# DDDMP Writer

This transformation serializes an in-memory BDD representation into a DDDMP file. This is useful for saving and sharing BDDs.

---
## Code Examples

```python
from flamapy.metamodels.bdd_metamodel.transformations.dddmp_writer import DDDMPWriter

# Save the BDD to a DDDMP file
DDDMPWriter(path='path/to/save/bdd.dddmp', source_model=bdd_model).transform()
```
