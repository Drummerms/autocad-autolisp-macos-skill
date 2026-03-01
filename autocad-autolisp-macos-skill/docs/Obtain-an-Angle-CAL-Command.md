# Obtain an Angle (CAL Command)

The
*ang* function determines the angle between two lines. Angles are measured counterclockwise with respect to either the
*X* axis, in the two-dimensional case, or to a user-specified axis, in the three-dimensional case.

ang(v)
:   Determines the angle between the
    *X* axis and vector
    *v*. The vector
    *v* is considered 2D, projected on the
    *XY* plane of the current UCS.

ang(p1,p2)
:   Determines the angle between the
    *X* axis and the line (*p1,p2*), oriented from
    *p1* to
    *p2*. The points are considered 2D, projected on the
    *XY* plane of the current UCS.

ang(apex,p1,p2)
:   Determines the angle between lines (*apex,p1*) and (*apex,p2*). The points are considered 2D, projected on the
    *XY* plane of the current UCS.

ang(apex,p1,p2,p)
:   Determines the angle between lines (*apex,p1*) and (*apex,p2*). The lines are considered 3D. The last parameter, point
    *p*, is used to define the orientation of the angle. The angle is measured counterclockwise with respect to the axis going from
    apex to
    *p*.

The following examples show how angles are measured.

![](../images/GUID-CAC31210-EA23-4762-9E4E-9B54059268A1-low.png)

You can determine the angle between the two sides of a triangle using the
*ang* function, as shown in the following example:

Command:
*cal*

>> Expression:
*ang(end,end,end)*

Select the apex of the angle, and then select the two opposite vertices.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*