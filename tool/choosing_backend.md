---
layout: default
title: Choosing the backend (query planner)
parent: Flamapy as tool
permalink: /tool/choosing_backend
nav_order: 6
---

# Choosing the backend (query planner)
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

Most analysis operations are implemented by more than one plugin: `satisfiable` by the SAT,
BDD, SDD, d-DNNF and Z3 plugins, `configurations_number` by BDD, SDD, d-DNNF, sharpSAT, SAT and
Z3, and so on.
Every operation has a historical default (`satisfiable`, `core_features`, `dead_features`,
`false_optional_features` and `satisfiable_configuration` run on SAT; `configurations_number`,
`configurations` and `sampling` on BDD), and you can always name a backend yourself. The
*query planner* is a third option: it picks the backend per call from what the installed plugins
declare about themselves.

**The planner is opt-in in 2.9.** Nothing changes unless you ask for `auto`. It becomes the
default in 3.0.

## The three ways to pick a backend

```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel

fm = FLAMAFeatureModel("valid_model.uvl")

fm.configurations_number()               # 1. the operation's default backend (bdd)
fm.configurations_number(backend="sat")  # 2. a fixed backend: "sat", "bdd", "z3",
                                         #    "sdd", "sharpsat" or "dnnf" when installed
fm.configurations_number(backend="auto") # 3. the planner decides
```

`auto` can also be set once for a model, or for the whole process:

```python
fm = FLAMAFeatureModel("valid_model.uvl", backend="auto")   # every call of this model
```

```bash
export FLAMAPY_BACKEND=auto      # every FLAMAFeatureModel and every CLI call
flamapy satisfiable valid_model.uvl --backend auto   # or per CLI call
```

A per-call `backend=` always wins over the model's setting, which wins over the environment
variable. Operations that only one plugin implements (for example `explain_void_model`, which
needs the diagnosis plugin) ignore the setting and run where they always did. `atomic_sets` and
`commonality`, which take `backend=` since 2.9, follow only a per-call `backend=` in 2.x, so a
default set for the model or the process does not change their 2.8 results.

## Seeing what was chosen

After any call, `fm.last_result` holds the provenance of the result. Under `auto`, its
`planner` field tells which backend was picked and why; with a fixed backend it says
`explicit`, and with the default it is `None`.

```python
fm = FLAMAFeatureModel("valid_model.uvl", backend="auto")

fm.satisfiable()
fm.last_result.backend   # 'pysat'
fm.last_result.planner   # 'auto: pysat: estimated 2 ms (transformation 1, operation 1),
                         #  historical default backend'

fm.configurations_number()
fm.last_result.planner   # 'auto: bdd: estimated 12 ms (transformation 11, operation 1),
                         #  historical default backend'

fm.configurations_number()   # the BDD is already built: nothing to pay for it
fm.last_result.planner   # 'auto: bdd: estimated 1 ms (transformation 0, operation 1),
                         #  bdd model already built, historical default backend'
```

The CLI prints the same information with `-v`, and `flamapy plan` shows the decision without
running the operation:

```
$ flamapy plan configurations_number valid_model.uvl
operation:            configurations_number
chosen backend:       bdd_metamodel (extension 'bdd')
transformation chain: fm -> bdd
estimated cost:       12 ms (heuristic)
rationale:            bdd: estimated 12 ms (transformation 11, operation 1), historical default backend
alternatives:         sdd_metamodel, pysat_metamodel, z3_metamodel
```

## How the decision is made

Each plugin ships a *manifest* describing what it can do (see
[the framework page on plugins](/framework/plugins)). For an operation on a given model the
planner:

1. **Keeps the plugins that implement the operation and can handle the model**: the plugin
   must be usable (the d-DNNF plugin declares itself unavailable without the `d4` binary),
   support the model's language level (a model with string constraints or aggregate functions
   only fits Z3; group cardinalities fit every solver), and accept the model's size (each
   plugin declares the number of features beyond which it does not finish: 1,000 for the BDD
   plugin, 2,000 for SDD and sharpSAT, 30 for anything that enumerates every configuration).
2. **Estimates the time of each candidate**: the cost of building the plugin's model from the
   feature model (free when this `FLAMAFeatureModel` already built it, or when it is in the
   artifact cache) plus the cost of the operation at the model's size. The estimates are
   milliseconds measured on a calibration corpus (synthetic models of 20 to 10,000 features at
   two constraint densities, plus JHipster and busybox); they are worst cases, so the actual
   run is usually faster, and they only need to be right relative to each other.
3. **Takes the cheapest**, with two rules in 2.9: plugins whose manifest names no calibration
   run (the d-DNNF plugin, third-party plugins without measured costs) are only chosen when no
   calibrated plugin qualifies, and the operation's historical default backend gets a bonus of
   150 ms, so that on small models `auto` reproduces the historical routing. 3.0 drops the
   bonus.

Approximate implementations (sharpSAT counting and sampling, and the structural `core_features`
and `atomic_sets` of the fm plugin, which ignore cross-tree constraints) are never chosen unless
you allow them. `allow_approximate` has no effect with any other backend than `auto`:

```python
fm.core_features(allow_approximate=True)                     # per call
FLAMAFeatureModel(path, backend="auto", allow_approximate=True)   # per model
# or FLAMAPY_ALLOW_APPROXIMATE=1 in the environment; allow_approximate=False on the model
# overrides the variable
```

`fm.last_result.exact` is `False` when an approximate implementation produced the result.

## What you get in practice

With the plugins of the `flamapy` distribution (SAT, BDD, Z3) and `auto`, on the calibration
models:

