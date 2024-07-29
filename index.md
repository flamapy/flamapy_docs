---
layout: default
title: Home
nav_order: 1
description: "Official flamapy documentation, the cutting-edge Python-based tool for Automatic Analysis of Feature Models (AAFM)."
permalink: /
---


# {% include flamapy.html %} official documentation
{: .fs-9 }

Introducing {% include flamapy.html %}, the cutting-edge Python-based tool for Automated Analysis of Feature Models (AAFM) using UVL and more. {% include flamapy.html %} revolutionizes feature model analysis by integrating the strengths of previous AAFM tools with advanced multi-solver and multi-metamodel capabilities. 

[Get started now](getting-started){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View it on GitHub][flamapy repo]{: .btn .fs-5 .mb-4 .mb-md-0 }

---

### <i class="fa-solid fa-puzzle-piece"></i> Easily extensible
* **Plugin Generator**: Simplifies the process of creating new plugins with a semi-automatic generator, making customization and expansion straightforward.
* **Variability modelling in the wild**: Initially supports cardinality-based feature models, with the flexibility to easily incorporate other types like attributed feature models.

### <i class="fa-solid fa-life-ring"></i> Robust solver support

* **PySAT Integration**: Utilizes the PySAT metasolver, offering access to more than ten distinct solvers. This diversity allows for optimal solution finding across various complex scenarios.

* **BDD Integration**: Utilizes the CU-BDD metasolver, offering efficient variability model analysis for some operations. 

### <i class="fa-brands fa-searchengin"></i> Easy to use, easy to integrate

* **Easy-to-use python facade**: Designed with capabilities to analyse modes in Python with just a line of code.
* **Command line direct use**: Easy to inegrate in any ecosystem.
* **WASM support**: Run analysis in your browser. Currently, both {% include flamapy.html %} and PySAT are WASM compatible. Enable analysis with 0 configuration process.
* **REST / SWAGGER available**: Integrate the tool in yours by means of a robust backend Rest API.

### <i class="fa-solid fa-calculator"></i> Large set of operations

You can find all set operations [here](/framework/operations/)

{: .fs-6 .fw-300 }


---

### Changelog

Detailed changes for each release are documented in the [release notes].

### Contributing

When contributing to this repository, please first read [contributing].

[^1]: The [source file for this page] uses all three markup languages.

[^2]: [It can take up to 10 minutes for changes to your site to publish after you push the changes to GitHub](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll#creating-your-site).

[Jekyll]: https://jekyllrb.com
[Markdown]: https://daringfireball.net/projects/markdown/
[Liquid]: https://github.com/Shopify/liquid/wiki
[Front matter]: https://jekyllrb.com/front-matter/
[Jekyll configuration]: https://jekyllrb.com/configuration/
[source file for this page]: https://github.com/just-the-docs/just-the-docs/blob/main/index.md
[Just the Docs Template]: https://just-the-docs.github.io/just-the-docs-template/
[Just the Docs]: https://just-the-docs.com
[flamapy repo]: https://github.com/flamapy/
[Just the Docs README]: https://github.com/just-the-docs/just-the-docs/blob/main/README.md
[GitHub Pages]: https://pages.github.com/
[Template README]: https://github.com/just-the-docs/just-the-docs-template/blob/main/README.md
[GitHub Pages / Actions workflow]: https://github.blog/changelog/2022-07-27-github-pages-custom-github-actions-workflows-beta/

[use the template]: https://github.com/just-the-docs/just-the-docs-template/generate

[getting-started]: {% link getting-started.md %}

[release notes]: https://github.com/flamapy/flamapy_fw/releases

[contributing]: {%  link contributing/contributing.md %}