# SHORTCUTMENU (System Variable)

Controls whether Default, Edit, and Command mode shortcut menus are available in the drawing area.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 11 |

The setting is stored as a bitcode using the sum of the following values:

| 0 | Disables all Default, Edit, and Command mode shortcut menus, restoring AutoCAD Release 14 behavior. |
| 1 | Enables Default mode shortcut menus. |
| 2 | Enables Edit mode shortcut menus. |
| 4 | Enables Command mode shortcut menus whenever a command is active. |
| 8 | Enables Command mode shortcut menus only when command options are currently available at the Command prompt. |
| 16 | Enables the display of a shortcut menu when the right button on the pointing device is held down long enough. |

NOTE:When this system variable is set to a value greater than 15, the
[SHORTCUTMENUDURATION](SHORTCUTMENUDURATION-System-Variable.md) system variable determines the length of time that the right button on the pointing device must be held down to display a
shortcut menu.

#### Related Concepts

* [About Setting Up the Drawing Area](About-Setting-Up-the-Drawing-Area.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*