# About Using DCL to Define Dialog Boxes (DCL)

You define dialog boxes by entering DCL descriptions in ASCII text files, much like writing AutoLISP code. DCL files have
a
*.dcl* extension. A single DCL file can contain the description of one or more dialog boxes, or it can contain only prototype tiles
and subassemblies for use by other DCL files. A DCL file consists of the following three parts, which can appear in any order.
Depending on your application, only one or more of these parts is required.

* References to other DCL files

  These consist of include directives as described in About Referencing DCL Files (DCL).
* Prototype tile and subassembly definitions

  These are tile definitions you can refer to in subsequent tile definitions (including dialog box definitions).
* Dialog box definitions

  These define the attributes of tiles or override the attributes defined in prototype tiles and subassemblies.

#### Topics in this section

* [About The Base.dcl and Acad.dcl/Acadlt.dcl Files (DCL)](About-The-Base.dcl-and-Acad.dcl-Acadlt.dcl-Files-DCL.md)

  The
  base.dcl and
  acad.dcl (or
  acadlt.dcl for AutoCAD LT) files contain the predefined tiles and DCL dialog boxes.
* [About Referencing DCL Files (DCL)](About-Referencing-DCL-Files-DCL.md)

  When you create dialog boxes, you must create a new, application-specific DCL file.
* [About Syntax and Comments in DCL Files (DCL)](About-Syntax-and-Comments-in-DCL-Files-DCL.md)

  Dialog control language (DCL) files are plain ASCII files which define a dialog box and its elements.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*