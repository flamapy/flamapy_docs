---
layout: default
title: Operations
has_children: true
parent: flamapy as framework
permalink: /framework/operations
nav_order: 1
---
### Concept of Operations in Flamapy

The concept of operations in the Flamapy framework is a central component that defines the specific tasks or analyses that can be performed on feature models. Each operation is designed to extract useful information or metrics from the feature models, thereby aiding in various aspects of software product line engineering.

#### Tied to a Metamodel

In Flamapy, operations are intrinsically tied to the metamodel they are designed for. A metamodel provides the abstract syntax and semantic rules of the variability model, essentially defining the structure and constraints of the feature models it represents. Operations leverage these definitions to perform analyses that are specific to the type of variability model they are applied to. This ensures that the operations are context-aware and can handle the specific intricacies and rules of the underlying model.

For example, an operation designed to count the number of leaf features in a feature model must understand the hierarchical structure defined by the metamodel. Similarly, an operation to check the satisfiability of a configuration needs to interpret the constraints and dependencies specified by the metamodel.

#### Transformations for Operations

To facilitate the execution of operations across different types of variability models, Flamapy employs a series of transformations. These transformations are necessary to convert models between various representations, enabling the application of operations that might require different metamodels or computational paradigms. Take a look to [transformations](/framework/transformations) for more information

Currently flamapy offers the following operations implemented in the marked plugins/metamodels and available in the interfaces shown.

<style>
  table {
    border-collapse: collapse;
    width: 100%;
  }
  th, td {
    border: 1px solid black;
    padding: 0px;
    text-align: center;
    min-width:0rem
  }
  th {
    white-space: nowrap;
    border: 1px solid black;
  }
  td {
    width: 50px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
  }
  th:nth-child(4),
  td:nth-child(4) {
    border-right: 2px solid black; /* Add extra line after the third column */
  }
  
</style>

<table>
  <thead>
    <tr>
      <th rowspan="1"></th>
      <th colspan="3">Plugin</th>
      <th colspan="4">Interface</th>
    </tr>
    <tr>
      <th>Title</th>
      <th>FM</th>
      <th>SAT</th>
      <th>BDD</th>
      <th>CMD</th>
      <th>Facade</th>
      <th>Python</th>
      <th>REST</th>
    </tr>
  </thead>
  <tbody>
    {% for operation in site.operations %}
    <tr>
      <td><a href="{{ operation.url }}">{{ operation.title }}</a></td>
      <td>{% if operation.flamapy_fm %}✔{% else %}✘{% endif %}</td>
      <td>{% if operation.flamapy_sat %}✔{% else %}✘{% endif %}</td>
      <td>{% if operation.flampy_bdd %}✔{% else %}✘{% endif %}</td>
      <td>{% if operation.cmd %}✔{% else %}✘{% endif %}</td>
      <td>{% if operation.facade %}✔{% else %}✘{% endif %}</td>
      <td>{% if operation.python %}✔{% else %}✘{% endif %}</td>
      <td>{% if operation.rest %}✔{% else %}✘{% endif %}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
