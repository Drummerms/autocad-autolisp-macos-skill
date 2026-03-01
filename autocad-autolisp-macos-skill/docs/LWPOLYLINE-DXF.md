# LWPOLYLINE (DXF)

The following group codes apply to lwpolyline entities.

| Lwpolyline group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbPolyline) |
| 90 | Number of vertices |
| 70 | Polyline flag (bit-coded); default is 0:  1 = Closed; 128 = Plinegen |
| 43 | Constant width (optional; default = 0). Not used if variable width (codes 40 and/or 41) is set |
| 38 | Elevation (optional; default = 0) |
| 39 | Thickness (optional; default = 0) |
| 10 | Vertex coordinates (in OCS), multiple entries; one entry for each vertex  DXF: *X* value; APP: 2D point |
| 20 | DXF: *Y* value of vertex coordinates (in OCS), multiple entries; one entry for each vertex |
| 91 | Vertex identifier |
| 40 | Starting width (multiple entries; one entry for each vertex) (optional; default = 0; multiple entries). Not used if constant width (code 43) is set |
| 41 | End width (multiple entries; one entry for each vertex) (optional; default = 0; multiple entries). Not used if constant width (code 43) is set |
| 42 | Bulge (multiple entries; one entry for each vertex) (optional; default = 0) |
| 210 | Extrusion direction (optional; default = 0, 0, 1)  DXF: *X* value; APP: 3D vector |
| 220, 230 | DXF: *Y* and *Z* values of extrusion direction (optional) |

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*