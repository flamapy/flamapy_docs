---
layout: default
title: Community and lab plugins
parent: Plugins
grand_parent: Flamapy as framework
permalink: /framework/plugins/community_plugins
nav_order: 10
---

# Community and lab plugins
{: .no_toc }

Plugins that extend {% include flamapy.html %} beyond its core distribution: community-contributed
knowledge-compilation backends and research prototypes from the flamapy team.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## SDD metamodel plugin

The `sdd_metamodel` plugin (`flamapy-sdd`) compiles a feature model into a **Sentential Decision
Diagram (SDD)** for **exact** analysis. SDD is a knowledge-compilation language (a subset of
d-DNNF, strictly more succinct than OBDD in cases), so it supports exact polytime queries — model
counting, consistency and conditioning — and can stay compact on models where a BDD blows up. It
is built on top of the SAT metamodel's CNF using the [PySDD](https://github.com/wannesm/PySDD)
library.

{: .highlight }
> Official repository
>
> ```
> https://github.com/flamapy/sdd_metamodel
> ```

### Operations

<ul>
  {% assign sdd_operations = site.operations | where: "flamapy_sdd", true %}
  {% for operation in sdd_operations %}
    <li><a href="{{ operation.url }}">{{ operation.title }}</a></li>
  {% endfor %}
</ul>

### Installation

```
pip install flamapy-sdd
```

or, together with the distribution, `pip install "flamapy[sdd]"`.

### Usage

Through the Python facade, pick the backend with `backend="sdd"`:

```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel

fm = FLAMAFeatureModel("path/to/feature/model")
print(fm.configurations_number(backend="sdd"))
```

Or through the framework, with the `sdd` model extension:

```python
from flamapy.core.discover import DiscoverMetamodels

dm = DiscoverMetamodels()
feature_model = dm.use_transformation_t2m("path/to/feature/model", 'fm')
sdd_model = dm.use_transformation_m2m(feature_model, "sdd")
operation = dm.get_operation(sdd_model, 'SDDConfigurationsNumber')
operation.execute(sdd_model)
print(operation.get_result())
```

## d-DNNF metamodel plugin

The `dnnf_metamodel` plugin (`flamapy-dnnf`) provides **exact** analysis via **d-DNNF knowledge
compilation** using the [d4](https://github.com/crillab/d4) compiler. d-DNNF (deterministic
Decomposable Negation Normal Form) is a highly succinct compilation target that supports exact,
polytime model counting and scales to large industrial models where OBDD compilation explodes.

It complements the counting backends: `flamapy-bdd` (OBDD, exact) and `flamapy-sdd` (SDD, exact,
more succinct) compile in-process, `flamapy-sharpsat` gives an *approximate* count for very large
models, and `flamapy-dnnf` gives an **exact** count at scale.

{: .highlight }
> Official repository
>
> ```
> https://github.com/flamapy/dnnf_metamodel
> ```

### Requirements: install the d4 compiler

{: .important }
> `pip install flamapy-dnnf` is **not enough on its own**: the plugin calls the
> [d4](https://github.com/crillab/d4) knowledge compiler, a native C++ binary that has **no PyPI
> package** and must be installed separately.

1. Build d4 from source by following the instructions in its repository,
   <https://github.com/crillab/d4>.
2. Make the binary available to flamapy in one of two ways:
   - put it on your `PATH` under the name `d4`, or
   - point the `FLAMAPY_D4_PATH` environment variable at the binary:
     ```bash
     export FLAMAPY_D4_PATH=/path/to/d4
     ```
3. Check that it is found, e.g. with `which d4` (or `ls "$FLAMAPY_D4_PATH"`).

If d4 cannot be found, every d-DNNF operation fails with
`The d4 compiler was not found. Install d4 (https://github.com/crillab/d4) and expose it as "d4"
on PATH or via the FLAMAPY_D4_PATH environment variable.` (the Python facade logs this error and
returns `None`).

### Operations

<ul>
  {% assign dnnf_operations = site.operations | where: "flamapy_dnnf", true %}
  {% for operation in dnnf_operations %}
    <li><a href="{{ operation.url }}">{{ operation.title }}</a></li>
  {% endfor %}
</ul>

### Installation

```
pip install flamapy-dnnf
```

or, together with the distribution, `pip install "flamapy[dnnf]"`. Remember to also install d4
(see the requirements above).

### Usage

Through the Python facade, pick the backend with `backend="dnnf"`:

```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel

fm = FLAMAFeatureModel("path/to/feature/model")
print(fm.configurations_number(backend="dnnf"))
```

Or through the framework, with the `dnnf` model extension:

```python
from flamapy.core.discover import DiscoverMetamodels

dm = DiscoverMetamodels()
feature_model = dm.use_transformation_t2m("path/to/feature/model", 'fm')
dnnf_model = dm.use_transformation_m2m(feature_model, "dnnf")
operation = dm.get_operation(dnnf_model, 'DDNNFConfigurationsNumber')
operation.execute(dnnf_model)
print(operation.get_result())
```

## BDD for colosal feature models

The BDD model plugin provides the metaclases required to work with 
colosal feature models and transform them to BDD.

However, this implementation relies on the optimizations performed in the paper by Ruben Heradio, David Fernández-Amorós, José A. Galindo, David Benavides, and Don S. Batory: "Uniform and scalable sampling of highly configurable systems" (*Empirical Software Engineering*, 27(2): 44, 2022), which enables better scalability of the analysis.

{: .highlight }
> Official repository
>
> ```
> https://www.github.com/flamapy/bdd_metamodel
> ```

### Operations
Currently, this plugin enables the following operations. 

* Sampling
* Feature Inclusion Probability
* Product distribution

### Transformations supported
Currently this plugins enables a set of transformations for CNF and feature models. 

## SMT Metamodel plugin of flamapy framework

The `smt_metamodel` plugin is a key component of the {% include flamapy.html %} framework, providing integration with SMT (Satisfiability Modulo Theories) solvers to enable advanced feature model analyses. This plugin leverages SMT solvers to perform detailed constraint-solving tasks, offering robust capabilities for handling complex feature models. More information in [this publication](https://doi.org/10.1016/j.cose.2023.103669).

{: .highlight }
> Official repository
>
> ```
> https://github.com/flamapy/smt_metamodel
> ```

## Dependency network metamodel plugin of flamapy framework
The dependency_network_metamodel plugin has been designed to manage and analyze dependency networks. This plugin provides the necessary tools to represent and manipulate dependencies among features, facilitating detailed dependency analysis. More information in [this publication](https://doi.org/10.1016/j.cose.2023.103669).

{: .highlight }
> Official repository
>
> ```
> https://github.com/flamapy/dependency_network_metamodel
> ```
