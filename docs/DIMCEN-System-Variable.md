# DIMCEN (System Variable)

Controls drawing of circle or arc center marks and centerlines by the DIMCENTER, DIMDIAMETER, and DIMRADIUS commands.

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | Drawing |
| Initial value: | 0.0900 (imperial) or 2.5000 (metric) |

For DIMDIAMETER and DIMRADIUS, the center mark is drawn only if you place the dimension line outside the circle or arc.

| 0 | No center marks or lines are drawn |
| <0 | Centerlines are drawn |
| >0 | Center marks are drawn |

The absolute value specifies the size of the center mark or centerline.

The size of the centerline is the length of the centerline segment that extends outside the circle or arc. It is also the
size of the gap between the center mark and the start of the centerline.

The size of the center mark is the distance from the center of the circle or arc to the end of the center mark.

#### Related Concepts

* [About Creating Radial Dimensions](About-Creating-Radial-Dimensions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*