# About Specifying a Point Relative to an Existing Point

You can specify a point that is located a specified distance and direction from a temporary point, or a series of temporary
points.

## Using the Tracking Method

You can use the tracking method whenever you are prompted for a point. Tracking uses the pointing device to specify a point
by offsetting vertically and horizontally from a series of temporary points. When you start tracking and specify an initial
reference point, the next reference point is constrained to a path that extends vertically or horizontally from that point.
The direction of the offset is indicated by the rubber-band line. You change the direction of the offset by moving the cursor
through the reference point. You can track as many points as you need. Typically, you use tracking in combination with object
snaps or direct distance entry.

For example, you can use tracking to find the center point of a rectangle without using construction lines. Start tracking,
and specify the midpoint of a horizontal line. Drag the cursor vertically and specify the midpoint of a vertical line (2).
Press Enter to accept the point (3) at the center of the rectangle.

![](../images/GUID-55291241-34C0-4CD7-B7B7-0FC1E3E20B65-low.png)

## Using the From Method

Similar to the tracking method, you can establish a temporary reference point as a base point for offsetting subsequent points.
The From command modifier establishes a temporary reference point as a base point for offsetting subsequent points, and usually
is used in combination with object snaps. The From method does not constrain the cursor to the horizontal and vertical directions.

## Dimension Input With Dynamic Tooltips

When dimension input is turned on for dynamic tooltips, the tooltip displays distance and angle values when a command prompts
you for a second point. The values in the dimension tooltips change as you move the cursor. Press Tab to move to the value
that you want to change. Dimensional input is available for the ARC, CIRCLE, ELLIPSE, LINE, and PLINE commands.

![](../images/GUID-75732BD3-F180-4CF5-98C9-5A3C571266CB-low.png)

When you use grips to edit an object, the dimension input tooltip can display the following information:

* Original length
* A length that updates as you move the grip
* The change in the length
* Angle
* The change in the angle as you move the grip
* The radius of an arc

![](../images/GUID-7D2A7705-89AD-4CBF-82A1-64831C0B867C-low.png)

If this is too much information, use the dimension input settings to display only the information that you want to see.

When you use grips to stretch objects or when you create new objects, dimension input displays only acute angles: all angles
are displayed as 180 degrees or less. Thus, an angle of 270 degrees is displayed as 90 degrees regardless of the ANGDIR system
variable setting. Angles specified when creating new objects rely on the cursor location to determine the positive angle direction.

#### Related Tasks

* [To Specify a Point From a Temporary Reference Point](To-Specify-a-Point-From-a-Temporary-Reference-Point.md)
* [To Specify a Point Relative to a Series of Orthogonal Offsets](To-Specify-a-Point-Relative-to-a-Series-of-Orthogonal-Offsets.md)

#### Related References

* [FROM (Command Modifier)](FROM-Command-Modifier.md)

#### Related Concepts

* [About Specifying Distances, Lengths, and Angles](About-Specifying-Distances,-Lengths,-and-Angles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*