---
title: DDDMP Reader
layout: default
parent: Transformations
grand_parent: flamapy as framework
permalink: /framework/transformations/dddmp_reader
nav_order: 4
metamodel: flamapy_bdd
type: text_to_model
---

# DDDMP Reader

This transformation reads a BDD serialized in DDDMP format and converts it into an in-memory BDD representation. DDDMP is a common format for storing and exchanging BDDs.

---
## Code Examples

```python
from flamapy.metamodels.bdd_metamodel.transformations.dddmp_reader import DDDMPReader

# Load the BDD from a DDDMP file
bdd_model = DDDMPReader('path/to/bdd.dddmp').transform()

print(bdd_model)
```
