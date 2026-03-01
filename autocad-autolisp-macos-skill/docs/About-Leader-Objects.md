# About Leader Objects

A leader object is a line or a spline with an arrowhead at one end and a multiline text object or block at the other.

In some cases, a short horizontal line, called a landing, connects text or blocks and feature control frames to the leader
line.

The landing and leader line are associated with the multiline text object or block, so when the landing is relocated, the
content and leader line move along with it.

![](../images/GUID-979AF8A8-A819-4E54-B566-D42CD3A543D4-low.png)

When associative dimensioning is turned on and object snaps are used to locate the leader arrowhead, the leader is associated
with the object to which the arrowhead is attached. If the object is relocated, the arrowhead is relocated, and the landing
stretches accordingly.

NOTE: The leader object should not be confused with the leader line that is automatically generated as part of a dimension line.

Associativity between a leader and an object may be lost for several reasons. For example:

* Associativity is not maintained between a leader and a block reference, if the block is redefined such that the point the
  leader is attached to moves.
* Associativity is not maintained between a leader and a model documentation drawing view, when an update or edit event removes
  point attached to the leader.

You can use the annotation monitor to track leader associativity. When the annotation monitor is on, it flags leaders that
lose associativity by displaying a badge on the leader. (See ANNOMONITOR.)

Clicking a badge displays a menu that contains options specific to the corresponding disassociated annotation. The menu on
a leader that has lost associativity provides access to the DIMREASSOCIATE and ERASE commands.

## Rotated Views

Leader landings, components of dimensions, and text objects determine their horizontal and vertical directions from the UCS
axes at the time when they are created. If a view in a drawing is rotated, you can first use the UCS /View option to set the
horizontal and vertical directions relative to the
*drawing* rather than the rotated view.

#### Related Tasks

* [To Convert a Multiline Text to a Leader](To-Convert-a-Multiline-Text-to-a-Leader.md)

#### Related Concepts

* [About Creating Leaders](About-Creating-Leaders.md)

#### Related Information

* [To Create a Leader With Straight Lines](To-Create-a-Leader-With-Straight-Lines.md)
* [To Work with the Annotation Monitor](To-Work-with-the-Annotation-Monitor.md)
* [To Create a Leader Attached to Block Content at an Angle](To-Create-a-Leader-Attached-to-Block-Content-at-an-Angle.md)
* [To Create a Spline Leader With Text or a Block](To-Create-a-Spline-Leader-With-Text-or-a-Block.md)
* [To Create Multiple Leaders From the Same Annotation](To-Create-Multiple-Leaders-From-the-Same-Annotation.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*