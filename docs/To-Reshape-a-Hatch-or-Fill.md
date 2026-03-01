# To Reshape a Hatch or Fill

Reshape an associative hatch by modifying the boundary objects. Reshape a nonassociative hatch by modifying the hatch object.

## Modify the Extents of Associative Hatches and Fills

If you modify the boundary objects of an associative hatch, and the result maintains a closed boundary, the associated hatch
object is automatically updated. If the changes result in an open boundary, the hatch loses its associativity with the boundary
objects, and the hatch remains unchanged.

![](../images/GUID-46ED8660-D821-4F9E-AB35-F6385D8BD88E-low.png)

When you select an associative hatch object, it displays a circular grip, called the *control grip*, at the center of the hatch extents. Hover over the control grip to display a shortcut menu with several hatch options, or
right-click to display additional options.

![](../images/GUID-27731B8D-B7BA-4BF0-963F-463D406459D2-low.png)

You can also change the hatch object by editing the grips of the associated boundary objects. To easily select all of the
objects in a complex boundary, use the Display Boundary Objects option.

![](../images/GUID-0F6091FE-2B0A-445B-A559-2DCE562FEFAA-low.png)

If the boundary object is a polyline or spline, *multi-functional grips* are displayed. For more information, Use Object Grips.

## Modify the Extents of Non-associative Hatches and Fills

When you select a non-associative hatch, multi-functional grips are displayed on the hatch. Use these grips to modify the
hatch extents and some several hatch properties.

![](../images/GUID-AEF5F210-C454-47F3-B054-68C042E05298-low.png)

When you *hover* over a grip on a nonassociative hatch object, a grip menu displays several edit options based on the type of grip. For example,
a linear segment grip has an option to convert the segment to an arc, or to add a vertex.

![](../images/GUID-D5B95280-DBDE-4FA5-9D54-19E7DAD4275D-low.png)

NOTE:For drastic changes, you can use TRIM to reduce the area covered by a hatch object, or EXPLODE to disassemble a hatch into
its component objects.

#### Related Concepts

* [About Editing with Grips](About-Editing-with-Grips.md)

#### Related Information

* [Overview of Hatch Patterns and Fills](Overview-of-Hatch-Patterns-and-Fills.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*