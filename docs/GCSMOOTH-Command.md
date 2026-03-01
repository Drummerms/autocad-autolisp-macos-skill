# GCSMOOTH (Command)

Constrains a spline to be contiguous and maintain G2 continuity with another spline, line, arc, or polyline.

## Access Methods

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Parametric panel ![](../images/ac.menuaro.gif) Geometric Constraint drop-down ![](../images/ac.menuaro.gif) Smooth.
![](../images/GUID-99DC1441-40C1-426E-994D-E85FF201BD03-low.png)

*Menu*:
Tools ![](../images/ac.menuaro.gif) Parametric ![](../images/ac.menuaro.gif) Geometric Constraints ![](../images/ac.menuaro.gif) Smooth.

## Summary

This command is equivalent to the Smooth option in
[GEOMCONSTRAINT](GEOMCONSTRAINT-Command.md).

Following are the valid constraint objects and points:

* Spline, line
* Polyline segment
* Arc
* Polyline arc

The splines are updated to be contiguous with one another.

NOTE:Endpoints of the curves to which you apply the smooth constraints are made coincident.

## List of Prompts

The following prompts are displayed.

Select first spline
[curve](GCSMOOTH-Command.md):
*Select a spline object*

Curve

Selects an endpoint of a curve.

First Spline Curve
:   Selects the first spline curve to be constrained.

Second Curve
:   Selects the second curve to be made continuous with the first spline curve.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*