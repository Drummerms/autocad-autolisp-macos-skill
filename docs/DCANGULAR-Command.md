# DCANGULAR (Command)

Constrains the angle between line or polyline segments, the angle swept out by an arc or a polyline arc segment, or the angle
between three points on objects.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Parametric panel ![](../images/ac.menuaro.gif) Dimensional Constraint drop-down ![](../images/ac.menuaro.gif) Angular.
![](../images/GUID-3CF36A56-1D6C-42B7-8A31-625FD67A9822-low.png)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Parametric ![](../images/ac.menuaro.gif) Dimensional Constraints ![](../images/ac.menuaro.gif) Angular.

## Summary

This command is equivalent to the Angular option in
[DIMCONSTRAINT](DIMCONSTRAINT-Command.md).

When you enter or edit an angle value that is either negative or is greater than 360 degrees, the number entered is stored
for the expression (for example, 390), but the value displayed is based on the formatting of the units (for example, 30 if
decimal degrees).

When an expression with variables evaluates to greater than 360 or less than -360, the constraint value is displayed in the
Parameters Manager based on the units of the drawing.

The following table outlines the valid constraint objects and points:

| Valid Objects or Points | Characteristics |
| Pair of lines  Pair of polyline segment  Three constraint points  Arc | * When two lines are selected, the angle between the lines is constrained. The initial value always defaults to a value less   than 180 degrees. * When three constraint points are specified, the following applies:   + First point — angle vertex   + Second and third points — endpoints of the angle * When an arc is selected, a three-point angular constraint is created. The angle vertex is at the center of the arc and the   angle endpoints of the arc are at the endpoints of the arc. |

## List of Prompts

The following prompts are displayed.

Select first
[line](DCANGULAR-Command.md) or
[arc](DCANGULAR-Command.md) or [[3Point](DCANGULAR-Command.md)] <3Point>:
*Pick a line, or an arc, or three points to be constrained*

Line

Selects a line object.

First Line
:   Specifies the first line to be constrained.

Second Line
:   Specifies the second line to be constrained.

Dimension Line Location
:   Determines where the dimension line is located on the constrained object.

Arc

Selects an arc and constrains the angle.

Dimension Line Location
:   Determines where the dimension line is located on the constrained object.

3Point

Selects three valid constraint points on the object.

Angle Vertex
:   Specifies the angle vertex, which is at the center point of the constraint.

First Angle Constraint Point
:   Specifies the first angle endpoint of the arc.

Second Angle Constraint Point
:   Specifies the second angle endpoint of the arc.

Dimension Line Location
:   Determines where the dimension line is located on the constrained object.

#### Related Concepts

* [About Dimensional Constraints](About-Dimensional-Constraints.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*