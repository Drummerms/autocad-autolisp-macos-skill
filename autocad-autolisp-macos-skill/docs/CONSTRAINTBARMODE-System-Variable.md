# CONSTRAINTBARMODE (System Variable)

Controls the display of geometrical constraints on constraint bars.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | Registry |
| Initial value: | 4095 |

| 1 | Horizontal |
| 2 | Vertical |
| 4 | Perpendicular |
| 8 | Parallel |
| 16 | Tangent |
| 32 | Smooth |
| 64 | Coincident |
| 128 | Concentric |
| 256 | Colinear |
| 512 | Symmetric |
| 1024 | Equal |
| 2048 | Fix |

For example, set CONSTRAINTBARMODE to 12 (8+4) to display parallel and perpendicular constraints on the constraint bars.

Set CONSTRAINTBARMODE to 4095 to display constraint bars for all constraint types.

#### Related Concepts

* [About Displaying and Verifying Geometric Constraints](About-Displaying-and-Verifying-Geometric-Constraints.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*