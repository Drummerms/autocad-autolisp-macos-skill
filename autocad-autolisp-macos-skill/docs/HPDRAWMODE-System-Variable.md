# HPDRAWMODE (System Variable)

Controls the drawing mode used when defining new boundaries to hatch or fill.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 0 or AREA |

| Value | Description |
| 0 or AREA | New boundary to be hatched or filled is defined by a closed object; circle, rectangle, or closed polyline. |
| 1 or PATH | New boundary to be hatched or filled is defined along an open or closed path. Boundary is calculated using the path's width (HPPATHWIDTH system variable) and alignment (HPPATHALIGNMENT system variable) settings. |

#### Related Concepts

* [Overview of Hatch Patterns and Fills](Overview-of-Hatch-Patterns-and-Fills.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*