# APPID (DXF)

The following group codes apply to APPID symbol table entries.

| APPID group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbRegAppTableRecord) |
| 2 | User-supplied (or application-supplied) application name (for extended data). These table entries maintain a set of names for all registered applications |
| 70 | Standard flag values (bit-coded values):  16 = If set, table entry is externally dependent on an xref  32 = If both this bit and bit 16 are set, the externally dependent xref has been successfully resolved  64 = If set, the table entry was referenced by at least one entity in the drawing the last time the drawing was edited. (This flag is for the benefit of AutoCAD commands. It can be ignored by most programs that read DXF files and need not be set by programs that write DXF files) |

#### Related References

* [Common Group Codes for Symbol Table Entries (DXF)](Common-Group-Codes-for-Symbol-Table-Entries-DXF.md)
* [About the DXF TABLES Section (DXF)](About-the-DXF-TABLES-Section-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*