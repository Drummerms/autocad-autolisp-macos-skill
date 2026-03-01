# About Chamfers and Bevels

A chamfer or bevel connects two objects with an angled line in 2D, or creates an angled face between the adjacent faces of
a 3D solid.

You can create a chamfer or bevel using the CHAMFER command.

These object types can be selected to define a chamfer or bevel:

* 2D polylines
* 3D solids and surfaces (not available in AutoCAD LT)
* Lines
* Rays
* Xlines

![](../images/GUID-CC33098A-1E5C-45C3-8988-5926CF83C568-low.png)

## Length and Angle of a Chamfer or Bevel

A chamfer or bevel can be defined using one of two methods; distance or angle. The current method to define a chamfer or
bevel is set with the Method option.

* *Distance.* The resulting angled line is based on two distance values. The distance values are used to trim or extend the selected objects
  to meet the resulting angled line. The first distance value affects the first object selected, while the second distance value
  affects the second object selected.

  ![](../images/GUID-9E0159E7-80F8-42D7-861A-FDC3C9B6CC68-low.png)
* *Angle.* The resulting angled line is based on a distance and an angle value. The distance and angular value are used to trim or extend
  the selected objects to meet the resulting angled line. The distance value directly affects the first object selected.

  ![](../images/GUID-0285D815-21EC-4792-954E-6EFF0C966276-low.png)

NOTE:If the distance and angle values are set to 0, the selected objects are trimmed or extended until they intersect and no angled
line is created.

## Add Chamfers and Bevels to 2D Polylines

A chamfer or bevel can be inserted at a single vertex or all the vertices of a 2D polyline using a single command. Use the
Polyline option add a chamfer or bevel to each vertex of a polyline.

![](../images/GUID-D8EFE0A5-232E-4786-8454-2BEF31D7D70D-low.png)

NOTE:The Multiple option can also be used to chamfer or bevel more than one set of objects without exiting the command.

You add a chamfer or bevel to a polyline by setting the current distance or angle values to a nonzero value and selecting
two 2D polyline segments that intersect. The distance between the selected line segments must be long enough to accommodate
the resulting angled line, otherwise the angled line will not be inserted. If the selected line segments are separated by
no more than one arc segment, the arc segment is removed and replaced with a new line segment that represents the chamfer
or bevel.

When the current distance and angle values are set to 0 and the two line segments selected are separated by an arc segment,
the arc segment is removed and the two line segments are extended until they intersect.

NOTE:Chamfering the start and end segments of an open polyline results in a closed polyline.

## Trim and Extend Objects

By default, the objects selected to define a chamfer or bevel are trimmed or extended to the resulting angled line. You can
use the Trim option to specify whether the selected objects are changed or left unchanged.

![](../images/GUID-843D3A18-7772-4952-B643-07038CCDC725-low.png)

If the Trim option is enabled and two line segments of a polyline are selected, the chamfer or bevel added is joined with
the polyline as a new line segment.

#### Related Concepts

* [About Fillets and Rounds](About-Fillets-and-Rounds.md)

#### Related Information

* [To Work With 2D Chamfers and Bevels](To-Work-With-2D-Chamfers-and-Bevels.md)
* [To Work With 2D Fillets and Rounds](To-Work-With-2D-Fillets-and-Rounds.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*