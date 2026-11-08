---
layout: default
title: Migrating to 3.0
parent: Developing
nav_order: 5
---

# Migrating to flamapy 3.0

Flamapy 2.9 is the **bridge release** towards 3.0. It follows 2.6.0, the previous release (2.7 and
2.8 were development lines that were never published), keeps the calls of 2.6 working, and ships
the groundwork for the 3.0 major release behind non-breaking seams. This page collects the
results that 2.9 changes on purpose (bug fixes and one encoding default) and the changes 3.0 will
make, so you can prepare while still on 2.x. It is updated as 3.0 lands.

## Behaviour changes in 2.9

No call that worked in 2.6 stops working, but these results or outputs differ:

### Cross-tree constraints are encoded with `cnf_method='auto'`

The CNF builders (`FmToPysat`, `FmToDiagPysat`, `FmToSDD`, `FmToSharpSAT`, `FmToDDNNF`) default to
`cnf_method='auto'`: a constraint is expanded distributively unless the expansion would be larger
than its Tseytin encoding, which then gets auxiliary variables. Operation results are identical
and the auxiliaries never appear in them; the clauses only differ on models with constraints that
blow up (129 of the 1,538 benchmark models). What this changes for code that reads the raw CNF:

- The CNF can hold variables that are not features. Use `PySATModel.feature_variables()` and
  `top_variable()` (new variables must start above it) instead of `len(variables) + 1`, or pass
  `cnf_method='distributive'` to get the 2.6 clauses.
- `DimacsWriter` counts every variable in the `p cnf` header and names only the features;
  `DimacsReader` marks the unnamed variables of such a file as auxiliary.
- `PysatToFM` refuses a SAT model with auxiliary variables and says how to build one it can
  convert.
- `PySATModel` records the encoding in a new `cnf_method` attribute, `None` for models flamapy did
  not encode (e.g. read from DIMACS).

### Analysis results

- **Commonality** of a configuration with several features is the fraction of products that
  include all of them (the FLAME definition); 2.6 used the first feature only. A feature that is
  not in the model is now an error.
- **Diagnoses and conflicts** (HSDAG) follow the reference algorithm: 2.6 took different label
  sets with the same sum for the same node, so it missed some diagnoses, and it reported some
  non-minimal ones.
- **BDD build defaults** change the variable order (feature-tree pre-order, clause by clause, with
  reordering on CUDD). The set of configurations is the same, but the order of
  `BDDConfigurations`, seeded samples, the DDDMP/JSON/graph exports and `get_expression()` differ.
  `FmToBDD(fm, build="monolithic", var_order="model", reorder=False)` is the closest to 2.6. Invalid build options raise a `FlamaException` (still a
  `ValueError`). `PLModel.variables` is a list in feature-tree pre-order instead of a set.
- **Metrics** from a backend model report the metrics of every metamodel the model can reach, and
  skip (recording the reason in `Metrics.get_skipped()`) a metamodel whose plugin is unavailable
  or whose `max_features` the model exceeds, instead of raising.
- **AFM writer**: XOR is written as `NOT (A IFF B)`, `read_relation` is an instance method and
  `read_attribute` returns `None` for attributes AFM cannot hold.

### Facade

- `atomic_sets` and `commonality` accept `backend=`; in 2.x only a per-call `backend=` changes
  them, not the model's default backend or `FLAMAPY_BACKEND`, so code that sets a default keeps
  its 2.6 results.

### REST API

A failing operation still answers `404`, as in 2.6, now with its reason instead of "Not valid
result"; an unexpected error inside a plugin answers `500`. Responses carry the provenance of the result in
`X-Flamapy-*` headers.

## Announced breaking changes (3.0)

### Facade and CLI return typed result envelopes

Today every `FLAMAFeatureModel` method returns a bare value (`True`, a list, an int). In 3.0
they return an `OperationResult` envelope carrying the value plus its provenance: which
plugin and backend produced it, whether it is exact or approximate, the model's canonical
hash, and the wall time.

Migration is mechanical: append `.value` (or call `.unwrap()`).

