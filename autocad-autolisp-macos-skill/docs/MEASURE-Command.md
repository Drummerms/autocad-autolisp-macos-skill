# MEASURE (Command)

Creates point objects or blocks at measured intervals along the length or perimeter of an object.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Draw panel ![](../images/ac.menuaro.gif) Point drop-down ![](../images/ac.menuaro.gif) Measure.
![](../images/GUID-D6E62826-5FF1-43A8-86EA-4D9B5EEE53F5-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) Point ![](../images/ac.menuaro.gif) Measure.

The resulting points or blocks are always located on the selected object and their orientation is determined by the
*XY* plane of the UCS.

Use DDPTYPE to set the style and size of all point objects in a drawing.

![](../images/GUID-D59849B2-5F47-4DB3-A031-83CB2F1E63FA-low.gif)

The points or blocks are placed in the Previous selection set, so you can select them all by entering
*p* at the next Select Objects prompt. You can use the Node object snap to draw an object by snapping to the point objects. You
can then remove the points by entering
*erase previous*.

The following prompts are displayed.

Object to measure
:   Select the reference object along which you want to add the point objects or blocks.

Length of segment
:   Places point objects at the specified interval along the selected object, starting at the endpoint closest to the point you
    used to select the object.

    Measurement of closed polylines starts at their initial vertex (the first one drawn).

    Measurement of circles starts at the angle from the center set as the current snap rotation angle. If the snap rotation angle
    is 0, then the measurement of the circle starts to the right of center, on its circumference.

    ![](../images/GUID-D9B07AA6-08BC-4F88-B835-9AA702D41C55-low.png)

    The illustration shows how MEASURE marks 0.5-unit distances along a polyline, with the PDMODE system variable set to 35.

    ![](../images/GUID-98497873-F532-4C49-9690-038CD54E8F42-low.png)

Block
:   Places blocks at a specified interval along the selected object.

Align block with object
:   * *Yes.* The block is rotated about its insertion point so that its horizontal lines are aligned with, and drawn tangent to, the object
      being measured.
    * *No.*The block is always inserted with a 0 rotation angle.

    After you specify the segment length, the block is inserted at the specified interval. If the block has variable attributes,
    these attributes are not included.

#### Related References

* [Commands for Measuring and Dividing](Commands-for-Measuring-and-Dividing.md)

#### Related Concepts

* [About Specifying Equal Intervals on Objects](About-Specifying-Equal-Intervals-on-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*