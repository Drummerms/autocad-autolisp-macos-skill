# About Creating Angular Dimensions

Angular dimensions measure the angle between two lines or three points.

To measure the angle between two radii of a circle, you select the circle and specify the angle endpoints. With other objects,
you select the objects and then specify the dimension location. You can also dimension an angle by specifying the angle vertex
and endpoints. As you create the dimension, you can modify the text content and alignment before specifying the dimension
line location.

NOTE:

You can create baseline and continued angular dimensions relative to existing angular dimensions. Baseline and continued angular
dimensions are limited to 180 degrees or less. To obtain baseline and continued angular dimensions larger than 180 degrees,
use grip editing to stretch the location of the extension line of an existing baseline or continued dimension.

## Dimension Lines

If you use two straight, nonparallel lines to specify an angle, the dimension line arc spans the angle between the two lines.
If the dimension line arc does not meet one or both of the lines being dimensioned, The program draws one or two extension
lines to intersect the dimension line arc. The arc is always less than 180 degrees.

## Dimension Circles and Arcs

If you use an arc or a circle or three points to specify an angle, the program draws the dimension line arc between the extension
lines. The extension lines are drawn from the angle endpoints to the intersection of the dimension line arc.

![](../images/GUID-285027A4-F037-46FA-80A7-B650C06C37CD-low.png)

The location that you specify for the dimension line arc determines the quadrant of the dimensioned angle.

## Dimension to a Quadrant

Angular dimensions can measure a specific quadrant that is formed when dimensioning the angle between of the endpoints of
a line or arc, center point of a circle, or two vertices. As an angular dimension is being created, there are four possible
angles that can be measured. By specifying a quadrant it allows you to ensure that the correct angle is dimensioned. When
placing an angular dimension after a quadrant has been specified, you can place the dimension text outside of the extension
lines of the dimension. The dimension line is automatically extended.

![](../images/GUID-44F2AC64-BD5F-4BA9-8ED4-AE166E5BC660-low.png)

#### Related Tasks

* [To Create an Angular Dimension](To-Create-an-Angular-Dimension.md)

#### Related Concepts

* [About Dimension Styles](About-Dimension-Styles.md)
* [About Creating Linear Dimensions](About-Creating-Linear-Dimensions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*