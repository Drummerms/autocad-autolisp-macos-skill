# VSOBSCUREDCOLOR (System Variable)

Specifies the color of obscured (hidden) lines in the visual style applied to the current viewport.

|  |  |
| --- | --- |
| Type: | String |
| Saved in: | Drawing |
| Initial value: | BYENTITY |

Valid values include ByLayer (256), ByBlock (0), ByEntity (257), and any AutoCAD Color Index (ACI) color (an integer from
1 to 255).

You can also specify a true color or a color book color. Valid values for true colors are a string of integers each from 1
to 255 separated by commas and preceded by RGB. The True Color setting is entered as follows:

RGB:000,000,000

NOTE:Existing visual styles are not changed when you enter a new value for this system variable. Any new value entered for this
system variable temporarily creates an unsaved new visual style.

#### Related Concepts

* [Shade and Color Faces](Shade-and-Color-Faces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*