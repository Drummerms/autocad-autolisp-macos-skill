# OBSCUREDCOLOR (System Variable) (DELETE)

Specifies the color of obscured lines.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 257 |

Value 0 designates ByBlock, value 256 designates ByLayer, and value 257 designates ByEntity. Values 1-255 designate an AutoCAD
Color Index (ACI).

An obscured line is a hidden line made visible by changing its color and linetype. OBSCUREDCOLOR is available only in 2D views.
In 3D views, the [VSOBSCUREDCOLOR](VSOBSCUREDCOLOR-System-Variable.md) system variable is used.

The OBSCUREDCOLOR setting is visible only if the [OBSCUREDLTYPE](OBSCUREDLTYPE-System-Variable.md) system variable is turned on by setting it to a value other than 0.

#### Related Concepts

* [About Controlling the Display of Edges](About-Controlling-the-Display-of-Edges.md)
* [About Hiding Lines in 3D Objects](About-Hiding-Lines-in-3D-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*