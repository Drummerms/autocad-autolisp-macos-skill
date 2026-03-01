# CONE (Command)

Creates a 3D solid cone.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Solid drop-down ![](../images/ac.menuaro.gif) Cone.
![](../images/GUID-2ED7D3ED-793D-4F34-BCC7-D7C5217FA844-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Cone.

## Summary

Creates a 3D solid with a circular or elliptical base that tapers symmetrically to a point or to a circular or elliptical
planar face. You can control the smoothness of 3D curved solids, such as a cone, in a shaded or hidden visual style with the
FACETRES system variable.

![](../images/GUID-0DA4EA5F-3868-4D85-8724-2C4C5AE8921D-low.gif)

Use the Top Radius option to create a cone frustum.

Initially, the default base radius is not set to any value. During a drawing session, the default value for the base radius
is always the previously entered base radius value for any solid primitive.

![](../images/GUID-84284654-C24B-444F-ADA8-47B6CE8E0BE4-low.png)

![](../images/GUID-33B09BA9-9409-4264-B56B-79F2B1DAA09B-low.png)

## List of Prompts

The following prompts are displayed.

Specify center point of base or [[3P](CONE-Command.md)/[2P](CONE-Command.md)/[Ttr](CONE-Command.md)/[Elliptical](CONE-Command.md)]:
*Specify a point (1) or enter an option*

Specify base radius or [[Diameter](CONE-Command.md)] <default>:
*Specify a base radius, enter**d**to specify a diameter, or press*Enter *to specify the default base radius value*

Specify height or [[2Point](CONE-Command.md)/[Axis endpoint](CONE-Command.md)/[Top radius](CONE-Command.md)] <default>:
*Specify a height, enter an option, or press*Enter *to specify the default height value*

Center Point of Base

2Point
:   Specifies that the height of the cone is the distance between the two specified points.

Axis Endpoint
:   Specifies the endpoint location for the cone axis. The axis endpoint is the top point of the cone or the center point of the
    top face of the cone frustum (Top Radius option). The axis endpoint can be located anywhere in 3D space. The axis endpoint
    defines the length and orientation of the cone.

Top Radius
:   Specifies the top radius of the cone, creating a cone frustum.

    Initially, the default top radius is not set to any value. During a drawing session, the default value for the top radius
    is always the previously entered top radius value for any solid primitive.

Diameter
:   Specifies the diameter for the base of the cone.

    Initially, the default diameter is not set to any value. During a drawing session, the default value for the diameter is always
    the previously entered diameter value for any solid primitive.

    ![](../images/GUID-F2106948-BD5F-4F1A-9F24-3F66B498E488-low.png)

3P (Three Points)

Defines the base circumference and base plane of the cone by specifying three points.

* [2Point](CONE-Command.md)
* [Axis Endpoint](CONE-Command.md)
* [Top Radius](CONE-Command.md)

2P (Two Points)

Defines the base diameter of the cone by specifying two points.

* [2Point](CONE-Command.md)
* [Axis Endpoint](CONE-Command.md)
* [Top Radius](CONE-Command.md)

TTR (Tangent, Tangent, Radius)

Defines the base of the cone with a specified radius tangent to two objects.

Sometimes, more than one base matches the specified criteria. The program draws the base of the specified radius whose tangent
points are closest to the selected points.

* [2Point](CONE-Command.md)
* [Axis Endpoint](CONE-Command.md)
* [Top Radius](CONE-Command.md)

Elliptical

Specifies an elliptical base for the cone.

Center
:   Creates the base of the cone by using a specified center point.

* [2Point](CONE-Command.md)
* [Axis Endpoint](CONE-Command.md)
* [Top Radius](CONE-Command.md)

#### Related Concepts

* [About Using Grips to Edit 3D Objects](About-Using-Grips-to-Edit-3D-Objects.md)
* [About Creating Basic 3D Solids and Walls](About-Creating-Basic-3D-Solids-and-Walls.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*