# RECOVERAUTO (System Variable)

Controls the display of recovery notifications before or after opening a damaged drawing file.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | Registry |
| Initial value: | 0 |

| 0 | Displays a task dialog to recover damaged files while opening a drawing that needs recovery. The task dialog interrupts any running scripts. |
| 1 | Automatically recovers the damaged files, opens the drawing, and displays a task dialog with the information of the recovered files. If a script is running, the task dialog is suppressed. |
| 2 | Automatically recovers the damaged files and opens the drawing without displaying any task dialog. The information of the recovered files is displayed at the command prompt. |

#### Related Concepts

* [About Repairing Damaged Drawing Files](About-Repairing-Damaged-Drawing-Files.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*