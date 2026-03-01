# FAQ: How Do I Process Curve-Fit and Spline-Fit Polylines? (AutoLISP)

A "legacy" polyline might contain vertices that were not created explicitly; these auxiliary vertices were inserted automatically
by the AutoCAD PEDIT command's Fit and Spline options.

You can safely ignore these additional vertices when stepping through a polyline with
entnext because changes to these vertices will be discarded the next time the AutoCAD PEDIT command is used to fit or convert the
polyline to a spline. The group code 70 flags of a "legacy" polyline entity indicate whether the polyline has been curve-fit
(bit value 2) or spline-fit (bit value 4). If neither bit is set, all the polyline's vertices are regular user-defined vertices.

However, if the curve-fit bit (2) is set, alternating vertices of the polyline have the bit value 1 set in their 70 group
code to indicate that they were inserted by the curve-fitting process. If you use
entmod to move the vertices of such a polyline with the intent of refitting the curve by means of the AutoCAD PEDIT command, ignore
these vertices.

Likewise, if the "legacy" polyline entity's spline-fit flag bit (bit 4) is set, an assortment of vertices will be found—some
with flag bit 1 (inserted by curve fitting if the AutoCAD SPLINESEGS system variable was negative), some with bit value 8
(inserted by spline fitting), and all others with bit value 16 (spline frame-control point). Here again, if you use
entmod to move the vertices and you intend to refit the spline afterward, move only the control-point vertices.

#### Related Concepts

* [About Creating Complex Entities without Using the Command Function (AutoLISP)](About-Creating-Complex-Entities-without-Using-the-Command-Function-AutoLISP.md)
* [About Modifying an Entity without the Command Function (AutoLISP)](About-Modifying-an-Entity-without-the-Command-Function-AutoLISP.md)
* [About Obtaining Entity Information (AutoLISP)](About-Obtaining-Entity-Information-AutoLISP.md)
* [FAQ: What is the Difference Between Lightweight Polylines and "Legacy" Polylines? (AutoLISP)](FAQ-What-is-the-Difference-Between-Lightweight-Polylines-and-Legacy-Polylines-AutoLISP.md)
* [Object-Handling Functions Reference (AutoLISP)](Object-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*