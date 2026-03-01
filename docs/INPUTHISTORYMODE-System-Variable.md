# INPUTHISTORYMODE (System Variable)

Controls the content and location of the user input history.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | Registry |
| Initial value: | 15 |

The setting is stored as a bitcode using the sum of the following values:

| Value | Description |
| 0 | No history of recent input is displayed. |
| 1 | History of recent input is displayed at the command line or in a dynamic prompt tooltip. Access with the Up Arrow and Down Arrow keys at the Command prompt, or at an input prompt. |
| 2 | History of recent input for the current *command* is displayed in the shortcut menu under Recent Input. |
| 4 | History of recent input for all *commands* in the current session is displayed in the shortcut menu under Recent Input. |
| 8 | Markers for recent input of point locations are displayed. Use the arrow keys at the Command prompt for specifying a point location. |

#### Related Concepts

* [About Shortcut Menus](About-Shortcut-Menus.md)

#### Related Information

* [Enter System Variables on the Command Line](Enter-System-Variables-on-the-Command-Line.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*