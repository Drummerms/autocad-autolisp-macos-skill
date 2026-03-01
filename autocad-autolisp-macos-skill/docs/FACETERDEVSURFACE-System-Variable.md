# FACETERDEVSURFACE (System Variable)

Sets how closely the converted mesh object adheres to the original shape of the solid or surface.

|  |  |
| --- | --- |
| Type: | Real |
| Saved in: | User-settings |
| Initial value: | 0.001 |

This setting affects mesh that is converted from another object using the [MESHSMOOTH](MESHSMOOTH-Command.md) command. (For a complete list of objects that can be converted to mesh, see [Objects That Can Be Converted to Mesh](MESHSMOOTH-Command.md).)

You can enter any non-negative number, including 0 (zero). Smaller values result in a higher number of faces, more accurate
meshes with less deviation from the object surface, and slower performance. Set the value to 0 to turn off the option.

NOTE:The value of this system variable reflects the value for objects with no smoothness.

#### Related Concepts

* [About Creating Meshes by Conversion](About-Creating-Meshes-by-Conversion.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*