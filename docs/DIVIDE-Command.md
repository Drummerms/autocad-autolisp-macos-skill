# DIVIDE (Command)

Creates evenly spaced point objects or blocks along the length or perimeter of an object.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Draw panel ![](../images/ac.menuaro.gif) Point drop-down ![](../images/ac.menuaro.gif) Divide.
![](../images/GUID-6EC11511-8D3E-4D01-92C3-883E60D59ED7-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) Point ![](../images/ac.menuaro.gif) Divide.

The following prompts are displayed.

## Select Object to Divide

Specifies a single geometric object such as a line, polyline, arc, circle, ellipse, or spline.

## Number of Segments

Places point objects at equal intervals along the selected objects.

![](../images/GUID-732498DC-74B9-47E3-8F51-B36C6877FB29-low.png)

Use DDPTYPE to set the style and size of all point objects in a drawing.

![](../images/GUID-F5CF70F8-83EE-426A-8C7D-ECE1296311D7-low.gif)

## Block

Places specified blocks at equal intervals along the selected object. The blocks will be inserted on the plane in which the
selected object was originally created. If the block has variable attributes, these attributes are not included.

Yes
:   Aligns the blocks according to the curvature of the selected object. The
    *X* axes of the inserted blocks will be tangent to, or collinear with, the selected object at the dividing locations

No
:   Aligns the blocks according to the current orientation of the user coordinate system. The
    *X* axes of the inserted blocks will be parallel to the
    *X* axis of the UCS at the dividing locations.

The illustration shows an arc divided into five equal parts using a block consisting of a vertically oriented ellipse.

![](../images/GUID-5C79E0F0-6F2F-4076-9D5E-B32CE5D5E266-low.png)

#### Related References

* [DDPTYPE (Command)](DDPTYPE-Command.md)

#### Related Concepts

* [About Specifying Equal Intervals on Objects](About-Specifying-Equal-Intervals-on-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*