---
title: FM to PySAT
layout: default
parent: Transformations
grand_parent: flamapy as framework
nav_order: 12
metamodel: flamapy_sat
type: model_to_model
---

## FM to PySAT

This transformation converts a feature model into a PySAT representation, enabling advanced SAT-based analysis of the feature model.

### Code Examples

```python
from flamapy.metamodels.fm_metamodel.transformations.featureide_reader import FeatureIDEReader
from flamapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPySAT

# Load the feature model from a FeatureIDE file
feature_model = FeatureIDEReader('path/to/feature/model.xml').transform()

# Transform the feature model into a PySAT representation
pysat_model = FmToPySAT(feature_model).transform()

print(pysat_model)
```
