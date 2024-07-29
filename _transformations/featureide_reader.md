---
title: FeatureIDE Reader
layout: default
parent: Transformations
grand_parent: flamapy as framework
permalink: /framework/transformations/featureide_reader
nav_order: 1
metamodel: flamapy_fm
type: text_to_model
---

# FeatureIDE Reader

FeatureIDE is an extensible framework for feature-oriented software development. Currently you can find the latest version in their [website](https://github.com/FeatureIDE/FeatureIDE)

{% include flamapy.html %} relies on file extensions to identify which transformation is required. If you are not an expert we recommend to specify the correct extension for this file type. **The file extension for this file is .fide**

---
## Code Examples
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation 
# required to get to the fm metamodel
# the transformation is identified by file extension .fide
feature_model = dm.use_transformation_t2m(model_path,'fm') 
# Call the operation, no automatic transformations will be needed
print(feature_model)
```