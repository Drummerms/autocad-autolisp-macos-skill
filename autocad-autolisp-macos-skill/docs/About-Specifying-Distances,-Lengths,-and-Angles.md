# About Specifying Distances, Lengths, and Angles

When creating or moving objects, you can specify a point by moving the cursor to indicate a direction and then entering the
distance.

To specify a line length without entering coordinates, you can specify the second point of the line by moving the cursor
to indicate a direction and then entering the distance from the first point. You can also enter calculated distances and points
using the QuickCalc calculator or the command line calculator (CAL).

You can use direct distance entry to specify points for all commands requiring more than one point. When the cursor is locked
to an angle with Ortho mode or polar tracking is on, this method is an efficient way to create lines of specified length and
direction, and to move or copy objects.

## Specify an Angle Override

To specify an angle override, enter a left angle bracket (<) followed by an angle whenever a command prompts you to specify
a point. The example below demonstrates how to specify a 30-degree angle override when you create a line.

Command: *line*

Specify first point: *Specify a start point for the line*

Specify next point or [Undo]: *<**30*

Angle Override: *30*

Specify next point or [Undo]: *Specify a point*

The angle you specify will lock the cursor, overriding Grid Snap, Ortho mode, and PolarSnap. However, coordinates and object
snaps take precedence over an angle override.

#### Related Information

* [To Create a Line Using a Direction and a Distance](To-Create-a-Line-Using-a-Direction-and-a-Distance.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*