| Model | satisfiable, core/dead, false-optional, satisfiable_configuration | configurations_number, commonality | configurations | sampling |
|---|---|---|---|---|
| Boolean, up to 150 features | SAT | BDD | BDD | BDD up to about 150 features, then SAT |
| Boolean, 151 to 1,000 features | SAT | BDD | refused | SAT |
| Boolean, more than 1,000 features | SAT | refused | refused | SAT |
| Typed attributes, strings, aggregates | Z3 | counting: Z3 up to 30 features; commonality: refused | Z3 up to 30 features | refused |

`refused` means that no installed plugin declares that it finishes on a model of that size.
The SAT sampler returns valid configurations but enumerates them in a fixed order instead of
drawing them uniformly at random; pass `backend="bdd"` when you need a uniform sample.

Installing `flamapy-sdd` adds a counter that scales further than the BDD on sparse models: the
planner moves counting to SDD on many models from about 200 features on, and up to 2,000
features. `flamapy-sharpsat` adds approximate counting and sampling for the models nothing else
can handle, on `allow_approximate=True`.

When no installed plugin can run the operation, the planner refuses with the reason for every
candidate. In 2.9 the facade logs it and returns `None` (as it does for any operation error;
3.0 raises the `NoCompatibleBackendError`), and `flamapy plan` prints it:

```
$ flamapy plan configurations_number betty_5000.uvl
No compatible backend: No installed backend can run 'configurations_number' on this model
(Major: BOOLEAN, Minor: {}, 5000 features): bdd: model has 5000 features, declared limit is
1000; sdd: model has 5000 features, declared limit is 2000; pysat: model has 5000 features,
declared limit is 30; ...
```

A fixed backend is never refused: `fm.configurations_number(backend="bdd")` on that model
simply tries, as it always did.

## Measured limits per plugin (2.9)

The numbers behind the manifests, measured on 2026-11-06 with pure-Python `dd` (the BDD engine
2.9 ships), z3 4.14, PySDD and ApproxMC/UniGen. Times are the worst of the two constraint
densities at that size, in milliseconds; a dash means the size was not measured because a
smaller model already hit the cap.

| Plugin, operation | 100 f | 200 f | 500 f | 1,000 f | 2,000 f | 10,000 f | Limit |
|---|---|---|---|---|---|---|---|
| SAT, build model | 0.5 | 1 | 2 | 4 | 8 | 46 | none |
| SAT, satisfiable / core / dead | 0.1 | 0.3 | 0.8 | 2 | 4 | 68 | none |
| SAT, false_optional_features | 0.5 | 0.7 | 2 | 6 | 12 | 301 | none |
| SAT, pairwise (t-wise) sampling | 315 | 1,201 | 55,766 | 394,168 | timeout | — | none (only implementation) |
| BDD, build model | 23 | 204 | 384 or timeout | 1,693 or 32,336 | — | — | 1,000 features |
| BDD, any query once built | ≤ 3 | ≤ 42 | ≤ 72 | ≤ 303 | — | — | |
| SDD, build model | 5 | 10 | 7,515 | 55 or timeout | 266 (sparse only) | — | 2,000 features |
| SDD, configurations_number | 0.0 | 0.1 | 66 | 1 | 9 | — | |
| SDD, core / dead features | 1 | 5 | 40,555 / timeout | 82 | 22,837 | — | |
| sharpSAT, configurations_number | 104 | 1,641 | 50,146 or timeout | 1,487 | 7,943 | — | 2,000 features, approximate |
| Z3, build model | 6 | 9 | 24 | 32 | 64 | 253 | none |
| Z3, satisfiable / core / dead | 1 | 3 | 9 | 19 | 39 | 102 | none |
| Z3, false_optional_features | 3 | 8 | 29 | 102 | 423 | 10,984 | none |
| any, configurations / counting by enumeration (SAT, Z3) | | | | | | | 30 features |

Two values in a cell are the sparse and the dense model of that size: compiling a BDD or an SDD
depends on the constraints far more than on the number of features, which is why the limits
are conservative and the estimates are worst cases. The BDD limit matches the SoSyM benchmark
on real models with the same engine (29 of 41 models between 501 and 1,000 features compiled
within 300 s; 2 of 120 beyond).

## For plugin authors

A plugin takes part in the planning by declaring a `MANIFEST` in its package `__init__`:

```python
from flamapy.core.manifest import OperationCapability, PluginManifest
from flamapy.core.models.language_level import LanguageLevel, MajorLevel, MinorLevel

MANIFEST = PluginManifest(
    name='sdd',
    extension='sdd',                         # the model extension the operations run on
    supported_level=LanguageLevel(MajorLevel.BOOLEAN, {MinorLevel.GROUP_CARDINALITY}),
    max_features=2000,                       # plugin-wide ceiling (compilation)
    transformation_cost_curve=((50, 3), (100, 5), (200, 10), (500, 7500), (1000, 300000)),
    operations={                             # keyed by the facade operation name
        'satisfiable': OperationCapability(cost=1),
        'configurations_number': OperationCapability(cost_curve=((200, 1), (500, 66))),
        'core_features': OperationCapability(cost_curve=((100, 1), (200, 5), (500, 41000))),
    },
)
```

A cost curve is a tuple of `(features, milliseconds)` pairs: the cost applies up to that many
features, and beyond the last pair it grows in proportion to the size. An operation without an
entry gets the plugin's `default_cost` and `max_features`; a plugin without a manifest gets a
default one (Boolean level, exact, default costs) that the planner ranks last. `exact=False`
marks an approximate implementation (declare `exact = False` on the operation class too, so the
result envelope reports it), and `available=False` with `unavailable_reason` a plugin whose
native dependency is missing. Set `calibration` to the date or name of the run your costs come
from (`calibration='2026-11-06'` in the in-tree plugins): a manifest without it is ranked after
every calibrated one, so estimates that were never measured cannot win.
