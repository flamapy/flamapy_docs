---
layout: default
title: Python facade
parent: Flamapy as tool
nav_order: 2
---

# Python facade

## Easy to use python facade

Using Python as a scripting language can be highly convenient for developing scripts and integrating our analysis into other processes. However, learning a framework as complex as {% include flamapy.html %} can initially seem overwhelming. To alleviate this, {% include flamapy.html %} provides a straightforward method for executing the most common operations in Python.

After installing {% include flamapy.html %} we can use the tool as easy as 
```python
from flamapy.interfaces.python.flama_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# This method could be called with the param  with_sat: bool = True if you want to force pysat (useful for WASM enviroments) 
result = fm.satisfiable() 
print(result)
```

As you might notice, this interface is heavily inspired in the way [FAMILIAR](https://doi.org/10.1016/j.scico.2012.12.004) worked in the java 6 years 

## Supported operations

You can find a comprehensive list of the supported operations for the command line and code snipets if you want to run them:

<ul>
  {% assign fm_operations = site.operations | where: "facade", true %}
  {% for operation in fm_operations %}
    <li><a href="{{ operation.url }}">{{ operation.title }}</a></li>
  {% endfor %}
</ul>