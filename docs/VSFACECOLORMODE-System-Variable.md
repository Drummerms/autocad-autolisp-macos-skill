# VSFACECOLORMODE (System Variable)

Controls how the color of faces is calculated.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 0 |

| 0 | Normal: Does not apply a face color modifier |
| 1 | Monochrome: Displays all faces in the color that is specified in the [VSMONOCOLOR](VSMONOCOLOR-System-Variable.md) system variable |
| 2 | Tint: Uses the color that is specified in the [VSMONOCOLOR](VSMONOCOLOR-System-Variable.md) system variable to shade all faces by changing the hue and saturation values of the color |
| 3 | Desaturate: Softens the color by reducing its saturation component by 30 percent |

NOTE:Existing visual styles are not changed when you enter a new value for this system variable. Any new value entered for this
system variable temporarily creates an unsaved new visual style.

#### Related Concepts

* [Shade and Color Faces](Shade-and-Color-Faces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*