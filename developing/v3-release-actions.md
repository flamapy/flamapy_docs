---
layout: default
title: Release-day actions (2.9 / 3.0)
parent: Developing
nav_order: 6
---

# Release-day actions

Push-side and admin actions that are performed manually at release time (never by the
in-repo development work). Maintainers: check items off as they are done.

## 2.9.0 (bridge release)

2.9.0 is the first release after 2.6.0: the 2.7 and 2.8 development lines were never published,
so the release notes compare with 2.6.0. Every repository's develop branch carries
`2.9.0.devN` with `~=2.9.0.devN` pins.

- [ ] **Security (do first, independent of the release):** revoke the Google
      service-account key committed in `flamapy-stats` (`plasma-hope-*.json`) and purge it
      from the repository history.
- [ ] Optional dev release: `flamapy-dev version release 2.9.0.devN` tags develop in every
      repo; each release workflow waits for its flamapy dependencies on PyPI before
      publishing, so the tags go out back to back.
- [ ] Stable release: `flamapy-dev version stabilize` drops the `.devN` suffix (versions and
      pins → `2.9.0` / `~=2.9.0`), merges develop into each stable branch (`master` in fw,
      fm, sat and bdd; `main` in the others) and tags `v2.9.0` there, in dependency order
      (fw → fm → sat → bdd → z3 → sdd → dnnf → sharpsat → flamapy → rest).
- [ ] Decide whether the IDE wheels bundle includes the optional solver extras
      (sharpsat/dnnf/sdd) — see the note in `flamapy/.github/workflows/build_wheels.sh`.
      Default: not included.
- [ ] Regenerate the docs operation catalog (`bin/generate_operation_docs.py`) and fill
      the TODO prose in the stub pages (explain_dead_feature, explain_void_model,
      covering_array, coverage, sample_reduction, ...).
- [ ] Release notes, against 2.6.0: query planner (`backend='auto'`) and capability
      manifests, entry-point discovery (namespace scan deprecated), `last_result`
      provenance + CLI `-v`, optional solver extras, explanation and SPL testing operations,
      the REST API generated from the facade, and the "Behaviour changes in 2.9" section of
      the [3.0 migration page](/developing/migrating_to_v3).

## 3.0.0

- [ ] Archive on GitHub: `uvlparser`, `afmparser`, `flamapy-fm-dist`,
      `flamapy-configurator-mcp`, `vscode_extension`.
- [ ] Push pointer READMEs to superseded repos: `flamapy-configurator-mcp`
      (→ flamapy-mcp), `vscode_extension` (→ flamapy-ide `apps/vscode`).
- [ ] After B.2 configurator parity: pointer README + archive `flamapy.conf`.
- [ ] After D.2 BDD unification: pointer README + archive `bdd_metamodel_colosal`.
- [ ] Delete the stale `flamapy.github.io` branch `adding_try_it_out_wasm` (already
      merged to master).
- [ ] Swap the try-it and IDE wheels to v3 (`update-flamapy-wheels` workflow).
- [ ] Publish the benchmark results (B.5 harness run) with the release notes.
- [ ] Link the ecosystem inventory page from the org profile README (`.github` repo).
- [ ] PyPI releases in dependency order.
