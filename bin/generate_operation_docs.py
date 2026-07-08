#!/usr/bin/env python3
"""Regenerate the per-operation reference blocks in ``_operations/*.md`` from the
installed flamapy OperationDescriptors and plugin manifests.

Run from the flamapy_docs repo root, with a virtualenv that has the flamapy packages
installed (e.g. ``../env/bin/python bin/generate_operation_docs.py``). For each facade
operation it rewrites only the region between the BEGIN/END GENERATED markers of
``_operations/<name>.md`` — hand-written prose outside the markers is preserved. Pages
missing the markers get them appended; descriptors with no page at all get a stub page
with a TODO prose section, so new operations cannot silently ship undocumented.

The script is idempotent: running it twice produces a no-op diff.
"""
import inspect
import sys
from pathlib import Path

from flamapy.core.discover import DiscoverMetamodels
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel

BEGIN = '<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->'
END = '<!-- END GENERATED -->'

# Docs front-matter flags per implementing plugin (module name -> flag).
PLUGIN_FLAGS = {
    'pysat_metamodel': 'flamapy_sat',
    'bdd_metamodel': 'flamapy_bdd',
    'fm_metamodel': 'flamapy_fm',
    'z3_metamodel': 'flamapy_z3',
    'pysat_diagnosis_metamodel': 'flamapy_diagnosis',
}


def implementing_plugins(discover, descriptor):
    """The plugins that ship an operation class carrying this descriptor."""
    plugins = []
    for plugin in discover.plugins:
        for operation in plugin.operations:
            if getattr(operation, 'facade', None) is not None \
                    and operation.facade.name == descriptor.name:
                plugins.append(plugin)
                break
    return plugins


def render_block(name, descriptor, plugins):
    signature = inspect.signature(getattr(FLAMAFeatureModel, name))
    lines = [BEGIN, '']
    lines.append(f'**Facade signature**: `{name}{signature}`')
    lines.append('')
    if descriptor.inputs:
        lines.append('**Inputs**:')
        lines.append('')
        lines.append('| name | type | required | default |')
        lines.append('|------|------|----------|---------|')
        for spec in descriptor.inputs:
            type_name = getattr(spec.type, '__name__', str(spec.type))
            default = '—' if spec.required else repr(spec.default)
            lines.append(
                f'| `{spec.name}` | {type_name} | '
                f'{"yes" if spec.required else "no"} | {default} |')
        lines.append('')
    backend = descriptor.default_backend or 'none (runs on the feature model)'
    lines.append(f'**Default backend**: {backend}'
                 + (' (selectable via `backend=`)' if descriptor.selectable_backend else ''))
    lines.append('')
    if plugins:
        lines.append('**Implemented by**:')
        lines.append('')
        lines.append('| plugin | exact | scale limit |')
        lines.append('|--------|-------|-------------|')
        for plugin in plugins:
            capability = plugin.manifest.capability(descriptor.name)
            limit = capability.max_features or '—'
            lines.append(
                f'| {plugin.name} | {"yes" if capability.exact else "approximate"} '
                f'| {limit} |')
        lines.append('')
    lines.append(END)
    return '\n'.join(lines)


def _first_sentence(doc):
    collapsed = ' '.join((doc or '').split())
    if not collapsed:
        return 'TODO'
    end = collapsed.find('. ')
    return collapsed[:end + 1] if end != -1 else collapsed


def stub_page(name, descriptor, plugins, block):
    flags = {flag: 'false' for flag in PLUGIN_FLAGS.values()}
    for plugin in plugins:
        flag = PLUGIN_FLAGS.get(plugin.module.__name__.split('.')[-1])
        if flag:
            flags[flag] = 'true'
    flag_lines = '\n'.join(f'{flag}: {value}' for flag, value in flags.items())
    title = name.replace('_', ' ').capitalize()
    return f"""---
title: {title}
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/{name}

{flag_lines}
cmd: true
facade: true
python: true
rest: true
---

# {title}
**Description**:
{_first_sentence(descriptor.doc)}

TODO: application and example prose.

---

{block}
"""


def main():
    operations_dir = Path(__file__).resolve().parent.parent / '_operations'
    discover = DiscoverMetamodels.instance()
    written, stubs = 0, 0
    for name, descriptor in sorted(discover.available_operations().items()):
        plugins = implementing_plugins(discover, descriptor)
        block = render_block(name, descriptor, plugins)
        page = operations_dir / f'{name}.md'
        if not page.exists():
            page.write_text(stub_page(name, descriptor, plugins, block), encoding='utf-8')
            stubs += 1
            continue
        text = page.read_text(encoding='utf-8')
        if BEGIN in text and END in text:
            head, rest = text.split(BEGIN, 1)
            _, tail = rest.split(END, 1)
            new_text = head + block + tail
        else:
            new_text = text.rstrip('\n') + '\n\n---\n\n' + block + '\n'
        if new_text != text:
            page.write_text(new_text, encoding='utf-8')
            written += 1
    print(f'updated {written} pages, created {stubs} stubs')
    return 0


if __name__ == '__main__':
    sys.exit(main())
