# LTGAPSELECTION (System Variable)

Controls whether you can select or snap to the gaps on objects defined with non-continuous linetype.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 1 |

| Value | Description |
| 0 | Prevents selection or snapping within gaps (legacy behavior) |
| 1 | Allows selection or snapping within gaps  When on, the gaps are recognized by object snaps which allow you to snap to the objects even when picking on a blank space. |

NOTE: Hardware acceleration must be turned on for LTGAPSELECTION to take effect.

#### Related References

* [3DCONFIG, -3DCONFIG, GRAPHICSCONFIG, -GRAPHICSCONFIG (Command)](3DCONFIG,-3DCONFIG,-GRAPHICSCONFIG,-GRAPHICSCONFIG-Command.md)

#### Related Concepts

* [Performance Tuning](Performance-Tuning.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*