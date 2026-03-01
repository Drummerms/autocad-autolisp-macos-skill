# FACETERPRIMITIVEMODE (System Variable)

Specifies whether the smoothness settings for objects that are converted to a mesh.

|  |  |
| --- | --- |
| Type: | Bitcode |
| Saved in: | User-settings |
| Initial value: | 1 |

| 0 | Applies settings from the FACETERSMOOTHLEV system variable to the converted object. |
| 1 | Applies settings from the DIVMESH\* system variables to the converted object. |

This setting affects a mesh that is converted from a primitive 3D solid object (such as box or cone) using the [MESHSMOOTH](MESHSMOOTH-Command.md) command. (For a complete list of objects that can be converted to mesh, see [Objects That Can Be Converted to Mesh](MESHSMOOTH-Command.md).)

#### Related Concepts

* [About Creating Meshes by Conversion](About-Creating-Meshes-by-Conversion.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*