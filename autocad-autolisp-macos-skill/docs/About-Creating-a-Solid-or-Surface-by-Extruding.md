# About Creating a Solid or Surface by Extruding

Create a 3D solid or surface by stretching curves into 3D space.

The EXTRUDE command creates a solid or surface that extends the shape of a curve. Open curves create surfaces and closed
curves create solids or surfaces.

![](../images/GUID-8BCE01D7-5238-45E3-B1C3-A78C68D0B90B-low.png)

## Options for Extrusion

When you extrude objects, you can specify any of the following options:

* *Mode.* Sets whether the extrude creates a surface or a solid.
* *Specify a path for extrusion.* With the Path option, create a solid or surface by specifying an object to be the path for the profile, or shape, of the extrusion.
  The extruded object starts from the plane of the profile and ends on a plane perpendicular to the path at the endpoint of
  the path. For best results, use object snaps to make sure that the path is on or within the boundary of the object being extruded.

  ![](../images/GUID-94F2B075-DBD0-4BB0-AE02-E69E738C037D-low.png)

  Extruding is different from sweeping. When you extrude a profile along a path, the profile follows the shape of the path,
  even if the path does not intersect the profile. Sweeping usually provides greater control and better results.
* *Taper angle.* Tapering the extrusion is useful for defining part that require a specific taper angle, such as a mold used to create metal
  products in a foundry.

  ![](../images/GUID-B1D23679-CF21-4CD0-BB48-AD6D91940993-low.png)
* *Direction.* With the Direction option, you can specify two points to set the length and direction of the extrusion.

  ![](../images/GUID-F3B25321-0D71-4C63-8BB6-6BBE709CA431-low.png)
* *Expression.* Enter a mathematical expression to constrain the height of the extrusion.

#### Related Concepts

* [About Constructing Solids and Surfaces From 2D Geometry](About-Constructing-Solids-and-Surfaces-From-2D-Geometry.md)

#### Related Information

* [To Create a NURBS Surface by Extruding](To-Create-a-NURBS-Surface-by-Extruding.md)
* [To Create a 3D Solid by Extruding](To-Create-a-3D-Solid-by-Extruding.md)
* [To Create a Procedural Surface by Extruding Along a Path](To-Create-a-Procedural-Surface-by-Extruding-Along-a-Path.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*