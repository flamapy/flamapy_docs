---
layout: default
title: Testing plugins
parent: Developing
nav_order: 3
---

# Testing plugins
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

{: .important }
> We must go to the folder of the plugin in question in order to carry out the following commands. We also encourage to use [act](https://github.com/nektos/act) and use the main action in local, which will execute the three above-mentioned tools. 

### Run tests
To run all the tests of a plugin:

```
pip install pytest
make test
```

### Run test with coverage

```
pip install pytest coverage
make cov
```

### Review code quality and styles error

```
pip install prospector
make lint
```

### Review hint typing

```
pip install mypy
make mypy
```
