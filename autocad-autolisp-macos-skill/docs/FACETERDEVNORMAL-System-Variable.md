# FACETERDEVNORMAL (System Variable)

Sets the maximum angle between the surface normal and contiguous mesh faces.

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | User-settings |
| Initial value: | 40 |

This setting affects mesh that is converted from another object using the [MESHSMOOTH](MESHSMOOTH-Command.md) command. (For a complete list of objects that can be converted to mesh, see [Objects That Can Be Converted to Mesh](MESHSMOOTH-Command.md).)

Use this setting to retain visual consistency between mesh objects that have the same shape but different sizes. You can enter
any non-negative number between 0 (zero) and 180. Lowering the value increases the density in areas of high curvature and
decreases density in flatter areas.

Lowering the value might increase the drawing file size, and should be saved for larger objects with high [FACETERDEVSURFACE](FACETERDEVSURFACE-System-Variable.md) settings. Avoid lowering this value for objects with small details such as holes or fillets.

NOTE:The value of this system variable reflects the value for objects with no smoothness.

#### Related Concepts

* [About Creating Meshes by Conversion](About-Creating-Meshes-by-Conversion.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*