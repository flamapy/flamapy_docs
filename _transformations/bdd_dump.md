---
title: BDD Dump
layout: default
parent: Transformations
grand_parent: flamapy as framework
permalink: /framework/transformations/bdd_dump
nav_order: 8
metamodel: flamapy_bdd
type: model_to_text
---

# BDD Dump

This transformation serializes an in-memory BDD representation into a textual format for debugging and analysis purposes. The BDD Dump provides a detailed textual representation of the BDD structure.

---
## Code Examples

```python
from flamapy.metamodels.bdd_metamodel.transformations.bdd_dump import BDDDump

# Save the BDD to a textual dump file
BDDDump(path='path/to/save/bdd.txt', source_model=bdd_model).transform()
```
