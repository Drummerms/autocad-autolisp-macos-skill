# DBMOD (System Variable)

Indicates the drawing modification status.

(Read-only)

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Not-saved |
| Initial value: | 0 |

The setting is stored as a bitcode using the sum of the following values:

| 1 | Object database modified |
| 4 | Database variable modified |
| 8 | Window modified |
| 16 | View modified |
| 32 | Field modified |

The DBMOD value is reset to 0 when you save the drawing.

#### Related Concepts

* [About Saving Drawings](About-Saving-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*