# CONSTRAINTBARDISPLAY (System Variable)

Controls the display of constraint bars after you apply constraints and when you select geometrically constrained drawings.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | Registry |
| Initial value: | 3 |

| 0 | Does not display constraint bars for selected objects after applying geometric constraints  NOTE:Constraint bars will always be displayed when CONSTRAINTBAR = Showall, even if you set the value of the CONSTRAINTBARDISPLAY system variable to 0. |
| 1 | Displays constraint bars for selected objects after applying constraints |
| 2 | Temporarily displays constraint bars for the selected geometrically constrained objects |
| 3 | Bits 1 and 2 are both turned on |

#### Related Concepts

* [About Displaying and Verifying Geometric Constraints](About-Displaying-and-Verifying-Geometric-Constraints.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*