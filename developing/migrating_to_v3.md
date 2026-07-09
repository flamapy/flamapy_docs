---
layout: default
title: Migrating to 3.0
parent: Developing
nav_order: 5
---

# Migrating to flamapy 3.0

Flamapy 2.7 is a **bridge release**: it is fully backward compatible with 2.6, and it ships
the groundwork for the 3.0 major release behind non-breaking seams. This page collects the
changes 3.0 will make, so you can prepare while still on 2.7. It is updated as 3.0 lands.

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

You can already see the envelope in 2.7: after any operation it is available as
`fm.last_result`, and the CLI prints it with `flamapy -v <operation> <model>` (well,
`flamapy <operation> <model> -v`).

### Operation errors raise instead of returning None

In 2.x, a failing operation logs the error and returns `None`. From 3.0 the underlying
`FlamaException` is raised. 2.7 emits a `DeprecationWarning` whenever the None-swallowing
path triggers.

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

## Deprecations already active in 2.7

### Namespace-scan plugin discovery

Plugins should declare a `flamapy.plugins` entry point in their packaging metadata:

```toml
[project.entry-points."flamapy.plugins"]
myplugin = "flamapy.metamodels.myplugin_metamodel"
```

Plugins found only through the legacy `flamapy.metamodels` namespace scan still work in 2.7
(with a `DeprecationWarning`); the scan is removed in 3.0.

## New, non-breaking machinery you can adopt today

- **Capability manifests** — plugins can declare a `MANIFEST` (`PluginManifest`) in their
  package `__init__` describing supported language level, exactness and scale per
  operation. Plugins without one get a conservative default. The 3.0 query planner routes
  on these.
- **`OperationResult` / `run_and_wrap`** — `flamapy.core.execution.run_and_wrap` executes
  any operation and returns the envelope; useful for benchmarking and services.
- **Optional solver extras** — `pip install "flamapy[sharpsat]"`, `[dnnf]`, `[sdd]`, or
  `[all-solvers]` add the optional backends; select them per call with
  `backend='sharpsat'` (etc.) or per model with `FLAMAFeatureModel(path, backend=...)`.
