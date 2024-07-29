---
title: FM to BDD
layout: default
parent: Transformations
grand_parent: Flamapy as framework
permalink: /framework/transformations/fm_to_bdd
nav_order: 2
metamodel: flamapy_bdd
type: model_to_model
---

# FM to BDD

This transformation converts a feature model into a Binary Decision Diagram (BDD) representation. BDDs are efficient for representing and manipulating logical functions, making them ideal for feature model analysis.

{% include flamapy.html %} relies on file extensions to identify the required transformation. Ensure you specify the correct file extension for this transformation.

---
## Code Examples

```python
from flamapy.metamodels.fm_metamodel.transformations.featureide_reader import FeatureIDEReader
from flamapy.metamodels.bdd_metamodel.transformations.fm_to_bdd import FmToBDD

# Load the feature model from a FeatureIDE file
feature_model = FeatureIDEReader('path/to/feature/model.xml').transform()

# Transform the feature model into a BDD representation
bdd_model = FmToBDD(feature_model).transform()

print(bdd_model)
```
