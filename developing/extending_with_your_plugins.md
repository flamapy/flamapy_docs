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
flamapy generate_plugin./ovm_metamodel ovm ovm
```

This will populate the skeleton to create your plugin. 