# MIRROR3D (Command)

Creates a mirrored copy of selected objects across a mirroring plane.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) 3D Mirror.
![](../images/GUID-9C86B6FB-83F2-4569-91F9-D08837AE0004-low.png)

*Menu*:
Modify
![](../images/ac.menuaro.gif) 3D Operations
![](../images/ac.menuaro.gif) 3D Mirror.

## Summary

It is recommended that you use the gizmos available through the
[3DMOVE](3DMOVE-Command.md),
[3DROTATE](3DROTATE-Command.md), and
[3DSCALE](3DSCALE-Command.md) commands to manipulate 3D objects.

For example:

![](../images/GUID-73E204D4-50E7-4C90-A531-44581772418C-low.gif)

## List of Prompts

The following prompts are displayed.

Select objects: *Use an object selection method and press*Enter *to finish*

Specify first point of mirror plane (3 points) or [Object/Last/Zaxis/View/XY/YZ/ZX/3points] <3points>: *Enter an option, specify a point, or press*Enter

![](../images/GUID-9DEE46E8-55B8-4FDA-90B8-D6C986994710-low.png)

Object
:   Uses the plane of a selected planar object as the mirroring plane.

    ![](../images/GUID-229591F7-A477-4FD6-8F59-09DD2459EF08-low.png)

Delete Source Objects
:   If you enter
    *y*, the reflected object is placed into the drawing and the original objects are deleted. If you enter
    *n*or press Enter, the reflected object is placed into the drawing and the original objects are retained.

Last
:   Mirrors the selected objects about the last defined mirroring plane.

Z Axis
:   Defines the mirroring plane by a point on the plane and a point normal to the plane.

    ![](../images/GUID-0A36687B-369D-4EDB-82E9-7A759E6F053A-low.png)

View
:   Aligns the mirroring plane with the viewing plane of the current viewport through a point.

XY/YZ/ZX
:   Aligns the mirroring plane with one of the standard planes
    *(XY*,
    *YZ*, or
    *ZX)* through a specified point.

    ![](../images/GUID-97ADE9DD-F5A3-4386-876C-B466B4707831-low.png)

3 Points
:   Defines the mirroring plane by three points. If you select this option by specifying a point, the First Point on Mirror Plane
    prompt is not displayed.

    ![](../images/GUID-74B0C44C-09D5-447B-AA84-0D7842B29732-low.png)

#### Related Concepts

* [About Mirroring Objects](About-Mirroring-Objects.md)
* [About Using 3D Gizmos](About-Using-3D-Gizmos.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*