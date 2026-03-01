# About Using the Spline Tool to Create NURBS Surfaces and Splines

The spline tool is optimized to work with NURBS modeling.

NURBS surfaces can be created from a number of 2D objects, including edge subobjects, polylines, and arcs. But the spline
tool is the only object that has options that are compatible with creating NURBS surface. Not only do splines consist of Bezier
arcs, but they also can be defined with both control vertices and fit points, which offer different editing options.

## Moving Fit Points versus Moving Control Vertices

NURBS curves have both fit points and control vertices. The fit points are directly on the curve, and the control vertices
are outside the line. Use fit points to make small, localized changes to a curve; use control vertices to make changes will
affect the shape of the curve as a whole.

## Clamp Surfaces and Curves with Open and Closed Geometry

NURBS surfaces and curves can have a clamp, closed, or open form. The form affects how the object can be modified.

* *Clamp curve* is a closed loop with a seam that creates extra, unseen control vertices (CVs). These unseen CVs can cause the shape to wrinkle
  and crease when it is reshaped.
* *Closed curves and surfaces* are a loop with coinciding start and end CVs. Their intersection is called a seam. If you move one CV, the other moves with
  it.
* *Open curves and surfaces* have start and end CVs in different positions (no loop). If you snap the start control vertex to the end control vertex,
  the curve is still open.

#### Related Tasks

* [To Create a NURBS Surface by Lofting](To-Create-a-NURBS-Surface-by-Lofting.md)
* [To Convert a Solid Into a NURBS Surface](To-Convert-a-Solid-Into-a-NURBS-Surface.md)
* [To Convert a Mesh Object Into a NURBS Surface](To-Convert-a-Mesh-Object-Into-a-NURBS-Surface.md)

#### Related Concepts

* [About Creating NURBS Surfaces](About-Creating-NURBS-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*