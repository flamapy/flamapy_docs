---
title: SPLOT Writer
layout: default
parent: Transformations
grand_parent: flamapy as framework
nav_order: 1
metamodel: flamapy_fm
type: model_to_text
---

## SPLOT Writer

"SPLot" (Software Product Line online tools) refers to a suite of tools designed to assist with the management and configuration of software product lines (SPLs). SPLs are sets of software-intensive systems that share a common set of features but also exhibit variations to meet different customer needs or market demands.

flamapy relies on file extensions to identify which transformation is required. If you are not an expert we recommend to specify the correct extension for this file type. **The file extension for this file is .sxfm**

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
dm.use_transformation_m2t(feature_model,'path/to/feature/model.sxfm')
```