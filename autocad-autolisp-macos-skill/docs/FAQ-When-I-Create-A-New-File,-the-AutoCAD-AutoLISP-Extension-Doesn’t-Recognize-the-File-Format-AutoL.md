# FAQ: When I Create A New File, the AutoCAD AutoLISP Extension Doesn’t Recognize the File Format? (AutoLISP/VS Code)

VS Code can be used to edit a variety of files, not just AutoLISP source (LSP) files, and therefore uses the default file
format of 'Plain Text'. After creating a new file, you should save the file with the
*.lsp* file extension. Upon saving the file, the AutoCAD AutoLISP Extension will recognize the format of the file as being 'AutoLISP'
instead of 'Plain Text'.

Alternatively, you can change the default format that VS Code uses to 'AutoLISP' if you commonly use VS Code to create and
edit LSP files. To change the default file format of VS Code, do the following:

1. In Visual Studio Code, click File menu > Preferences > Settings (or click Code menu > Preferences > Settings on Mac OS).
2. In the Settings window, Search Settings text box, type
   *default language*.
3. In the settings list, click in the Files: Default Language text box and type
   *autolisp*.

   Now when a new file is created in VS Code, it will default to the 'AutoLISP' format without first saving the file.

#### Related Information

* [Getting Started with Visual Studio Code (AutoLISP/VS Code)](Getting-Started-with-Visual-Studio-Code-AutoLISP-VS-Code.md)
* [Creating and Opening AutoLISP Files (AutoLISP/VS Code)](Creating-and-Opening-AutoLISP-Files-AutoLISP-VS-Code.md)
* [To Create a New AutoLISP or DCL File (AutoLISP/VS Code)](To-Create-a-New-AutoLISP-or-DCL-File-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*