---
layout: default
title: Plugins
has_children: true
parent: Flamapy as framework
permalink: /framework/plugins
nav_order: 1
---

# Plugins
{: .no_toc }

The {% include flamapy.html %} framework is designed to support automated analysis of feature models through a modular and extensible architecture. This flexibility is primarily achieved through the use of plugins, each encapsulating specific functionality, metamodels, and operations.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Concept of plugins

**Plugins** in {% include flamapy.html %} are the fundamental building blocks that extend the framework’s capabilities. Each plugin is designed to handle a specific type of analysis or transformation related to feature models. The plugins encapsulate:

### Metamodel classes
Define the structure and constraints of the variability models.

### Operations
Implement the actual analyses or computations that can be performed on the models.

### Transformations
Handle the conversion between different model representations, crucial for leveraging various computational techniques.

## Architecture overview

### Core plugin
The core plugin provides the foundational elements of the framework, including interfaces for different transformations (Text-to-Model, Model-to-Text, Model-to-Model), and mechanisms for identifying and executing available operations.

### Metamodel plugins
These plugins define the specific variability models and their associated operations and transformations. Examples include the feature model plugin, PySAT plugin, and BDD plugin.

## Available plugins

{% include flamapy.html %} offers a variety of plugins, each tailored to specific analysis needs and model types. Here are some of the key plugins available. Each plugin is provided in the [Pypi](https://pypi.org/project/flamapy/) package manager:

### flamapy_fw
This is the main repository hosting the core components of {% include flamapy.html %}. It includes the essential infrastructure for the framework, enabling plugin management, and execution of operations and transformations. [Github](https://github.com/flamapy/flamapy_fw)

### fm_metamodel
Hosts the concrete classes for feature models. It supports multiple feature model formats and provides various operations such as counting leaf features, estimating the number of valid configurations, and identifying core features. [Github](https://github.com/flamapy/fm_metamodel)

### pysat_metamodel
Provides the integration with PySAT, a meta-solver that enables the analysis of feature models using various SAT solvers. This plugin is essential for performing constraint satisfaction problems and other complex analyses. [Github](https://github.com/flamapy/pysat_metamodel)

### bdd_metamodel
Supports Binary Decision Diagrams (BDDs) for the automated analysis of feature models. This plugin is particularly useful for operations that benefit from BDD techniques, such as counting valid configurations efficiently. [Github](https://github.com/flamapy/bdd_metamodel)
