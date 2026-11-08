---
layout: default
title: Ecosystem inventory
parent: Flamapy as framework
permalink: /framework/ecosystem
nav_order: 5
---

# Ecosystem inventory

Every repository in the [flamapy GitHub organization](https://github.com/flamapy), its
role, its PyPI package (if any), and where its functionality lives today. Statuses follow
the v2.9/v3 planning decisions; superseded repos point at their replacement.

## Core framework and coordinated plugins

Released together, in lock-step versions.

| Repository | PyPI package | Role | Status |
|---|---|---|---|
| `core` (flamapy_fw) | `flamapy-fw` | Framework: base classes, discovery, manifests | stable |
| `fm_metamodel` | `flamapy-fm` | Feature-model metamodel + readers/writers | stable |
| `pysat_metamodel` | `flamapy-sat` | SAT analysis + diagnosis metamodel | stable |
| `bdd_metamodel` | `flamapy-bdd` | BDD analysis | stable |
| `z3_metamodel` | `flamapy-z3` | SMT analysis of typed attributes | stable |
| `flamapy-feature-model` (flamapy) | `flamapy` | Meta-distribution: CLI + Python facade | stable |
| `sharpsat_metamodel` | `flamapy-sharpsat` | Approximate counting/sampling | optional extra `flamapy[sharpsat]` (since 2.9) |
| `dnnf_metamodel` | `flamapy-dnnf` | d-DNNF compilation (d4) | optional extra `flamapy[dnnf]` (since 2.9) |
| `sdd_metamodel` | `flamapy-sdd` | SDD compilation | optional extra `flamapy[sdd]` (since 2.9) |

## Applications and tooling

| Repository | Role | Status |
|---|---|---|
| `flamapy-ide` | Browser IDE (Pyodide/WASM) | active |
| `flamapy_rest` | REST API (rest.flamapy.org) | active; v2 (async jobs) planned for 3.1 |
| `featuredraw` | Visual feature-model editor | active; IDE round-trip planned for 3.1 |
| `flamapy_dev` | Multi-repo development CLI | active |
| `flamapy_docs` | This documentation site | active |
| `flamapy.github.io` | Landing page + WASM try-it | active |
| `FlamaExperimentExecutor` | Benchmark/experiment harness | active; being promoted to the public benchmark harness |

## Archived / superseded

| Repository | Superseded by |
|---|---|
| `uvlparser` | UVL parsing inside `fm_metamodel` |
| `afmparser` | AFM reading inside `fm_metamodel` |
| `flamapy-fm-dist` | the `flamapy` meta-distribution |
| `benchmarking` | corpus source for FlamaExperimentExecutor |
| `docs`, `old_site` | this documentation site |
