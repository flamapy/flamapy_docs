---
layout: default
title: Diagnosis plugin
parent: Plugins
grand_parent: Flamapy as framework
permalink: /framework/plugins/diagnosis_plugin
nav_order: 7
---

# Diagnosis plugin
{: .no_toc }

The diagnosis plugin extends the PySAT metamodel with conflict detection and diagnosis capabilities, explaining why a configuration is inconsistent with a feature model.
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

## pysat_diagnosis metamodel plugin of flamapy framework

The `pysat_diagnosis_metamodel` plugin builds on top of the PySAT metamodel to support automated debugging of feature models and configurations. Given a configuration and a test case, it computes **conflict sets** (minimal subsets of constraints that are inconsistent) and **diagnoses** (minimal sets of constraints whose removal restores consistency). It is shipped together with the `flamapy-sat` package.

### Features of the Diagnosis Metamodel Plugin

1. **Conflict and Diagnosis Algorithms**
   - Implements QuickXPlain for computing minimal conflict sets.
   - Implements FastDiag for computing minimal diagnoses.
   - Uses an HSDAG (Hitting Set Directed Acyclic Graph) to enumerate multiple conflicts/diagnoses.

2. **Metamodel Classes**
   - Provides the `DiagnosisModel` (extension `pysat_diagnosis`) to represent the knowledge base, the constraints set, and the diagnosis task.

3. **Operations**
   - Conflict detection and diagnosis given a configuration and a test case.

4. **Transformations**
   - **Model-to-Model (M2M)**: Transforms feature models (`fm`) into the diagnosis model (`pysat_diagnosis`).

### Installation instructions

The diagnosis metamodel is distributed together with the PySAT plugin:

1. **Install Python**: Ensure that Python 3.9 or later is installed on your system.

2. **Install the PySAT Metamodel Plugin** (which includes the diagnosis metamodel):
   ```bash
   pip install flamapy-sat
   ```

### Links

- **PyPI**: [pysat_metamodel on PyPI](https://pypi.org/project/flamapy-sat/)
- **GitHub Repository**: [pysat_metamodel on GitHub](https://github.com/flamapy/pysat_metamodel)


## Operations

Currently, this plugin enables the following operations:

<ul>
  {% assign fm_operations = site.operations | where: "flamapy_diagnosis", true %}
  {% for operation in fm_operations %}
    <li><a href="{{ operation.url }}">{{ operation.title }}</a></li>
  {% endfor %}
</ul>


## Transformations supported

### Model to model transformations
<ul>
  {% assign transformations = site.transformations | where: "metamodel", "flamapy_diagnosis" %}
  {% assign m2m_transformations = transformations | where: "type", "model_to_model" %}
  {% for transformation in m2m_transformations %}
    <li><a href="{{ transformation.url }}">{{ transformation.title }}</a></li>
  {% endfor %}
</ul>
