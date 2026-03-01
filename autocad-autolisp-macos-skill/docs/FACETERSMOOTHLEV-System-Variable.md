# FACETERSMOOTHLEV (System Variable)

Sets the default level of smoothness for objects that are converted to mesh.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | User-settings |
| Initial value: | 1 |

| -1 or any negative number | Does not smooth the object after conversion |
| 0 | Does not smooth the object after conversion |
| 1 | Applies smoothness level 1 after conversion |
| 2 | Applies smoothness level 2 after conversion |
| 3 | Applies smoothness level 3 after conversion |

This variable sets the default level of smoothness that is applied to mesh that is created as a result of conversion from
another object with the [MESHSMOOTH](MESHSMOOTH-Command.md) command.

The value cannot be greater than the value of [SMOOTHMESHMAXLEV](SMOOTHMESHMAXLEV-System-Variable.md).

Mesh objects that are created under the following circumstances are always created without smoothness, and are not affected
by this system variable:

* Mesh created using [REVSURF](REVSURF-Command.md), [TABSURF](TABSURF-Command.md), [RULESURF](RULESURF-Command.md), or [EDGESURF](EDGESURF-Command.md)
* Mesh created using MESHSMOOTH when the type of mesh is set to be quadrilateral or triangular ([FACETERMESHTYPE](FACETERMESHTYPE-System-Variable.md))

For a complete list of objects that can be converted to mesh, see [Objects That Can Be Converted to Mesh](MESHSMOOTH-Command.md).

#### Related Concepts

* [About Creating Meshes by Conversion](About-Creating-Meshes-by-Conversion.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*