#!/bin/bash -v
#
#
mkdir -p ../_build/eoas_python
rm -rf ../_build/eoas_python/*
#
# build the website
#
jb build book/
rsync -avz book/_build/html/* ../_build/eoas_python/.





