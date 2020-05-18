#
$VerbosePreference = "continue"
$env:PYTHONUTF8=1
$filename=$args[0]
jb build $filename
