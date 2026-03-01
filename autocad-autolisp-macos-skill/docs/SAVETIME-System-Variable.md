# SAVETIME (System Variable)

Sets the automatic save interval, in minutes.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 10 |

| 0 | Turns off automatic saving. |
| >0 | Saves the drawing at intervals specified by the nonzero integer automatically |

The value of SAVETIME is an integer between 0 and 600.

The SAVETIME timer starts as soon as you make a change to a drawing. It is reset and restarted by a manual [QSAVE](QSAVE-Command.md), [SAVE](SAVE-Command.md), or [SAVEAS](SAVEAS-Command.md). The current drawing is saved to the path specified by the  [SAVEFILEPATH](SAVEFILEPATH-System-Variable.md) system variable. The file name is stored in the  [SAVEFILE](SAVEFILE-System-Variable.md) system variable.

#### Related Concepts

* [About Saving Drawings](About-Saving-Drawings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*