---
layout: default
title: SharpSAT plugin
parent: Plugins
grand_parent: Flamapy as framework
permalink: /framework/plugins/sharpsat_plugin
nav_order: 8
---

# SharpSAT plugin
{: .no_toc }

The SharpSAT model plugin provides **scalable approximate model counting** and
**almost-uniform sampling** of feature-model configurations.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

{: .highlight }
> Official repository
>
> ```
> https://www.github.com/flamapy/sharpsat_metamodel
> ```

## SharpSAT metamodel plugin of flamapy framework

The `sharpsat_metamodel` plugin adds scalable analyses over the CNF of a feature model. It
complements the existing backends: the SAT and Z3 backends count configurations by full
enumeration (which does not scale), and the BDD backend counts exactly but its diagram can
blow up on large models. `sharpsat_metamodel` instead uses **hashing-based tools from the
CryptoMiniSat family** that scale to far larger models:

- [ApproxMC](https://github.com/meelgroup/approxmc) for an *(epsilon, delta)* **approximate**
  count of the number of valid configurations.
- [UniGen](https://github.com/meelgroup/unigen) for **almost-uniform** sampling of valid
  configurations.

### Features of the SharpSAT Metamodel Plugin

1. **Approximate model counting**
   - Uses ApproxMC (`pyapproxmc`) to estimate the number of valid configurations with
     probabilistic guarantees, scaling beyond exact enumeration or BDD compilation.

2. **Almost-uniform sampling**
   - Uses UniGen (`pyunigen`) to draw configurations almost uniformly at random, honouring a
     partial configuration and with/without replacement.

3. **Reuses the SAT CNF**
   - The CNF (including the optional Tseytin encoding) is produced by reusing the SAT
     metamodel's `FmToPysat` transformation, so counting and sampling are always projected
     onto the feature variables — auxiliary variables never distort the results.

### Installation instructions

To install the `sharpsat_metamodel` plugin, follow these steps:

1. **Install Python**: Ensure that Python 3.11 or later is installed on your system.

2. **Install the SharpSAT Metamodel Plugin**:
   - Using pip, the Python package manager, you can install the `flamapy-sharpsat` plugin
     directly from PyPI:
     ```bash
     pip install flamapy-sharpsat
     ```
     This also pulls in `pyapproxmc` and `pyunigen`.

### Links

- **PyPI**: [flamapy-sharpsat on PyPI](https://pypi.org/project/flamapy-sharpsat/)
- **GitHub Repository**: [sharpsat_metamodel on GitHub](https://github.com/flamapy/sharpsat_metamodel)

## Usage

```python
from flamapy.metamodels.fm_metamodel.transformations import UVLReader
from flamapy.metamodels.sharpsat_metamodel.transformations import FmToSharpSAT
from flamapy.metamodels.sharpsat_metamodel.operations import (
    SharpSATConfigurationsNumber,
    SharpSATSampling,
)

fm = UVLReader('model.uvl').transform()
model = FmToSharpSAT(fm).transform()

count = SharpSATConfigurationsNumber().execute(model).get_result()

sampler = SharpSATSampling()
sampler.set_sample_size(10)
sample = sampler.execute(model).get_sample()
```

## Operations

Currently, this plugin enables the following operations:

<ul>
  {% assign sharpsat_operations = site.operations | where: "flamapy_sharpsat", true %}
  {% for operation in sharpsat_operations %}
    <li><a href="{{ operation.url }}">{{ operation.title }}</a></li>
  {% endfor %}
</ul>

## Transformations supported

The plugin provides a single Model-to-Model transformation, `FmToSharpSAT`, which builds the
CNF of a feature model (reusing the SAT metamodel encoding). Counting and sampling then run
directly on that CNF.
