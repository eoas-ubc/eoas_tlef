#!/bin/bash -v
#
#
mkdir -p ../_build/ebp
rm -rf ../_build/ebp/*
#
# build the website
#
jb build book/
rsync -avz book/_build/html/* ../_build/ebp/.





