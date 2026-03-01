# MAXINTERSECTIONCURVEPOINTS (System Variable)

Controls the upper limit of the number of control points or vertices that splines and polylines can include in the intersection
calculations.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 300 |

Valid range is 0 to 1000000.

If the number of control points or vertices for both objects in an intersection calculation exceeds the value of the MAXINTERSECTIONCURVEPOINTS
system variable, no intersection calculation occurs.

This improves performance when using the Intersection object snap.

Setting MAXINTERSECTIONCURVEPOINTS to 0 restores the legacy behavior, with no limit applied.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*