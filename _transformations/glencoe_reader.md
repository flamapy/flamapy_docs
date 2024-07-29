---
title: Glencoe Reader
layout: default
parent: Transformations
grand_parent: Flamapy as framework
permalink: /framework/transformations/glencoe_reader
nav_order: 1
metamodel: flamapy_fm
type: text_to_model
---

# Glencoe Reader

Glencoe is an easy to use web application which enables you to visualize, analyze and configure multivariant product lines. It is backed by well-known and industry approved concepts as well as state-of-the-art approaches based on current research.

{% include flamapy.html %} relies on file extensions to identify which transformation is required. If you are not an expert we recommend to specify the correct extension for this file type. **The file extension for this file is .gfm.json**

---
## Code Examples
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation 
# required to get to the fm metamodel
# the transformation is identified by file extension .gfm.json
feature_model = dm.use_transformation_t2m(model_path,'fm') 
# Call the operation, no automatic transformations will be needed
print(feature_model)
```