# About Geometric Constraints

You can specify geometric constraints between 2D objects or points on objects. When you later edit the constrained geometry,
the constraints are maintained.

Thus, using geometric constraints, you have a method of including design requirements in your drawing.

For example, in the illustration below, the following constraints are applied to the geometry.

* Every endpoint is constrained to remain coincident with the endpoint of every adjacent object—these constraints are displayed
  as small blue squares
* The vertical lines are constrained to remain parallel with each other and to remain equal to each other in length
* The right vertical line is constrained to remain perpendicular to the horizontal line
* The horizontal line is constrained to remain horizontal
* The location of the circle and the horizontal line are constrained to remain fixed in space—these "fix" constraints are displayed
  as lock icons

NOTE:The locked geometry is not associated to the other geometry without geometric constraints linked to it.

![](../images/GUID-994E67BE-20E2-4B82-8954-80A7A3D842AF-low.png)

The geometry of the above design is not *fully constrained*. Using grips, you can still change the radius of the arc, the diameter of the circle, the length of the horizontal line,
and the length of the vertical lines. To specify these distances, you need to apply *dimensional constraints*.

NOTE:Constraints can be added to segments within a polyline as if they were separate objects.

#### Related Information

* [About Dimensional Constraints](About-Dimensional-Constraints.md)
* [About Parametric Drawing](About-Parametric-Drawing.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*