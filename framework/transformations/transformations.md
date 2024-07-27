---
layout: default
title: Transformations
has_children: true
parent: flamapy as framework
permalink: /framework/transformations
nav_order: 1
---

### Flamapy Framework Architecture and Model Transformations

The flamapy tool relies on the flampy framework which is heavily inspired by Model-Driven Development (MDD) principles, focusing on facilitating the automated analysis of feature models through a structured and modular approach. Here’s an overview of how the architecture and model transformations work within Flamapy:

**Core Concepts**:
1. **Metamodels**: Represent the abstract syntax of different variability models (e.g., feature models). Each metamodel defines the structure and constraints of the models it represents.
2. **Plugins**: Encapsulate metamodels, transformations, and operations. Plugins allow the framework to be extended and customized for various analysis tasks.
3. **Transformations**: Divided into three main types:
   - **Text-to-Model (T2M)**: Converts textual representations of models into in-memory objects.
   - **Model-to-Text (M2T)**: Serializes in-memory models back into text formats.
   - **Model-to-Model (M2M)**: Transforms models from one metamodel to another, facilitating different types of analysis.

#### Model Transformations

**1. Text-to-Model (T2M) Transformations**:
   - **Purpose**: To read and parse the textual representation of feature models into their corresponding in-memory objects.
   - **Example**: Reading a UVL (Universal Variability Language) file and converting it into an internal feature model representation.

**2. Model-to-Text (M2T) Transformations**:
   - **Purpose**: To serialize the in-memory model objects into a specific textual format, enabling storage, sharing, and further processing.
   - **Example**: Converting an internal feature model representation back into a UVL file or other supported formats like XML.

**3. Model-to-Model (M2M) Transformations**:
   - **Purpose**: To translate models between different metamodels, often required for leveraging various analysis tools and techniques.
   - **Example**: Transforming a feature model into a SAT (Boolean satisfiability problem) representation to perform complex constraint analysis.

#### Example Scenario

1. **Loading a Model**: Use T2M transformation to read a UVL file and create an in-memory feature model.
2. **Basic Operations**: Perform operations such as counting the number of leaf features directly on the feature model.
3. **Complex Analysis**: Transform the feature model into a SAT metamodel using M2M transformation to leverage SAT solvers for deeper analysis, such as checking satisfiability or identifying dead features.
4. **Serialization**: Use M2T transformation to convert the SAT results back into a human-readable format for reporting.

#### Using Flamapy Framework

Here’s an example of how these transformations and operations might be used in the Flamapy framework:

```python
from flamapy.core.discover import DiscoverMetamodels

# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Text-to-Model transformation: Load the feature model from a UVL file
feature_model = dm.use_transformation_t2m('path/to/feature/model.uvl', 'fm')
# Perform an operation directly on the feature model
leaf_count = dm.use_operation(feature_model,'FMCountLeafs').get_result()
print(f'Leaf Count: {leaf_count}')
# Model-to-Model transformation: Transform the feature model to SAT metamodel
sat_model = dm.use_transformation_m2m(feature_model, 'pysat')
# Perform a SAT-based operation
sat = dm.use_operation(feature_model,'PySATSatisfiable').get_result()
print(f'Satisfiable: {sat}')
# Model-to-Text transformation: Serialize the SAT model to CNF format
dm.use_transformation_m2t(sat_model, 'path/to/output.cnf')
```
