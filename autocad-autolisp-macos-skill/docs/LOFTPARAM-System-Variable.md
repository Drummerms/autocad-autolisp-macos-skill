# LOFTPARAM (System Variable)

Controls the shape of lofted solids and surfaces.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | Drawing |
| Initial value: | 7 |

The setting is stored as a bitcode using the sum of the following values:

| 1 | No twist (minimizes the twist between cross sections) |
| 2 | Align direction (aligns the start to end direction of each cross section curve) |
| 4 | Simplify (produces simple solids and surfaces, such as a cylinder or plane, instead of spline solids and surfaces) |
| 8 | Close (closes the surface or solid between the first and the last cross sections) |

#### Related Concepts

* [About Creating a Solid or Surface by Lofting](About-Creating-a-Solid-or-Surface-by-Lofting.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*