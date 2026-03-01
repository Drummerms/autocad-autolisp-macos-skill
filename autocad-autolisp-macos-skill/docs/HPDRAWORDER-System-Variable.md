# HPDRAWORDER (System Variable)

Controls the draw order of hatches and fills.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Not-saved |
| Initial value: | 3 |

Controls whether hatch and fill objects are displayed in front or behind all other objects, or in front or behind their associated
boundaries.

| 0 | None. The hatch or fill is not assigned a draw order. |
| 1 | Send to back. The hatch or fill is sent to the back of all other objects. |
| 2 | Bring to front. The hatch or fill is brought to the front of all other objects. |
| 3 | Send behind boundary. The hatch or fill is sent behind the hatch’s boundary objects. |
| 4 | Bring in front of boundary. The hatch or fill is brought in front of the hatch’s boundary objects. |

#### Related Concepts

* [Overview of Hatch Patterns and Fills](Overview-of-Hatch-Patterns-and-Fills.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*