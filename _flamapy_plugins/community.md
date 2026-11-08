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

* Configurations number (exact model counting)
* Satisfiable (non-void check)
* Core features
* Dead features

### Installation

```
pip install flamapy-sdd
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

### Requirements

d4 is a native binary with no PyPI package — install it from
<https://github.com/crillab/d4> and expose it as `d4` on `PATH` or via the `FLAMAPY_D4_PATH`
environment variable.

### Operations

* Configurations number (exact model counting)
* Satisfiable (non-void check)

### Installation

```
pip install flamapy-dnnf
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
