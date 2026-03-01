# Boundary Path Data (DXF)

The boundary of each hatch object is defined by a path (or
*loop*) that consists of one or more segments. Path segment data varies depending on the entity type (or types) that make up the
path. Each path segment is defined by its own set of group codes.

| Hatch boundary path data group codes | |
| Group code | Description |
| 92 | Boundary path type flag (bit coded):  0 = Default  1 = External  2 = Polyline  4 = Derived  8 = Textbox  16 = Outermost |
| *varies* | Polyline boundary type data (only if boundary = polyline). See Polyline boundary data table below |
| 93 | Number of edges in this boundary path (only if boundary is not a polyline) |
| 72 | Edge type (only if boundary is not a polyline):  1 = Line  2 = Circular arc  3 = Elliptic arc  4 = Spline |
| *varies* | Edge type data (only if boundary is not a polyline). See appropriate Edge data table below |
| 97 | Number of source boundary objects |
| 330 | Reference to source boundary objects (multiple entries) |

| Polyline boundary data group codes | |
| Group code | Description |
| 72 | Has bulge flag |
| 73 | Is closed flag |
| 93 | Number of polyline vertices |
| 10 | Vertex location (in OCS)  DXF: *X* value; APP: 2D point (multiple entries) |
| 20 | DXF: *Y* value of vertex location (in OCS) (multiple entries) |
| 42 | Bulge (optional, default = 0) |

| Line edge data group codes | |
| Group code | Description |
| 10 | Start point (in OCS)  DXF: *X* value; APP: 2D point |
| 20 | DXF: *Y* value of start point (in OCS) |
| 11 | Endpoint (in OCS)  DXF: *X* value; APP: 2D point |
| 21 | DXF: *Y* value of endpoint (in OCS) |

| Arc edge data group codes | |
| Group code | Description |
| 10 | Center point (in OCS)  DXF: *X* value; APP: 2D point |
| 20 | DXF: *Y* value of center point (in OCS) |
| 40 | Radius |
| 50 | Start angle |
| 51 | End angle |
| 73 | Is counterclockwise flag |

| Ellipse edge data group codes | |
| Group code | Description |
| 10 | Center point (in OCS)  DXF: *X* value; APP: 2D point |
| 20 | DXF: *Y* value of center point (in OCS) |
| 11 | Endpoint of major axis relative to center point (in OCS)  DXF: *X* value; APP: 2D point |
| 21 | DXF: *Y* value of endpoint of major axis (in OCS) |
| 40 | Length of minor axis (percentage of major axis length) |
| 50 | Start angle |
| 51 | End angle |
| 73 | Is counterclockwise flag |

| Spline edge data group codes | |
| Group code | Description |
| 94 | Degree |
| 73 | Rational |
| 74 | Periodic |
| 95 | Number of knots |
| 96 | Number of control points |
| 40 | Knot values (multiple entries) |
| 10 | Control point (in OCS)  DXF: *X* value; APP: 2D point |
| 20 | DXF: *Y* value of control point (in OCS) |
| 42 | Weights (optional, default = 1) |
| 97 | Number of fit data |
| 11 | Fit datum (in OCS)  DXF: X value; APP: 2D point |
| 21 | DXF: Y value of fit datum (in OCS) |
| 12 | Start tangent  DXF: X value; APP: 2D vector |
| 22 | DXF: Y value of start tangent (in OCS) |
| 13 | End tangent  DXF: X value; APP: 2D vector |
| 23 | DXF: Y value of end tangent (in OCS) |

#### Related References

* [HATCH (DXF)](HATCH-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*