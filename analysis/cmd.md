---
layout: default
title: Command line
parent: flamapy as a tool
nav_order: 1
---

# Command line interface


Nonetheless, as mentioned above, flamapy as a tool aims at being easily ussable, therefore it provides a simple command line interface that do not require to learn the framework and enable the most common feature modelling operations. For example, if you want to execute the satisfiable operation just run:

```bash
flamapy satisfiable "path/to/feature/model"
```

All available operations could be read by running
```bash
flamapy -h
```

However, below, you can find a comprehensive list of the supported operations for the command line and code snipets if you want to run them:

<ul>
  {% assign fm_operations = site.operations | where: "cmd", true %}
  {% for operation in fm_operations %}
    <li><a href="{{ operation.url }}">{{ operation.title }}</a></li>
  {% endfor %}
</ul>