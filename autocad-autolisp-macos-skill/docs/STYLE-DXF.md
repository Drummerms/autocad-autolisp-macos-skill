# STYLE (DXF)

The following group codes apply to STYLE symbol table entries.

| STYLE group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbTextStyleTableRecord) |
| 2 | Style name |
| 70 | Standard flag values (bit-coded values):  1 = If set, this entry describes a shape  4 = Vertical text  16 = If set, table entry is externally dependent on an xref  32 = If both this bit and bit 16 are set, the externally dependent xref has been successfully resolved  64 = If set, the table entry was referenced by at least one entity in the drawing the last time the drawing was edited. (This flag is for the benefit of AutoCAD commands. It can be ignored by most programs that read DXF files and need not be set by programs that write DXF files) |
| 40 | Fixed text height; 0 if not fixed |
| 41 | Width factor |
| 50 | Oblique angle |
| 71 | Text generation flags:  2 = Text is backward (mirrored in *X*)  4 = Text is upside down (mirrored in *Y*) |
| 42 | Last height used |
| 3 | Primary font file name |
| 4 | Bigfont file name; blank if none |
| 1071 | A long value which contains a truetype font’s pitch and family, character set, and italic and bold flags |

A STYLE table item is also used to record shape file LOAD command requests. In this case the first bit (1) is set in the 70
group flags and only the 3 group (shape file name) is meaningful (all the other groups are output, however).

#### Related References

* [Common Group Codes for Symbol Table Entries (DXF)](Common-Group-Codes-for-Symbol-Table-Entries-DXF.md)
* [About the DXF TABLES Section (DXF)](About-the-DXF-TABLES-Section-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*