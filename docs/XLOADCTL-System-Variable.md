# XLOADCTL (System Variable)

Turns xref demand-loading on and off, and controls whether it opens the referenced drawing or a copy.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 2 |

| 0 | Turns off demand-loading; the entire drawing is loaded. |
| 1 | Turns on demand-loading. Referenced drawings are kept open and locked. |
| 2 | Turns on demand-loading. Copies of referenced drawings are opened and locked; referenced drawings are not locked |

When XLOADCTL is set to 2, a copy of each referenced drawing file is stored in the folder specified by the XLOADPATH system
variable or the temporary files folder (set in the Application Preferences dialog box).

Additionally, xrefs load faster when you work across a network: the performance enhancement is most pronounced when you open
drawings with many xrefs.

#### Related Concepts

* [About Improving Performance When Using Xrefs](About-Improving-Performance-When-Using-Xrefs.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*