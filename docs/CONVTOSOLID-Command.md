# CONVTOSOLID (Command)

Converts 3D meshes and polylines and circles with thickness to 3D solids.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Convert to Solid.
![](../images/GUID-7BF57DDA-E80D-4A8F-BFC8-3C4183E6A629-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) 3D Operations ![](../images/ac.menuaro.gif) Convert to Solid.

## Summary

Take advantage of the solid modeling capabilities available for 3D solids. When you convert mesh, you can specify whether
the converted objects are smoothed or faceted, and whether the faces are merged.

![](../images/GUID-D677B662-6018-4359-894F-BA8A979E0911-low.gif)

The smoothness and number of faces of the resulting 3D solid are controlled by the
[SMOOTHMESHCONVERT](SMOOTHMESHCONVERT-System-Variable.md) system variable. Whereas the previous example shows a conversion to a smooth, optimized 3D solid, the following example shows
a conversion to a faceted 3D solid in which the faces are not merged, or optimized.

![](../images/GUID-A1F51AC7-CD62-42DD-B152-741D5F694DE8-low.gif)

The following tables list the objects that can be converted to solid objects and some limitations on their conversion.

Objects that Can Be Converted to 3D Solids

| Object | Required properties |
| Mesh | Encloses a volume with no gaps between edges (watertight) |
| Polyline | Closed, uniform-width, with thickness |
| Polyline | Closed, zero-width, with thickness |
| Surface | Encloses a volume with no gaps between edges (such as a revolved surface that is capped at both ends or closed mesh objects that were converted to surfaces). If the surfaces enclose a watertight area, you can also convert to a solid with the [SURFSCULPT](SURFSCULPT-Command.md) command. |

Limitations on Conversion to Solid Objects

| Object | Description |
| Polyline | Cannot contain zero-width vertices. |
| Polyline | Cannot contain segments of variable width. |
| Separate objects that simulate a closed surface | Cannot be a planar surface with contiguous edges or an exploded 3D solid box into six regions. However, you cannot convert those separate objects back to a solid with CONVTOSOLID. |
| Planar surfaces with contiguous edges | Cannot convert separate objects unless they enclose a volume without gaps. If the surfaces enclose a watertight area, you can convert to a solid with the [SURFSCULPT](SURFSCULPT-Command.md) command. |
| Exploded 3D solid | Cannot convert separate objects (in this case, regions) with the CONVTOSOLID command. You can, however, convert them to a solid with the [SURFSCULPT](SURFSCULPT-Command.md) command. |

You can select the objects to convert before you start the command.

The
[DELOBJ](DELOBJ-System-Variable.md) system variable controls whether the geometry used to create 3D objects is automatically deleted when the new object is created
or whether you are prompted to delete the objects.

## List of Prompts

The following prompts are displayed.

Select objects
:   Specifies one or more objects to convert to 3D solid objects. You can select objects with thickness or mesh objects.

    If one or more objects in the selection set are invalid for the command, you will be prompted again to select objects.

#### Related Concepts

* [About Converting Surfaces and Meshes to 3D Solids](About-Converting-Surfaces-and-Meshes-to-3D-Solids.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*