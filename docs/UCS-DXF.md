# UCS (DXF)

The following group codes apply to UCS symbol table entries.

| UCS group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbUCSTableRecord) |
| 2 | UCS name |
| 70 | Standard flag values (bit-coded values):  16 = If set, table entry is externally dependent on an xref  32 = If both this bit and bit 16 are set, the externally dependent xref has been successfully resolved  64 = If set, the table entry was referenced by at least one entity in the drawing the last time the drawing was edited. (This flag is for the benefit of AutoCAD commands. It can be ignored by most programs that read DXF files and need not be set by programs that write DXF files) |
| 10 | Origin (in WCS)  DXF: *X* value; APP: 3D point |
| 20, 30 | DXF: *Y* and *Z* values of origin (in WCS) |
| 11 | *X*-axis direction (in WCS)  DXF: *X* value; APP: 3D vector |
| 21, 31 | DXF: *Y* and *Z* values of *X*-axis direction (in WCS) |
| 12 | *Y*-axis direction (in WCS)  DXF: *X* value; APP: 3D vector |
| 22, 32 | DXF: *Y* and *Z* values of *Y*-axis direction (in WCS) |
| 79 | Always 0 |
| 146 | Elevation |
| 346 | ID/handle of base UCS if this is an orthographic. This code is not present if the 79 code is 0. If this code is not present and 79 code is non-zero, then base UCS is assumed to be WORLD |
| 71 | Orthographic type (optional; always appears in pairs with the 13, 23, 33 codes):  1 = Top; 2 = Bottom  3 = Front; 4 = Back  5 = Left; 6 = Right |
| 13 | Origin for this orthographic type relative to this UCS  DXF: *X* value of origin point; APP: 3D point |
| 23, 33 | DXF: *Y* and *Z* values of origin point |

Each 71/13,23,33 pair defines the UCS origin for a particular orthographic type relative to this UCS. For example, if the
following pair is present, then invoking the UCS/LEFT command when UCSBASE is set to this UCS will cause the new UCS origin
to become (1,2,3).

```
71: 5
13: 1.0
23: 2.0
33: 3.0
```

If this pair were not present, then invoking the UCS/LEFT command would cause the new UCS origin to be set to this UCS's origin
point.

#### Related References

* [Common Group Codes for Symbol Table Entries (DXF)](Common-Group-Codes-for-Symbol-Table-Entries-DXF.md)
* [About the DXF TABLES Section (DXF)](About-the-DXF-TABLES-Section-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*