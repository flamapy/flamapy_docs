---
layout: default
title: REST / SWAGGER
parent: flamapy as tool
nav_order: 4
---

# REST / SWAGGER

## Using the flamapy-rest plugin

{: .warning }
> This is a work in progress documentation page


REST (Representational State Transfer) is an architectural style for designing networked applications. It relies on a stateless, client-server communication protocol, usually HTTP. RESTful services allow resources, identified by URIs (Uniform Resource Identifiers), to be manipulated using a standard set of HTTP methods such as GET, POST, PUT, DELETE. This approach simplifies interactions between clients and servers, making it easier to build scalable and flexible web services.

Swagger, now part of the OpenAPI Initiative, is a powerful toolset for developing and documenting RESTful APIs. It provides a standard way to describe the structure of your APIs, enabling both humans and computers to understand the capabilities of the service without direct access to the source code or documentation. Swagger includes an intuitive user interface that allows developers to interact with the API endpoints, try out various requests, and visualize responses. This makes it an invaluable resource for both creating and consuming APIs, ensuring consistency, and improving the overall developer experience.

{% include flamapy.html %} offers a package that enable REST/SWAGGER access to the {% include flamapy.html %} facade. To use it, it is mandatoy to install this plugin appart. Take into account that it will add several dependencies. 

```bash
pip install flamapy-rest
```

Later, you should run the server within. 

TODO

## Swagger operations

Currently the SWAGGER documents the following operations

<ul>
  {% assign fm_operations = site.operations | where: "rest", true %}
  {% for operation in fm_operations %}
    <li><a href="{{ operation.url }}">{{ operation.title }}</a></li>
  {% endfor %}
</ul>