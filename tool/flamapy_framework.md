---
layout: default
title: flamapy framework
parent: Flamapy as tool
nav_order: 3
---

# flamapy framework

## Using the flamapy underlying framework

While this option required to know the underpinnings of the {% include flamapy.html %} framework. It also allows users to use any operation available in the ecosystem instead of just the most common ones. 

This interface would require to use Python, for example like this:

```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
# Use BDDConfigurations if you want to rely on BDD solver
result = dm.use_operation_from_file("PySATSatisfiable","path/to/feature/model")
print(result)
```

## Supported operations

To run other operations that could be less tested, you have to look at their names in the GitHub repositories of the [plugins](framework/plugins). However, most of the operations are already documented with code snippets.

<ul>
  {% assign fm_operations = site.operations | where: "python", true %}
  {% for operation in fm_operations %}
    <li><a href="{{ operation.url }}">{{ operation.title }}</a></li>
  {% endfor %}
</ul>