---
layout: default
title: Release-day actions (2.7 / 3.0)
parent: Developing
nav_order: 6
---

# Release-day actions

Push-side and admin actions that are performed manually at release time (never by the
in-repo development work). Maintainers: check items off as they are done.

## 2.7.0 (bridge release)

- [ ] **Security (do first, independent of the release):** revoke the Google
      service-account key committed in `flamapy-stats` (`plasma-hope-*.json`) and purge it
      from the repository history.
- [ ] Merge the `version2.7` branches (fw, fm, sat, bdd, z3, sharpsat, dnnf, sdd,
      flamapy, docs) and tag.
- [ ] Finalize versions `2.7.0.dev0` → `2.7.0` (and `~=2.7.0.dev0` pins → `~=2.7.0`)
      across the nine packages.
- [ ] Publish to PyPI in dependency order (fw → fm → sat/bdd/z3/sharpsat/dnnf/sdd →
      flamapy), e.g. via `flamapy-dev`.
- [ ] Decide whether the IDE wheels bundle includes the optional solver extras
      (sharpsat/dnnf/sdd) — see the note in `flamapy/.github/workflows/build_wheels.sh`.
      Default: not included.
- [ ] Regenerate the docs operation catalog (`bin/generate_operation_docs.py`) and fill
      the TODO prose in the stub pages (explain_dead_feature, explain_void_model,
      covering_array, coverage, sample_reduction, ...).
- [ ] Release notes: entry-point discovery (namespace scan deprecated), capability
      manifests, `last_result` provenance + CLI `-v`, optional solver extras, explanation
      operations, SPL testing operations, 3.0 migration page.

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
