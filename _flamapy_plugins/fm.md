---
layout: default
title: Feature model plugin
parent: Plugins
grand_parent: flamapy as framework
permalink: /framework/plugins/feature_model_plugin
nav_order: 2
---

# Feature model plugin
{: .no_toc }


The feature model plugin provides the metaclases required to work with feature models.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

{: .highlight }
> Official repository
>
> ```
> https://www.github.com/flamapy/fm_metamodel
> ```

## fm_metamodel plugin of flamapy framework

The `fm_metamodel` plugin is a crucial component of the {% include flamapy.html %} framework, providing the concrete classes and operations necessary for working with feature models. This plugin encapsulates the core functionalities required for defining, transforming, and analyzing feature models, making it a fundamental part of the {% include flamapy.html %} ecosystem.

### Features of the fm_metamodel Plugin

1. **Metamodel Classes**:
   - Defines the structure and constraints of feature models.
   - Supports multiple feature model formats, ensuring compatibility and flexibility.

2. **Operations**:
   - Implements various operations specific to feature models, such as counting leaf features, estimating the number of valid configurations, and identifying core features.
   - Provides robust mechanisms for performing detailed analyses on feature models.

3. **Transformations**:
   - Supports Text-to-Model (T2M) transformations to read feature models from various textual representations.
   - Enables Model-to-Model (M2M) transformations to convert feature models into different formats or computational paradigms for advanced analysis.
   - Facilitates Model-to-Text (M2T) transformations to serialize in-memory feature models back into text formats for storage and sharing.

### Installation instructions

To install the `fm_metamodel` plugin, follow these steps:

1. **Install Python**: Ensure that Python 3.9 or later is installed on your system.

2. **Install the fm_metamodel Plugin**:
   - Using pip, the Python package manager, you can install the `fm_metamodel` plugin directly from PyPI:
     ```bash
     pip install flamapy-fm
     ```
#### Links

- **PyPI**: [fm_metamodel on PyPI](https://pypi.org/project/flamapy-fm/)
- **GitHub Repository**: [fm_metamodel on GitHub](https://github.com/flamapy/fm_metamodel)

## Operations

Currently, this plugin enables the following operations. Note that these operations are executed without a backend solver which makes them scalable and fast while having some limitations:

<ul>
  {% assign fm_operations = site.operations | where: "flamapy_fm", true %}
  {% for operation in fm_operations %}
    <li><a href="{{ operation.url }}">{{ operation.title }}</a></li>
  {% endfor %}
</ul>


## Transformations supported

Currently this plugins enables a set of TextToModel transformations (a.k.a Parsers) and ModelToText transformations (a.k.a serializations) for the most common variability serializations found in the literatures. Concretely we support:

### Model to text transformations
<ul>
  {% assign transformations = site.transformations | where: "metamodel", "flamapy_fm" %}
  {% assign m2t_transformations = transformations | where: "type", "model_to_text" %}
  {% for transformation in m2t_transformations %}
    <li><a href="{{ transformation.url }}">{{ transformation.title }}</a></li>
  {% endfor %}
</ul>

### Text to model transformations
<ul>
  {% assign transformations = site.transformations | where: "metamodel", "flamapy_fm" %}
  {% assign t2m_transformations = transformations | where: "type", "text_to_model" %}
  {% for transformation in t2m_transformations %}
    <li><a href="{{ transformation.url }}">{{ transformation.title }}</a></li>
  {% endfor %}
</ul>

### Model to model transformations
<ul>
  {% assign transformations = site.transformations | where: "metamodel", "flamapy_fm" %}
  {% assign m2m_transformations = transformations | where: "type", "model_to_model" %}
  {% for transformation in m2m_transformations %}
    <li><a href="{{ transformation.url }}">{{ transformation.title }}</a></li>
  {% endfor %}
</ul>