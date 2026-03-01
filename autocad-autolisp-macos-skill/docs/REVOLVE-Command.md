# REVOLVE (Command)

Creates a 3D solid or surface by sweeping an object around an axis.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Modeling drop-down ![](../images/ac.menuaro.gif) Revolve.
![](../images/GUID-76BD4AC0-B463-4FCA-A8F2-50EEDD4C542A-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Revolve.

## Summary

Open profiles create surfaces and closed profiles can create either a solid or a surface. The MOde option controls is a solid
of surface is created. When creating a surface, SURFACEMODELINGMODE system variable controls if a procedural or NURBS surface
is created.

![](../images/GUID-1F54DE75-7FC2-4A0F-B32D-53EB239BA6C5-low.gif)

Revolve path and profile curves can be:

* Open or closed
* Planar or non-planar
* Solid and surface edges
* A single object (to extrude multiple lines, convert them to a single object with the JOIN command)
* A single region (to extrude multiple regions, convert them to a single object with the REGION command)

To automatically delete the profile, use the DELOBJ system variable. If
[associativity](SURFACEASSOCIATIVITY-System-Variable.md) is on, the DELOBJ system variable is ignored and the originating geometry is not deleted.

### Objects That Can Be Revolved

| Surfaces | Elliptical arcs | 2D solids |
| Solids | 2D and 3D splines | Traces |
| Arcs | 2D and 3D polylines | Ellipses |
| Circles | Regions |  |

NOTE:Select face and edge subobjects by pressing Ctrl while you select them.

You cannot revolve objects contained within a block or objects that will self-intersect. REVOLVE ignores the width of a polyline
and revolves from the center of the path of the polyline.

The right-hand rule determines the positive direction of rotation.

## List of Prompts

The following prompts are displayed.

Objects to Revolve
:   Specifies the objects to be revolved about an axis.

Mode
:   Controls whether the revolve action creates a solid or a surface. Surfaces are extended as either NURBS surfaces or procedural
    surfaces, depending on the SURFACEMODELINGMODE system variable.

Axis Start Point
:   Specifies the first point of the axis of revolution. The positive axis direction is from the first to the second point.

Axis Endpoint
:   Sets the endpoint for the axis of revolution.

Start Angle
:   Specifies an offset for the revolution from the plane of the object being revolved.

    Drag your cursor to specify and preview the start angle of the object.

Angle of Revolution
:   Specifies how far the selected object revolves about the axis.

    A positive angle revolves the objects in a counterclockwise direction. A negative angle revolves the objects in a clockwise
    direction. You can also drag the cursor to specify and preview the angle of revolution.

    ![](../images/GUID-980F4DE6-9CF8-4FB3-B988-1D74FB9A6541-low.png)

Object
:   Specifies an existing object to be used as an axis. The positive axis direction is from the closest to the farthest endpoint
    of this object.

    ![](../images/GUID-7CA179E8-469A-48B9-8E5A-D109646F3C09-low.png)

    You can use lines, linear polyline segments, and linear edges of solids or surfaces as an axis.

    NOTE:Select an edge subobject by pressing Ctrl while you select an edge.

X (Axis)
:   Sets the positive
    *X* axis of the current UCS as the positive axis direction.

    ![](../images/GUID-40190CE8-BC79-4445-8002-628C015C027C-low.png)

Y (Axis)
:   Sets the positive
    *Y* axis of the current UCS as the positive axis direction.

    ![](../images/GUID-2876C823-A5FE-400B-8DF8-B65582D90813-low.png)

Z (Axis)
:   Sets the positive
    *Z* axis of the current UCS as the positive axis direction.

Reverse
:   Changes the direction of the revolve; similar to entering a - (minus) angle value. The revolved object on the right shows
    a spline revolved at the same angle as the object on the left, but using the reverse option.

    ![](../images/GUID-01379C14-4547-4556-ADF3-B0A7DAACF65F-low.png)

Expression
:   Enter a formula or equation to specify the revolve angle.

#### Related Concepts

* [About Using Grips to Edit 3D Objects](About-Using-Grips-to-Edit-3D-Objects.md)
* [About Creating a Solid or Surface by Revolving](About-Creating-a-Solid-or-Surface-by-Revolving.md)
* [About the User Coordinate System (UCS)](About-the-User-Coordinate-System-UCS.md)
* [About Parametric Formulas and Equations](About-Parametric-Formulas-and-Equations.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*