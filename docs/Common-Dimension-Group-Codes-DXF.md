# Common Dimension Group Codes (DXF)

The following group codes apply to all dimension entity types.

| Common dimension group codes | |
| Group code | Description |
| 100 | Subclass marker (AcDbDimension) |
| 280 | Version number:  0 = 2010 |
| 2 | Name of the block that contains the entities that make up the dimension picture |
| 10 | Definition point (in WCS)  DXF: *X* value; APP: 3D point |
| 20, 30 | DXF: *Y* and *Z* values of definition point (in WCS) |
| 11 | Middle point of dimension text (in OCS)  DXF: *X* value; APP: 3D point |
| 21, 31 | DXF: *Y* and *Z* values of middle point of dimension text (in OCS) |
| 70 | Dimension type:  Values 0-6 are integer values that represent the dimension type. Values 32, 64, and 128 are bit values, which are added to the integer values (value 32 is always set in R13 and later releases)  0 = Rotated, horizontal, or vertical  1 = Aligned  2 = Angular  3 = Diameter  4 = Radius  5 = Angular 3-point  6 = Ordinate  32 = Indicates that the block reference (group code 2) is referenced by this dimension only  64 = Ordinate type. This is a bit value (bit 7) used only with integer value 6. If set, ordinate is X-type; if not set, ordinate is Y-type  128 = This is a bit value (bit 8) added to the other group 70 values if the dimension text has been positioned at a user-defined location rather than at the default location |
| 71 | Attachment point:  1 = Top left  2 = Top center  3 = Top right  4 = Middle left  5 = Middle center  6 = Middle right  7 = Bottom left  8 = Bottom center  9 = Bottom right |
| 72 | Dimension text line-spacing style (optional):  1 (or missing) = At least (taller characters will override)  2 = Exact (taller characters will not override) |
| 41 | Dimension text-line spacing factor (optional):  Percentage of default (3-on-5) line spacing to be applied. Valid values range from 0.25 to 4.00 |
| 42 | Actual measurement (optional; read-only value) |
| 1 | Dimension text explicitly entered by the user. Optional; default is the measurement. If null or “<>”, the dimension measurement is drawn as the text, if ““ (one blank space), the text is suppressed. Anything else is drawn as the text |
| 53 | The optional group code 53 is the rotation angle of the dimension text away from its default orientation (the direction of the dimension line) (optional) |
| 51 | All dimension types have an optional 51 group code, which indicates the horizontal direction for the dimension entity. The dimension entity determines the orientation of dimension text and lines for horizontal, vertical, and rotated linear dimensions  This group value is the negative of the angle between the OCS *X* axis and the UCS *X* axis. It is always in the *XY* plane of the OCS |
| 210 | Extrusion direction (optional; default = 0, 0, 1)  DXF: *X* value; APP: 3D vector |
| 220, 230 | DXF: *Y* and *Z* values of extrusion direction (optional) |
| 3 | Dimension style name |

Xdata belonging to the application ID
"ACAD" follows a dimension entity if any dimension overrides have been applied to this entity.

For all dimension types, the following group codes represent 3D WCS points:

* (10, 20, 30)
* (13, 23, 33)
* (14, 24, 34)
* (15, 25, 35)

For all dimension types, the following group codes represent 3D OCS points:

* (11, 21, 31)
* (12, 22, 32)
* (16, 26, 36)

#### Related References

* [Common Group Codes for Entities (DXF)](Common-Group-Codes-for-Entities-DXF.md)
* [Dimension Style Overrides (DXF)](Dimension-Style-Overrides-DXF.md)
* [DIMENSION (DXF)](DIMENSION-DXF.md)

#### Related Concepts

* [About DXF Formatting Conventions](About-DXF-Formatting-Conventions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*