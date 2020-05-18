#
$VerbosePreference = "continue"
$env:PYTHONUTF8=1
$filename=$args[0]
sphinx-build  -N -v -b html $filename _build/html

