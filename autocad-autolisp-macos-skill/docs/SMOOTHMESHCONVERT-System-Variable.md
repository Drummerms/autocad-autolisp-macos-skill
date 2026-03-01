# SMOOTHMESHCONVERT (System Variable)

Sets whether mesh objects that you convert to 3D solids or surfaces are smoothed or faceted, and whether their faces are merged.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | User-settings |
| Initial value: | 0 |

| 0 | Creates a smooth model. Coplanar faces are optimized, or merged. |
| 1 | Creates a smooth model. Original mesh faces are retained in the converted object. |
| 2 | Creates a model with flattened faces. Coplanar faces are optimized, or merged. |
| 3 | Creates a model with flattened faces. Original mesh faces are retained in the converted object. |

This system variable sets the default value for operations that use [CONVTOSOLID](CONVTOSOLID-Command.md) and [CONVTOSURFACE](CONVTOSURFACE-Command.md) commands.

#### Related Concepts

* [About Converting Surfaces and Meshes to 3D Solids](About-Converting-Surfaces-and-Meshes-to-3D-Solids.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*