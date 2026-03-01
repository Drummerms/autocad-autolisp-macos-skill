# SPLFRAME (System Variable)

Controls the display of helixes and smoothed mesh objects.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Drawing |
| Initial value: | 0 |

| 0 | * Does not display the control polygon for helixes. * Displays smoothed mesh objects if they have been smoothed. * Does not display the invisible edges of 3D faces or polyface meshes. |
| 1 | * Displays the control polygon for helixes. * Displays unsmoothed mesh objects, even if they have been smoothed. * Displays the edges of 3D faces and polyface meshes. |

NOTE:To control the display for splines, use the [CVSHOW](CVSHOW-Command.md) and the [CVHIDE](CVHIDE-Command.md) commands.

#### Related Concepts

* [About Creating Meshes](About-Creating-Meshes.md)
* [About Helixes](About-Helixes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*