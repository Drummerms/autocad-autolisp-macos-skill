# 3DFACE (DXF)

The following group codes apply to 3dface entities. In addition to the group codes described here, see Common Group Codes
for Entities.

| 3dface group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbFace) |
| 10 | First corner (in WCS)  DXF: *X* value; APP: 3D point |
| 20, 30 | DXF: *Y* and *Z* values of first corner (in WCS) |
| 11 | Second corner (in WCS)  DXF: *X* value; APP: 3D point |
| 21, 31 | DXF: *Y* and *Z* values of second corner (in WCS) |
| 12 | Third corner (in WCS)  DXF: *X* value; APP: 3D point |
| 22, 32 | DXF: *Y* and *Z* values of third corner (in WCS) |
| 13 | Fourth corner (in WCS). If only three corners are entered, this is the same as the third corner  DXF: *X* value; APP: 3D point |
| 23, 33 | DXF: *Y* and *Z* values of fourth corner (in WCS) |
| 70 | Invisible edge flags (optional; default = 0):  1 = First edge is invisible  2 = Second edge is invisible  4 = Third edge is invisible  8 = Fourth edge is invisible |

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*