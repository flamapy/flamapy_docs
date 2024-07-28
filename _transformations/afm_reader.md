---
title: AFM Reader
layout: default
parent: Transformations
grand_parent: flamapy as framework
nav_order: 1
metamodel: flamapy_fm
type: text_to_model
---

## AFM reader

This transformation is used to manipulate AFM serializations of feature models. It was used in the [fama](isa.us.es/fama) tool. FaMa-FW is a Framework for automated analyses of feature models integrating some of the most commonly used logic representations and solvers proposed in the literature (BDD, SAT and CSP solvers are implemented). FaMa is the first tool integrating different solvers for the automated analyses of feature models. It was implemented in Java and no longer maintained. 

flamapy relies on file extensions to identify which transformation is required. If you are not an expert we recommend to specify the correct extension for this file type. **The file extension for this file is .afm**

### This is an example of the serialization used by then
```
%Relationships
root : [F1]  F2  F3  F4  F5 [1,3] {F6 F7 F8 }[1,2] {F9 F10 };
F3 : [F11]  F12 [F13] [F14]  F15  F16  F17 [1,2] {F18 F19 };

%Attributes
F1.Attribute1: Integer[0 to 100],17,0;
F1.Attribute0: Integer[0 to 100],75,0;
F1.Attribute3: Integer[0 to 100],85,0;
F1.Attribute2: Integer[0 to 100],45,0;
F1.Attribute4: Integer[0 to 100],85,0;
F2.Attribute1: Integer[0 to 100],37,0;

%Constraints
F8 requires F2;
F5 requires F10;
F10 requires F11;
F15 excludes F6;
F4 requires F7;
F7 requires F8;
```

---
## Code Examples
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation 
# required to get to the fm metamodel
# the transformation is identified by file extension .afm
feature_model = dm.use_transformation_t2m(model_path,'fm') 
print(feature_model)
```