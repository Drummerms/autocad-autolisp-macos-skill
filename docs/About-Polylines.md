# About Polylines

A polyline is a connected sequence of line segments created as a single object. You can create straight line segments, arc
segments, or a combination of the two.

![](../images/GUID-9C5AA6F5-E3FD-41CF-BD3E-EB295787755F-low.png)

Some reasons you may choose to use polylines include the following:

* Vertices remain joined even after grip editing
* Absolute line width (as an alternative to relative lineweight) that can be constant or tapered across a segment
* Move and copy a polyline as a unit
* Easily create rectangles and polygons as single objects
* Smart application of non-continuous linetypes across vertices
* Easy extrusion for 3D solids in AutoCAD

## Modifying Polylines

Several methods are available to change the shape and appearance of a polyline.

When you select a polyline you can use grips to move, add, or delete individual vertices, and convert between arc and straight
segments.

![](../images/GUID-FA36A660-9414-46C9-9D27-ECCA3D3F4A03-low.png)

You can also convert a polyline to a spline-fit or curve-fit polyline.

![](../images/GUID-2EF8C7DD-57AF-4099-819E-CE90E54E7F80-low.png)

NOTE:You can convert a spline-fit polyline into a B-spline with the Spline command, object option.
![](../images/GUID-E2AD358A-8B16-4439-AF57-74388059DFE7-low.png) Find

Use the PEDIT command to change the width of an individual segment or the entire polyline.

![](../images/GUID-8C3D9908-91ED-4734-A583-B5F0C41DF9A7-low.png)

NOTE: Many of the options for modifying polylines are also on the Properties palette.

## Linetypes and Polyline Vertices

For polylines, you can specify whether a linetype pattern is centered on each segment or is continuous across vertices throughout
the entire length of the polyline.

![](../images/GUID-68E7FD4C-850A-460C-854D-BBAF85E4BEA4-low.png)

Use the PLINEGEN system variable to specify this option for new objects. You can update existing polylines on the Properties
palette in the Linetype Generation setting.

#### Related Concepts

* [About Lines](About-Lines.md)

#### Related Information

* [To Create a Wide Polyline](To-Create-a-Wide-Polyline.md)
* [To Draw a Polyline with Straight Segments](To-Draw-a-Polyline-with-Straight-Segments.md)
* [To Draw a Line and Arc Polyline](To-Draw-a-Line-and-Arc-Polyline.md)
* [To Create a Boundary Polyline](To-Create-a-Boundary-Polyline.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*