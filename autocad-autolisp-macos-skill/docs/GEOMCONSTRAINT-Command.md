# GEOMCONSTRAINT (Command)

Applies or persists geometric relationships between objects or points on objects.

## Access Methods

*Menu:* Tools ![](../images/ac.menuaro.gif) Parametric ![](../images/ac.menuaro.gif) Geometric Constraints.

## Summary

When you apply a geometric constraint to a pair of objects, the order in which the objects are selected and the point on
which each object is selected can affect how the objects are positioned relative to each other.

The following table outlines the valid constraint points for an object.

| Objects | Valid Constraint Points |
| Line | Endpoints, midpoint |
| Arc | Center, endpoints, midpoint |
| Spline | Endpoints |
| Circle | Center |
| Ellipse | Center, major and minor axes |
| Polyline | Endpoints, midpoints of line and arc subobjects, center of arc subobjects |
| Xref, attribute, table | Insertion point |
| Block | Insertion point, nested entities |
| Text, multiline text | Insertion point, alignment point |

The following commands are equivalent to each GEOMCONSTRAINT option:

Horizontal ([GCHORIZONTAL](GCHORIZONTAL-Command.md))
:   Causes lines or pairs of points to lie parallel to the X axis of the current coordinate system.

Vertical ([GCVERTICAL](GCVERTICAL-Command.md))
:   Causes lines or pairs of points to lie parallel to the Y axis of the current coordinate system.

Perpendicular ([GCPERPENDICULAR](GCPERPENDICULAR-Command.md))
:   Causes selected lines to lie 90 degrees to one another.

Parallel ([GCPARALLEL](GCPARALLEL-Command.md))
:   Causes selected lines to lie parallel to each other.

Tangent ([GCTANGENT](GCTANGENT-Command.md))
:   Constrains two curves to maintain a point of tangency to each other or their extensions.

Smooth ([GCSMOOTH](GCSMOOTH-Command.md))
:   Constrains a spline to be contiguous and maintain G2 continuity with another spline, line, arc, or polyline.

Coincident ([GCCOINCIDENT](GCCOINCIDENT-Command.md))
:   Constrains two points together or a point to a curve (or an extension of a curve).

Concentric ([GCCONCENTRIC](GCCONCENTRIC-Command.md))
:   Constrains two arcs, circles, or ellipses to the same center point.

Collinear ([GCCOLLINEAR](GCCOLLINEAR-Command.md))
:   Causes two or more line segments to lie along the same line.

Symmetric ([GCSYMMETRIC](GCSYMMETRIC-Command.md))
:   Causes selected objects to become symmetrically constrained about a selected line.

Equal ([GCEQUAL](GCEQUAL-Command.md))
:   Resizes selected arcs and circles to the same radius, or selected lines to the same length.

Fix ([GCFIX](GCFIX-Command.md))
:   Locks points and curves in position.

#### Related Concepts

* [About Applying and Deleting Geometric Constraints](About-Applying-and-Deleting-Geometric-Constraints.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*