---
layout: default
title: flamapy as tool
has_children: true
permalink: /tool
nav_order: 3
---

# flamapy as tool
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## flamapy for feature models

{% include flamapy.html %} has been developed thinking on extensibility and on supporting various flavours of variability models such as OVM, Doppler models, Feature Models, and Debian Variability models, among others. However, feature modelling is the de facto standard when researching and depicting variability. Therefore, we offer a prepackaged version of {% include flamapy.html %} with all the plugins related to feature modelling, thus their operations, serializers, parsers, and the rest of the utilities for feature model reasoning. 

If you want to just use {% include flamapy.html %} for feature models simply installs as follows:

```bash
pip install flamapy
```
This will install the following plugins:

* [flamapy_fw](/flamapy_plugins/core/) which installs all the backend utilities to find operations and execute them.
* [flamapy_fm](/flamapy_plugins/fm/) which installs the plugin required to read and manipulate feature models
* [flamapy_sat](/flamapy_plugins/sat/) which enables SAT solving operations on feature models
* [flamapy_bdd](/flamapy_plugins/bdd/) which enables BDD solving oerations on feature models. 

## Interfaces

Also, to be easily used {% include flamapy.html %} offers different interfaces. 
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

### Command-line interface
Using a command-line interface significantly enhances the tool's efficiency and convenience, enabling quick and precise task execution with minimal overhead. You can find examples and more information [here](/tool/command_line_interface/).

### Easy-to-Use Python Interface
Using Python as a scripting language could be very convenient when developing scripts and integrating our analysis into other processes. However, learning how a framework as complex as {% include flamapy.html %} could be overwhelming. To help with that {% include flamapy.html %} offers a straightforward way to execute the most common operations in Python. You can find examples and more information [here](/tool/python_facade/).

### Using the underlying framework
Finally, even if you need to understand the framework, you can also rely on this meta-package or distribution if you just need to analyze feature models. You can find examples and more information [here](/tool/flamapy_framework/). 

## More ways to run flamapy
After those off-the-shelf options, there are other mechanisms to run or integrate {% include flamapy.html %} in different contexts.

{: .important }
> These ways of running {% include flamapy.html %}, require some more knowledge of those ecosystems.

<div class="button-container">
    <a href="analysis/rest/" class="highlight-button">REST Interface</a>
    <a href="analysis/wasm/" class="highlight-button">WASM Interface</a>
</div>

### REST Interface

{% include flamapy.html %} can be integrated into a REST/Swagger backend, allowing for remote operations and interactions. More detailes can be find [here](/analysis/rest/). 

### WASM Interface
{% include flamapy.html %} is WASM compatible, which means it can be run directly on the client side in a web environment. This enables powerful feature model analysis directly in the browser. More detailes can be find [here](/analysis/WASM/). 


