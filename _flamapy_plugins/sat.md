---
layout: default
title: SAT plugin
parent: Plugins
grand_parent: flamapy as framework
nav_order: 3
---

# PySAT plugin
{: .no_toc }


The pysat model plugin provides the metaclases required to work with SAT models and to transform feature models into SAT.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

{: .highlight }
> Official repository
>
> ```
> https://www.github.com/flamapy/pysat_metamodel
> ```

## Description

This plugin implements the classes to perform AAFM using the [PySAT](https://pysathq.github.io/) metasolver. It encompasses the set of variables and constraints objects to execute the analysis operations using PySAT as the backend. This allows us to rely on more than ten SAT solvers. This plugin offers the following functionality:

#### Features of the PySAT Metamodel Plugin

1. **SAT Solver Integration**:
   - Integrates with the PySAT toolkit, which supports a wide range of SAT solvers.
   - Enables the framework to perform complex constraint satisfaction problems, such as checking the satisfiability of feature models and identifying dead features.

2. **Metamodel Classes**:
   - Provides the necessary classes to represent the SAT-based metamodel, facilitating the transformation of feature models into SAT representations.

3. **Operations**:
   - Implements various operations specific to SAT-based analysis, such as satisfiability checks, identification of core features, and detection of dead features.
   - Offers robust mechanisms for performing detailed analyses on feature models using SAT solvers.

4. **Transformations**:
   - Supports Text-to-Model (T2M) transformations to read feature models and convert them into SAT representations.
   - Enables Model-to-Model (M2M) transformations to translate feature models into different formats for SAT-based analysis.
   - Facilitates Model-to-Text (M2T) transformations to serialize SAT results back into human-readable formats.

#### Installation Instructions

To install the `pysat_metamodel` plugin, follow these steps:

1. **Install Python**: Ensure that Python 3.9 or later is installed on your system.

2. **Install the PySAT Metamodel Plugin**:
   - Using pip, the Python package manager, you can install the `flamapy-sat` plugin directly from PyPI:
     ```bash
     pip install flamapy-sat
     ```

#### Links

- **PyPI**: [pysat_metamodel on PyPI](https://pypi.org/project/flamapy-sat/)
- **GitHub Repository**: [pysat_metamodel on GitHub](https://github.com/flamapy/pysat_metamodel)



## Operations

Currently, this plugin enables the following operations. Note that these operations are executed without a backend solver which makes them scalable and fast while having some limitations:

<ul>
  {% assign fm_operations = site.operations | where: "flamapy_sat", true %}
  {% for operation in fm_operations %}
    <li><a href="{{ operation.url }}">{{ operation.title }}</a></li>
  {% endfor %}
</ul>


# Transformations supported

Currently this plugins enables a set of TextToModel transformations (a.k.a Parsers) and ModelToText transformations (a.k.a serializations) for the most common variability serializations found in the literatures. Concretely we support:

**Model to text transformations**
<ul>
  {% assign transformations = site.transformations | where: "metamodel", "flamapy_sat" %}
  {% assign m2t_transformations = transformations | where: "type", "model_to_text" %}
  {% for transformation in m2t_transformations %}
    <li><a href="{{ transformation.url }}">{{ transformation.title }}</a></li>
  {% endfor %}
</ul>

**Text to model transformations**
<ul>
  {% assign transformations = site.transformations | where: "metamodel", "flamapy_sat" %}
  {% assign t2m_transformations = transformations | where: "type", "text_to_model" %}
  {% for transformation in t2m_transformations %}
    <li><a href="{{ transformation.url }}">{{ transformation.title }}</a></li>
  {% endfor %}
</ul>

**Model to model transformations**
<ul>
  {% assign transformations = site.transformations | where: "metamodel", "flamapy_sat" %}
  {% assign m2m_transformations = transformations | where: "type", "model_to_model" %}
  {% for transformation in m2m_transformations %}
    <li><a href="{{ transformation.url }}">{{ transformation.title }}</a></li>
  {% endfor %}
</ul>