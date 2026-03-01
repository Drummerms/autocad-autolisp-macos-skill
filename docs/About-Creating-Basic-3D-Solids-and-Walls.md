# About Creating Basic 3D Solids and Walls

3D solid objects can start from basic primitives, or from extruded, swept, revolved, or lofted profiles. You can combine these
using Boolean operations.

## Specify 3D Solid Primitives

You can create several basic 3D shapes, known as *solid primitives* with commands such as CYLINDER, PYRAMID, and BOX.

![](../images/GUID-709B17DF-6DBC-48FA-B146-F26570AA0DBB-low.png)

A fast way to create 3D solids in the shape of walls is with the POLYSOLID command. The process is similar to creating polyline
including both straight and curved segments, except that you can specify a default height, width, and justification for the
resulting 3D solid. You can also convert 2D objects such as a lines, polylines, arcs, and circles to 3D solids with this command.

![](../images/GUID-00785F5E-3D7D-458C-AACC-59BF1C43F191-low.png)

## Extrude, Revolve, and Sweep Profiles

You can also create 3D solids through operations such as extruding, revolving, or sweeping closed 2D objects. In the illustration,
the same closed 2D polyline is swept along a path, revolved around an axis, and extruded in a specified direction.

![](../images/GUID-28BA5E62-3C0A-4B11-9522-FC4D961A9895-low.png)

The commands used were SWEEP, REVOLVE, and EXTRUDE.

## Create Composite 3D Solids With Boolean Operations

By combining 3D solids using Boolean operations such as union and subtract, you can create a single, composite solid as illustrated.

![](../images/GUID-23BBD05E-7B44-4776-B549-DA9A59BBD24F-low.png)

To create the hole, a cylinder was created and then subtracted from the wall.

You can also combine 3D solids using Boolean intersections. The following illustration shows two solids that were extruded
from closed polylines corresponding to two profiles of the bracket. The extrusions were then combined by intersecting their
volumes.

![](../images/GUID-1C31FCED-9999-4012-B6F9-518D00711466-low.gif)

The commands for Boolean operations include UNION, SUBTRACT and INTERSECT.

#### Related Tasks

* [To Work With Creating Solid Boxes](To-Work-With-Creating-Solid-Boxes.md)
* [To Work With Creating Solid Cones](To-Work-With-Creating-Solid-Cones.md)
* [To Work With Creating Solid Cylinders](To-Work-With-Creating-Solid-Cylinders.md)
* [To Work With Creating Solid Spheres](To-Work-With-Creating-Solid-Spheres.md)
* [To Work With Creating Solid Pyramids](To-Work-With-Creating-Solid-Pyramids.md)
* [To Create a Solid Torus](To-Create-a-Solid-Torus.md)
* [To Work With Creating Solid Wedges](To-Work-With-Creating-Solid-Wedges.md)
* [To Work With Creating Polysolids](To-Work-With-Creating-Polysolids.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*