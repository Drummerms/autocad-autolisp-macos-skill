# About Moving, Rotating, and Scaling 3D Subobjects

Move, rotate, and scale individual subobjects on 3D solids and surfaces.

Use the same methods to modify a face, edge, or vertex that you use to modify the entire object:

* Drag grips
* Use gizmos (3DMOVE, 3DROTATE, 3DSCALE)
* Enter object editing commands (MOVE, ROTATE, SCALE)

## About Modifying Subobjects

When you move, rotate, or scale a subobject, the subobject is modified in a way that maintains the integrity of the 3D solid
or surface. For example, when you drag an edge to move it, the adjacent faces are adjusted so that they remain adjacent to
the edge.

![](../images/GUID-CBB7857C-5CC9-4727-B155-747321157B99-low.png)

Several results are possible when you modify a solid or surface. When you move, rotate, or scale subobjects, you can press
Ctrl one or more times as you drag to cycle through modification options.

The following illustration shows the modification options for moving a face.

![](../images/GUID-B4E76B3F-1D71-4B95-B8F8-77EE18AEA2FB-low.png)

## Move, Rotate, and Scale Subobjects on Composite Solids

When you modify composite solids, the effect of the edits depends on the current setting of the History property.

* To modify subobjects of each history component separately, the History property must be set to Record (On).
* To modify subobjects of the combined composite solid as a whole, the History property must be set to None (Off).

## Rules and Limitations When Moving, Rotating, and Scaling Subobjects on 3D Solids

You can only move, rotate, and scale subobjects on 3D solids if the operation maintains the integrity of the solid. The following
rules and limitations apply to moving, rotating, and scaling subobjects:

* When you use grips to modify subobjects, grips are not displayed on the subobjects that cannot be moved, rotated, or scaled.
* In most cases, you can move, rotate, and scale both planar and non-planar faces.
* You can only modify an edge that is a straight line and that has at least one planar adjacent face. The planes of the adjacent
  planar faces are adjusted to contain the modified edge.
* You cannot move, rotate, or scale edges (or their vertices) that are imprinted inside faces.
* You can only modify a vertex if it has at least one planar adjacent face. The planes of the adjacent planar faces are adjusted
  to contain the modified vertex.
* When you drag a subobject, the final result might be different than the preview displayed during the modification. This result
  occurs when the solid geometry is adjusted in order to maintain its topology. In some cases, the modification is not possible
  because it changes the topology of the solid too severely.
* If the modification causes spline surfaces to be extended, the operation is often unsuccessful.
* You cannot move, rotate, or scale non-manifold edges (edges that are shared by more than two faces) or non-manifold vertices.
  Also, if some non-manifold edges or vertices are present near faces, edges, and vertices that you modify, the operation might
  not be possible.

#### Related Tasks

* [To Work With 3D Gizmo Tools](To-Work-With-3D-Gizmo-Tools.md)
* [To Move 3D Objects Along a Plane or Axis](To-Move-3D-Objects-Along-a-Plane-or-Axis.md)
* [To Rotate 3D Objects Along an Axis](To-Rotate-3D-Objects-Along-an-Axis.md)
* [To Scale a 3D Object](To-Scale-a-3D-Object.md)

#### Related Concepts

* [About Using 3D Gizmos](About-Using-3D-Gizmos.md)
* [About Moving 3D Objects](About-Moving-3D-Objects.md)
* [About Rotating 3D Objects](About-Rotating-3D-Objects.md)
* [About Scaling 3D Objects](About-Scaling-3D-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*