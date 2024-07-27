---
layout: default
title: BDD plugin
parent: Plugins
grand_parent: flamapy as framework
nav_order: 4
---

# BDD plugin
{: .no_toc }


The BDD model plugin provides the metaclases required to work with 
SAT models and to transform feature models into BDD.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

{: .highlight }
> Official repository
>
> ```
> https://www.github.com/flamapy/bdd_metamodel
> ```
### BDD Metamodel Plugin of Flamapy Framework

The `bdd_metamodel` plugin is an integral part of the Flamapy framework, designed to support Binary Decision Diagrams (BDDs) representations for feature models. This plugin enhances the framework's capability to handle complex feature model analyses using BDDs, which are efficient for various computational tasks.

#### Features of the BDD Metamodel Plugin

1. **BDD Integration**:
   - Utilizes the `dd` library to manipulate BDDs.
   - Efficiently represents and processes feature models using BDDs, which can handle large and complex models effectively.

2. **Metamodel Classes**:
   - Provides necessary classes to represent BDD-based feature models.
   - Supports various transformations and operations to facilitate detailed analysis.

3. **Operations**:
   - Implements numerous operations such as counting the number of products, sampling configurations, and calculating feature inclusion probabilities.
   - Supports partial configurations for more targeted analyses.

4. **Transformations**:
   - **Text-to-Model (T2M)**: Reads feature models from textual representations.
   - **Model-to-Model (M2M)**: Transforms feature models into BDD representations for analysis.
   - **Model-to-Text (M2T)**: Serializes BDD representations into different formats, including PNG, SVG, and DDDMP.


{: .highlight }
> This plugin could be installed in a different version that enables the analysis of [colosal feature models](https://doi.org/10.1007/s10664-021-10102-5). **Use at your own risk** (pip install flamapy-bdd==2.0.0.colosal) by taking a look to the pypi repo and choosing the most appropiaded version
>
> ```
> https://www.github.com/flamapy/bdd_metamodel, uned branch
> ```

#### Installation Instructions

To install the `bdd_metamodel` plugin, follow these steps:

1. **Install Python**: Ensure that Python 3.9 or later is installed on your system.

2. **Install the BDD Metamodel Plugin**:
   - Using pip, the Python package manager, you can install the `bdd_metamodel` plugin directly from PyPI:
     ```bash
     pip install flamapy-bdd
     ```

#### Links

- **PyPI**: [bdd_metamodel on PyPI](https://pypi.org/project/flamapy-bdd/)
- **GitHub Repository**: [bdd_metamodel on GitHub](https://github.com/flamapy/bdd_metamodel)


## Operations

Currently, this plugin enables the following operations. Note that these operations are executed without a backend solver which makes them scalable and fast while having some limitations:

<ul>
  {% assign fm_operations = site.operations | where: "flamapy_bdd", true %}
  {% for operation in fm_operations %}
    <li><a href="{{ operation.url }}">{{ operation.title }}</a></li>
  {% endfor %}
</ul>


# Transformations supported

Currently this plugins enables a set of TextToModel transformations (a.k.a Parsers) and ModelToText transformations (a.k.a serializations) for the most common variability serializations found in the literatures. Concretely we support:

**Model to text transformations**
<ul>
  {% assign transformations = site.transformations | where: "metamodel", "flamapy_bdd" %}
  {% assign m2t_transformations = transformations | where: "type", "model_to_text" %}
  {% for transformation in m2t_transformations %}
    <li><a href="{{ transformation.url }}">{{ transformation.title }}</a></li>
  {% endfor %}
</ul>

**Text to model transformations**
<ul>
  {% assign transformations = site.transformations | where: "metamodel", "flamapy_bdd" %}
  {% assign t2m_transformations = transformations | where: "type", "text_to_model" %}
  {% for transformation in t2m_transformations %}
    <li><a href="{{ transformation.url }}">{{ transformation.title }}</a></li>
  {% endfor %}
</ul>

**Model to model transformations**
<ul>
  {% assign transformations = site.transformations | where: "metamodel", "flamapy_bdd" %}
  {% assign m2m_transformations = transformations | where: "type", "model_to_model" %}
  {% for transformation in m2m_transformations %}
    <li><a href="{{ transformation.url }}">{{ transformation.title }}</a></li>
  {% endfor %}
</ul>
