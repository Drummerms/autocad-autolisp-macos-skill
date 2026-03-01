# FACETERMAXEDGELENGTH (System Variable)

Sets the maximum length of edges for mesh objects that are created by conversion from solids and surfaces.

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | User-settings |
| Initial value: | 0.0000 |

You can use any non-negative number, including 0 (zero). A value of 0 (zero) does not restrict the length an edge can be when
a surface or solid is converted to a mesh.

This setting affects mesh that is converted from another object using the [MESHSMOOTH](MESHSMOOTH-Command.md) command. (For a complete list of objects that can be converted to mesh, see [Objects That Can Be Converted to Mesh](MESHSMOOTH-Command.md).)

NOTE:The value of this system variable reflects the value for objects with no smoothness.

#### Related Concepts

* [About Creating Meshes by Conversion](About-Creating-Meshes-by-Conversion.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*