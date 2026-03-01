# VISRETAIN (System Variable)

Controls the properties of xref-dependent layers.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 1 |

Controls visibility, color, linetype, lineweight, and plot styles. Use this system variable in conjunction with the VISRETAINMODE
system variable to manage which xref layer property overrides you want to automatically sync on reload.

| 0 | The layer table, as stored in the reference drawing (xref), takes precedence. Changes made to xref-dependent layers in the current drawing are valid in the current session only and are not saved with the drawing. When the current drawing is reopened, the layer table is reloaded from the reference drawing, and the current drawing reflects all of those layer property settings. |
| 1 | Xref-dependent layer changes made in the current drawing take precedence. Layer settings are saved with the current drawing's layer table and persist from session to session. |

#### Related References

* [VISRETAINMODE (System Variable)](VISRETAINMODE-System-Variable.md)

#### Related Concepts

* [About Attaching and Detaching Referenced Drawings (Xrefs)](About-Attaching-and-Detaching-Referenced-Drawings-Xrefs.md)
* [About Xref Layer Properties and Overrides](About-Xref-Layer-Properties-and-Overrides.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*