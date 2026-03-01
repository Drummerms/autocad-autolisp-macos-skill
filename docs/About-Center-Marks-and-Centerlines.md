# About Center Marks and Centerlines

Center marks and centerlines are dimensioning references to centers of holes and axes of symmetry.

![](../images/GUID-C89E478D-E096-4B3A-A3EE-B060F2F8808B-low.png)

Center marks and centerlines are associative objects. If you move or modify the associated objects, the center marks and centerlines
adjust accordingly. You can disassociate center marks and centerlines from objects, or reassociate them to selected objects.

## Center Marks

You can create a center mark to indicate the center of a circle or an arc.

![](../images/GUID-9733D1A0-263E-4165-B35E-48F8E3B656C9-low.png)

You can control the center mark size and the scale and font of the centerline extensions. You can also turn off the centerline
extension.

## Centerlines

You can create an associative centerline by selecting two line segments.

A centerline is created between the apparent midpoint of the start and endpoints of the selected two lines. When selecting
nonparallel lines, the centerline is drawn between the imaginary intersection point and the endpoints of the selected lines.

![](../images/GUID-F7DFC100-AF79-4C64-80FE-A704E3D56603-low.png)

The centerline bisects the angles of the two intersecting lines. In this example, the location of the pick points defines
the direction of the centerline.

![](../images/GUID-7CAA3B04-5CDE-4463-B632-0E27E9C51F97-low.png)

## Current Layer Override

By default, all new objects are created on the
*current* layer. For new centerline and center mark objects, you can specify a default layer that's different than the current layer
by specifying the layer with the CENTERLAYER system variable.

## Limitations

The center mark and centerline feature set is best suited for the following methods:

* Drawings that will be printed or published from model space.
* Drawings that are annotated in paper space.

Both annotative scaling and dimension style support is not available.

#### Related Tasks

* [To Create an Associative Center Mark](To-Create-an-Associative-Center-Mark.md)
* [To Create an Associative Centerline](To-Create-an-Associative-Centerline.md)

#### Related References

* [Commands for Center Marks and Centerlines](Commands-for-Center-Marks-and-Centerlines.md)

#### Related Information

* [About Editing Center Marks and Centerlines](About-Editing-Center-Marks-and-Centerlines.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*