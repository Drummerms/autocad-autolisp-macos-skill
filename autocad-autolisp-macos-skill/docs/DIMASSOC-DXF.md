# DIMASSOC (DXF)

The following group codes are used by DIMASSOC objects.

| DIMASSOC group codes | |
| Group code | Description |
| 0 | Object name (DIMASSOC) |
| 5 | Handle |
| 102 | Persistent reactors group; always “{ACAD\_REACTORS}” |
| 330 | Soft-pointer ID |
| 100 | Subclass marker (AcDbDimAssoc) |
| 330 | ID of dimension object |
| 90 | Associativity flag  1 = First point reference  2 = Second point reference  4 = Third point reference  8 = Fourth point reference |
| 70 | Trans-space flag (true/false) |
| 71 | Rotated Dimension type (parallel, perpendicular) |
| 1 | Class name (AcDbOsnapPointRef) |
| 72 | Object Osnap type  0 = None  1 = Endpoint  2 = Midpoint  3 = Center  4 = Node  5 = Quadrant  6 = Intersection  7 = Insertion  8 = Perpendicular  9 = Tangent  10 = Nearest  11 = Apparent intersection  12 = Parallel  13 = Start point |
| 331 | ID of main object (geometry) |
| 73 | SubentType of main object (edge, face) |
| 91 | GsMarker of main object (index) |
| 301 | Handle (string) of Xref object |
| 40 | Geometry parameter for Near Osnap |
| 10 | Osnap point in WCS; X value |
| 20 | Osnap point in WCS; Y value |
| 30 | Osnap point in WCS; Z value |
| 332 | ID of intersection object (geometry) |
| 74 | SubentType of intersction object (edge/face) |
| 92 | GsMarker of intersection object (index) |
| 302 | Handle (string) of intersection Xref object |
| 75 | hasLastPointRef flag (true/false) |

DIMASSOC objects implement associative dimensions by specifying an association between a dimension object and drawing geometry
objects. An associative dimension is a dimension that will automatically update when the associated geometry is modified.

#### Related References

* [Common Group Codes for Objects (DXF)](Common-Group-Codes-for-Objects-DXF.md)
* [About the DXF OBJECTS Section](About-the-DXF-OBJECTS-Section.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*