---
layout: default
title: Lab plugins
parent: Plugins
grand_parent: Flamapy as framework
permalink: /framework/plugins/lab_plugins
nav_order: 5
---

# Lab plugins
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## BDD for colosal feature models

The BDD model plugin provides the metaclases required to work with 
colosal feature models and transform them to BDD.

However, this implementation relies on the optimizations performed in the paper by Ruben Heradio, David Fernández-Amorós, José A. Galindo, David Benavides, and Don S. Batory: "Uniform and scalable sampling of highly configurable systems" (*Empirical Software Engineering*, 27(2): 44, 2022), which enables better scalability of the analysis.

{: .highlight }
> Official repository
>
> ```
> https://www.github.com/flamapy/bdd_metamodel
> ```

### Operations
Currently, this plugin enables the following operations. 

* Sampling
* Feature Inclusion Probability
* Product distribution

### Transformations supported
Currently this plugins enables a set of transformations for CNF and feature models. 

## SMT Metamodel plugin of flamapy framework

The `smt_metamodel` plugin is a key component of the {% include flamapy.html %} framework, providing integration with SMT (Satisfiability Modulo Theories) solvers to enable advanced feature model analyses. This plugin leverages SMT solvers to perform detailed constraint-solving tasks, offering robust capabilities for handling complex feature models. More information in [this publication](https://doi.org/10.1016/j.cose.2023.103669).

{: .highlight }
> Official repository
>
> ```
> https://github.com/flamapy/smt_metamodel
> ```

## Dependency network metamodel plugin of flamapy framework
The dependency_network_metamodel plugin has been designed to manage and analyze dependency networks. This plugin provides the necessary tools to represent and manipulate dependencies among features, facilitating detailed dependency analysis. More information in [this publication](https://doi.org/10.1016/j.cose.2023.103669).

{: .highlight }
> Official repository
>
> ```
> https://github.com/flamapy/dependency_network_metamodel
> ```
