# Getting Started with Visual Studio Code (AutoLISP/VS Code)

Before you can start developing AutoLISP programs with Visual Studio (VS) Code, there are some steps that you will need to
complete first. This topic outlines the various steps needed to install, configure, and use Visual Studio (VS) Code and the
AutoCAD AutoLISP Extension to develop and debug AutoLISP programs for AutoCAD.

1. *Install VS Code.* - VS Code isn't part of the AutoCAD install, and must be downloaded and installed separately. The version of VS Code built
   by Microsoft can be downloaded from the
   [Visual Studio Code website](https://code.visualstudio.com/). See
   [To Download and Install VS Code](To-Download-and-Install-VS-Code-AutoLISP-VS-Code.md) for a general overview on how to download and install VS Code.

   NOTE:Once installed and if you are using AutoCAD on Windows, VS Code can be launched with the VLISP command; not available in AutoCAD
   LT for Windows or on Mac OS.
2. *Install the AutoCAD AutoLISP Extension.* - While VS Code can be used to edit AutoLISP source (LSP) files without doing anything additional, it won't understand the
   syntax of or how to debug an AutoLISP program without installing the AutoCAD AutoLISP Extension. The AutoCAD AutoLISP Extension
   contains a set of special functions that provide syntax checking in the editor window and the ability to attach VS Code to
   AutoCAD which allows you to load and debug your custom programs. See
   [To Install the AutoCAD AutoLISP Extension](To-Install-the-AutoCAD-AutoLISP-Extension-AutoLISP-VS-Code.md) for steps on how to locate and install the AutoCAD AutoLISP Extension from the VS Code Extensions Marketplace.
3. *Add the Debug Configurations.* - Debug configurations are used to inform VS Code as to which application should be used when testing and debugging your
   custom AutoLISP programs. There are two different debug configurations available for use with the AutoCAD AutoLISP Extension;
   AutoCAD Debug Attach and AutoCAD Debug Launch. These debug configurations are stored as part of the extension's settings.
   See
   [To Setup the AutoCAD AutoLISP Extension for Debug](To-Setup-the-AutoCAD-AutoLISP-Extension-for-Debug-AutoLISP-VS-Code.md) for information on how to setup these debug configurations.

   NOTE:Debugging is not available with AutoCAD LT for Windows.
4. *Create or Open an Existing AutoLISP Project.* - AutoLISP projects allow you to logically group AutoLISP source (LSP) files. An AutoLISP project is saved to a file with
   the
   *.prj* extension. After an AutoLISP project has been opened in the AutoLISP Project Manager, you can add, edit, and remove LSP files.
   For information on using the AutoLISP Project Manager, see
   [Manage AutoLISP Files](Managing-AutoLISP-Files-AutoLISP-VS-Code.md) and
   [To Manage AutoLISP Projects.](To-Manage-Source-Files-with-an-AutoLISP-Project-AutoLISP-VS-Code.md).
5. *Create or Open an Existing AutoLISP Source (LSP) File.* - LSP files opened in VS Code with the AutoCAD AutoLISP Extension installed are evaluated for proper syntax and can be edited
   using extension specific features; autocomplete, code snippets, code formatting, and many more. For information on how to
   create, open, and edit LSP files in VS Code, see
   [Creating and Opening AutoLISP Files](Creating-and-Opening-AutoLISP-Files-AutoLISP-VS-Code.md),
   [Editing AutoLISP Files](Editing-AutoLISP-Files-AutoLISP-VS-Code.md), and
   [Formatting AutoLISP Files](Formatting-AutoLISP-Files-AutoLISP-VS-Code.md).
6. *Debug an Open AutoLISP Source (LSP) File.* - After adding the AutoLISP debug configurations to VS Code and opening an LSP file, you can step through and debug the AutoLISP
   statements stored in the LSP file. VS Code provides a variety of tools that allow you to watch the values of variables, set
   breakpoints and step through statements, inspect the current call stack, and much more. See
   [Debugging AutoLISP Files](Debugging-AutoLISP-Files-AutoLISP-VS-Code.md) for information on how to debug AutoLISP programs with VS Code and the AutoCAD AutoLISP Extension.

   NOTE:Debugging is not available with AutoCAD LT for Windows.
7. *Compile AutoLISP Source (LSP) Files.* - Optionally, before deploying your custom programs, you can compile your LSP files to protect the original source code.
   Based on the method used to compile an LSP file, either a FAS or VLX file is built. For information on how to compile your
   LSP files, see
   Compiling AutoLISP Files.

   NOTE:Compiling LSP files is supported in AutoCAD for Windows only; not available in AutoCAD LT for Windows or on Mac OS. VLX files
   can be loaded on Windows only.
8. *Deploy AutoLISP Programs.* - Once you have tested and debugged your AutoLISP programs, they are ready for deployment. Deploying your AutoLISP programs
   can be as simple as copying them to a local or network drive, bundling them into a plug-in, or installing them with an installation
   program. Copying the files directly to a drive is often the simplest approach, but you will also need to setup AutoCAD to
   locate and load your programs. See
   [About Loading AutoLISP Applications](About-Loading-AutoLISP-Applications.md) and
   [About Installing and Uninstalling Plug-In Applications](About-Installing-and-Uninstalling-Plug-In-Applications.md) for information on loading and creating plug-in bundles for your AutoLISP programs.

#### Related Information

* [Tutorial: Installing and Configuring the AutoLISP Extension (AutoLISP/VS Code)](Tutorial-Installing-and-Configuring-the-AutoLISP-Extension-AutoLISP-VS-Code.md)
* [Tutorial: Getting Started with the AutoLISP Extension (AutoLISP/VS Code)](Tutorial-Getting-Started-with-the-AutoLISP-Extension-AutoLISP-VS-Code.md)
* [Tutorial: Debugging LSP Files with the AutoLISP Extension (AutoLISP/VS Code)](Tutorial-Debugging-LSP-Files-with-the-AutoLISP-Extension-AutoLISP-VS-Code.md)
* [Tutorial: Formatting LSP Files with the AutoLISP Extension (AutoLISP/VS Code)](Tutorial-Formatting-LSP-Files-with-the-AutoLISP-Extension-AutoLISP-VS-Code.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*