#region conda initialize
# !! Contents within this block are managed by 'conda init' !!
(& "C:\Users\phil\minjn20\Scripts\conda.exe" "shell.powershell" "hook") | Out-String | Invoke-Expression
#endregion
$env:tlef = "~\repos\eoas_tlef"
$tl =  "~\repos\eoas_tlef"
Set-PSReadLineOption -EditMode Emacs
function prompt 
{
    $l = Split-Path -leaf -path (Get-Location)
    $p = Split-Path -parent -path (Get-Location)
    $p = Split-path -leaf $p
    $e = Split-Path -leaf $env:conda_prefix
    write-host "($e):$p/$l"
    return "> "
}
function strip_file
{
    $d=(Get-Item $profile).DirectoryName
    write-output "your powershell directory is $d"
    # write-output "stored in the variable powerdir"
    return $d
}
#$powerdir=strip_file
$options = Get-PSReadLineOption
$options.StringColor = 'DarkBlue'
$options.StringColor = 'White'
write-output "through $profile"
# Chocolatey profile
$ChocolateyProfile = "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"
if (Test-Path($ChocolateyProfile)) {
  Import-Module "$ChocolateyProfile"
}
