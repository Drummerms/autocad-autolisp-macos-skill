# Creating and Opening AutoLISP Files (AutoLISP/VS Code)

VS Code allows you to work many different types of files that are saved in plain text; this includes AutoLISP source (LSP),
AutoLISP Menu source (MNL), and Dialog Control Language (DCL) files.

Creating a new LSP, MNL, or DCL file in VS Code is similar to creating a new file in most other applications with one exception.
When you create a new file in most applications, the application automatically assumes the new file is of a specific type.
For example, a new file in AutoCAD or Microsoft Word is assumed to be a drawing or document file. However, new files created
in VS Code are recognized as a
*plain text file* and are not assumed to be of a specific type.

A plain text file in VS Code is a file that has:

* No extension
* An extension of
  *.txt* or
  *.gitignore*
* An extension without an associated application

After you create a new file, save the file with its expected extension to help VS Code identify and enable all installed extensions
associated for that file type. For example, if you save a new file with the extension of
*.lsp* all the tools associated with the AutoCAD AutoLISP Extension are enabled. Similarly, when opening a file, VS Code identifies
a file's type based on its extension and enables all installed extensions based on the file's extension.

TIP:It is possible to force VS Code to create new files as being of a specific type. For example, if you primarily use VS Code
to create and edit LSP files, you can set the Default Language setting of VS Code to
*autolisp*. See
[FAQ: When I Create A New File, the AutoCAD AutoLISP Extension Doesn’t Recognize the File Format?](FAQ-When-I-Create-A-New-File,-the-AutoCAD-AutoLISP-Extension-Doesn’t-Recognize-the-File-Format-AutoL.md) for more information on how to change the Default Language setting of VS Code.

When a new file has been saved, it can be managed from a folder on a local or network drive, or an AutoLISP project that has
been opened in the AutoLISP Project Manager. For information on managing LSP files, see
[Managing AutoLISP Files with VS Code](Managing-AutoLISP-Files-AutoLISP-VS-Code.md).

#### Topics in this section

* [To Create a New AutoLISP or DCL File (AutoLISP/VS Code)](To-Create-a-New-AutoLISP-or-DCL-File-AutoLISP-VS-Code.md)
* [To Open an AutoLISP or DCL File (AutoLISP/VS Code)](To-Open-an-AutoLISP-or-DCL-File-AutoLISP-VS-Code.md)

#### Related Information

* [Getting Started with Visual Studio Code (AutoLISP/VS Code)](Getting-Started-with-Visual-Studio-Code-AutoLISP-VS-Code.md)
* [Editing AutoLISP Files (AutoLISP/VS Code)](Editing-AutoLISP-Files-AutoLISP-VS-Code.md)
* [Formatting AutoLISP Files (AutoLISP/VS Code)](Formatting-AutoLISP-Files-AutoLISP-VS-Code.md)
* [FAQ: When I Create A New File, the AutoCAD AutoLISP Extension Doesn’t Recognize the File Format? (AutoLISP/VS Code)](FAQ-When-I-Create-A-New-File,-the-AutoCAD-AutoLISP-Extension-Doesn’t-Recognize-the-File-Format-AutoL.md)
* [Tutorial: Getting Started with the AutoLISP Extension (AutoLISP/VS Code)](Tutorial-Getting-Started-with-the-AutoLISP-Extension-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*