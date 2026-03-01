# ERRNO (System Variable)

Displays the number of the appropriate error code when an AutoLISP function call causes an error that AutoCAD detects.

(Read-only)

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Not-saved |
| Initial value: | 0 |

AutoLISP applications can inspect the current value of ERRNO with (getvar "errno").

The ERRNO system variable is not always cleared to zero. Unless it is inspected immediately after an AutoLISP function has
reported an error, the error that its value indicates may be misleading. This variable is always cleared when starting or
opening a drawing.

See the *AutoLISP Developer's Guide* for more information.

#### Related Concepts

* [About AutoLISP Applications](About-AutoLISP-Applications.md)

#### Related Information

* [Commands for Customization](Commands-for-Customization-2.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*