# ELLIPSE (DXF)

The following group codes apply to ellipse entities.

| Ellipse group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbEllipse) |
| 10 | Center point (in WCS)  DXF: *X* value; APP: 3D point |
| 20, 30 | DXF: *Y* and *Z* values of center point (in WCS) |
| 11 | Endpoint of major axis, relative to the center (in WCS)  DXF: *X* value; APP: 3D point |
| 21, 31 | DXF: *Y* and *Z* values of endpoint of major axis, relative to the center (in WCS) |
| 210 | Extrusion direction (optional; default = 0, 0, 1)  DXF: *X* value; APP: 3D vector |
| 220, 230 | DXF: *Y* and *Z* values of extrusion direction (optional) |
| 40 | Ratio of minor axis to major axis |
| 41 | Start parameter (this value is 0.0 for a full ellipse) |
| 42 | End parameter (this value is 2pi for a full ellipse) |

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*