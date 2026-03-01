# About Modifying Splines

Several methods are available for editing splines and changing their underlying mathematical parameters.

You can edit splines using multifunctional grips, SPLINEDIT, and the Properties Inspector. In addition to these operations,
splines can be trimmed, extended, and filleted.

## Edit Splines with Multi-functional Grips

Multi-functional grips provide options that include adding control vertices and changing the tangent direction of the spline
at its endpoints. Display a menu of options by hovering over a grip.

![](../images/GUID-10AD8435-545F-4E1A-9214-626A9AFDD30D-low.png)

The editing options available with multi-functional grips differ depending on whether the spline is set to display *control vertices* or *fit points*. The spline on the left displays control vertices, and the one on the right displays fit points.

![](../images/GUID-67FDAE6B-6EEE-49AF-981B-E395C98B8EEE-low.png)

To switch between displaying control vertices and displaying fit points, click the triangular grip.

![](../images/GUID-6DE2C9A2-FB81-4253-9233-CDE1DB097F45-low.png)

IMPORTANT:

Switching from displaying control vertices to fit points automatically changes the selected spline to degree 3. Splines originally
created using higher-degree equations will likely change shape as a result.

In general, editing a spline with control vertices provides finer control over reshaping a small section of the curve than
editing a spline with fit points.

![](../images/GUID-402429FB-CE1C-412B-9D97-061395C0E51C-low.png)

You can insert additional control vertices to a section of a spline to obtain greater control in that section at the expense
of making the shape of the spline more complicated. The Refine option adds a *knot* to the spline resulting in replacing the selected control vertex with two control vertices.

![](../images/GUID-D259EDD2-B449-4637-95EA-A9735D1621DB-low.png)

## Edit Splines with SPLINEDIT

SPLINEDIT provides additional editing options, such as adding a kink to the spline, and joining a spline to another contiguous
object, such as a line, arc, or other spline. As shown, objects are joined to splines with C0 continuity.

![](../images/GUID-59EA04F5-7849-44F4-8CBB-0B6A0597780C-low.png)

## Edit Splines with 3DEDITBAR

(Not available in AutoCAD LT)

3DEDITBAR displays a gizmo that can move a portion of a spline proportionately, or change the direction and magnitude of
the tangent at a specified *base point* on the spline. To display a menu of control options, right-click the gizmo.

The gizmo in the illustration is the default setting, which is the Move Point Location option. The square grip is located
at a specified base point on the spline, and is used to stretch a portion of the spline.

![](../images/GUID-42E3AB1F-29ED-407E-89E8-08F2F3FA6A71-low.png)

The red and green axis arrow grips constrain the movement of the square grip in their respective directions.

TIP: Not visible in the illustration is a blue axis arrow grip that points toward you. This axis is visible in other views such
as a 3D isometric view, and can be used to modify the shape of a spline in 3D.

Click the downward-pointing triangular grip to switch to the Move Tangent Direction option as illustrated below. Even though
the axes of the gizmo change their location, the base point remains the same. With this option, moving the square grip changes
the slope of the tangent at the base point.

The tangent arrow grip changes the magnitude of the tangent at the base point, creating either a sharper or a flatter curvature
at the base point. In the illustration, the magnitude of the tangent is being increased.

## Edit Splines with a Palette

The Properties Inspector provides access to several spline parameters and options, including the degree of the spline, the
weight for each control point, the *knot parameterization* method used in conjunction with fit points, and whether the spline is closed.

## Trim, Extend, and Fillet Splines

Trimming a spline shortens it without changing the shape of the portion that remains. Extending a spline lengthens it by
adding a linear portion that is tangent to the end of the spline (C1 continuity). If the shape of the spline is later changed,
the tangency of the linear portion is not maintained.

![](../images/GUID-AD8AC4AB-272A-4B3B-9CD7-B3ECCD8AC903-low.png)

Trimming a spline shortens it without changing the shape of the portion that remains.

Filleting a spline creates an arc that is tangent to the spline and the other selected object. The spline might be extended
with a linear portion to complete the fillet operation.

![](../images/GUID-237E7F3E-920E-4EB2-A707-61A023EDC44C-low.png)

#### Related References

* [Commands for Editing Specific Objects](Commands-for-Editing-Specific-Objects.md)

#### Related Information

* [To Join Polylines, Splines, Lines, and Arcs Into a Single Polyline](To-Join-Polylines,-Splines,-Lines,-and-Arcs-Into-a-Single-Polyline.md)
* [To Convert a Spline to a Polyline](To-Convert-a-Spline-to-a-Polyline.md)
* [To Reverse Lines, Polylines, Splines, or Helixes](To-Reverse-Lines,-Polylines,-Splines,-or-Helixes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*