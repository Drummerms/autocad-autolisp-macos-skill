# OFFSETGAPTYPE (System Variable)

Controls how potential gaps between segments are treated when polylines are offset.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 0 |

| 0 | Extends line segments to their projected intersections. |
| 1 | Fillets line segments at their projected intersections. The radius of each arc segment is equal to the offset distance. |
| 2 | Chamfers line segments at their projected intersections. The perpendicular distance from each chamfer to its corresponding vertex on the original object is equal to the offset distance. |

#### Related Concepts

* [About Offsetting Objects](About-Offsetting-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*