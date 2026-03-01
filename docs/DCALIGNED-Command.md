# DCALIGNED (Command)

Constrains the distance between two points on different objects.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Parametric panel ![](../images/ac.menuaro.gif) Dimensional Constraint drop-down ![](../images/ac.menuaro.gif) Aligned.
![](../images/GUID-DFF73B4D-AEB3-42B7-A6EC-DD0E98B1CE08-low.png)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Parametric ![](../images/ac.menuaro.gif) Dimensional Constraints ![](../images/ac.menuaro.gif) Aligned.

## Summary

This command is equivalent to the Aligned option in
[DIMCONSTRAINT](DIMCONSTRAINT-Command.md).

The following table outlines the valid constraint objects and points:

| Valid Objects or Points | Characteristics |
| Line  Polyline segment  Arc  Two constraint points on objects  Line and constraint point  Two lines | * When a line or an arc is selected, the distance between the endpoints of the object is constrained. * When a line and a constraint point are selected, the distance between the point and the closest point on the line is constrained. * When two lines are selected, the lines are made parallel and the distance between them is constrained. |

## List of Prompts

The following prompts are displayed.

Specify first
[contraint point](DCALIGNED-Command.md) or [[Object](DCALIGNED-Command.md)/[Point & line](DCALIGNED-Command.md)/[2Lines](DCALIGNED-Command.md)] <Object>:
*Pick a constraint point or select an object, a point and a line, or two lines to be constrained*

Constraint Point

Specifies a constraint point for the object.

First Constraint Point
:   Specifies the first point of the object to be constrained.

Second Constraint Point
:   Specifies the second point of the object to be constrained.

Dimension Line Location
:   Determines where the dimension line is located on the constrained object.

Object

Selects an object instead of a constraint point.

Dimension Line Location
:   Determines where the dimension line is located on the constrained object.

Point & Line

Selects a point and a line object. The aligned constraint controls the distance between a point and the closest point on a
line.

Constraint Point
:   [Constraint Point](DCALIGNED-Command.md)

Line
:   Selects a line object.

Dimension Line Location
:   Determines where the dimension line is located on the constrained object.

2Lines

Selects two line objects. The lines are made parallel and the aligned constraint controls the distance between the two lines.

First Line
:   Select the first line to be constrained.

Second Line to Make Parallel
:   Select the second line to constrain the distance between the two selected lines.

Dimension Line Location
:   Determines where the dimension line is located on the constrained object.

#### Related Concepts

* [About Dimensional Constraints](About-Dimensional-Constraints.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*