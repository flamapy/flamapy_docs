---
layout: default
title: Community plugins
parent: Plugins
grand_parent: Flamapy as framework
permalink: /framework/plugins/community_plugins
nav_order: 9
---

# Community plugins
{: .no_toc }

Newer, community-contributed backends that extend {% include flamapy.html %} with additional
knowledge-compilation and machine-learning capabilities.
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

## GNN metamodel plugin

The `gnn_metamodel` plugin (`flamapy-gnn`) represents feature models as **graphs** and applies
**Graph Neural Networks** (via [PyTorch Geometric](https://pyg.org)). A feature model is encoded
as an attributed graph — one node per feature with a structural feature vector, plus parent-child
and cross-tree-constraint edges — and GNN operations run over it.

The *learned* operations are self-supervised: their labels come from the SAT/BDD backends, so no
hand-labelling is needed. They are **inference-first** (load a checkpoint and predict, no solver),
falling back to on-the-fly training that needs the optional `learning` extra
(`pip install "flamapy-gnn[learning]"`). Large-scale training over a corpus of models (for
example, LLM-generated feature models) lives in the companion
[flamapy-gnn-experiments](https://github.com/jagalindo/flamapy-gnn-experiments) package, which
reuses the plugin's training code and produces checkpoints the plugin loads directly.

{: .highlight }
> Official repository
>
> ```
> https://github.com/flamapy/gnn_metamodel
> ```

### Operations

*Representation (pure GNN, no solver):* feature embeddings, feature clustering, link prediction
(constraint suggestion), configuration recommendation, whole-model embedding + retrieval, and a
structural graph summary.

*Learned (self-supervised; inference from a checkpoint or training with the `learning` extra):*
per-feature analysis prediction (core/dead), feature importance, prediction explanation,
redundant-constraint prediction, configuration validity prediction and completion, model-count
regression, backend/hardness prediction, and void-model classification.

### Installation

```
pip install flamapy-gnn              # core: no solver dependencies
pip install "flamapy-gnn[learning]"  # add SAT/BDD to train the learned operations
```
