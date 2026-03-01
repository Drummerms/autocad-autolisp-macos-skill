# CMDACTIVE (System Variable)

Indicates whether an ordinary command, transparent command, script, or dialog box is active.

(Read-only)

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Not-saved |
| Initial value: | Varies |

The setting is stored as a bitcode using the sum of the following values:

| 0 | No active command |
| 1 | Ordinary command is active |
| 2 | Transparent command is active |
| 4 | Script is active |
| 8 | Dialog box is active |
| 16 | Not used |
| 32 | AutoLISP is active (only visible to an ObjectARX-defined command) |
| 64 | ObjectARX command is active |

#### Related Concepts

* [Switch Between Dialog Boxes and the Command Line](Switch-Between-Dialog-Boxes-and-the-Command-Line.md)
* [About Entering Commands on the Command Line](About-Entering-Commands-on-the-Command-Line.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*