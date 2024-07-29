---
title: Pickle Reader
layout: default
parent: Transformations
grand_parent: Flamapy as framework
permalink: /framework/transformations/pickle_reader
nav_order: 6
metamodel: flamapy_bdd
type: text_to_model
---

# Pickle Reader

This transformation reads a BDD serialized in Pickle format and converts it into an in-memory BDD representation. Pickle is a Python-specific format for serializing and deserializing Python object structures.

---
## Code Examples

```python
from flamapy.metamodels.bdd_metamodel.transformations.pickle_reader import PickleReader

# Load the BDD from a Pickle file
bdd_model = PickleReader('path/to/bdd.pickle').transform()

print(bdd_model)
```

