# Ordinate Dimension Group Codes (DXF)

The following group codes apply to ordinate dimensions. In addition to the group codes described here, those listed in Common
Group Codes for Entities and Common Dimension Group Codes can also be present.

| Ordinate dimension group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbOrdinateDimension) |
| 13 | Definition point for linear and angular dimensions (in WCS)  DXF: *X* value; APP: 3D point |
| 23, 33 | DXF: *Y* and *Z* values of definition point for linear and angular dimensions (in WCS) |
| 14 | Definition point for linear and angular dimensions (in WCS)  DXF: *X* value; APP: 3D point |
| 24, 34 | DXF: *Y* and *Z* values of definition point for linear and angular dimensions (in WCS) |

The point (13,23,33) specifies the feature location and the point (14,24,34) specifies the leader endpoint. The point (11,21,31)
specifies the midpoint of the dimension text. Point (10,20,30) is placed at the origin of the UCS that is current when the
dimension is created.

![](../images/GUID-96E6F4E4-8244-48F5-BCFB-1ED30D93532B-low.png)

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [Common Dimension Group Codes (DXF)](Common-Dimension-Group-Codes-DXF.md)
* [DIMENSION (DXF)](DIMENSION-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*