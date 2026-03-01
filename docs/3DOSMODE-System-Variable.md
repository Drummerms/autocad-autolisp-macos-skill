# 3DOSMODE (System Variable)

Controls the settings for the 3D object snaps.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 11 |

Controls which 3D object snaps are enabled. The setting is stored as a bitcode using the sum of the following values:

| Value | Description | Shortcut Keys |
| 0 | Enables all 3D object snaps |  |
| 1 | Disables all 3D object snaps | ZNON |
| 2 | Snaps to a vertex or a control vertex | ZVER |
| 4 | Snaps to the midpoint on a face edge | ZMID |
| 8 | Snaps to the center of a face | ZCEN |
| 16 | Snaps to a spline or surface knot | ZKNO |
| 32 | Snaps to a perpendicular face (planar faces only) | ZPER |
| 64 | Snaps to an object nearest to a face | ZNEA |
| 126 | Turns on all 3D object snaps |  |

To specify more than one object snap, enter the sum or their values. For example, entering 6 specifies the vertex (2) and
midpoint (4) object snaps. Entering 126 turns on all 3D object snaps.

#### Related Concepts

* [About Using Object Snaps in 3D](About-Using-Object-Snaps-in-3D.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*