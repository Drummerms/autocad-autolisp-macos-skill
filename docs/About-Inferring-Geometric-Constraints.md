# About Inferring Geometric Constraints

You can automatically apply geometric constraints while creating and editing geometric objects.

Enabling *Infer Constraints* mode automatically applies constraints between the object you are creating or editing, and the object or points associated
with object snaps. Similar to the AUTOCONSTRAIN command, constraints are applied only if the objects meet the constraint conditions.
Objects are not repositioned as a result of inferring constraints.

With Infer Constraints turned on, the object snaps that you specify when creating geometry are used to infer geometric constraints.
However, the following object snaps are not supported:

* Intersection
* Apparent Intersection
* Extension
* Quadrant

The following constraints cannot be inferred:

* Fix
* Smooth
* Symmetric
* Concentric
* Equal
* Collinear

## Infer Constraints with Line and Polyline

Certain object creation and editing commands can infer constraints regardless of the current object snap settings.

LINE and PLINE commands infer coincident *point-to-point* constraints. The Close option infers a coincident constraint between the start point of the first line and the endpoint of
the last line.

## Infer Constraints with Rectangle, Fillet, and Chamfer

The RECTANG, FILLET, and CHAMFER commands infer constraints as follows:

* RECTANG applies a pair of parallel constraints and a perpendicular constraint to the closed polyline.
* FILLET applies tangent and coincident constraints between the newly created arc and the existing trimmed or extended pair
  of lines.
* CHAMFER applies coincident contraints between the newly created line and the existing trimmed or extended pair of lines.

The following commands are unaffected by the Infer Constraints setting:

* SCALE
* MIRROR
* OFFSET
* BREAK
* TRIM
* EXTEND
* ARRAY

## Infer Constraints with Move, Copy, and Stretch

When moving, copying, or stretching with the Infer Constraints on, you can apply coincident, perpendicular, parallel, or tangent
constraints between the object being edited and the object being snapped to if the base point of the edited object is a valid
constraint point of that object.

For example, if a line is stretched and snapped to an endpoint of another line, a coincident constraint is applied between
the endpoints of the two lines.

A vertical or horizontal constraint can be applied between objects when you move, copy, or stretch an object from a valid
constraint point while object tracking vertically or horizontally along a valid constraint point on another object.

#### Related Information

* [To Infer Geometric Constraints When Creating Objects](To-Infer-Geometric-Constraints-When-Creating-Objects.md)
* [About Geometric Constraints](About-Geometric-Constraints.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*