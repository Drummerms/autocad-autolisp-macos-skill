# POLARMODE (System Variable)

Controls settings for polar and object snap tracking.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 0 |

The setting is stored as a bitcode using the sum of the following values:

Polar angle measurements

| 0 | Measure polar angles based on current UCS (absolute) |
| 1 | Measure polar angles from selected objects (relative) |

Object snap tracking

| 0 | Track orthogonally only |
| 2 | Use polar tracking settings in object snap tracking |

Use additional polar tracking angles

| 0 | No |
| 4 | Yes |

Acquire object snap tracking points

| 0 | Acquire automatically |
| 8 | Press SHIFT to acquire |

NOTE:In a 3D view, a tracking vector parallel to the *Z* axis of the UCS is also displayed, and the tooltip displays +Z and -Z for the angle depending on the direction along the
*Z* axis.

#### Related Concepts

* [About Polar Tracking and PolarSnap](About-Polar-Tracking-and-PolarSnap.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*