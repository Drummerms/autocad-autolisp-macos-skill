# Linear and Rotated Dimension Group Codes (DXF)

The following group codes apply to linear and rotated dimensions (note that linear and rotated dimensions are part of the
AcDbAlignedDimension subclass). In addition to the group codes described here, those listed in Common Group Codes for Entities
and Common Dimension Group Codes can also be present.

| Linear and rotated dimension group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbAlignedDimension) |
| 12 | Insertion point for clones of a dimension—Baseline and Continue (in OCS)  DXF: *X* value; APP: 3D point |
| 22, 32 | DXF: *Y* and *Z* values of insertion point for clones of a dimension—Baseline and Continue (in OCS) |
| 13 | Definition point for linear and angular dimensions (in WCS)  DXF: *X* value; APP: 3D point |
| 23, 33 | DXF: *Y* and *Z* values of definition point for linear and angular dimensions (in WCS) |
| 14 | Definition point for linear and angular dimensions (in WCS)  DXF: *X* value; APP: 3D point |
| 24, 34 | DXF: *Y* and *Z* values of definition point for linear and angular dimensions (in WCS) |
| 50 | Angle of rotated, horizontal, or vertical dimensions |
| 52 | Linear dimension types with an oblique angle have an optional group code 52. When added to the rotation angle of the linear dimension (group code 50), it gives the angle of the extension lines |
| 100 | Subclass marker (AcDbRotatedDimension) |

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [Common Dimension Group Codes (DXF)](Common-Dimension-Group-Codes-DXF.md)
* [DIMENSION (DXF)](DIMENSION-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*