# UCSICON (System Variable)

Displays the UCS icon for the current viewport or layout.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 3 |

This system variable has the same name as a command. Use the SETVAR command to access this system variable.

The setting is stored as a bitcode using the sum of the following values:

| 0 | No icon is displayed |
| 1 | On; the icon is displayed in the lower-left corner of the current viewport or layout |
| 2 | Origin; if the icon is on, the icon is displayed at the UCS origin, if possible |

The setting of this system variable is viewport and layout specific.

#### Related Concepts

* [About Controlling the User Coordinate System (UCS)](About-Controlling-the-User-Coordinate-System-UCS.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*