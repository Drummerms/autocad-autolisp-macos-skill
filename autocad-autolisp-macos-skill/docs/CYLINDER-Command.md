# CYLINDER (Command)

Creates a 3D solid cylinder.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Solid drop-down ![](../images/ac.menuaro.gif) Cylinder.
![](../images/GUID-B5FCBEFD-B5F8-4D76-AFA2-0CFA4C896D24-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Cylinder.

## Summary

In the illustration, the cylinder was created using a center point (1), a point on the radius (2), and a point for the height
(3). The base of the cylinder is always on a plane parallel with the workplane. You can control the smoothness of curved 3D
solids, such as a cylinder, in a shaded or hidden visual style with the FACETRES system variable.

![](../images/GUID-D53B665F-6880-4F72-978E-B416BF0FEE18-low.gif)

During a drawing session, the default value for the base radius is always the previously entered base radius value.

## List of Prompts

The following prompts are displayed.

Specify center point of base or [[3P](CYLINDER-Command.md)/[2P](CYLINDER-Command.md)/[Ttr](CYLINDER-Command.md)/[Elliptical](CYLINDER-Command.md)]:
*Specify a center point or enter an option*

Specify base radius or [[Diameter](CYLINDER-Command.md)] <default>:
*Specify a base radius, or enter**d**to specify a diameter, or press*Enter *to specify the default base radius value*

Specify height or [2Point/Axis endpoint] <default>:
*Specify a height, enter an option, or press*Enter *to specify the default height value*

3P (Three Points)

Defines the base circumference and base plane of the cylinder by specifying three points.

2Point
:   Specifies that the height of the cylinder is the distance between the two specified points.

Axis Endpoint
:   Specifies the endpoint location for the cylinder axis. This endpoint is the center point of the top face of the cylinder.
    The axis endpoint can be located anywhere in 3D space. The axis endpoint defines the length and orientation of the cylinder.

2P (Two Points)

Defines the base diameter of the cylinder by specifying two points.

* 2Point
* Axis endpoint

TTR (Tangent, Tangent, Radius)

Defines the base of the cylinder with a specified radius tangent to two objects.

Sometimes more than one base matches the specified criteria. The program draws the base of the specified radius whose tangent
points are closest to the selected points.

* 2Point
* Axis endpoint

Elliptical

Specifies an elliptical base for the cylinder.

![](../images/GUID-035AC913-5590-425E-81C4-057CEADC6B96-low.png)

Center
:   Creates the base of the cylinder by using a specified center point.

* 2Point
* Axis endpoint

Diameter

Specifies the diameter for the base of the cylinder.

![](../images/GUID-5448319B-E0DF-4DF1-B112-A7E5411FA226-low.png)

* 2Point
* Axis endpoint

#### Related Concepts

* [About Modeling 3D Objects](About-Modeling-3D-Objects.md)
* [About Creating Basic 3D Solids and Walls](About-Creating-Basic-3D-Solids-and-Walls.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*