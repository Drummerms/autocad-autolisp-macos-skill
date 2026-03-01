# LEADER (DXF)

The following group codes apply to leader entities.

| Leader group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbLeader) |
| 3 | Dimension style name |
| 71 | Arrowhead flag: 0 = Disabled; 1 = Enabled |
| 72 | Leader path type: 0 = Straight line segments; 1 = Spline |
| 73 | Leader creation flag (default = 3):  0 = Created with text annotation  1 = Created with tolerance annotation  2 = Created with block reference annotation  3 = Created without any annotation |
| 74 | Hookline direction flag:  0 = Hookline (or end of tangent for a splined leader) is the opposite direction from the horizontal vector  1 = Hookline (or end of tangent for a splined leader) is the same direction as horizontal vector (see code 75) |
| 75 | Hookline flag:  0 = No hookline  1 = Has a hookline |
| 40 | Text annotation height |
| 41 | Text annotation width |
| 76 | Number of vertices in leader (ignored for OPEN) |
| 10 | Vertex coordinates (one entry for each vertex)  DXF: *X* value; APP: 3D point |
| 20, 30 | DXF: *Y* and *Z*values of vertex coordinates |
| 77 | Color to use if leader's DIMCLRD = BYBLOCK |
| 340 | Hard reference to associated annotation (mtext, tolerance, or insert entity) |
| 210 | Normal vector  DXF: *X* value; APP: 3D vector |
| 220, 230 | DXF: *Y* and *Z* values of normal vector |
| 211 | “Horizontal” direction for leader  DXF: *X* value; APP: 3D vector |
| 221, 231 | DXF: *Y* and *Z* values of “horizontal” direction for leader |
| 212 | Offset of last leader vertex from block reference insertion point  DXF: *X* value; APP: 3D vector |
| 222, 232 | DXF: *Y* and *Z* values of offset |
| 213 | Offset of last leader vertex from annotation placement point  DXF: *X* value; APP: 3D vector |
| 223, 233 | DXF: *Y* and *Z* values of offset |

Xdata belonging to the application ID
"ACAD" follows a leader entity if any dimension overrides have been applied to this entity. See Dimension Style Overrides.

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [Dimension Style Overrides (DXF)](Dimension-Style-Overrides-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*