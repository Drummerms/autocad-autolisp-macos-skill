# About Moving, Rotating, and Scaling Faces on 3D Solids and Surfaces

You can select and modify faces of 3D solids and surfaces.

## Modify the Location, Rotation, and Size of Faces on a 3D Solids and Surfaces.

![](../images/GUID-9C3BBE68-5BBB-44F4-B681-3085754FF1FA-low.png)

cube with top face moved, rotated, and scaled

Use the MOVE, ROTATE, and SCALE commands to modify faces, just as you would with any other object. Press and hold Ctrl while
you select a face on a solid.

If you move, rotate, or scale a face on a 3D solid primitive, the solid primitive’s history is removed. The solid is no longer
a true primitive and cannot be manipulated using grips or the Properties palette.

## Face Modification Options

As you drag a face, press Ctrl to cycle through modification options.

![](../images/GUID-B4E76B3F-1D71-4B95-B8F8-77EE18AEA2FB-low.png)

![](../images/GUID-EDFC3F3E-CF33-431C-9DE1-C6BA24DE19BD-low.png)

* *Extend Adjacent Faces*. When you move or rotate a face without pressing Ctrl, the shape and size of the face is maintained. However, the planes
  of adjacent faces might change.
* *Move Face*.When you move a face and press and release Ctrl once while dragging, the position of the face is modified within the boundary,
  or footprint, of the adjacent faces.
* *Allow Triangulation*.When you move or rotate a face and press and release Ctrl twice while dragging, the size and shape of the face is maintained.
  (This behavior is the same as if you had not pressed Ctrl). However, the adjacent planar faces are triangulated (divided into
  two or more planar triangular faces), if necessary.

If you press and release Ctrl a third time, the modification returns to the first option, as if you had not pressed Ctrl.

#### Related Tasks

* [To Copy a Face on a 3D Solid](To-Copy-a-Face-on-a-3D-Solid.md)
* [To Delete a Face on a 3D Solid](To-Delete-a-Face-on-a-3D-Solid.md)
* [To Change the Color of a Face on a 3D Solid](To-Change-the-Color-of-a-Face-on-a-3D-Solid.md)

#### Related Concepts

* [About Modifying Faces on 3D Solids](About-Modifying-Faces-on-3D-Solids.md)
* [About Imprinting Facets on Faces](About-Imprinting-Facets-on-Faces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*