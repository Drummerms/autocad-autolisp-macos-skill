# GCCOINCIDENT (Command)

Constrains two points together or a point to a curve (or an extension of a curve).

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Parametric panel ![](../images/ac.menuaro.gif) Geometric Constraint drop-down ![](../images/ac.menuaro.gif) Coincident.
![](../images/GUID-EEF0B94F-AECB-420D-A229-E2A93CFF3BA8-low.png)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Parametric ![](../images/ac.menuaro.gif) Geometric Constraints ![](../images/ac.menuaro.gif) Coincident.

## Summary

This command is equivalent to the Coincident option in
[GEOMCONSTRAINT](GEOMCONSTRAINT-Command.md).

A constraint point on an object can be made coincident with an object or a constraint point on another object.

Following are the valid constraint objects and points:

* Line
* Polyline segment
* Circle
* Arc
* Polyline arc
* Ellipse
* Spline
* Two valid constraint points

## List of Prompts

The following prompts are displayed.

Select first
[point](GCCOINCIDENT-Command.md) or [[Object](GCCOINCIDENT-Command.md)/[Autoconstrain](GCCOINCIDENT-Command.md)] <Object>:
*Select a constraint point, or an object, or enter* *a**to apply constraints to selected objects*

Point

Specifies a point to be constrained.

First Point
:   Specifies the first point of the object to be constrained.

Second Point
:   Specifies the second point of the object to be constrained.

Object

Selects an object to be constrained.

Point
:   [Point](GCCOINCIDENT-Command.md)

Multiple
:   Picks successive points to coincide with the first object. The Multiple option is displayed when you use the Object option
    to select the first object.

Autoconstrain

Selects multiple objects. Coincident constraints are applied to selected objects with unconstrained points that are coincident
to each other.

The number of constraints applied is displayed at the Command prompt.

When a coincident constraint is applied between a point and an arc or line, the point can lie on the line or arc or the extension
of the line or arc.

#### Related Concepts

* [About Applying and Deleting Geometric Constraints](About-Applying-and-Deleting-Geometric-Constraints.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*