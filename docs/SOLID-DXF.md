# SOLID (DXF)

The following group codes apply to solid entities.

| Solid group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbTrace) |
| 10 | First corner  DXF: *X* value; APP: 3D point |
| 20, 30 | DXF: *Y* and *Z* values of first corner |
| 11 | Second corner  DXF: *X* value; APP: 3D point |
| 21, 31 | DXF: *Y* and *Z* values of second corner |
| 12 | Third corner  XF: *X* value; APP: 3D point |
| 22, 32 | DXF: *Y* and *Z* values of third corner |
| 13 | Fourth corner. If only three corners are entered to define the SOLID, then the fourth corner coordinate is the same as the third.  DXF: *X* value; APP: 3D point |
| 23, 33 | DXF: *Y* and *Z* values of fourth corner |
| 39 | Thickness (optional; default = 0) |
| 210 | Extrusion direction (optional; default = 0, 0, 1)  DXF: *X* value; APP: 3D vector |
| 220, 230 | DXF: *Y* and *Z* values of extrusion direction (optional) |

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*