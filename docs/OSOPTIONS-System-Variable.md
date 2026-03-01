# OSOPTIONS (System Variable)

Controls whether objects snaps are suppressed on hatch objects, geometry with negative Z values when using dynamic UCS, or
dimension extension lines.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | Registry |
| Initial value: | 7 |

The setting is stored as a bitcode using the sum of the following values:

| Value | Description |
| 0 | Object snaps operate on patterned hatch objects, on geometry with negative Z values when using a dynamic UCS, and on endpoints of dimension extension lines.  A REGEN is *required* for snapping to hatch intersections after changing to this setting.  A REGEN is *recommended* for performance reasons after changing from this setting to a value that includes 1. |
| 1 | Object snaps ignore hatch objects. |
| 2 | Object snaps ignore geometry with negative Z values during use of a dynamic UCS. (Not available in AutoCAD LT.) |
| 4 | Object snaps ignore endpoints of dimension extension lines. |

#### Related Concepts

* [About Using Object Snaps](About-Using-Object-Snaps.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*