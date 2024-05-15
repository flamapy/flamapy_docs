---
layout: default
title: Getting started
nav_order: 2
---

# Getting started
{: .no_toc }


## Installation

To analyze feature models, you can use the `flamapy-fm-dist` distribution. It requires Python >= 3.9. It's recommended to use a virtual environment (venv) for installation to avoid conflicts with other packages. Here’s how you can set it up:

1. **Create a virtual environment:**

   ```bash
   python -m venv flamapy-env
   ```

2. **Activate the virtual environment (on Windows):**

    Yoy can activate the virtual environment on Windows systems:

    ```
    .\flamapy-env\Scripts\activate
    ```

    or macOs and Linux systems:

    ```
    source flamapy-env/bin/activate
    ```

3. **Install the distribution:**

```
pip install flamapy-fm-dist
```

## Basic operations

To test some basic operations, you need UVL models. Several are available at [UVLHub](https://www.uvlhub.io). If you prefer, you can download a test one:

```
wget -q "https://raw.githubusercontent.com/flamapy/flamapy-fm-dist/main/resources/models/valid_model.uvl" && wget -q "https://raw.githubusercontent.com/flamapy/flamapy-fm-dist/main/resources/configurations/valid_configuration.csvconf"
```

The distribution provides a CLI specific for feature models.

### Validate the model

To check if the model is valid, run:

```
flamapy-fm-cli --modelPath="./valid_model.uvl" valid
```

### Get all products

To generate all possible products from the model, use:

```
flamapy-fm-cli --modelPath="./valid_model.uvl" products
```

### Validate a configuration

To verify if a specific configuration is valid, run:


```
flamapy-fm-cli --modelPath="./valid_model.uvl" valid_configuration ./valid_configuration.csvconf
```


## Subseccion

Blablabla