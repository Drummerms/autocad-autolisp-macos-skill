# 3DEDITBAR (Command)

Reshapes splines and NURBS surfaces, including their tangency properties.

## Summary

Several grips are available for moving a point and changing the magnitude and direction of tangents at specific points on
splines, and in the
*U*,
*V* , and
*W* directions on NURBS surfaces.

![](../images/GUID-0E04DDE4-E7F4-43D0-B854-0183BAF5BF0A-low.png)

## The Grips on the Gizmo

The 3D Edit Bar gizmo includes three grips:

* *Triangle grip*. Specifies the method for reshaping the selected object.

  ![](../images/GUID-21BBBF74-AC87-4B73-8062-5E2A7B86FCAB-low.png)
* *Square grip*. Reshapes the selected object by moving the base point or changing the tangent direction at the base point. Use the three
  axes to restrict the movement option to a specified axis. Similarly, the three squares that touch the square grip restrict
  the movement option to the specified planes.

  ![](../images/GUID-24AA0A7D-E244-43A4-A1B4-2695357CD506-low.png)
* *Tangent arrow grip*. Changes the magnitude of the tangent at the base point. For example, lengthening the tangent arrow grip flattens the curvature
  of the surface at the point of tangency. The tangent arrow points in the direction of one of the surface’s
  *U*,
  *V*, or
  *W* axes, depending on the tangent direction specified in
  [3D Edit Bar Shortcut Menu](3D-Edit-Bar-Shortcut-Menu.md).

  ![](../images/GUID-8A1AFC60-92A4-48E3-AC9C-85F33A1DEC75-low.png)

## List of Prompts

The following prompts are displayed.

Select a NURBS surface or curve to edit
:   Specifies the object to be modified. Valid objects include lines, arcs, circles, ellipses and elliptical arcs, polylines,
    helixes, splines, and NURBS surfaces. Objects other than surfaces can be converted to splines.

Select point on curve *or* Select point on NURBS surface
:   Specifies a
    *base point* on the selected curve or NURBS surface. Changes to the selected object are relative to this point.

Base point
:   Specifies a new base point on the curve or NURBS surface.

Displacement
:   Specifies a new base point by projecting the absolute coordinates entered onto the selected curve or surface, when possible.

Undo
:   Cancels the previous change without exiting the command.

Exit
:   Cancels the current operation and returns to the previous prompt, or it exits the command.

#### Related References

* [3D Edit Bar Shortcut Menu](3D-Edit-Bar-Shortcut-Menu.md)

#### Related Concepts

* [About Editing NURBS Surfaces](About-Editing-NURBS-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*