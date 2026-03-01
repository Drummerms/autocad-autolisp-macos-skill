# PLINEGCENMAX (System Variable)

Sets the maximum number of segments that a polyline can have for the application to calculate the geometric center.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 50000 |

Valid values are from 0 to 10,000,000. When the number of segments in a polyline exceeds the PLINEGCENMAX value, the application
stops calculating the center point and does not display the geometric center object snap.

To restore the legacy behavior, where the application keeps calculating the center point regardless of the number of polyline
segments, set PLINEGCENMAX to 0.

#### Related Concepts

* [About Using Object Snaps](About-Using-Object-Snaps.md)
* [About Polylines](About-Polylines.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*