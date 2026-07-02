---
layout: default
title: Extending with your plugins
parent: Developing
nav_order: 2
---

# Extending with your plugins
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

{: .important }
> In order to use the CLI, you need to install the flamapy basic package

{: .important }
> It's recommended to use a **virtual environment** (venv) for installation to avoid conflicts with other packages. Here’s how you can set it up:
> ```
> python -m venv flamapyenv && source flamapyenv/bin/activate
> ```   

Install the distribution:

```
pip install flamapy
```
## Create your own plugin

{: .highlight }
Let's take as an example that we want to develop a plugin for OVM (Orthogonal Variability Model)

We go to the `core` repository of {% include flamapy.html %} and create a directory for the metamodel:

```
cd core && mkdir ./ovm_metamodel
```

We use the `flamapy` CLI to generate the new plugin:

```
flamapy generate_plugin ./ovm_metamodel ovm ovm
```

The three arguments are the destination directory, the plugin **name** and the file
**extension** it will register with the ecosystem. This populates a skeleton package under
`flamapy/metamodels/ovm/`:

```
ovm_metamodel/
└── flamapy/metamodels/ovm/
    ├── models/models.py             # your variability model
    ├── transformations/
    │   ├── text2model.py            # parse a file into your model
    │   ├── model2text.py            # serialize your model
    │   └── model2model.py           # convert from/to another metamodel
    └── operations/
        ├── valid.py                 # an example analysis operation
        └── products.py
```

{: .highlight }
> {% include flamapy.html %} uses **namespace packages** and **auto-discovery**: any class
> under `flamapy.metamodels.*` that subclasses a core `VariabilityModel`, `Transformation`
> or `Operation` is found automatically once the package is installed — there is no registry
> file to edit.

### 1. Implement the model

Your model subclasses `VariabilityModel` and declares the extension used to identify it:

```python
from flamapy.core.models import VariabilityModel

class OVMModel(VariabilityModel):

    @staticmethod
    def get_extension() -> str:
        return 'ovm'

    def __init__(self) -> None:
        self.elements = {}
```

### 2. Implement a transformation

A parser (`TextToModel`) reads a file into your model. The `get_source_extension` must match
the extension you registered:

```python
from flamapy.core.transformations import TextToModel
from flamapy.metamodels.ovm.models.models import OVMModel

class TextToOVM(TextToModel):

    @staticmethod
    def get_source_extension() -> str:
        return 'ovm'

    def __init__(self, path: str) -> None:
        self.path = path
        self.model = OVMModel()

    def transform(self) -> OVMModel:
        # TODO: parse self.path and populate self.model
        return self.model
```

To interoperate with the existing solvers, add a `ModelToModel` transformation (e.g.
`OVMToFM`) whose `get_source_extension`/`get_destination_extension` are `'ovm'` and `'fm'`;
the framework can then chain your model into the SAT/BDD/Z3 backends automatically.

### 3. Implement an operation

Operations subclass a core operation interface so they are discovered and can be called by
name:

```python
from flamapy.core.operations import Satisfiable
from flamapy.metamodels.ovm.models.models import OVMModel

class OVMValid(Satisfiable):

    def __init__(self) -> None:
        self.result = False

    def execute(self, model: OVMModel) -> 'OVMValid':
        # TODO: your analysis
        return self

    def is_satisfiable(self) -> bool:
        return self.result

    def get_result(self) -> bool:
        return self.result
```

### 4. Install and use it

Install your plugin in editable mode and it is picked up automatically:

```
pip install -e ./ovm_metamodel
```

Then drive it through the discovery API, which finds your model, transformation and
operation automatically:

```python
from flamapy.core.discover import DiscoverMetamodels

dm = DiscoverMetamodels()
model = dm.use_transformation_t2m('example.ovm', 'ovm')   # parse with TextToOVM
result = dm.use_operation(model, 'OVMValid').get_result()  # run your operation by name
```

See [Testing your plugins]({{ site.baseurl }}/developing/testing_plugins) for how to add a
test suite, and the existing `pysat_metamodel`, `bdd_metamodel` and `z3_metamodel` repositories
as complete references.