# Working with VS-Code

See VS-Code [documentation](https://code.visualstudio.com/docs).

* Managing version control from within VS Code is explained [here](https://code.visualstudio.com/docs/editor/versioncontrol) and there is a [video based on this](https://www.youtube.com/watch?v=wMqukSKYcvU) page. 
* Working with GitHub from inside VS-Code is outlined [here](https://code.visualstudio.com/docs/editor/github).
* [stackoverflow: saving and loading extensions](https://stackoverflow.com/questions/35773299/how-can-you-export-the-visual-studio-code-extension-list)
* [austin_vscode.txt extension list](support_files/austin_vscode.txt)
* loading these extensions with powershell:

```
cd docs/support_files

* [saving and loading extensions](https://stackoverflow.com/questions/35773299/how-can-you-export-the-visual-studio-code-extension-list)

* [an extension list](support_files/austin_vscode.txt)

* loading the extensions with powershell:

```
cat austin_vscode.txt |% { code --install-extension $_}
```

* with bash:

```
cd docs/support_files

cat austin_vscode.txt | xargs -L 1 echo code --install-extension
```

