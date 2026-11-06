---
layout: default
title: REST / SWAGGER
parent: Flamapy as tool
nav_order: 4
---

# REST / SWAGGER

## Using the flamapy-rest plugin

REST (Representational State Transfer) is an architectural style for designing networked applications. It relies on a stateless, client-server communication protocol, usually HTTP. RESTful services allow resources, identified by URIs (Uniform Resource Identifiers), to be manipulated using a standard set of HTTP methods such as GET, POST, PUT, DELETE. This approach simplifies interactions between clients and servers, making it easier to build scalable and flexible web services.

Swagger, now part of the OpenAPI Initiative, is a powerful toolset for developing and documenting RESTful APIs. It provides a standard way to describe the structure of your APIs, enabling both humans and computers to understand the capabilities of the service without direct access to the source code or documentation. Swagger includes an intuitive user interface that allows developers to interact with the API endpoints, try out various requests, and visualize responses. This makes it an invaluable resource for both creating and consuming APIs, ensuring consistency, and improving the overall developer experience.

{% include flamapy.html %} offers a package that enable REST/SWAGGER access to the {% include flamapy.html %} facade. To use it, it is mandatoy to install this plugin appart. Take into account that it will add several dependencies. 

```bash
pip install flamapy-rest
```

Later, you should run the server within. 

```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

Also a working version is available on onRender [HERE](https://flamapy-rest.onrender.com)

## The same operations as the Python facade

Every operation of the [Python facade](/tool/python_facade) is a `POST` endpoint under
`/api/v1/operations/<operation>`, with the same parameters as the Python method sent as
multipart form fields: the model as the `model` file, files for the parameters that take a
path (`configuration`, `test_case`), JSON text for the structured ones (`objectives`,
`configurations`), plain values for the rest. The operations that return a feature model
(`generate_random_feature_model`, which needs no upload, and `generate_random_attribute`)
answer with UVL text.

```bash
curl -X POST http://localhost:8000/api/v1/operations/configurations_number \
  -F "model=@valid_model.uvl"
```

### Choosing the backend over REST

The `backend` field works like the Python argument: a plugin name, or `auto` to let the
[query planner](/tool/choosing_backend) choose; `allow_approximate=true` also admits approximate
implementations. The response body is the bare value, and the provenance the facade keeps in
`last_result` comes back in headers: `X-Flamapy-Plugin`, `X-Flamapy-Backend`, `X-Flamapy-Exact`,
`X-Flamapy-Planner` (the planner's choice and reasons under `auto`) and `X-Flamapy-Wall-Time`.

```bash
curl -i -X POST http://localhost:8000/api/v1/operations/configurations_number \
  -F "model=@valid_model.uvl" -F "backend=auto"
# X-Flamapy-Backend: bdd
# X-Flamapy-Planner: auto: bdd: estimated 12 ms (transformation 11, operation 1), historical default backend
# 816
```

`POST /api/v1/operations/<operation>/plan` returns the planner's decision without running the
operation (the facade's `plan()`), and a call that no installed plugin can run answers `422` with
the reason. Setting `FLAMAPY_BACKEND=auto` in the server's environment makes `auto` the default
for every call that does not name a backend.

## Swagger operations

Currently the SWAGGER documents the following operations

<ul>
  {% assign fm_operations = site.operations | where: "rest", true %}
  {% for operation in fm_operations %}
    <li><a href="{{ operation.url }}">{{ operation.title }}</a></li>
  {% endfor %}
</ul>