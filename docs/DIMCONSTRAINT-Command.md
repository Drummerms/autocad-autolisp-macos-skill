# DIMCONSTRAINT (Command)

Applies dimensional constraints to selected objects or points on objects, or converts associative dimensions to dimensional
constraints.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Parametric panel ![](../images/ac.menuaro.gif) Dimensional Constraint drop-down.
![](../images/GUID-506AB966-57B9-439B-941B-062A8D20B594-low.png)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Parametric ![](../images/ac.menuaro.gif) Dimensional Constraints.

## Summary

Applies a dimensional constraint to a selected object or converts an associative dimension to a dimensional constraint.

NOTE:The L option (last object drawn) is not allowed in the DIMCONSTRAINT command as the constraint behavior is dependent on where
you pick the object.

The following table outlines the valid constraint points for an object.

| Objects | Valid Constraint Points |
| Line | Endpoints, Midpoint |
| Arc | Center, Endpoints, Midpoint |
| Spline | Endpoints |
| Ellipse, Circle | Center |
| Polyline | Endpoints, midpoints of line and arc subobjects, center of arc subobjects |
| Block, Xref, Text, Mtext, Attribute, Table | Insertion point |

After you specify the dimensional constraint type, you can either enter an expression value or accept the default (constraintname=value).

The DIMCONSTRAINT command gives the same options as the following commands:

Linear ([DCLINEAR](DCLINEAR-Command.md))
:   Creates a horizontal, vertical, or rotated constraint based on the locations of the extension line origins and the dimension
    line.

Horizontal ([DCHORIZONTAL](DCHORIZONTAL-Command.md))
:   Constrains the X distance between points on an object, or between two points on different objects.

Vertical ([DCVERTICAL](DCVERTICAL-Command.md))
:   Constrains the Y distance between points on an object, or between two points on different objects.

Aligned ([DCALIGNED](DCALIGNED-Command.md))
:   Constrains the distance between two points on different objects.

Angular ([DCANGULAR](DCANGULAR-Command.md))
:   Constrains the angle between line or polyline segments, the angle swept out by an arc or a polyline arc segment, or the angle
    between three points on objects.

Radius ([DCRADIUS](DCRADIUS-Command.md))
:   Constrains the radius of a circle or an arc.

Diameter ([DCDIAMETER](DCDIAMETER-Command.md))
:   Constrains the diameter of a circle or an arc.

Form ([DCFORM](DCFORM-Command.md))
:   Specifies whether the dimensional constraint being created is dynamic or annotational.

Convert ([DCCONVERT](DCCONVERT-Command.md))
:   Converts associative dimensions to dimensional constraints.

#### Related Concepts

* [About Dimensional Constraints](About-Dimensional-Constraints.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*