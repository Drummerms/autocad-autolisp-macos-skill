# SORTENTS (System Variable)

Controls object sorting in support of draw order for several operations.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 127 |

The setting is stored as a bitcode using the sum of the following values:

| 0 | Turns off all object sorting |
| 1 | Sorts for object selection |
| 2 | Sorts for object snaps |
| 4 | Obsolete, has no effect |
| 8 | Obsolete, has no effect |
| 16 | Sorts for REGEN commands |
| 32 | Sorts for plotting |
| 64 | Obsolete, has no effect |

#### Related Concepts

* [To turn on or off the display of solid fills](To-turn-on-or-off-the-display-of-solid-fills.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*