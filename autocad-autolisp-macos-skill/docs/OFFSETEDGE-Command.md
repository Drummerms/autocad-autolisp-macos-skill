# OFFSETEDGE (Command)

Creates a closed polyline or spline object that is offset at a specified distance from the edges of a selected planar face
on a 3D solid or surface.

## Summary

You can offset the edges of a planar face on a 3D solid or surface. The result is a closed polyline or spline that is located
on the same plane as the selected face or surface, and can be inside or outside the original edges.

TIP:You can use the resulting object with
[PRESSPULL](PRESSPULL-Command.md) or
[EXTRUDE](EXTRUDE-Command.md) to create new solids.

![](../images/GUID-44FA3DE4-1DF2-4819-9A15-388D1B5E3939-low.png)

## List of Prompts

The following prompts are displayed.

Corner =
*current*

Select face:
*Select a planar face on a 3D solid or surface*

Specify through point or [Distance/Corner] <*current*>:
*Specify a point, or enter an option*

Through Point

Creates an offset object that passes through the specified point. This point is always projected line-of-sight onto the plane
of the selected face.

Distance

Creates an offset object at a specified distance from the edges of the selected face.

Specify distance: <*current*>
:   Enter the offset distance, or press Enter to accept the current distance.

Specify point on side to offset
:   Specify a point location to determine whether the offset distance is applied inside or outside the edges of the face.

Corner

Specifies the type of corners on the offset object when it is created outside the edges of the selected face.

Sharp
:   Creates sharp corners between offset linear segments.

Rounded
:   Creates rounded corners between offset linear segments, using a radius that is equal to the offset distance.

#### Related Concepts

* [About Offsetting Objects](About-Offsetting-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*