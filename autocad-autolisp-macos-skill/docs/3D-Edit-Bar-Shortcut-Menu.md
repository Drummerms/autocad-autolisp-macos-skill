# 3D Edit Bar Shortcut Menu

Displays options to set the location of the base point, constraints, and tangency.

## Access Methods

Shortcut menu: Right-click on the 3D Edit Bar gizmo.

## Summary

The 3D Edit Bar shortcut menu displays several options depending on whether a spline or a NURBS surface is selected, where
you click, and which editing method, move or tangent, is current.

The illustration displays an imaginary
*UV* plane in yellow that is tangent to the surface, and contains the base point. It displays the
*U* axis in red, the
*V* axis in green, and
*W* axis, which is
*normal* to the surface, in blue.

![](../images/GUID-CC2E39E6-6D50-4C30-BFF5-20A8A5BF8420-low.png)

NOTE:By default, the orientation of the 3D Edit Bar gizmo is aligned with the World Coordinate System, but its alignment can be
changed using the shortcut menu. To align the axes with the
*U*,
*V*, and
*W* axes of a NURBS surface, choose Align Gizmo With > Object.

## List of Options

The following options are displayed.

Move Point Location
:   Reshapes the selected object by moving the base point.

Move Tangent Direction
:   Reshapes the selected object by changing the slope of the tangent at the base point.

U Tangent Direction
:   Locates the tangent arrow grip on the
    *U* axis. Changes to the tangency are constrained to the
    *UW* plane.

V Tangent Direction
:   Locates the tangent arrow grip on the
    *V* axis. Changes to the tangency are constrained to the
    *VW* plane.

Normal Tangent Direction
:   Locates the tangent arrow grip on the
    *W* axis, which is normal to the surface at the base point. Changes to the tangency are constrained to the
    *UW* plane.

Set Constraint
:   Sets whether the change in tangency or point location is constrained to a specific axis or major plane.

    * *X, Y* or
      *Z*. Restricts the change to the specified World Coordinate System (WCS) axis.
    * *XY, YZ*, or
      *XZ*. Restricts the change to the specified World Coordinate System (WCS) plane.

Relocate Base Point
:   Specifies a new base point on the curve or NURBS surface.

Align Gizmo With
:   Reorients the gizmo to align with the WCS or UCS, or with a selected face or object.

#### Related Concepts

* [About Editing NURBS Surfaces](About-Editing-NURBS-Surfaces.md)
* [About Modifying Splines](About-Modifying-Splines.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*