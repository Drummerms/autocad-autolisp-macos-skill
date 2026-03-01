# VERTEX (DXF)

The following group codes apply to vertex entities.

| Vertex group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbVertex) |
| 100 | Subclass marker (AcDb2dVertex or AcDb3dPolylineVertex) |
| 10 | Location point (in OCS when 2D, and WCS when 3D)  DXF: *X* value; APP: 3D point |
| 20, 30 | DXF: *Y* and *Z* values of location point (in OCS when 2D, and WCS when 3D) |
| 40 | Starting width (optional; default is 0) |
| 41 | Ending width (optional; default is 0) |
| 42 | Bulge (optional; default is 0). The bulge is the tangent of one fourth the included angle for an arc segment, made negative if the arc goes clockwise from the start point to the endpoint. A bulge of 0 indicates a straight segment, and a bulge of 1 is a semicircle |
| 70 | Vertex flags:  1 = Extra vertex created by curve-fitting  2 = Curve-fit tangent defined for this vertex. A curve-fit tangent direction of 0 may be omitted from DXF output but is significant if this bit is set  4 = Not used  8 = Spline vertex created by spline-fitting  16 = Spline frame control point  32 = 3D polyline vertex  64 = 3D polygon mesh  128 = Polyface mesh vertex |
| 50 | Curve fit tangent direction |
| 71 | Polyface mesh vertex index (optional; present only if nonzero) |
| 72 | Polyface mesh vertex index (optional; present only if nonzero) |
| 73 | Polyface mesh vertex index (optional; present only if nonzero) |
| 74 | Polyface mesh vertex index (optional; present only if nonzero) |
| 91 | Vertex identifier |

Every vertex that is part of a polyface mesh has its vertex flag 128 bit set. If the entity supplies the coordinate of a vertex
of the mesh, its 64 bit is set as well, and the 10, 20, 30 groups give the vertex coordinate. The vertex index values are
determined by the order in which the vertex entities appear within the polyline, with the first being numbered 1.

If the vertex defines a face of the mesh, its vertex flags group has the 128 bit set but not the 64 bit. In this case, the
10, 20, 30 (location) groups of the face entity are irrelevant and are always written as 0 in a DXF file. The vertex indexes
that define the mesh are given by 71, 72, 73, and 74 group codes, the values of which specify one of the previously defined
vertexes by index. If the index is negative, the edge that begins with that vertex is invisible. The first 0 vertex marks
the end of the vertices of the face.

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*