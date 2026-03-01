# SPATIAL\_FILTER (DXF)

The following group codes are used by SPATIAL\_FILTER objects.

| SPATIAL\_FILTER group codes | |
| Group code | Description |
| 0 | Object name (SPATIAL\_FILTER) |
| 5 | Handle |
| 102 | Start of persistent reactors group; always “{ACAD\_REACTORS” |
| 330 | Soft-pointer ID/handle to owner dictionary (SPATIAL) |
| 102 | End of persistent reactors group, always “}” |
| 100 | Subclass marker (AcDbFilter) |
| 100 | Subclass marker (AcDbSpatialFilter) |
| 70 | Number of points on the clip boundary  2 = Rectangular clip boundary (lower-left and upper-right)  greater than 2 = Polyline clip boundary |
| 10 | Clip boundary definition point (in OCS) (always 2 or more) based on an xref scale of 1  DXF: *X* value; APP: 2D point |
| 20 | DXF: *Y* value of boundary definition point (always 2 or more) |
| 210 | Normal to the plane containing the clip boundary  DXF: *X* value; APP: 3D vector |
| 220, 230 | DXF: *Y* and *Z* values of extrusion direction |
| 11 | Origin used to define the local coordinate system of the clip boundary  DXF: *X* value; APP: 3D point |
| 21, 31 | Origin used to define the local coordinate system of the clip boundary  DXF: *Y* and *Z* values |
| 71 | Clip boundary display enabled flag  0 = Disabled; 1 = Enabled |
| 72 | Front clipping plane flag; 0 = No; 1 = Yes |
| 40 | Front clipping plane distance (if code 72 = 1) |
| 73 | Back clipping plane flag; 0 = No; 1 = Yes |
| 41 | Back clipping plane distance (if code 73 = 1) |
| 40 | 4x3 transformation matrix written out in column major order. This matrix is the inverse of the original block reference (insert entity) transformation. The original block reference transformation is the one that is applied to all entities in the block when the block reference is regenerated (always 12 entries) |
| 40 | 4x3 transformation matrix written out in column major order. This matrix transforms points into the coordinate system of the clip boundary (12 entries) |

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*