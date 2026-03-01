# LAYER (DXF)

The following group codes apply to LAYER symbol table entries.

| LAYER group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbLayerTableRecord) |
| 2 | Layer name |
| 70 | Standard flags (bit-coded values):  1 = Layer is frozen; otherwise layer is thawed  2 = Layer is frozen by default in new viewports  4 = Layer is locked  16 = If set, table entry is externally dependent on an xref  32 = If both this bit and bit 16 are set, the externally dependent xref has been successfully resolved  64 = If set, the table entry was referenced by at least one entity in the drawing the last time the drawing was edited. (This flag is for the benefit of AutoCAD commands. It can be ignored by most programs that read DXF files and need not be set by programs that write DXF files) |
| 62 | Color number (if negative, layer is off) |
| 6 | Linetype name |
| 290 | Plotting flag. If set to 0, do not plot this layer |
| 370 | Lineweight enum value |
| 390 | Hard-pointer ID/handle of PlotStyleName object |
| 347 | Hard-pointer ID/handle to Material object |

Xref-dependent layers are output during SAVEAS. For these layers, the associated linetype name in the DXF file is always CONTINUOUS.

#### Related References

* [Common Group Codes for Symbol Table Entries (DXF)](Common-Group-Codes-for-Symbol-Table-Entries-DXF.md)
* [About the DXF TABLES Section (DXF)](About-the-DXF-TABLES-Section-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*