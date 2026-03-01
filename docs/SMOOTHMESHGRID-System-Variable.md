# SMOOTHMESHGRID (System Variable)

Sets the maximum level of smoothness at which the underlying mesh facet grid is displayed on 3D mesh objects.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | User-settings |
| Initial value: | 3 |

| 0 | Never displays the underlying mesh facet grid |
| 1 | Displays the facet grid for smoothing levels 0 and 1 |
| 2 | Displays the facet grid for smoothing levels 2 and lower |
| 3 | Displays the facet grid for smoothing levels 3 and lower |
| 4 | Displays the facet grid for smoothing levels 4 and lower |

Use this variable to help visualize smooth surfaces. By setting limits, you can simplify the display of the underlying facet
grid when you work with extremely dense mesh objects.

You can enter any number, depending on the number of smoothing levels you expect. This variable does not affect the smoothing
level of the mesh. Its value cannot exceed the value of SMOOTHMESHMAXLEV.

If the [VSLIGHTINGQUALITY](VSLIGHTINGQUALITY-System-Variable.md) system variable is 0, this system variable is ignored and all smoothness levels are displayed as faceted.

#### Related Concepts

* [About Changing Mesh Smoothness Levels](About-Changing-Mesh-Smoothness-Levels.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*