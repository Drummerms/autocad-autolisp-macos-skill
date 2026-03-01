# About Breaking and Joining Objects

You can break an object into two objects with or without a gap between them. You can also join objects to create a single
object or multiple objects.

## Break Objects

Use BREAK to create a gap in an object, resulting in two objects with a gap between them. BREAK is often used to create space
for block or text.

![](../images/GUID-105C5CE1-FE88-4B5A-A236-A199D09A8B7C-low.png)

You can create breaks in most geometric objects except blocks, dimensions, multilines, and regions. As an alternative, use
EXPLODE on these types of objects, and create breaks in the dissociated geometry.

To break an object such as a line, arc, or open polyline at a single point without creating a gap, use BREAKATPOINT instead.

## Join Objects

Use JOIN to combine lines, arcs, elliptical arcs, polylines, 3D polylines, splines, and helixes by their endpoints into a
single object.

NOTE:Helixes are not available in AutoCAD LT.

The result of the join operation varies depending on the objects selected. Typical applications include

* Replacing two collinear lines with a single line.
* Closing the gap in a line that resulted from a BREAK.
* Completing an arc into a circle or an elliptical arc into an ellipse. To access the Close option, select a single arc or elliptical
  arc.
* Combining several long polylines in a topographic map.
* Joining two splines, leaving a kink between them.

In general cases, joining objects that touch end-to-end, but that are not in the same plane result in 3D polylines and splines.

NOTE: You can also use the Join option of the PEDIT command to combine a series of lines, arcs, and polylines into a single polyline

#### Related Information

* [To Join Objects](To-Join-Objects.md)
* [To Join Polylines, Splines, Lines, and Arcs Into a Single Polyline](To-Join-Polylines,-Splines,-Lines,-and-Arcs-Into-a-Single-Polyline.md)
* [To Break an Object](To-Break-an-Object.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*