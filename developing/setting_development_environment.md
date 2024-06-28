---
layout: default
title: Setting development environment
parent: Developing
nav_order: 1
---

# Setting development environment
{: .no_toc }

{% include flamapy.html %} requires a specific configuration of libraries, environment variables and various artifacts to run in developer mode.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Setting workspace

To make it easier, we recommend creating the `flamapy` folder in your home directory:

```bash
mkdir ~/flamapy
cd ~/flamapy 
```

## Clone the core 

```
git clone https://github.com/flamapy/flamapy_fw.git
```

## Clone plugins

By itself, the {% include flamapy.html %} core does not provide parsing functionality. We can clone existing plugins to have artefacts to work with and not start from scratch:

```bash
git clone https://github.com/flamapy/fm_metamodel.git
git clone https://github.com/flamapy/pysat_metamodel.git
git clone https://github.com/flamapy/bdd_metamodel.git
```

## Setting up

### Setting plugin paths
First, we must set the `PLUGIN_PATHS` environment variable so that the core of {% include flamapy.html %} knows where the plugins are located. Assuming both the `flamapy_fw` repo and the plugins are in the `flamapy` directory, run:

```bash
export PLUGIN_PATHS=~/flamapy/fm_metamodel/:~/flamapy/pysat_metamodel/:~/flamapy/bdd_metamodel/
```

### Setting developer mode 

Once the variable is defined, we can start the development environment:

```bash
cd flamapy_fw
make dev
```

This command:

- **Creates and activates** a Python virtual environment
- **Installs** development dependencies
- **Installs** the core `flamapy_fw`
- **Installs** plugins
- **Configures** the specified plugins
