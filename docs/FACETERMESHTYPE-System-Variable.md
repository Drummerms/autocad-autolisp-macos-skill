# FACETERMESHTYPE (System Variable)

Sets the type of mesh to be created.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | User-settings |
| Initial value: | 0 |

| 0 | Objects are converted to an optimized mesh object type with fewer faces |
| 1 | Faces are mostly quadrilateral |
| 2 | Faces are mostly triangular |

This setting affects mesh that is converted from another object using the [MESHSMOOTH](MESHSMOOTH-Command.md) command. (For a complete list of objects that can be converted to mesh, see [Objects That Can Be Converted to Mesh](MESHSMOOTH-Command.md).)

#### Related Concepts

* [About Creating Meshes by Conversion](About-Creating-Meshes-by-Conversion.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*