---
title: JSON Writer
layout: default
parent: Transformations
grand_parent: Flamapy as framework
permalink: /framework/transformations/json_writer
nav_order: 1
metamodel: flamapy_fm
type: text_to_model
---

# JSON Writer
JSON (JavaScript Object Notation) is a lightweight data interchange format that's easy for humans to read and write, and easy for machines to parse and generate. It is commonly used to transmit data between a server and web application as text.

{% include flamapy.html %} relies on file extensions to identify which transformation is required. If you are not an expert we recommend to specify the correct extension for this file type. **The file extension for this file is .json**

---
## Code Examples
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation 
# required to get to the fm metamodel
# the transformation is identified by file extension 
feature_model = dm.use_transformation_t2m(model_path,'fm') 
# write to file
dm.use_transformation_m2t(feature_model,'path/to/feature/model.json')
```