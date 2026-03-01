# About Tracking Points Automatically Using Object Snaps

You can create objects at specific angles or in specific relationship to other objects along specified directions called alignment
paths.

AutoTrack ™  helps you draw objects at specific angles or in specific relationships to other objects. When you turn on AutoTrack, temporary
*alignment* paths help you create objects at precise locations and angles. AutoTrack includes two tracking options: polar tracking and
object snap tracking.

You can toggle AutoTrack on and off with the Polar and Object Snap Tracking buttons on the status bar. Use temporary override
keys to turn object snap tracking on and off or to turn off all snapping and tracking.

## Object Snap Tracking

Object snap tracking works in conjunction with object snaps. Use object snap tracking to track along alignment paths that
are based on object snap points. Acquired points display a small plus sign (+). After you acquire a point, horizontal, vertical,
or polar alignment paths relative to the point are displayed as you move the cursor over their drawing paths. For example,
you can select a point along a path based on an object endpoint or midpoint or an intersection between objects.

NOTE:You can track Perpendicular or Tangent object snap from the last picked point in a command even if the object snap tracking
is off.

In the following illustration, the Endpoint object snap is on. You start a line by clicking its start point (1), move the
cursor over another line's endpoint (2) to acquire it, and then move the cursor along the horizontal alignment path to locate
the endpoint you want for the line you are drawing (3).

![](../images/GUID-1A88D26C-83C0-46E4-85CB-33BC662FB55B-low.png)

## Change Object Snap Tracking Settings

By default, object snap tracking is set to orthogonal. Alignment paths are displayed at 0, 90, 180, and 270 degrees from acquired
object points. However, you can use polar tracking angles instead. For object snap tracking, object points are automatically
acquired.

## Change Alignment Path Display

You can change how AutoTrack displays alignment paths, and you can change how object points are acquired for object snap
tracking. By default, alignment paths stretch to the end of the drawing window. You can change their display to abbreviated
lengths, or no length.

## Tips for Using Object Snap Tracking

As you use AutoTrack (polar tracking and object snap tracking), you will discover techniques that make specific design tasks
easier.

* Use Perpendicular, End, and Mid object snaps with object snap tracking to draw to points that are perpendicular to the end
  and midpoints of objects.
* Use the Tangent and End object snaps with object snap tracking to draw to points that are tangent to the endpoints of arcs.
* Use object snap tracking with temporary tracking points. At a point prompt, enter
  *tt*, then specify a temporary tracking point. A small *+*appears at the point. As you move your cursor, AutoTrack alignment paths are displayed relative to the temporary point. To
  remove the point, move the cursor back over the +.
* After you acquire an object snap point, use direct distance to specify points at precise distances along alignment paths from
  the acquired object snap point. To specify a point prompt, select an object snap, move the cursor to display an alignment
  path, then enter a distance at the prompt.
* Use the Automatic and Shift to Acquire options set on the Drafting tab of the Options dialog box to manage point acquisition.
  Point acquisition is set to Automatic by default. When working in close quarters, press Shift to temporarily avoid acquiring
  a point.
* To facilitate creating section lines, an AutoTrack
  *extension* capability is available in paper space. For example, acquisition points between the centers of two circles along a diagonal
  can be used to extend a section line along the angle between those points. The acquisition points can be extracted from objects
  created either in model space or in paper space.

NOTE: The direct distance entry method is not available while you are using the temporary override key for object snap tracking.

#### Related References

* [TRACKING (Command Modifier)](TRACKING-Command-Modifier.md)

#### Related Information

* [To Change AutoTrack Settings](To-Change-AutoTrack-Settings.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*