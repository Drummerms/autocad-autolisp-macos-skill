# About Modifying Edges on 3D Objects

You can select and modify edges on a 3D solid or surface.

## Move, Rotate, and Scale Edges

Move, rotate, and scale the edges on 3D solids and surfaces using grips, gizmos, and commands.

![](../images/GUID-D619708D-E1CD-4395-833B-A783E4C1CEB8-low.png)

cubes with edges moved, rotated, and scaled

You can use MOVE, ROTATE, and SCALE to modify edges on 3D solids and surfaces just as you can for any other object. Press
and hold Ctrl to select the edge.

If you move, rotate, or scale an edge on a 3D solid primitive, the history of the solid primitive is removed. The solid is
no longer a true primitive and cannot be manipulated using grips and the Properties Inspector.

Edges on regions can be selected, but do not display grips. These edges can also be moved, rotated, and scaled.

## Edge Modification Options

As you drag an edge, press Ctrl to cycle through modification options.

![](../images/GUID-DF3014D7-6FBE-4024-B24B-E218B0379F84-low.png)

* *Extend Adjacent Faces*. When you move, rotate, or scale an edge without pressing Ctrl, the shared length of the edge and its vertices is maintained.
  However, the planes of the adjacent faces adjacent might be changed.
* *Move Edge*. When you move, rotate, or scale an edge and press and release Ctrl once while dragging, the edge is modified without its
  vertices. The surfaces of the adjacent faces are maintained, but the length of the modified edge might change.
* *Allow Triangulation*. When you move, rotate, or scale an edge and press and release Ctrl twice while dragging, the edge and its vertices are modified.
  (This behavior is the same as if you had not pressed Ctrl). However, if the adjacent faces are no longer planar, they are
  triangulated (divided into two or more planar triangular faces).

If you press and release Ctrl a third time, the modification returns to the first option, as if you had not pressed Ctrl.

TIP: Rather than pressing Ctrl to cycle through edge modification options, hover over an edge grip to display the grip multi-functional
menu.

## Delete Edges

You can also delete edges that completely divide two coplanar faces using one of the following methods:

* Select the edge and press Delete.
* Select the edge and enter the ERASE command.

## Fillet and Chamfer 3D Solids

Round, fillet, or bevel the edges of 3D solids using FILLETEDGE and CHAMFEREDGE.

![](../images/GUID-C78FD52A-1B98-420D-8DD7-59DED7DB4F14-low.png)

Use the fillet and chamfer grips to modify the fillet radius or the chamfer distance. The default fillet radius is set by
the FILLETRAD3D system variable.

TIP:Use the
*Chain* option of FILLETEDGE to limit selection to tangent edges.

## Color Edges

You can modify the color of an edge on a 3D object by selecting the edge and changing the Color property in the Properties
Inspector.

## Copy Edges

You can copy individual edges on a 3D solid object. Edges are copied as lines, arcs, circles, ellipses, or splines.

![](../images/GUID-98CBBAE6-0404-456C-9FEF-745312BCB025-low.png)

If you specify two points, the first point is used as a base point and a single copy is placed relative to the base point.
If you specify a single point, and then press Enter, the original selection point is used as a base point. The next point
is used as a point of displacement.

#### Related Tasks

* [To Fillet a 3D Solid Edge](To-Fillet-a-3D-Solid-Edge.md)
* [To Modify a Fillet or Chamfer on a 3D Solid](To-Modify-a-Fillet-or-Chamfer-on-a-3D-Solid.md)
* [To Change the Color of an Edge on a 3D Solid](To-Change-the-Color-of-an-Edge-on-a-3D-Solid.md)
* [To Copy an Edge of a 3D Solid](To-Copy-an-Edge-of-a-3D-Solid.md)

#### Related Information

* [To Chamfer a 3D Solid](To-Chamfer-a-3D-Solid.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*