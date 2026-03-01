# BOX (Command)

Creates a 3D solid box.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Solid drop-down ![](../images/ac.menuaro.gif) Box.
![](../images/GUID-E4DD1427-E3FC-4146-B9AF-6C7B5D088B0D-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Box.

## List of Prompts

The following prompts are displayed.

Specify first corner or [[Center](BOX-Command.md)]:
*Specify a point or enter**c* *for center*

Specify other corner or [[Cube](BOX-Command.md)/[Length](BOX-Command.md)]:
*Specify the other corner of the box or enter**an option*

If the other corner of the box is specified with a
*Z* value that differs from the first corner, then no height prompt is displayed.

Specify height or [[2Point](BOX-Command.md)] <default>:
*Specify the height or enter**2P* *for the 2 Point option*

Entering a positive value draws the height along the positive
*Z* axis of the current UCS. Entering a negative value draws the height along the negative
*Z* axis.

The base of the box is always drawn parallel to the
*XY* plane of the current UCS (work plane). The height of the box is specified in the
*Z*-axis direction. You can enter both positive and negative values for the height.

![](../images/GUID-C5256913-AED3-4DEB-8E7B-9F9A15340AAD-low.gif)

Center

Creates the box by using a specified center point.

![](../images/GUID-DC4F7566-8D18-4A59-8503-5BEA989DA440-low.png)

Cube
:   Creates a box with sides of equal length.

    ![](../images/GUID-7352DBCB-7330-4681-9373-A989D37E0D26-low.png)

Length
:   Creates a box with length, width, and height values you specify. The length corresponds to the
    *X* axis, the width to the
    *Y* axis, and the height to the
    *Z* axis.

    ![](../images/GUID-DE2D5728-8F3C-4FD7-8F55-0014B8421A6D-low.png)

Cube

Creates a box with sides of equal length.

![](../images/GUID-7352DBCB-7330-4681-9373-A989D37E0D26-low.png)

Length

Creates a box with length, width, and height values you specify. If you enter values, the length corresponds to the
*X* axis, the width to the
*Y* axis, and the height to the
*Z* axis. If you pick a point to specify the length, you also specify the rotation in the
*XY* plane.

![](../images/GUID-DE2D5728-8F3C-4FD7-8F55-0014B8421A6D-low.png)

2Point

Specifies that the height of the box is the distance between the two specified points.

#### Related Concepts

* [About Modeling 3D Objects](About-Modeling-3D-Objects.md)
* [About Creating Basic 3D Solids and Walls](About-Creating-Basic-3D-Solids-and-Walls.md)

#### Related Information

* [About Creating Basic 3D Solids and Walls](About-Creating-Basic-3D-Solids-and-Walls.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*