#!/bin/bash -v
echo "$PWD"
ls -ltd *
printenv
cp -R bin "$PREFIX/."
#chmod a+x "$PREFIX/bin/*"


