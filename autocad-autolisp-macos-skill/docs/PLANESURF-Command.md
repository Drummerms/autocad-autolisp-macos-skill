# PLANESURF (Command)

Creates a planar surface.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Surface panel ![](../images/ac.menuaro.gif) Surface drop-down ![](../images/ac.menuaro.gif) Planar Surface.
![](../images/GUID-55C167E8-35D2-443F-9A10-B048C1BB20ED-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Surfaces ![](../images/ac.menuaro.gif) Planar.

## Summary

You can create a planar surface by selecting closed objects or by specifying the opposite corners of a rectangular surface.
Supports pick-first selection and generates a planar surface out of a closed profile. When you specify the corners of the
surface through the command, the surface is created parallel to the work plane.

![](../images/GUID-9C095495-9CE2-4CC1-BD42-733AFD314552-low.gif)

The
[SURFU](SURFU-System-Variable.md) and
[SURFV](SURFV-System-Variable.md) system variables control the number of lines displayed on the surface.

## List of Prompts

The following prompts are displayed.

Specify first corner or [Object]:
*Specify the first point for the planar surface*

Specify other corner:
*Specify second point (other corner) for the planar surface*

Object

Creates a planar or trimmed surface by object selection. You can select one closed object or multiple objects that form a
closed area.

Similar to the
[REGION](REGION-Command.md) command, valid objects include: line, circle, arc, ellipse, elliptical arc, 2D polyline, planar 3D polyline, and planar spline.

The
[DELOBJ](DELOBJ-System-Variable.md) system variable controls whether the object(s) you select are automatically deleted when the surface is created or whether
you are prompted to delete the object(s).

#### Related Concepts

* [About Creating Planar Surfaces](About-Creating-Planar-Surfaces.md)
* [About Creating Procedural Surfaces](About-Creating-Procedural-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*