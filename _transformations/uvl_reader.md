---
title: UVL Reader
layout: default
parent: Transformations
grand_parent: Flamapy as framework
permalink: /framework/transformations/uvl_reader
nav_order: 1
metamodel: flamapy_fm
type: text_to_model
---

# UVL Reader

The Universal Variability Language (UVL) is a language designed to specify variability in software product lines (SPLs). It aims to provide a standardized way to describe the features and variations within a product line, facilitating the management of different configurations and enabling tool interoperability.

## Key features

Key features of [Universal Variability Language (UVL)](https://universal-variability-language.github.io/):
### Standardization
UVL provides a common, standardized way to represent variability, making it easier to share and reuse models across different tools and organizations.

### Expressiveness
It is designed to be expressive enough to capture complex variability, including hierarchical features, constraints, and dependencies between features.

### Simplicity and Usability
UVL aims to be simple to use, with a syntax that is easy to understand for both humans and machines. This makes it accessible to a wide range of stakeholders, including developers, product managers, and other domain experts.

### Tool Support
There is growing support for UVL in various SPL tools, which can interpret and manipulate UVL models. This includes tools for feature modeling, configuration, analysis, and visualization.

### Interoperability
By using a common language like UVL, different tools and platforms can more easily interoperate, enabling a more integrated and efficient SPL engineering process.

{% include flamapy.html %} relies on file extensions to identify which transformation is required. If you are not an expert we recommend to specify the correct extension for this file type. **The file extension for this file is .uvl**

A snipet of how it looks like 
```
features
    Sandwich
        mandatory
            Bread
        optional
            Sauce
                alternative
                    Ketchup
                    Mustard
            Cheese
constraints
    Ketchup => Cheese
```
---
## Code Examples
```python
from flamapy.core.discover import DiscoverMetamodels
# Initiallize the dicover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation 
# required to get to the fm metamodel
# the transformation is identified by file extension .uvl
feature_model = dm.use_transformation_t2m("path/to/feature/model",'fm') 
# Call the operation, no automatic transformations will be needed
print(feature_model)
```