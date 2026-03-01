# Calculate a Normal Vector (CAL Command)

The
*nor* function calculates the unit normal vector (a vector perpendicular to a line or plane), not a point. The vector defines the
direction of the normal, not a location in space. You can add this normal vector to a point to obtain another point.

nor
:   Determines the three-dimensional unit normal vector of a selected circle, arc, or polyline arc segment. This normal vector
    is the
    *Z* coordinate of the object coordinate system (OCS) of the selected object.

nor(v)
:   Determines the two-dimensional unit normal vector to vector
    *v*. Both vectors are considered 2D, projected on the
    *XY* plane of the current UCS. The orientation of the resulting normal vector points to the left of the original vector
    *v*.

nor(p1,p2)
:   Determines the 2D unit normal vector to line
    *p1,p2*. The line is oriented from
    *p1* to
    *p2*. The orientation of the resulting normal vector points to the left from the original line (*p1,p2*).

nor(p1,p2,p3)
:   Determines the 3D unit normal vector to a plane defined by the three points
    *p1, p2*, and
    *p3*. The orientation of the normal vector is such that the given points go counterclockwise with respect to the normal.

The following illustrations show how normal vectors are calculated:

![](../images/GUID-5CEF0C6D-7C8A-4CEE-BF15-19F683B36998-low.png)

The following example sets the view direction perpendicular to a selected object. The program displays the object in plan
view and does not distort the object by the parallel projection.

Command:
*vpoint*

Current view direction: VIEWDIR=*current*

Specify a view point or [Rotate] <display compass and tripod>:
*'cal*

>> Expression:
*nor*

>> Select circle, arc or polyline for NOR function:

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*