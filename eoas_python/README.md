# quantecon-example

- copied from https://github.com/ExecutableBookProject/quantecon-example.git

A demonstration of Jupyter Book functionality using QuantEcon Python
programming source material.

## How to create your own Jupyter Book

For the purposes of this project, we are replicating the content under [Python
Programming for Quantitative Economics](https://python-programming.quantecon.org). To demonstrate at a high
level what has been done, we first convert each source file from rST to
MyST-syntax markdown, then build the book by following the instructions in the
[Books with Jupyter documentation](https://beta.jupyterbook.org/intro.html). 


### Creating an environment

1. `conda env create -f environment.yml`
2.  `conda activte ebp`

### Building a Jupyter Book

Run the following commands in your (Unix) terminal: 

```
cd quantecon-example
./build_website.sh
```

### Publishing this Jupyter Book

Run `ghp-import -n -p -f book/_build/html`

open https://eoas-ubc.github.io/eoas_tlef/ebp/docs/index.html
to see a sample build -- substitute your forked repo-address for
https://eoas-ubc.github.io  to see your build

