# DYNDIGRIP (System Variable)

Controls which dynamic dimensions are displayed during grip stretch editing.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | Registry |
| Initial value: | 31 |

The DYNDIVIS system variable must be set to 2, which displays all dynamic dimensions.

The setting is stored as a bitcode using the sum of the following values:

| 0 | None |
| 1 | Resulting dimension |
| 2 | Length change dimension |
| 4 | Absolute angle dimension |
| 8 | Angle change dimension |
| 16 | Arc radius dimension |

The  [DYNMODE](DYNMODE-System-Variable.md) system variable turns Dynamic Input features on and off.

#### Related Concepts

* [About Using Dynamic Input Tooltips](About-Using-Dynamic-Input-Tooltips.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*