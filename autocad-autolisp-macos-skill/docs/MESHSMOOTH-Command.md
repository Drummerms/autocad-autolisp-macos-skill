# MESHSMOOTH (Command)

Converts 3D objects such as polygon meshes, surfaces, and solids to mesh objects.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Mesh panel ![](../images/ac.menuaro.gif) Smooth Object.
![](../images/GUID-CC5A20F2-223C-4B04-84F8-C845F78C669B-low.png)

*Menu*:
Draw
![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Meshes ![](../images/ac.menuaro.gif) Smooth Mesh.

## Summary

Take advantage of the detailed modeling capabilities of 3D mesh by converting objects such as 3D solids and surfaces to mesh.

![](../images/GUID-EA03DC78-B311-4DD3-B940-02EF931149DC-low.gif)

Use this method to convert 3D faces (3DFACE) and legacy polygonal and polyface meshes (from AutoCAD 2009 and earlier). You
can also convert 2D objects such as regions and closed polylines.

The level of smoothness upon conversion depends on the mesh type setting ([FACETERMESHTYPE](FACETERMESHTYPE-System-Variable.md) system variable). If the mesh type is not set to be optimized, the converted object is not smoothed.

To convert mesh objects to 3D surfaces or solids, use
[CONVTOSOLID](CONVTOSOLID-Command.md) or
[CONVTOSURFACE](CONVTOSURFACE-Command.md) commands.

Objects That Can Be Converted to Mesh

| Object type |
| 3D solids |
| 3D surfaces |
| 3D faces |
| Polyface and polygon meshes (legacy) |
| Regions |
| Closed polylines |

#### Related Concepts

* [About Changing Mesh Smoothness Levels](About-Changing-Mesh-Smoothness-Levels.md)
* [About Creating Meshes](About-Creating-Meshes.md)
* [About Creating Meshes by Conversion](About-Creating-Meshes-by-Conversion.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*