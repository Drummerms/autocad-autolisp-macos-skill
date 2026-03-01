# UNDOCTL (System Variable)

Indicates the state of the Auto, Control, and Group options of the UNDO command.

(Read-only)

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Not-saved |
| Initial value: | 53 |

The setting is stored as a bitcode using the sum of the following values:

| 0 | UNDO is turned off |
| 1 | UNDO is turned on |
| 2 | Only one command can be undone |
| 4 | Auto is turned on |
| 8 | A group is currently active |
| 16 | Zoom and pan operations are grouped as a single action |
| 32 | Layer property operations are grouped as a single action |

#### Related Concepts

* [About Correcting Mistakes](About-Correcting-Mistakes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*