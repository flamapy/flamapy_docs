---
layout: default
title: Getting started
nav_order: 2
---

# Getting started
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview
{% include flamapy.html %} provides an ecosystem to build up automated analysis tools [AAFM](https://doi.org/10.1145/3336294.3342373). While the framework support any kind of variability model, it provides easy use and extensibility in the case of feature models. 

## <i class="fa-solid fa-laptop"></i> Installation
To analyze feature models, you can rely on the `flamapy` distribution. **It requires Python >= 3.9**.  

{: .important }
> It's recommended to use a **virtual environment** (venv) for installation to avoid conflicts with other packages. Here’s how you can set it up:
> ```
> python -m venv flamapyenv && source flamapyenv/bin/activate
> ```   

Install the distribution:

```
pip install flamapy
```

## <i class="fa-solid fa-toolbox"></i> Basic operations

To test some basic operations, you need UVL models. Several are available at [UVLHub](https://www.uvlhub.io). If you prefer, you can download a test one:

```
wget -q "https://raw.githubusercontent.com/flamapy/flamapy/main/resources/models/simple/valid_model.uvl"
wget -q "https://raw.githubusercontent.com/flamapy/flamapy/main/resources/configurations/valid_configuration.csvconf"
```

Now we will present some examples of operations so you can check if the tool is working as expected, but first, let's see which operations are available using the `flamapy` command line.

```
flamapy --help
```

### Validate the model

To check if the model is valid, run:

```
flamapy satisfiable ./valid_model.uvl
```

### Get all configurations depicted in a model

To generate all possible configurations from the model, use:

```
flamapy configurations ./valid_model.uvl
```

### Validate a configuration

To verify if a specific configuration is valid, run:

```
flamapy satisfiable_configuration ./valid_model.uvl ./valid_configuration.csvconf
```
---

## <i class="fa-solid fa-magnifying-glass-chart"></i> I want to use more feature models analysis operations:

{% include flamapy.html %} runs on a framework based on `Core / Plugins` architecture. If you are interested in more feature model operations, check the [flama as a tool sute](/analysis)

### Option 1: using the feature models distribution

We have prepared `flamapy` to provide support by default to the most used operations in a ready and easy way of using. You can execute it using an easy-to-use facade, a cli o directly using the framework. You can see how to execute each operation and which interface are available in the [operations] documentation.

### Option 2: using the framework as it is

You can choose not to use the distribution. In that case, yo have to select the most suitable plugins for your variability model analysis. Therefore **you have to install the core and the corresponding plugins**.

You can check the rest of [plugins]({{site.baseurl}}/framework/plugins).

