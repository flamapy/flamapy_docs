---
layout: default
title: flamapy as a tool
has_children: true
permalink: /analysis
nav_order: 3
---

# flamapy for feature models
flamapy has been developed thinking on extensivility and on supporting various flavors of variability models such as OVM, Doppler models, Feature Models, Debian Variability models among other. However, feature modelling is the defacto standard when researching and depicting variability. Therefore, we offer a prepackaged version of flamapy with all the plugins related to feature modelling, thus their operations, serializers, parsers, and the rest of utilities for feature model reasoning. 

If you want to just use flamapy for feature models simply installs as follows:

```bash
pip install flamapy
```
This will install the following plugins:

* [flamapy_fw](/flamapy_plugins/core/) which installs all the backend utilities to find operations and execute them.
* [flamapy_fm](/flamapy_plugins/fm/) which installs the plugin required to read and manipulate feature models
* [flamapy_sat](/flamapy_plugins/sat/) which enables SAT solving operations on feature models
* [flamapy_bdd](/flamapy_plugins/bdd/) which enables BDD solving oerations on feature models. 

Also, to be easily used flamapy offers different interfaces. 
   <style>
        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 20px 0;
        }
        .highlight-button {
            background-color: #1a73e8;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 1.2em;
            text-align: center;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        .highlight-button:hover {
            background-color: #155a9c;
        }
    </style>

<div class="button-container">
    <a href="/analysis/cmd/" class="highlight-button">Command Line Interface</a>
    <a href="/analysis/python_facade/" class="highlight-button">Easy-to-Use Python Interface</a>
    <a href="/analysis/python/" class="highlight-button">Using the underlying framework</a>
</div>

* A command line interface: Using a command line interface significantly enhances the efficiency and convenience of the tool, enabling quick and precise execution of tasks with minimal overhead. You can fins examples and more information [here](/analysis/cmd/).

* A easy-to-use interface: Using Python as scripting language could be very convinient when developing scripts and integrating our analysis in other proceses. However, learning how a framework as complex as flamapy could be a bit overwhelming. To help with that flamapy offers a very easy way to execute the most common operations in python. You can fins examples and more information [here](/analysis/python_facade/).

* Finally, even it requires to understand the framework, you can also rely on this meta-package or distribution if just needing to analyze feature models. You can fins examples and more information [here](/analysis/python/). 

## More ways to run flamapy
After those off-the-shelf options, there are other mechanisms to run or integrate flamapy in different contexts.

{: .important }
> These ways of running flamapy, require some more knowledge of those ecosystems:

<div class="button-container">
    <a href="analysis/rest/" class="highlight-button">REST Interface</a>
    <a href="analysis/wasm/" class="highlight-button">WASM Interface</a>
</div>

* Within a REST/Swagger Backend: Flamapy can be integrated into a REST/Swagger backend, allowing for remote operations and interactions. More detailes can be find [here](/analysis/rest/). 

* WASM Compatibility: Flamapy is WASM compatible, which means it can be run directly on the client side in a web environment. This enables powerful feature model analysis directly in the browser. More detailes can be find [here](/analysis/WASM/). 


