# working with vscode

* [saving and loading extensions](https://stackoverflow.com/questions/35773299/how-can-you-export-the-visual-studio-code-extension-list)

* [an extension list](support_files/austin_vscode.txt)

* loading the extensions with powershell:

```
cat austin_vscode.txt |% { code --install-extension $_}
```

* with bash:

```
cat austin_vscode.txt | xargs -L 1 echo code --install-extension
```

