# About Setting the Auditing Level to Affect Error Messages (DCL)

The level of semantic auditing affects which messages are issued for a DCL file.

NOTE:Semantic auditing is supported on Windows only.

If you set the audit level to 3, an alert dialog box is displayed with a warning message when an error is encountered. You
can see this for yourself by inserting the following line at the beginning of a DCL file:

```
dcl_settings : default_dcl_settings
{
  audit_level = 3;
}
```

Try viewing a dialog box with an error, such as adding a duplicate attribute. You will be alerted to view the
*acad.dce* file, which contains the following messages:

```
=== DCL semantic audit of C:/PROGRA~1/AUTOCA~1/VLISP/$vld$.dcl ===
```

At lower (less discriminating) levels of semantic auditing, AutoCAD does not look for redundant attribute definitions and
the dialog box displays normally. Remove the duplicate attribute statement from the DCL to correct the situation you were
warned about.

#### Related Concepts

* [About Semantic Auditing of DCL Files (DCL)](About-Semantic-Auditing-of-DCL-Files-DCL.md)
* [About DCL Error Handling (DCL)](About-DCL-Error-Handling-DCL.md)
* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Syntax and Comments in DCL Files (DCL)](About-Syntax-and-Comments-in-DCL-Files-DCL.md)
* [About The Base.dcl and Acad.dcl/Acadlt.dcl Files (DCL)](About-The-Base.dcl-and-Acad.dcl-Acadlt.dcl-Files-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*