# About Creating Radial Dimensions

Radial dimensions measure the radii and diameters of arcs and circles with optional centerlines or a center mark.

There are two types of radial dimensions:

* DIMRADIUS measures the radius of an arc or circle, and displays the dimension text with the letter *R* in front of it.

  ![](../images/GUID-C385C32C-6B8A-43F0-B9EA-0D8257697B49-low.png)
* DIMDIAMETER measures the diameter of an arc or circle, and displays the dimension text with the diameter symbol in front
  of it.

  ![](../images/GUID-BB5EE377-E09E-4C3E-9066-B6CD954FB70B-low.png)

For horizontal dimension text, if the angle of the radial dimension line is greater than 15 degrees from horizontal, a hook
line, also called a *dogleg* or *landing*, one arrowhead long, is created next to the dimension text.

## Control Extension Lines

When an arc is dimensioned, the radial or diametric dimension does not have to be positioned along the arc directly. If a
dimension is positioned past the end of an arc, either an extension line will be drawn that follows the path of the arc being
dimensioned or no extension line will be drawn. When the extension line is suppressed (off), the dimension line of the radial
or diametric dimension is drawn through the center point of the arc instead of to the extension line.

![](../images/GUID-BB84EAA0-6B3D-4A9B-A9EE-8A06CAB7C8F6-low.png)

The DIMSE1 system variable controls whether or not a radial or diametric dimension will be drawn with an extension line when
it is positioned off the end of an arc. When the display of the arc extension line is not suppressed, a gap between the arc
and arc extension line is made. The size of the gap drawn is controlled with the DIMEXO system variable.

![](../images/GUID-180500DA-BC55-4031-86B2-C8E3A29BF4B4-low.png)

## Control Centerlines and Center Marks

Depending on your dimension style settings, center marks and lines generate automatically for diameter and radius dimensions.
They are created only if the dimension line is placed outside the circle or arc. You can create centerlines and center marks
directly with the DIMCENTER command.

You can control the size and visibility of centerlines and center marks with the DIMCEN system variable and in the Dimension
Style dialog box.

![](../images/GUID-CD0ED749-00F9-41CA-B754-18B395CD82D4-low.png)

The size of the centerline is the length of the centerline segment that extends outside the circle or arc. It is also the
size of the gap between the center mark and the start of the centerline. The size of the center mark is the distance from
the center of the circle or arc to the end of the center mark.

![](../images/GUID-984DBDC3-3474-4BD2-A741-FE10F5F46DD7-low.png)

## Create Jogged Radius Dimensions

With the DIMJOGGED command, you can create jogged radius dimensions, also called “foreshortened radius dimensions,” when
the center of an arc or circle is located off the layout and cannot be displayed in its true location. The origin point of
the dimension can be specified at a more convenient location called the *center location override*.

![](../images/GUID-75E49393-AE89-45DE-B366-F2B04AEED805-low.png)

You can control the default angle of the jog in the Dimension Style dialog box, under Radius Dimension Jog.

![](../images/GUID-7BB161AC-A9BF-42C0-B9BB-B34BFAAA8862-low.png)

Once a jogged radius dimension is created, you can modify the jog and the center location override by

* Using grips to move the features
* Changing the locations of the features with the Properties palette
* Using the STRETCH command

NOTE:Jogged radius dimensions can be viewed but not edited in versions previous to AutoCAD 2006-based products.

#### Related Tasks

* [To Work with Radial Dimensions](To-Work-with-Radial-Dimensions.md)
* [To Create Centerlines Automatically With Radial Dimensions](To-Create-Centerlines-Automatically-With-Radial-Dimensions.md)
* [To Create a Non-Associative Center Mark](To-Create-a-Non-Associative-Center-Mark.md)

#### Related Concepts

* [About Dimension Styles](About-Dimension-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*