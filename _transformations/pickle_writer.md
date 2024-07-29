---
title: Pickle Writer
layout: default
parent: Transformations
grand_parent: Flamapy as framework
permalink: /framework/transformations/pickle_writer
nav_order: 7
metamodel: flamapy_bdd
type: model_to_text
---

# Pickle Writer

This transformation serializes an in-memory BDD representation into a Pickle file. This is useful for saving BDDs in a Python-specific format that can be easily loaded and manipulated within Python environments.

---
## Code Examples

```python
from flamapy.metamodels.bdd_metamodel.transformations.pickle_writer import PickleWriter

# Save the BDD to a Pickle file
PickleWriter(path='path/to/save/bdd.pickle', source_model=bdd_model).transform()
```

