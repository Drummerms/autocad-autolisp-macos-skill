# ALIGN (Command)

Aligns objects with other objects in 2D and 3D.

## Access Methods

*Tool Sets*:
Drafting tab ![](../images/ac.menuaro.gif) Modify panel ![](../images/ac.menuaro.gif) Align.
![](../images/GUID-E8A89848-B847-4C63-B8F0-7FDC4925AD9A-low.png)

NOTE:Hidden by default. Click
![](../images/GUID-78DED619-51B3-49C1-AD71-F928B5F69C0A-low.png) to display the icon on the tool set panel.

*Menu*:
Modify
![](../images/ac.menuaro.gif) 3D Operations
![](../images/ac.menuaro.gif) Align.

Either one, two, or three pairs of source points and definition points can be specified to move, rotate, or tilt the selected
objects, aligning them with points on another object.

![](../images/GUID-E85DF25C-AEB9-4B5A-86E2-6A95B54A65F9-low.gif)

The following prompts are displayed.

Select objects
:   Select the objects to align and press Enter.

    The next series of prompts asks for source and destination points. The number of point pairs that you specify determines the
    results.

First source point, First destination point
:   When you select only one source point and destination point pair, the selected objects move in 2D or 3D from the source point
    (1) to the destination point (2).

    ![](../images/GUID-EFDA2C49-6DF9-41DC-ABB6-77D1BA8C8AFD-low.png)

First and Second source and destination points
:   When you select two point pairs, you can move, rotate, and scale the selected objects to align with other objects.

    ![](../images/GUID-5CA0489D-9C17-42FD-8902-2EC2229A7F5D-low.png)

    The first set of source and destination points defines the base point for the alignment (1, 2). The second set of points defines
    the angle of rotation (3, 4).

    After you enter the second set of points, you are prompted to scale the object. The distance between the first and second
    destination points (2, 4) is used as the reference length to which the object is scaled. Scaling is available only when you
    are aligning objects using two point pairs.

    NOTE: If you use two source and destination points to perform a 3D alignment on non-perpendicular working planes, you get unpredictable
    results.

First, Second, and Third source and destination points
:   When you select three point pairs, you can move and rotate the selected objects in 3D to align with other objects.

    ![](../images/GUID-D1DF21D8-73F7-473E-A47A-05F676CB8900-low.png)

    The selected objects move from the source point (1) to the destination point (2).

    The selected object is rotated (1 and 3) so that it aligns with the destination object (2 and 4).

    The selected object is then rotated again (3 and 5) so that it aligns with the destination object (4 and 6).

#### Related Tasks

* [To Align Two Objects in 2D](To-Align-Two-Objects-in-2D.md)

#### Related Concepts

* [About Aligning Objects](About-Aligning-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*