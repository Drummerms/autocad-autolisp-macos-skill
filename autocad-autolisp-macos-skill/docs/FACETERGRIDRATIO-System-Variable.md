# FACETERGRIDRATIO (System Variable)

Sets the maximum aspect ratio for the mesh subdivisions that are created for solids and surfaces converted to mesh.

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | User-settings |
| Initial value: | 0.0000 |

This setting affects mesh that is converted from another object using the [MESHSMOOTH](MESHSMOOTH-Command.md) command. (For a complete list of objects that can be converted to mesh, see [Objects That Can Be Converted to Mesh](MESHSMOOTH-Command.md).)

Permissible values range from 0 to 100, and set the height/width ratio of the face. Use this variable to prevent long, thin
faces that can result from cylindrical object conversions. Smaller values result in more, better-formed faces, but can affect
performance. Set this value to 0 to turn it off.

If the value you enter is less than 1, the ratio calculation is based on 1/*n*. For example, if you enter 0.2, the variable value is 1/0.2 = 5.

NOTE:The value of this system variable reflects the value for objects with no smoothness.

#### Related Concepts

* [About Creating Meshes by Conversion](About-Creating-Meshes-by-Conversion.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*