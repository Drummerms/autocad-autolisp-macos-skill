# About Polar Tracking and PolarSnap

Polar tracking restricts cursor movement to specified angles. PolarSnap restricts cursor movement to specified increments
along a polar angle.

When you create or modify objects, you can use polar tracking to display temporary alignment paths defined by the polar angles
you specify. In 3D views, polar tracking additionally provides an alignment path in the up and down directions. In that case,
the tooltip displays a +Z or -Z for the angle.

Polar angles are relative to the orientation of the current user coordinate system (UCS) and the setting for the base angle
convention in a drawing, which is set in the Drawing Units dialog box.

Use PolarSnap™ to snap to specified distances along the polar alignment path. For example, in the following illustration you
draw a two-unit line from point 1 to point 2, and then draw a two-unit line to point 3 at a 45-degree angle to the line. If
you turn on the 45-degree polar angle increment, an alignment path and tooltip are displayed when your cursor crosses the
0 or 45-degree angle. The alignment path and tooltip disappear when you move the cursor away from the angle.

![](../images/GUID-DB5AC26A-87F8-4E12-A194-D8E0EEC1364E-low.png)

As you move your cursor, alignment paths and tooltips are displayed when you move the cursor near specified polar angles.
The default angle measurement is 90 degrees. Use the alignment path and tooltip to draw your object. You can use polar tracking
with Intersection and Apparent Intersection object snaps to find where a polar alignment path intersects another object.

NOTE:Ortho mode and polar tracking cannot be turned on at the same time. Turning on polar tracking turns off Ortho mode. Similarly,
PolarSnap and grid snap cannot be turned on at the same time. Turning on PolarSnap turns off grid snap.

## Specify Polar Angles (Polar Tracking)

You can use polar tracking to track along polar angle increments of 90, 60, 45, 30, 22.5, 18, 15, 10, and 5 degrees, or you
can specify different angles. The following illustration shows the alignment paths displayed as you move your cursor 90 degrees
with the polar angle increment set to 30 degrees.

![](../images/GUID-1613B5FC-4BD0-4C8A-BB64-C51D092FB3F9-low.png)

The orientation of 0 depends on the angle you set in the Drawing Units dialog box. The direction of snap (clockwise or counterclockwise)
depends on the units direction you specify when setting units of measurement.

You can turn polar tracking on and off temporarily by using an override key. The direct distance entry method is not available
while you are using the temporary override key for polar tracking.

## Specify Polar Distances (PolarSnap)

PolarSnap restricts cursor movement to incremental distances along a polar tracking angle. For example, if you specify a
distance of 4 units, the cursor snaps from the first point specified to distances of 0, 4, 8, 12, 16, and so on. As you move
your cursor, a tooltip indicates the nearest PolarSnap increment. To restrict point entry to polar distances, both polar tracking
and Snap mode (set to PolarSnap) must be on.

#### Related Tasks

* [To Turn On and Turn Off Polar Tracking](To-Turn-On-and-Turn-Off-Polar-Tracking.md)
* [To Set Polar Tracking Angles](To-Set-Polar-Tracking-Angles.md)
* [To Set the Polar Snap Distance](To-Set-the-Polar-Snap-Distance.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*