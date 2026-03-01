# GRIDDISPLAY (System Variable)

Controls the display behavior and display limits of the grid.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | Drawing |
| Initial value: | 3 |

The setting is stored as a bitcode using the sum of the following values:

| 0 | Restricts the grid to the area specified by the LIMITS command |
| 1 | Does not restrict the grid to the area specified by the LIMITS command |
| 2 | Turns on adaptive grid display, which limits the density of the grid when zoomed out |
| 4 | If the grid is set to adaptive display and when zoomed in, generates additional, more closely spaced grid lines in the same proportion as the intervals of the major grid lines |
| 8 | Changes the grid plane to follow the XY plane of the dynamic UCS. |

NOTE:Setting 4 is ignored unless setting 2 is specified.

#### Related Concepts

* [About Adjusting the Grid and Grid Snap](About-Adjusting-the-Grid-and-Grid-Snap.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*