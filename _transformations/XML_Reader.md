---
title: XML Reader
layout: default
parent: Transformations
grand_parent: Flamapy as framework
permalink: /framework/transformations/xml_reader
nav_order: 1
metamodel: flamapy_fm
type: text_to_model
---

# XML Reader

This transformation is used to manipulate AFM serializations of feature models. It was used in the [fama](isa.us.es/fama) tool. FaMa-FW is a Framework for automated analyses of feature models integrating some of the most commonly used logic representations and solvers proposed in the literature (BDD, SAT and CSP solvers are implemented). FaMa is the first tool integrating different solvers for the automated analyses of feature models. It was implemented in Java and no longer maintained. 

## Example of serialization
This is an example of the serialization used by then
```
<?xml version="1.0" encoding="UTF-8" ?>
<feature-model xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.tdg-seville.info/benavides/featuremodelling/feature-model.xsd">
	<feature name="A">
	<binaryRelation name="BR-1">
		<cardinality min="0" max="1"/>
		<solitaryFeature name="B">
		</solitaryFeature>
	</binaryRelation>
	</feature>
</feature-model>
```

---
## Code Examples
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation 
# required to get to the fm metamodel
# the transformation is identified by file extension .xml
feature_model = dm.use_transformation_t2m(model_path,'fm') 
# Call the operation, no automatic transformations will be needed
print(feature_model)
```