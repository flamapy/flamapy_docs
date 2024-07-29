---
layout: default
title: Core plugin
parent: Plugins
grand_parent: flamapy as framework
permalink: /framework/plugins/core_plugin
nav_order: 1
---

# Core plugin
{: .no_toc }

The core component is the main entry point of {% include flamapy.html %}.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

{: .highlight }
> Official repository
>
> ```
> https://www.github.com/flamapy/flamapy_fw
> ```

## Core plugin of flamapy framework

The core plugin is the foundation of the {% include flamapy.html %} framework, providing essential functionalities and interfaces that support the integration and operation of various metamodels and plugins. It ensures the cohesive functioning of the framework, enabling seamless interaction between different components.

### Features of the core plugin

#### Transformation Interfaces

   - **Text-to-Model (T2M)**: Converts textual representations of feature models into in-memory objects.
   - **Model-to-Text (M2T)**: Serializes in-memory models back into text formats.
   - **Model-to-Model (M2M)**: Transforms models from one metamodel to another.

#### Operation Management

   - Provides a mechanism to identify and execute available operations on different metamodels.
   - Ensures that operations are performed correctly by managing the required transformations.

#### Plugin Management

   - Facilitates the discovery and integration of plugins.
   - Manages the communication between plugins and coordinates the execution of transformations and operations.

### Installation instructions

To install the core plugin of {% include flamapy.html %}, follow these steps:

1. **Install Python**: Ensure that Python 3.9 or later is installed on your system.

2. **Install the Core Plugin**:
   - Using pip, the Python package manager, you can install the core plugin directly from PyPI:
     ```bash
     pip install flamapy_fw
     ```

### Links

- **PyPI**: [Flamapy on PyPI](https://pypi.org/project/flamapy/)
- **GitHub Repository**: [Flamapy Core on GitHub](https://github.com/flamapy/flamapy_fw)

