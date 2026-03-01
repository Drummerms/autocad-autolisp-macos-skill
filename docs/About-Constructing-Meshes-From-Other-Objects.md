# About Constructing Meshes From Other Objects

Create meshes by filling the space between other objects such as lines and arcs.

You can use a variety of methods to create several types of mesh objects whose edges are defined by other objects. Mesh types
include ruled, tabulated, revolved, and edge-defined meshes. The MESHTYPE system variable controls whether the new objects
are valid mesh objects, or whether they are created using legacy polyface or polygon geometry.

You can control how the mesh is displayed by changing the visual style (VISUALSTYLES).

## Create a Ruled Mesh

RULESURF creates a mesh that represents the ruled surface between two lines or curves.

![](../images/GUID-81FCF7BE-75D0-4E23-BE9C-20F12857FEB5-low.png)

There are several methods for creating ruled meshes. For example, you can use two objects to define the edges of the ruled
mesh: lines, points, arcs, circles, ellipses, elliptical arcs, 2D polylines, 3D polylines, or splines.

Both objects that are used as the “rails” of a ruled mesh must be either open or closed. You can pair a point object with
either an open or a closed object.

![](../images/GUID-05947548-118E-4562-A47D-8BBA7AC86B58-low.png)

You can specify any two points on closed curves to complete the operation.

For open curves, construction of the ruled mesh is based on the locations of the specified points on the curves.

![](../images/GUID-D7342A0D-22E4-48D6-98CF-BF286CAF4982-low.png)

![](../images/GUID-FD74F465-E418-4FDC-B7EC-B262080ED9AA-low.png)

## Create a Tabulated Mesh

TABSURF creates a mesh that represents a general tabulated surface. The surface is defined by the extrusion of a line or curve
(called a path curve) in a specified direction and distance (called a direction vector or path).

![](../images/GUID-DBC44C95-B300-4D07-A87A-F70DAEC508D3-low.png)

The path curve can be a line, arc, circle, ellipse, elliptical arc, 2D polyline, 3D polyline, or spline. The direction vector
can be based on a line or an open 2D or 3D polyline.

This method creates the mesh as a series of parallel polygons running along a specified path. The original object and the
direction vector must already be drawn, as shown in the following illustrations.

![](../images/GUID-80DFAF8B-1CA3-46CD-B04A-05DA1EEDF2AB-low.png)

## Create a Revolved Mesh

REVSURF creates a mesh that approximates a surface of revolution by rotating a profile about a specified axis. A profile
can consist of lines, circles, arcs, ellipses, elliptical arcs, polylines, splines, closed polylines, polygons, closed splines,
and donuts.

![](../images/GUID-43ECE536-75CC-4E8A-97EB-B4E42F8CC1F3-low.png)

This method is useful for mesh forms with rotational symmetry.

![](../images/GUID-51BB4BBF-8E95-4D4F-935E-06AC8994B683-low.png)

## Create an Edge-Defined Mesh

EDGESURF creates a mesh approximating a Coons surface patch mesh from four adjoining edges. A Coons surface patch mesh is
a bicubic surface that is interpolated between four adjoining edges (which can be general space curves).

![](../images/GUID-28656EDB-5511-45E9-84AE-0C80C54C75BB-low.png)

The mesh in the following illustration was derived from four objects called
*edges*. Edges can be arcs, lines, polylines, splines, or elliptical arcs that form a closed loop and share endpoints. A Coons patch
is a bicubic surface (one curve in the
*M* direction and another in the
*N* direction) interpolated between the four edges.

![](../images/GUID-FE3F4A43-3800-4D91-9658-3AA8230237C9-low.png)

#### Related Tasks

* [To Create a Ruled Mesh](To-Create-a-Ruled-Mesh.md)
* [To Create a Tabulated Mesh](To-Create-a-Tabulated-Mesh.md)
* [To Create a Revolved Mesh](To-Create-a-Revolved-Mesh.md)
* [To Create an Edge-defined Coons Surface Patch Mesh](To-Create-an-Edge-defined-Coons-Surface-Patch-Mesh.md)

#### Related Concepts

* [About Creating Meshes](About-Creating-Meshes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*