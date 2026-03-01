# SPLINE (DXF)

The following group codes apply to spline entities.

| Spline group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbSpline) |
| 210 | Normal vector (omitted if the spline is nonplanar)  DXF: *X* value; APP: 3D vector |
| 220, 230 | DXF: *Y* and *Z* values of normal vector (optional) |
| 70 | Spline flag (bit coded):  1 = Closed spline  2 = Periodic spline  4 = Rational spline  8 = Planar  16 = Linear (planar bit is also set) |
| 71 | Degree of the spline curve |
| 72 | Number of knots |
| 73 | Number of control points |
| 74 | Number of fit points (if any) |
| 42 | Knot tolerance (default = 0.0000001) |
| 43 | Control-point tolerance (default = 0.0000001) |
| 44 | Fit tolerance (default = 0.0000000001) |
| 12 | Start tangent—may be omitted (in WCS)  DXF: *X* value; APP: 3D point |
| 22, 32 | DXF: *Y* and *Z* values of start tangent—may be omitted (in WCS) |
| 13 | End tangent—may be omitted (in WCS)  DXF: *X* value; APP: 3D point |
| 23, 33 | DXF: *Y* and *Z* values of end tangent—may be omitted (in WCS) |
| 40 | Knot value (one entry per knot) |
| 41 | Weight (if not 1); with multiple group pairs, they are present if all are not 1 |
| 10 | Control points (in WCS); one entry per control point  DXF: *X* value; APP: 3D point |
| 20, 30 | DXF: *Y* and *Z* values of control points (in WCS); one entry per control point |
| 11 | Fit points (in WCS); one entry per fit point  DXF: *X* value; APP: 3D point |
| 21, 31 | DXF: *Y* and *Z* values of fit points (in WCS); one entry per fit point |

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*