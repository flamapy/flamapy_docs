---
layout: default
title: WASM
parent: flamapy as a tool
nav_order: 5
---

# flamapy and pysat are WASM compatible

{: .warning }
> This is a work in progress documentation page


WebAssembly (WASM) is a binary instruction format designed to be executed in web browsers at near-native speed. It provides a compact and efficient way to run code written in multiple languages, including C, C++, and Rust, on the web. WASM aims to improve web performance and enable more complex and resource-intensive applications to run in the browser. It is a critical technology for modern web development, allowing for high-performance applications without relying on JavaScript alone.

Pyodide is an exciting project that brings the Python runtime to the browser via WebAssembly. By compiling the Python interpreter and scientific libraries to WebAssembly, Pyodide allows developers to run Python code directly in the web browser. This opens up new possibilities for web applications, enabling the use of Python's rich ecosystem of data science and machine learning libraries without requiring a backend server. Pyodide facilitates the integration of Python with JavaScript, allowing seamless interaction between the two languages and providing a powerful tool for developing interactive, high-performance web applications.

This means that you can run {% include flamapy.html %} in your browser. 
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
    <a href="#" onclick="alert('Coming soon')" class="highlight-button">Try flamapy in your browser</a>
</div>

To do it so, we need to first install pyodide and {% include flamapy.html %} within the browser. Note that we manually manage the dependencies. This is to avoid installing other plugins such as BDD which are not yet available in wasm. 

```javascript
async function preparare_WASM(){
    pyodide = await loadPyodide();
    await pyodide.loadPackage("micropip");
    const micropip = pyodide.pyimport("micropip");

    await pyodide.runPythonAsync(`
        import micropip
        await micropip.install("flamapy==2.0.0.dev2", deps=False)
        await micropip.install("flamapy-fw==2.0.0.dev2")
        await micropip.install("flamapy-fm==2.0.0.dev2")
        await micropip.install("flamapy-sat==2.0.0.dev2")
        `)
}
```

Then we can call python, and {% include flamapy.html %} code within the browser using a javascript with python method.
Note that this method, first, check if the default execution relyis on bdd to force it, using the easy-to-use facade, to use pysat. In the following code, param is the operation of the facade to use. Nonetheless, any operation within the facade or implemented in pysat is available. 


```javascript
 async function flamapy(param) {

	//This call directly to the function that hides the loding gif in the page
    //Now we are executing the python code. 
	try {
    let output = pyodide.runPython(
`
import js
from collections.abc import Iterable
from flamapy.interfaces.python.FLAMAFeatureModel import FLAMAFeatureModel
import inspect

def requires_with_sat(method):
    # Get the signature of the method
    signature = inspect.signature(method)
    # Check if 'with_sat' is a parameter
    return 'with_sat' in signature.parameters

file_content = js.document.getElementById('uvlfile').value
div = js.document.createElement("result")

with open("uvlfile.uvl", "w") as text_file:
    print(file_content, file=text_file)

fm = FLAMAFeatureModel("uvlfile.uvl")

if requires_with_sat(fm.${param}):
    result=fm.${param}(with_sat=True)
else:
    result=fm.${param}()

if isinstance(result, Iterable):
    result = "<br>".join([f'P({i}): {p}' for i, p in enumerate(result, 1)])
div.innerHTML = "<div id='deleteme'>"+str(result)+"</div>"
exists=js.document.getElementById('deleteme')
if(exists):
	exists.remove()

js.document.getElementById('result').append(div)
    `);
    } catch (err) {
        console.log(err);
    }
    hideLoading()

}```
```
To un other operations, that could be less tested you have to take a look to the names of them in the github repositories of the  [sat plugin](/plugins/sat). However most of operations are already documented with code snippets in. 

<ul>
  {% assign fm_operations = site.operations | where: "python", true %}
  {% for operation in fm_operations %}
    <li><a href="{{ operation.url }}">{{ operation.title }}</a></li>
  {% endfor %}
</ul>