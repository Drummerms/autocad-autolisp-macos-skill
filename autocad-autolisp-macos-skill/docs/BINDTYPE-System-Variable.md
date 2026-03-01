# BINDTYPE (System Variable)

Specifies the default or controls the naming behavior to be applied to "named objects" in an xref when a bind or an edit-in-place
operation is performed on it.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Not-saved |
| Initial value: | 0 |

Named objects include layers, dimension and text styles, blocks, views, and so on.

For example, consider a drawing file named Floorplan that includes a layer named Electrical. If this drawing is attached as
an xref in the current drawing, that layer name would appear as
*drawingname*|*layername*, or in this case, Floorplan|Electrical. This naming style is designed to avoid a conflict with any existing layer names in
the current drawing.

When BINDTYPE is set to 0, the standard behavior, if a bind operation is performed on the xref, the layer name becomes
*drawingname*$0$*layername*, or in this case, Floorplan$0$Electrical. If the layer Floorplan$0$Electrical already exists from a previous bind operation,
the new layer name would be Floorplan$1$Electrical, and so on.

When BINDTYPE is set to 1, the merge behavior, if a bind operation is performed on the xref, the layer name remains the same,
in this case Electrical. This merges the layers from the xref with those in the current drawing which is similar to detaching
and inserting the reference drawing.

| Value | Description |
| 0 | Standard behavior |
| 1 | Merge behavior |

Here are the commands and how they are affected by this system variable:

* *-REFEDIT* - Controls whether layers and other named objects in the reference are uniquely named. This is equivalent to the Create Unique
  Layer, Style, and Block Names option on the Settings tab of the Reference Edit dialog box (REFEDIT command).
* *-XREF* - Controls the bind type to use when the Bind option is used. This is equivalent to the Bind and Insert options in the Bind
  Xrefs/DGN Underlays dialog box (EXTERNALREFERNCES and XREF commands).
* *EXTERNALREFERENCES or XREF* - Specifies the default bind type to use in the Bind Xrefs/DGN Underlays dialog box which is displayed by choosing Bind from
  the contextual menu on the External References palette.

NOTE:The XBIND and REFEDIT commands are not affected by this system variable.

#### Related Concepts

* [About Archiving Drawings with Xrefs (Binding)](About-Archiving-Drawings-with-Xrefs-Binding.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*