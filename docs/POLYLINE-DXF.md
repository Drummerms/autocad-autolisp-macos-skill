# POLYLINE (DXF)

The following group codes apply to polyline entities.

| Polyline group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDb2dPolyline or AcDb3dPolyline) |
| 66 | Obsolete; formerly an “entities follow flag” (optional; ignore if present) |
| 10 | DXF: always 0  APP: a “dummy” point; the *X* and *Y* values are always 0, and the *Z* value is the polyline's elevation (in OCS when 2D, WCS when 3D) |
| 20 | DXF: always 0 |
| 30 | DXF: polyline's elevation (in OCS when 2D; WCS when 3D) |
| 39 | Thickness (optional; default = 0) |
| 70 | Polyline flag (bit-coded; default = 0):  1 = This is a closed polyline (or a polygon mesh closed in the M direction)  2 = Curve-fit vertices have been added  4 = Spline-fit vertices have been added  8 = This is a 3D polyline  16 = This is a 3D polygon mesh  32 = The polygon mesh is closed in the N direction  64 = The polyline is a polyface mesh  128 = The linetype pattern is generated continuously around the vertices of this polyline |
| 40 | Default start width (optional; default = 0) |
| 41 | Default end width (optional; default = 0) |
| 71 | Polygon mesh M vertex count (optional; default = 0) |
| 72 | Polygon mesh N vertex count (optional; default = 0) |
| 73 | Smooth surface M density (optional; default = 0) |
| 74 | Smooth surface N density (optional; default = 0) |
| 75 | Curves and smooth surface type (optional; default = 0); integer codes, not bit-coded:  0 = No smooth surface fitted  5 = Quadratic B-spline surface  6 = Cubic B-spline surface  8 = Bezier surface |
| 210 | Extrusion direction (optional; default = 0, 0, 1)  DXF: *X* value; APP: 3D vector |
| 220, 230 | DXF: *Y* and *Z* values of extrusion direction (optional) |

Xdata with the "AUTOCAD\_POSTSCRIPT\_FIGURE" application ID may follow a polyline entity. This contains information related to PostScript images and PostScript fill information.

#### Topics in this section

* [Polyface Meshes (DXF)](Polyface-Meshes-DXF.md)

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)
* [Polyface Meshes (DXF)](Polyface-Meshes-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*