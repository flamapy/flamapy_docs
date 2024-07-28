---
title: BDD to PNG Writer
layout: default
parent: Transformations
grand_parent: flamapy as framework
nav_order: 3
metamodel: flamapy_bdd
type: model_to_text
---

## BDD to PNG Writer

This transformation serializes a BDD representation of a feature model into a PNG image. This is useful for visualizing the structure of the BDD.

### Code Examples

```python
from flamapy.metamodels.bdd_metamodel.transformations.bdd_writer import BDDWriter, BDDDumpFormat

# Save the BDD as an image in PNG format
BDDWriter(path='path/to/save/bdd.png',
          source_model=bdd_model,
          roots=[bdd_model.root],
          output_format=BDDDumpFormat.PNG).transform()
```
