# 3DALIGN (Command)

Aligns objects with other objects in 2D and 3D.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) 3D Align.
![](../images/GUID-6F686F1A-9AB0-4EFA-AD0C-77ABF0FA85A2-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) 3D Operations ![](../images/ac.menuaro.gif) 3D Align.

## Summary

You can specify one, two, or three points for the source object. Then, you can specify one, two, or three points for the destination.

![](../images/GUID-7FF8F93D-C9E6-410E-B7E2-DC473EA27214-low.gif)

## List of Prompts

The following prompts are displayed.

Select objects: *Select the objects to align and press* Enter

Specify source plane and orientation . . .

The selected object is moved and rotated so that the base points, and the
*X* and
*Y* axes of the source and destination align in 3D space. 3DALIGN works with dynamic UCS (DUCS), so you can dynamically drag
the selected objects and align them with the face of a solid object.

Specify base point or [Copy]: *Specify a point or enter* *c* *to create a copy*

The base point of the source object will be moved to the base point of the destination.

Specify second point or [Continue] <C>:
*Specify a point on the object’s X axis, or press Enter to skip forward to specifying destination points*

The second point specifies a new
*X* axis direction within a plane parallel to the
*XY* plane of the current UCS. If you press Enter instead of specifying a second point, the
*X* and
*Y* axes are assumed to be parallel with the
*X* and
*Y* axes of the current UCS.

Specify third point or [Continue] <C>: *Specify a point on the object’s positive XY plane, or press Enter to skip forward to specifying destination points*

The third point fully specifies the orientation of the
*X* and
*Y* axes of the source object that will be aligned with the destination plane.

Specify destination plane and orientation . . .

Specify first destination point: *Specify a point*

This point defines the destination of the base point of the source object.

Specify second source point or [eXit] <X>: *Specify a point for the X axis of the destination or press* Enter

The second point specifies a new
*X* axis direction for the destination within a plane parallel to the
*XY* plane of the current UCS. If you press Enter instead of specifying a second point, the
*X* and
*Y* axes of the destination are assumed to be parallel with the
*X* and
*Y* axes of the current UCS.

Specify third destination point or [eXit] <X>:
*Specify a point for the destination’s positive XY plane, or press* Enter

The third point fully specifies the orientation of the
*X* and
*Y* axes of the destination plane.

NOTE:If the destination is a plane on an existing solid object, you can define the destination plane with a single point by turning
on dynamic UCS.

#### Related Concepts

* [About Aligning Objects](About-Aligning-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*