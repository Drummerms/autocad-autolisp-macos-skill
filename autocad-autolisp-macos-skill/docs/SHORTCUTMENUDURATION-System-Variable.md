# SHORTCUTMENUDURATION (System Variable)

Specifies how long the right button on a pointing device must be pressed to display a shortcut menu in the drawing area.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 250 |

The value is expressed in milliseconds, and the valid range is 100 to 10,000.

If the right button is held down for the same or longer duration than the value of this system variable, a shortcut menu is
displayed.

If the right button is held down for a shorter duration, the result is the same as if you press the Enter or Return key.

NOTE:The
[SHORTCUTMENU](SHORTCUTMENU-System-Variable.md) system variable must be set to a value greater than 15 for this system variable to take effect.

#### Related Concepts

* [About Setting Up the Drawing Area](About-Setting-Up-the-Drawing-Area.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*