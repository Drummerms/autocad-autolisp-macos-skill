# WEDGE (Command)

Creates a 3D solid wedge.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Solid drop-down ![](../images/ac.menuaro.gif) Wedge.
![](../images/GUID-E6323DF7-45B1-4E99-B6D8-F23C52A62264-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Wedge.

## Summary

The direction of the taper is always in the positive
*X*-axis direction of the UCS.

![](../images/GUID-C66AAE97-7597-4199-BE0A-7185685DCB24-low.gif)

## List of Prompts

The following prompts are displayed.

Specify first corner or [[Center](WEDGE-Command.md)]:
*Specify a point or enter* *c* *for center*

Specify other corner or [[Cube](WEDGE-Command.md)/[Length](WEDGE-Command.md)]:
*Specify the other corner of the wedge or enter**an option*

If the other corner of the wedge is specified with a
*Z* value that differs from the first corner, then no height prompt is displayed.

Specify height or [[2Point](WEDGE-Command.md)] <default>:
*Specify the height or enter* *2P* *for the 2 Point option*

Entering a positive value draws the height along the positive
*Z* axis of the current UCS. Entering a negative value draws the height along the negative
*Z* axis.

Center

Creates the wedge by using a specified center point.

![](../images/GUID-279E5A1C-95A1-4A7D-A9C5-4ABF1B52CA45-low.png)

Cube
:   Creates a wedge with sides of equal length.

    ![](../images/GUID-1E36F837-370D-415F-8CA8-171ED8843CCE-low.png)

Length
:   Creates a wedge with length, width, and height values you specify. The length corresponds to the
    *X* axis, the width to the
    *Y* axis, and the height to the
    *Z* axis. If you pick a point to specify the length, you also specify the rotation in the
    *XY* plane.

    ![](../images/GUID-F38D29AF-474D-44CC-913E-C76806B372E2-low.png)

Cube

Creates a wedge with sides of equal length.

![](../images/GUID-1E36F837-370D-415F-8CA8-171ED8843CCE-low.png)

Length

Creates a wedge with length, width, and height values you specify. The length corresponds to the
*X* axis, the width to the
*Y* axis, and the height to the
*Z* axis.

![](../images/GUID-F38D29AF-474D-44CC-913E-C76806B372E2-low.png)

2Point

Specifies that the height of the wedge is the distance between the two specified points.

#### Related Concepts

* [About Creating Basic 3D Solids and Walls](About-Creating-Basic-3D-Solids-and-Walls.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*