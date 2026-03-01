# VSINTERSECTIONCOLOR (System Variable)

Specifies the color of intersection polylines in the visual style applied to the current viewport.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 7 |

The initial value is 7, which is a special value that inverts the color (black or white) based on the background color.

Value 0 designates ByBlock, value 256 designates ByLayer, and value 257 designates ByEntity. Values 1-255 designate an AutoCAD
Color Index (ACI) color. True Colors and Color Book colors are also available.

NOTE: [INTERSECTIONCOLOR](INTERSECTIONCOLOR-System-Variable.md) controls the color of intersection polylines when the visual style is set to 2D Wireframe.

NOTE: Existing visual styles are not changed when you enter a new value for this system variable. Any new value entered for this
system variable temporarily creates an unsaved new visual style.

#### Related Concepts

* [About Controlling the Display of Edges](About-Controlling-the-Display-of-Edges.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*