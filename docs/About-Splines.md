# About Splines

A spline is a smooth curve that passes through or near a set of points that influence the shape of the curve.

By default, a spline is a series of blended curve segments of degree 3 (also called cubic) polynomials. These curves are technically
called *nonuniform rational B-splines (NURBS)*, but are referred to as splines for simplicity. Cubic splines are the most common, and mimic the splines that are created
manually using flexible strips that are shaped by weights at data points.

In the following example, a spline was used to create the highlighted boundary of the concrete walkway.

![](../images/GUID-121A60F7-2BD0-4257-9A04-2BCBDFB04AA0-low.png)

## Understand Control Vertices and Fit Points

You can create or edit splines using either *control vertices*, or *fit points*. The spline on the left displays control vertices along a *control polygon*, and the spline on the right displays fit points.

![](../images/GUID-67FDAE6B-6EEE-49AF-981B-E395C98B8EEE-low.png)

Use the triangular grip on a selected spline to switch between displaying control vertices and displaying fit points. You
can use the round and square grips to modify a selected spline.

![](../images/GUID-6DE2C9A2-FB81-4253-9233-CDE1DB097F45-low.png)

IMPORTANT:Switching the display from control vertices to fit points automatically changes the selected spline to degree 3. Splines originally
created using higher-degree equations will likely change shape as a result.

## Create Splines Using Fit Points

When you create splines using fit points, the resulting curve passes through the specified points, and is influenced by the
spacing of mathematical *knots* in the curve.

You can choose the spacing of these knots with the *knot parameterization* option, which will result in different curves as shown in the example.

![](../images/GUID-C1CF448D-EFC3-4259-B047-F50BED1C0E2F-low.png)

NOTE: There is no best choice for knot parameterization for all cases. The chord length parameterization is commonly used, and
the square root (centripetal) parameterization often produces better curves depending on the data set.

When the Tolerance value is set to 0, the spline passes directly through the fit points. With larger tolerance values, the
spline passes near the fit points. Optionally, you can specify the tangent direction for the spline at each end.

NOTE: The fit point method always results in a degree 3 spline.

## Special Cases

You can create a spline with a parabolic shape by specifying a degree 2 spline created with exactly 3 control vertices as
shown on the left. Degree 3 splines created with 4 control vertices have the same shape as Bezier curves of degree 3 as shown
on the right.

![](../images/GUID-E480CF34-997D-470F-9C80-8EF28E2657AD-low.png)

#### Related Concepts

* [About Arcs](About-Arcs.md)
* [About Curved Objects](About-Curved-Objects.md)
* [About Ellipses](About-Ellipses.md)

#### Related Information

* [To Work With Splines](To-Work-With-Splines.md)
* [To Work With Circles](To-Work-With-Circles.md)
* [To Work With Ellipses](To-Work-With-Ellipses.md)
* [To Work With Arcs](To-Work-With-Arcs.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*