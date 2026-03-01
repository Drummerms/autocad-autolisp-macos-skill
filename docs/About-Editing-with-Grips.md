# About Editing with Grips

You can reshape, move, or manipulate objects in other ways using different types of grips and grip modes.

## Objects with Multi-Functional Grips

The following objects have multi-functional grips that offer object-specific and, in some cases, grip-specific options:

* *2D objects:* Lines, polylines, arcs, elliptical arcs, splines, and hatch objects.
* ![](../images/GUID-D5B95280-DBDE-4FA5-9D54-19E7DAD4275D-low.png)

  *Annotation objects:* Dimension objects and multileaders.
* *3D solids:* 3D faces, edges, and vertices.

![](../images/GUID-BB615E66-4620-41AB-A3EB-4C6876ACFFBD-low.png)

## Important Notes

* Grips are not displayed on objects that are on locked layers.
* When you select multiple objects that share coincident grips, you can edit these objects using grip modes; however, any object-
  or grip-specific options are not available.

## Tips for Stretching with Grips

* When you select more than one grip on an object to stretch it, the shape of the object is kept intact between the selected
  grips. To select more than one grip, press and hold the Shift key, and then select the appropriate grips.
* Grips on text, block references, midpoints of lines, centers of circles, and point objects move the object rather than stretching
  it.
* When a 2D object lies on a plane other than the current UCS, the object is stretched on the plane on which it was created,
  not on the plane of the current UCS.
* If you select a quadrant grip to stretch a circle or ellipse and then specify a distance at the Command prompt for the new
  radius—rather than moving the grip—this distance is measured from the center of the circle, not the selected grip.

## Limit the Display of Grips to Improve Performance

You can limit the maximum number of objects that display grips. For example, when a drawing contains hatch objects or polylines
with many grips, selecting these objects can take a long time. The GRIPOBJLIMIT system variable suppresses the display of
grips when the initial selection set includes more than the specified number of objects. If you add objects to the current
selection set, the limit does not apply.

#### Related Tasks

* [To Edit Objects Using Grips](To-Edit-Objects-Using-Grips.md)

#### Related References

* [Methods for Editing Objects: Reference](Methods-for-Editing-Objects-Reference.md)

#### Related Information

* [To Toggle Grips](To-Toggle-Grips.md)
* [To Toggle Grips in Blocks](To-Toggle-Grips-in-Blocks.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*