# VSEDGECOLOR (System Variable)

Sets the color of edges in the visual style in the current viewport.

|  |  |
| --- | --- |
| Type: | String |
| Saved in: | Drawing |
| Initial value: | BYENTITY |

Value 0 designates ByBlock, value 256 designates ByLayer, and value 257 designates ByEntity. Values 1-255 designate an AutoCAD
Color Index (ACI) color. True Colors and Color Book colors are also available.

Valid values for True Colors are a string of integers each from 0 to 255 separated by commas and preceded by RGB. The True
Color setting is entered as follows:

RGB:000,000,000

If you have a color book installed, you can specify any colors that are defined in the book.

NOTE:Existing visual styles are not changed when you enter a new value for this system variable. Any new value entered for this
system variable temporarily creates an unsaved new visual style.

#### Related Concepts

* [About Controlling the Display of Edges](About-Controlling-the-Display-of-Edges.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*