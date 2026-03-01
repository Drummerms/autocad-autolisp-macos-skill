# XCLIPFRAME (System Variable)

Determines whether xref clipping boundaries are visible or plotted in the current drawing.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 2 |

The [FRAME](FRAME-System-Variable.md) system variable overrides the XCLIPFRAME setting.Use the XCLIPFRAME system variable after the FRAME system variable to reset
the clipped xref frame settings

| 0 | The frame is not visible and it is not plotted.  The frame temporarily reappears during selection preview or object selection. |
| 1 | The clipped xref frame is displayed and plotted |
| 2 | The clipped xref frame is displayed but not plotted |

#### Related Information

* [About Updating Referenced Drawing Attachments](About-Updating-Referenced-Drawing-Attachments.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*