```python
# 2.x
result = fm.satisfiable()
# 3.0
result = fm.satisfiable().value
```

You can already see the envelope in 2.9: after any operation it is available as
`fm.last_result`, and the CLI prints it with `flamapy -v <operation> <model>` (well,
`flamapy <operation> <model> -v`).

### Default backends apply to every selectable operation

The model's default backend and `FLAMAPY_BACKEND` will also apply to `atomic_sets` and
`commonality`, which follow only a per-call `backend=` in 2.x.

### The REST API answers 422 when an operation cannot run

2.x answers `404` with the reason; 3.0 uses `422`, in line with the raising facade.

### Operation errors raise instead of returning None

In 2.x, a failing operation logs the error and returns `None`. From 3.0 the underlying
`FlamaException` is raised. 2.9 emits a `DeprecationWarning` whenever the None-swallowing
path triggers. Opt into the 3.0 contract today with `FLAMAFeatureModel(path, raise_errors=True)`, or
process-wide with `FLAMAPY_RAISE_ERRORS=1` (which also covers the producers such as
`generate_random_feature_model`); `raise_errors=False` on a model overrides the variable.

```python
# 2.x
if fm.commonality(config) is None:
    ...  # something went wrong
# 3.0
from flamapy.core.exceptions import FlamaException
try:
    fm.commonality(config)
except FlamaException as error:
    ...
```

## Deprecations in 2.9

### Namespace-scan plugin discovery

Plugins should declare a `flamapy.plugins` entry point in their packaging metadata:

```toml
[project.entry-points."flamapy.plugins"]
myplugin = "flamapy.metamodels.myplugin_metamodel"
```

Plugins found only through the legacy `flamapy.metamodels` namespace scan still work in 2.9
(with a `DeprecationWarning`); the scan is removed in 3.0.

## New, non-breaking machinery you can adopt today

- **Capability manifests** — plugins declare a `MANIFEST` (`PluginManifest`) in their
  package `__init__`: the language level they support (major level and minor levels such as
  group cardinalities or string constraints), whether the plugin is available at all (e.g.
  the d-DNNF plugin needs the `d4` binary), a plugin-wide `max_features` ceiling, the
  estimated cost of building its model (`transformation_cost`, constant or per size bin),
  and per operation the exactness, scale ceiling and cost (`cost` or a `cost_curve` of
  estimated milliseconds per size bin, measured on the calibration models, named in
  `calibration`). Plugins without one get a default that the planner ranks last.
- **Query planner** — `backend='auto'` (per model, per call, or `FLAMAPY_BACKEND=auto`)
  picks the backend per operation from the manifests: candidates are filtered by
  availability, language level, scale and exactness, then ranked by the estimated cost of
  building the backend model (free for the models the facade already built or has cached
  as artifacts) plus the operation's cost at the model's size. Approximate implementations
  (sharpSAT counting and sampling, the structural `core_features` of the fm plugin) are only
  candidates with `allow_approximate=True` (per call, per model, or
  `FLAMAPY_ALLOW_APPROXIMATE=1`; an explicit `allow_approximate=False` on the model overrides
  the variable). The SAT sampler is one of them: its configurations are valid but not drawn
  uniformly, and its results report `exact=False`. Plugins whose manifest names no calibration
  run are ranked after the calibrated ones, and the BDD plugin lists configurations only up to
  50 features, measured on the benchmark corpus. In 2.9 the operation's historical default backend still
  gets a bonus so that `auto` reproduces today's routing on plain Boolean models; 3.0 drops
  the bonus and routes purely on the estimates. `last_result.planner` records the choice and
  its rationale.
- **`OperationResult` / `run_and_wrap`** — `flamapy.core.execution.run_and_wrap` executes
  any operation and returns the envelope; useful for benchmarking and services.
- **Optional solver extras** — `pip install "flamapy[sharpsat]"`, `[dnnf]`, `[sdd]`, or
  `[all-solvers]` add the optional backends; select them per call with
  `backend='sharpsat'` (etc.) or per model with `FLAMAFeatureModel(path, backend=...)`.
