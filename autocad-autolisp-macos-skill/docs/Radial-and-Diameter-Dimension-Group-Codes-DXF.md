# Radial and Diameter Dimension Group Codes (DXF)

The following group codes apply to radial and diameter dimensions. In addition to the group codes described here, those listed
in Common Group Codes for Entities and Common Dimension Group Codes can also be present.

| Radial and diameter dimension group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbRadialDimension or AcDbDiametricDimension) |
| 15 | Definition point for diameter, radius, and angular dimensions (in WCS)  DXF: *X* value; APP: 3D point |
| 25, 35 | DXF: *Y* and *Z* values of definition point for diameter, radius, and angular dimensions (in WCS) |
| 40 | Leader length for radius and diameter dimensions |

The point (15,25,35) specifies the first point of the dimension line on the circle/arc and the point (10,20,30) specifies
the point opposite the first point. The point (11,21,31) specifies the midpoint of the dimension text.

![](../images/GUID-E2976076-C4AA-4F2E-8D3D-13C3BA40FA1E-low.png)

The point (15,25,35) specifies the first point of the dimension line on the circle/arc and the point (10,20,30) specifies
the center of the circle/arc. The point (11,21,31) specifies the midpoint of the dimension text.

![](../images/GUID-8FD0C3DF-3AF6-4E10-B4EB-3CAA72304D3B-low.png)

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [Common Dimension Group Codes (DXF)](Common-Dimension-Group-Codes-DXF.md)
* [DIMENSION (DXF)](DIMENSION-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*