# TORUS (Command)

Creates a donut-shaped 3D solid.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Solid drop-down ![](../images/ac.menuaro.gif) Torus.
![](../images/GUID-E80D156A-33DD-4D8B-9915-9A11DA80CF56-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Torus.

## Summary

You can create a torus by specifying the center, then the radius or diameter of the torus, and then the radius or diameter
of the tube that surrounds the torus. You can control the smoothness of curved 3D solids, such as a torus, in a shaded or
hidden visual style with the FACETRES system variable.

![](../images/GUID-846834AC-447C-4838-AEF7-46501E6B8004-low.gif)

## List of Prompts

The following prompts are displayed.

Specify center point or [[3P](TORUS-Command.md)/[2P](TORUS-Command.md)/[TTR](TORUS-Command.md)]: *Specify a point (1) or enter an option*

When you specify the center point, the torus is positioned so that its central axis is parallel to the
*Z* axis of the current user coordinate system (UCS). The torus is parallel to and bisected by the
*XY* plane of the current workplane.

Specify
[radius](TORUS-Command.md) or [[diameter](TORUS-Command.md)] <default>: *Specify a distance or enter**d*

![](../images/GUID-53FC4C39-0A82-4E4B-BEF3-F8A8AD10405A-low.png)

3P (Three Points)

Defines the circumference of the torus with three points that you specify. The three specified points also define the plane
of the circumference.

2P (Two Points)

Defines the circumference of the torus with two points that you specify. The plane of the circumference is defined by the
*Z* value of the first point.

TTR (Tangent, Tangent, Radius)

Defines the torus with a specified radius tangent to two objects. The specified tangency points are projected onto the current
UCS.

Radius

Defines the radius of the torus: the distance from the center of the torus to the center of the tube. A negative radius creates
a solid shaped like an American football.

Radius
:   Defines the radius of the tube.

Diameter
:   Defines the diameter of the tube.

    ![](../images/GUID-338A4DE5-B2D2-4D31-B7DA-A43AD4A1E9C2-low.png)

Diameter

Defines the diameter of the torus.

* [Radius](TORUS-Command.md)
* [Diameter](TORUS-Command.md)

#### Related Concepts

* [About Creating Basic 3D Solids and Walls](About-Creating-Basic-3D-Solids-and-Walls.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*