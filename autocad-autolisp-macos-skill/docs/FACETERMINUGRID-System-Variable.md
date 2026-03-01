# FACETERMINUGRID (System Variable)

Sets the minimum number of U grid lines for solids and surfaces that are converted to mesh.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | User-settings |
| Initial value: | 0 |

This setting affects mesh that is converted from another object using the [MESHSMOOTH](MESHSMOOTH-Command.md) command. (For a complete list of objects that can be converted to mesh, see [Objects That Can Be Converted to Mesh](MESHSMOOTH-Command.md).)

Permissible values range from 0 to 1023. Setting 0 (zero) turns off the setting. The value of this system variable cannot
exceed the value of [FACETERMAXGRID](FACETERMAXGRID-System-Variable.md)/[FACETERMINVGRID](FACETERMINVGRID-System-Variable.md).

NOTE:The value of this system variable reflects the value for objects with no smoothness.

#### Related Concepts

* [About Creating Meshes by Conversion](About-Creating-Meshes-by-Conversion.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*