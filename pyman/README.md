# pyman example

- This is a lightly edited copy of https://github.com/ronojoy/pyman, written
  originally by [David Pine](https://physics.nyu.edu/pine/Home.html) and
  converted from rst to ipynb notebooks

- To build a website from these notebooks we are using [myst-nb](https://myst-nb.readthedocs.io/en/latest/)


## Creating an environment

1. `conda env create -f environment.yml`
2.  `conda activte ebp`

## Building the website

Run the following commands in your (Unix) terminal: 

```
cd pyman
./build_website.sh
```

### Publishing this Jupyter Book

- Run `ghp-import -n -p -f book/_build`

- open https://eoas-ubc.github.io/eoas_tlef/pyman/index.html
  to see a sample build -- substitute your forked repo-address for
  https://eoas-ubc.github.io  to see your own build.

