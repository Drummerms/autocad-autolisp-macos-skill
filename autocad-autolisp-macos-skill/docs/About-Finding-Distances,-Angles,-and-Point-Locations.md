# About Finding Distances, Angles, and Point Locations

You can extract geometric information from point locations on objects in a drawing.

With each of these commands, it's a good idea to zoom into the area close enough to resolve any closely spaced or potentially
overlapping objects.

## Measure Objects Dynamically

The MEASUREGEOM command provides several options to report distances, angles, radius values, and several other measurements.

The Quick option, which is the default, is particularly useful for identifying several distances and angles dynamically as
you move your mouse over, near, and between 2D geometric objects.

As shown in the lower-left corner of the illustration, the orange rectangle indicates a right-angle corner.

![](../images/GUID-09CC5BA5-1C12-418F-8E92-A6E794B54CF1-low.png)

Click within an enclosed area to display its area and perimeter in the Command window.

If you want the default to be the last option used rather than Quick, use the Mode option in MEASUREGEOM.

NOTE:The Quick option is designed to work on 2D geometry in a plan view with the UCS set to World and the visual style set to 2D
Wireframe. Objects that aren't measured include typical annotations such as dimensions and hatches, and custom objects.

## Verify the Distance and Angle Between Point Locations

You can use the DIST command with object snaps to extract geometric information about the relationship between two points,
including the distance and angle between the points, and the change or delta between their coordinates. This information displays
in the Command window.

## Verify the Coordinates of a Point Location

You can use the ID command with object snaps to confirm the
*X*,
*Y*, and
*Z* coordinates of a specified location on an object. For example, this command can confirm whether the Z value of a point on
an object in a 2D drawing is not set to zero. This information displays in the Command window.

#### Related Information

* [To Find the Distance and Angle Between two Points](To-Find-the-Distance-and-Angle-Between-two-Points.md)
* [To Find the Cumulative Distance Between a Series of Points](To-Find-the-Cumulative-Distance-Between-a-Series-of-Points.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*