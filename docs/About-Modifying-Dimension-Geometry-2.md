# About Modifying Dimension Geometry

You can modify dimensions with the editing commands and with grip editing.

Grip editing is the quickest and easiest way to modify dimensions. How you edit dimensions depends on whether the dimension
is associative.

## Modify Associative Dimensions

Associative dimensions stay associated to dimensioned objects when these objects, and the associated geometry are selected
and operated on with a single command. For example, if a dimension and its associated geometry are moved, copied, or arrayed
in the same command, each dimension remains associated to its respective geometry.

In some circumstances, dimensions are automatically disassociated, including

* If the associated geometric object is erased
* If the associated geometric object undergoes a boolean operation such as UNION or SUBTRACT
* If grip editing is used to stretch a dimension parallel to its dimension line
* If the association to a geometric object is specified using the Apparent Intersection object snap, and the geometric object
  is moved so that the apparent intersection no longer exists

In other circumstances, a dimension may become partially associated. If a linear dimension is associated with the endpoints
of two geometric objects and one of the objects is erased, the remaining association is preserved. The disassociated end of
the linear dimension may then be associated with another geometric object using DIMREASSOCIATE.

NOTE:The Command prompt displays a warning message when a dimension is disassociated.

## Modify Non-associative Dimensions

For non-associative dimensions, when you edit dimensioned objects, you must include the relevant dimension definition points
in the selection set, or the dimension is not updated. Definition points determine the dimension location. For example, to
stretch a dimension, you include the appropriate definition points in the selection set. You can easily include them by turning
on grips and selecting the object so that the grips are highlighted.

The definition points for each type of dimension are indicated in the following illustrations. The middle point of the dimension
text is a definition point for all dimension types.

![](../images/GUID-8BF98ECE-F62A-4409-8160-877CE341A115-low.png)

If no angle vertex is shown, definition points are placed at the ends of the lines that form the angle. In the two-line angular
example, a definition point is placed at the center point of the dimensioned arc.

NOTE:Definition points are created on a special layer named Defpoints that is never printed or plotted.

## Use Dimension Line Grips

Hover over the grip on the endpoint of a dimension line to quickly access the following functionality:

* *Stretch.* Stretches the extension lines to move the dimension line farther away or closer to the object being dimensioned. Use command
  line prompts to specify a different base point or copy the dimension line.
* *Continue dimension.* Invokes the DIMCONTINUE command.
* *Baseline dimension.* Invokes the DIMBASELINE command.
* *Flip arrow.* Flips the direction of the dimension arrowhead.

## Modify Exploded Dimensions

You can edit exploded dimensions as you would any other objects because an exploded dimension is a collection of separate
objects: Lines, 2D solids, and text. Occasionally you may need to explode a dimension to perform operations such as creating
a break in a dimension line or extension line. Once a dimension is exploded, you cannot reassociate the dimension into a dimension
object.

#### Related Concepts

* [About Changing Dimension Associativity](About-Changing-Dimension-Associativity.md)
* [About Adjusting the Spacing Between Dimensions](About-Adjusting-the-Spacing-Between-Dimensions.md)
* [About Creating Breaks in Dimensions](About-Creating-Breaks-in-Dimensions.md)
* [About Adding a Jog to a Linear Dimension](About-Adding-a-Jog-to-a-Linear-Dimension.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*