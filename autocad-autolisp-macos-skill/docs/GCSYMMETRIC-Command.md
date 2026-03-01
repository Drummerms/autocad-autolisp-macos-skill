# GCSYMMETRIC (Command)

Causes selected objects to become symmetrically constrained about a selected line.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Parametric panel ![](../images/ac.menuaro.gif) Geometric Constraint drop-down ![](../images/ac.menuaro.gif) Symmetric.
![](../images/GUID-26768682-2083-4D9A-99D7-493DDC856A46-low.png)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Parametric ![](../images/ac.menuaro.gif) Geometric Constraints ![](../images/ac.menuaro.gif) Symmetric.

## Summary

This command is equivalent to the Symmetric option in
[GEOMCONSTRAINT](GEOMCONSTRAINT-Command.md).

For lines, the line’s angle is made symmetric (and not the endpoints). For arcs and circles, the center and radius are made
symmetric (not the endpoints of the arc).

Following are the valid constraint objects and points:

* Line
* Polyline segment
* Circle
* Arc
* Polyline arc
* Ellipse

NOTE:You must have an axis around which you will constrain the objects or points to be symmetrical. This is referred to as the
symmetry line.

## List of Prompts

The following prompts are displayed.

Select first
[object](GCSYMMETRIC-Command.md) or [[2Points](GCSYMMETRIC-Command.md)] <2Points>:
*Select an object or two constrained points*

Object

Selects an object to be constrained.

First Object
:   Selects the first object to be made symmetrical.

Second Object
:   Selects the second object to be made symmetrical.

Symmetric Line
:   Specifies the axis in which the objects and points are made to be symmetrical.

2Points

Selects two points and a symmetry line.

First Point
:   Selects the first point to be made symmetrical.

Second Point
:   Selects the second point to be made symmetrical.

Select Symmetric Line
:   Specifies the axis in which the objects and points are made to be symmetrical.

#### Related Concepts

* [About Applying and Deleting Geometric Constraints](About-Applying-and-Deleting-Geometric-Constraints.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*