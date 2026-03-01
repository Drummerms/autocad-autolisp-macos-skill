# MLINE (DXF)

The following group codes apply to mline entities.

| Mline group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbMline) |
| 2 | String of up to 32 characters. The name of the style used for this mline. An entry for this style must exist in the MLINESTYLE dictionary.  Do not modify this field without also updating the associated entry in the MLINESTYLE dictionary |
| 340 | Pointer-handle/ID of MLINESTYLE object |
| 40 | Scale factor |
| 70 | Justification:  0 = Top  1 = Zero  2 = Bottom |
| 71 | Flags (bit-coded values):  1 = Has at least one vertex (code 72 is greater than 0)  2 = Closed  4 = Suppress start caps  8 = Suppress end caps |
| 72 | Number of vertices |
| 73 | Number of elements in MLINESTYLE definition |
| 10 | Start point (in WCS)  DXF: *X* value; APP: 3D point |
| 20, 30 | DXF: *Y* and *Z* values of start point (in WCS) |
| 210 | Extrusion direction (optional; default = 0, 0, 1)  DXF: *X* value; APP: 3D vector |
| 220, 230 | DXF: *Y* and *Z* values of extrusion direction (optional) |
| 11 | Vertex coordinates (multiple entries; one entry for each vertex) DXF: *X* value; APP: 3D point |
| 21, 31 | DXF: *Y* and *Z* values of vertex coordinates |
| 12 | Direction vector of segment starting at this vertex (multiple entries; one for each vertex)  DXF: *X* value; APP: 3D vector |
| 22, 32 | DXF: *Y* and *Z* values of direction vector of segment starting at this vertex |
| 13 | Direction vector of miter at this vertex (multiple entries: one for each vertex)  DXF: *X* value; APP: 3D vector |
| 23, 33 | DXF: *Y* and *Z* values of direction vector of miter |
| 74 | Number of parameters for this element (repeats for each element in segment) |
| 41 | Element parameters (repeats based on previous code 74) |
| 75 | Number of area fill parameters for this element (repeats for each element in segment) |
| 42 | Area fill parameters (repeats based on previous code 75) |

The group code 41 parameterization is a list of real values, one real per group code 41. The list may contain zero or more
items. The first group code 41 value is the distance from the segment vertex along the miter vector to the point where the
line element's path intersects the miter vector. The next group code 41 value is the distance along the line element's path
from the point defined by the first group 41 to the actual start of the line element. The next is the distance from the start
of the line element to the first break (or cut) in the line element. The successive group code 41 values continue to list
the start and stop points of the line element in this segment of the mline. Linetypes do not affect group 41 lists.

The group code 42 parameterization is also a list of real values. Similar to the 41 parameterization, it describes the parameterization
of the fill area for this mline segment. The values are interpreted identically to the 41 parameters and when taken as a whole
for all line elements in the mline segment, they define the boundary of the fill area for the mline segment.

A common example of the use of the group code 42 mechanism is when an unfilled mline crosses over a filled mline and mledit
is used to cause the filled mline to appear unfilled in the crossing area. This would result in two group 42s for each line
element in the affected mline segment; one for the fill stop and one for the fill start.

The 2 group codes in mline entities and mlinestyle objects are redundant fields. These groups should not be modified under
any circumstances, although it is safe to read them and use their values. The correct fields to modify are as follows:

Mline
:   The 340 group in the same object, which indicates the proper MLINESTYLE object.

Mlinestyle
:   The 3 group value in the MLINESTYLE dictionary, which precedes the 350 group that has the handle or entity name of the current
    mlinestyle.

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [About the DXF ENTITIES Section](About-the-DXF-ENTITIES-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*