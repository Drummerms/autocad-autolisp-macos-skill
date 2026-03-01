# DIST (Command)

Measures the distance and angle between two points.

## Access Method

![](../images/ac.keyboard.gif) Command entry:  *'dist* for transparent use

## Summary

In general, the DIST command reports 3D distances in model space and 2D distances on a layout in paper space.

In model space, changes in X, Y, and Z component distances and angles are measured in 3D relative to the current UCS.

In paper space, distances are normally reported in 2D paper space units. However, when using object snaps on model space objects
that are displayed in a single viewport, distances are reported as 2D model space distances projected onto a plane parallel
to your screen.

## List of Prompts

The following prompts are displayed.

Specify first point: *Specify a point*

Specify second point or <Multiple points>: *Specify a second point*

The distance is displayed in the current units format.

![](../images/GUID-9328500E-343B-4763-89F8-6DEAE87C8A3A-low.png)

DIST assumes the current elevation for the first or second point if you omit the *Z* coordinate value.

NOTE:When using the DIST command for 3D distances, it is recommended that you switch to model space.

Multiple Points
:   If you specify multiple points, a running total of the distance based on the existing line segments and the current rubberband
    line is displayed in the tooltip. A dynamic dimension is also displayed. The distance is updated as you move the cursor.

#### Related Tasks

* [To Find the Distance and Angle Between two Points](To-Find-the-Distance-and-Angle-Between-two-Points.md)
* [To Find the Cumulative Distance Between a Series of Points](To-Find-the-Cumulative-Distance-Between-a-Series-of-Points.md)

#### Related Concepts

* [About Finding Distances, Angles, and Point Locations](About-Finding-Distances,-Angles,-and-Point-Locations.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*