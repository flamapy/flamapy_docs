---
layout: default
title: flamapy framework
parent: flamapy as a tool
nav_order: 3
---

# Using the flamapy underlying framework

While this opetion required to know the udnerpinnings of the flamapy framework. It also allows users to use ny operation available in the ecosystem instead of just the most common ones. 

This interface would require to use python, for example like this:

```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Call the operation. Transformations will be automatically executed
# Use BDDConfigurations if you want to rely on BDD solver
result=dm.use_operation_from_file("PySATSatisfiable","path/to/feature/model")
print(result)
```

To un other operations, that could be less tested you have to take a look to the names of them in the github repositories of the [plugins](framework/plugins). However most of operations are already documented with code snippets in. 

<ul>
  {% assign fm_operations = site.operations | where: "python", true %}
  {% for operation in fm_operations %}
    <li><a href="{{ operation.url }}">{{ operation.title }}</a></li>
  {% endfor %}
</ul>