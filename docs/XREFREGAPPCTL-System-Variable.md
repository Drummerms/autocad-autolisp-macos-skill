# XREFREGAPPCTL (System Variable)

Controls whether the registered application (RegApp) records stored in an xref being loaded are copied to the host drawing.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 2 |

| Value | Description |
| 0 | Legacy behavior. All regapp records are copied to the host drawing. |
| 1 | Current behavior. Only the necessary regapp records are copied to the host drawing, which usually results in none being copied. |
| 2 | Limits regapp records copied to the host drawing to those related to custom applications. |

NOTE:The XREFREGAPPCTL system variable only applies to DWG xrefs, not to other external references such as underlays.

#### Related Tasks

* [To Change Object Selection Settings](To-Change-Object-Selection-Settings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*