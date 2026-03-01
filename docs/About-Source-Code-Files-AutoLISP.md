# About Source Code Files (AutoLISP)

Although you can enter AutoLISP code at the AutoCAD Command prompt or Visual LISP Console window prompt (AutoCAD for Windows
only), any functions you define are lost when you close the drawing or session they were created in.

NOTE:The Visual LISP IDE is not available in AutoCAD LT for Windows and on Mac OS.

AutoLISP source code can be saved to an ASCII text file with a
*.lsp* extension. Saving AutoLISP source code to a file has the following advantages:

* Programs are not lost when the drawing they are defined in is closed.
* Programs can be used in more than one drawing and can be executed on multiple machines.
* Programs can be shared with others in your organization.
* Testing and debugging multiple expressions is considerably easier.

AutoLISP source code can also be stored in files with a
*.mnl* extension. A Menu AutoLISP (MNL) file contains custom functions and commands that are required for the elements defined in
a customization (CUIx) file. A MNL file is loaded automatically when it has the same name as a customization (CUIx) file that
is loaded into the AutoCAD-based product.

NOTE:AutoCAD LT doesn't support the automatic loading of MNL files, but the files can be loaded using the AutoLISP
LOAD function from another LISP file.

For example, in AutoCAD for Windows, when
*acad.cuix* is loaded, the file named
*acad.mnl* is also loaded if it is found in one of the folders listed as part of the program's Support File Search Path. If a CUIx file
does not have a corresponding MNL file, no error is displayed, the product just moves and loading other support files.

NOTE:While AutoLISP source code is commonly saved in files with a
*.lsp* or
*.mnl* extension, AutoLISP code can be loaded from any ASCII text file.

#### Topics in this section

* [About Formatting and Spaces in Code (AutoLISP)](About-Formatting-and-Spaces-in-Code-AutoLISP.md)

  AutoLISP code can span multiple lines, and contain empty lines and extra spaces. Empty lines and extra spaces do not have
  any significant meaning, but can make your code easier to read.
* [About Comments in AutoLISP Program Files (AutoLISP)](About-Comments-in-AutoLISP-Program-Files-AutoLISP.md)

  Comments are useful to both the programmer and future users who may need to revise a program to suit their needs.
* [To Create and Open AutoLISP Source Code Files (AutoLISP)](To-Create-and-Open-AutoLISP-Source-Code-Files-AutoLISP.md)

  AutoLISP source code files can be created and edited using a plain text editor.

#### Related Tasks

* [To Create and Open AutoLISP Source Code Files (AutoLISP)](To-Create-and-Open-AutoLISP-Source-Code-Files-AutoLISP.md)

#### Related Concepts

* [About Defining Commands (AutoLISP)](About-Defining-Commands-AutoLISP.md)
* [About Expressions (AutoLISP)](About-Expressions-AutoLISP.md)
* [About Function Syntax (AutoLISP)](About-Function-Syntax-AutoLISP.md)
* [About Variables (AutoLISP)](About-Variables-AutoLISP.md)
* [About Comments in AutoLISP Program Files (AutoLISP)](About-Comments-in-AutoLISP-Program-Files-AutoLISP.md)
* [About Formatting and Spaces in Code (AutoLISP)](About-Formatting-and-Spaces-in-Code-AutoLISP.md)
* [About Loading AutoLISP Applications](About-Loading-AutoLISP-Applications.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*