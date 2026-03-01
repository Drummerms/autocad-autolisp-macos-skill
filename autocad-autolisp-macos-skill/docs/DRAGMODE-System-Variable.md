# DRAGMODE (System Variable)

Controls the display of objects being dragged.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Registry |
| Initial value: | 2 |

This system variable has the same name as a command. Use the SETVAR command to access this system variable.

When it is on, the image of an object is displayed as you drag it to another location. With some computer configurations,
dragging can be time-consuming. Use DRAGMODE to suppress dragging.

| 0 | Does not display an outline of the object as you drag it |
| 1 | Displays the outline of the object as you drag it only if you enter *drag* at the Command prompt after selecting the object to drag |
| 2 | Auto; always displays an outline of the object as you drag it |

#### Related Concepts

* [About Setting Up the Drawing Area](About-Setting-Up-the-Drawing-Area.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*