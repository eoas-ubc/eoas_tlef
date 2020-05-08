# quantecon-example

- copied from https://github.com/executablebooks/quantecon-example.git


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

### Building a Jupyter Book (bash shell)

Run the following commands in your (Unix) terminal: 

```
cd quantecon-example
./build_website.sh
```

[Books with Jupyter documentation](https://beta.jupyterbook.org/intro.html).

### Creating an environment


1. `conda env create -f environment.yml`
2.  `conda activate edp`


### Building a Jupyter Book  (windows)

Run the following command in your powershell terminal: `jb build book/`.
If you would like to work with a clean build, you can empty the build folder by running `jb clean book/`. If the jupyter execution is cached, this command will not delete the cached folder. To remove the build folder, you can run `jb clean --all book/`.


### Publishing this Jupyter Book

Run `ghp-import -n -p -f book/_build/html`

open https://eoas-ubc.github.io/eoas_tlef/eoas_python/docs/index.html
to see a sample build -- substitute your forked repo-address for
https://eoas-ubc.github.io  to see your build


