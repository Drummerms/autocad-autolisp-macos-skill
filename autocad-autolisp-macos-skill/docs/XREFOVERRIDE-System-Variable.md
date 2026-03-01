# XREFOVERRIDE (System Variable)

Controls the display of object properties on referenced layers.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 0 |

The XREFOVERRIDE system variable affects display and plotting, and works in conjunction with the VISRETAIN system variable.
If you want the xref layers to retain their original layer settings, it is recommended to set VISRETAIN and XREFOVERRIDE system
variables to 0.

| Value | Description |
| 0 | When the properties of the objects (such as color, linetype, lineweight, transparency, or plot style) on the external reference drawing are set to ByLayer, any changes to the xref layer properties are displayed in the current drawing (legacy behavior) |
| 1 | When the visual properties of the objects on the external reference drawing are *not* set to ByLayer, objects on xref layers are treated as if their properties are set to ByLayer and every external reference layer can have its own set of layer overrides |

NOTE:The XREFOVERRIDE system variable only applies to DWG xrefs, not to other references such as underlays.

#### Related References

* [XREFTYPE (System Variable)](XREFTYPE-System-Variable.md)

#### Related Concepts

* [About Xref Layer Properties and Overrides](About-Xref-Layer-Properties-and-Overrides.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*