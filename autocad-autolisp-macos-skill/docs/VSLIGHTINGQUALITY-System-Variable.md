# VSLIGHTINGQUALITY (System Variable)

Sets the lighting quality in the current viewport.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 1 |

| 0 | Faceted. A single color is computed for each face of a surface or 3D solid. |
| 1 | Smooth. The colors are computed as a gradient between the vertices of the faces. |
| 2 | Smoothest. If the Per-Pixel Lighting setting is turned on in the Manual Performance Tuning dialog box, then the colors are computed for individual pixels. If not, the Smooth setting is used instead. |

NOTE:Existing visual styles are not changed when you enter a new value for this system variable. Any new value entered for this
system variable temporarily creates an unsaved new visual style.

#### Related Concepts

* [About Using Visual Styles](About-Using-Visual-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*