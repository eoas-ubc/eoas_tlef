#!/bin/bash -v
#
#
<<<<<<< HEAD
mkdir -p ../_build/eoas_python
rm -rf ../_build/eoas_python/*
=======
mkdir -p ../_build/ebp
rm -rf ../_build/ebp/*
>>>>>>> 2dce2c3... new eoas python book
#
# build the website
#
jb build book/
<<<<<<< HEAD
rsync -avz book/_build/html/* ../_build/eoas_python/.
=======
rsync -avz book/_build/html/* ../_build/ebp/.
>>>>>>> 2dce2c3... new eoas python book





