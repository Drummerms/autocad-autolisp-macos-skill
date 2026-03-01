# About Semantic Auditing of DCL Files (DCL)

AutoCAD provides a choice of four levels (0-3) of semantic auditing for DCL files.

Auditing attempts to detect code in the DCL file that is likely to be problematic or unnecessary. These audits are done at
DCL load time. An audit level for a DCL file can be set by including a line such as the following anywhere within the DCL
file, but not inside any tile definitions:

```
dcl_settings : default_dcl_settings
{
  audit_level = 3;
}
```

If your DCL file references other DCL files with include directives, you should define
dcl\_settings in only one file. The defined audit level is used in all included files. The following table describes each audit level:

| Semantic auditing levels | |
| Level | Description |
| 0 | No checking. Use only if the DCL files have been audited and have not been touched since the audit. |
| 1 | Errors. Finds DCL bugs that may cause AutoCAD to terminate. This level of checking is the default and involves almost no delay. Errors can include using undefined tiles and circular prototype definitions. |
| 2 | Warnings. Finds DCL bugs that result in dialog boxes with undesired layout or behavior. A modified DCL file should be audited at this level at least once. The warning level catches mistakes such as missing required attributes and inappropriate attribute values. |
| 3 | Hints. Finds redundant attribute definitions. |

NOTE:You should set
audit\_level to 3 during program development to get the most out of the auditing facility. Remember to remove or comment out the
dcl\_settings line before shipping DCL files to users.

#### Related Concepts

* [About Setting the Auditing Level to Affect Error Messages (DCL)](About-Setting-the-Auditing-Level-to-Affect-Error-Messages-DCL.md)
* [About DCL Error Handling (DCL)](About-DCL-Error-Handling-DCL.md)
* [About Designing Dialog Boxes (DCL)](About-Designing-Dialog-Boxes-DCL.md)
* [About Syntax and Comments in DCL Files (DCL)](About-Syntax-and-Comments-in-DCL-Files-DCL.md)
* [About The Base.dcl and Acad.dcl/Acadlt.dcl Files (DCL)](About-The-Base.dcl-and-Acad.dcl-Acadlt.dcl-Files-DCL.md)
* [DCL Tiles Reference (DCL)](DCL-Tiles-Reference-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*