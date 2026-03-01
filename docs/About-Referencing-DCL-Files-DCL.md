# About Referencing DCL Files (DCL)

When you create dialog boxes, you must create a new, application-specific DCL file.

All DCL files can use the tiles defined in the
*base.dcl* file. A DCL file can also use tiles defined in another DCL file by naming the other file in what is called an include directive.
You can create your own hierarchy of DCL files, as shown in the following figure:

![](../images/GUID-4E577CE5-E161-49E4-87B1-7FFD90BD1EBF-low.png)

In this figure, the
*user1.dcl* and
*user2.dcl* files are independent of each other, but
*user3.dcl* uses tiles defined in
*user1.dcl*. The include directive has the form:

```
@include filename
```

where
*filename* is a quoted string containing the full name of the other DCL file. For example, the following directive includes a file named
*usercore.dcl*:

```
@include "usercore.dcl"
```

If you specify only the file name, the PDB feature searches for the file first in the current directory and then in the same
directory as the DCL file itself (the one that contains the include directive). If you specify a full path name, the PDB feature
searches only the directory specified in that path.

NOTE:The DCL files you create cannot use the dialog boxes defined in
*acad.dcl* (or
*acadlt.dcl* for AutoCAD LT). You cannot specify
@include "acad.dcl" (@include "acadlt.dcl"). However, if you want to create similar dialog boxes, you can cut and paste the definitions into your own DCL file.

#### Related Concepts

* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Dialog Box Components (DCL)](About-Dialog-Box-Components-DCL.md)
* [About Nested Dialog Boxes (DCL)](About-Nested-Dialog-Boxes-DCL.md)
* [About Syntax and Comments in DCL Files (DCL)](About-Syntax-and-Comments-in-DCL-Files-DCL.md)
* [About The Base.dcl and Acad.dcl/Acadlt.dcl Files (DCL)](About-The-Base.dcl-and-Acad.dcl-Acadlt.dcl-Files-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*