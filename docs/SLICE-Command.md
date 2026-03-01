# SLICE (Command)

Creates new 3D solids and surfaces by slicing, or dividing, existing objects.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Slice.
![](../images/GUID-D7E30980-C9DD-4CDC-92F0-1FA149B06C51-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) 3D Operations ![](../images/ac.menuaro.gif) Slice.

## Summary

The cutting plane is defined with 2 or 3 points, by specifying a major plane of the UCS, or by selecting a surface object
(but not a mesh). Either one or both sides of the sliced 3D solids can be retained.

![](../images/GUID-FB8EDB1D-3FF8-4301-9957-8753C88890B8-low.gif)

The sliced objects retain the layer and color properties of the original solids. However, the resulting solid or surface objects
do not retain a history of the original objects.

Objects that Can Be Used in a Slice Operation

| Objects that can be sliced | Objects that can be used as cutting planes |
| 3D solids | Surfaces |
| Surfaces | Circles |
|  | Ellipses |
|  | Circular or elliptical arcs |
|  | 2D splines |
|  | 3D polyline segments |

## List of Prompts

The following prompts are displayed.

Objects to slice
:   Specifies the 3D solid or surface object that you want to slice. If you select a mesh object, you can choose to convert it
    to a 3D solid or surface before completing the slice operation.

    * [Start point of slicing plane](SLICE-Command.md)
    * [Planar object](SLICE-Command.md)
    * [Surface](SLICE-Command.md)
    * [Z axis](SLICE-Command.md)
    * [View](SLICE-Command.md)
    * [XY](SLICE-Command.md)
    * [YZ](SLICE-Command.md)
    * [ZX](SLICE-Command.md)
    * [3points](SLICE-Command.md)

Start point of slicing plane
:   Sets the first of two points that define the angle of the slicing plane. The slicing plane is perpendicular to the
    *XY* plane of the current UCS.

    * *Second point on plane.*Sets the second of two points on the slicing plane.
      + [Point on desired side](SLICE-Command.md)
      + [Keep both sides](SLICE-Command.md)

Planar object
:   Aligns the cutting plane with a plane that contains a selected circle, ellipse, circular or elliptical arc, 2D spline, or
    2D polyline segment.

    ![](../images/GUID-BECE6F43-F550-4782-BA8A-3A4A7C34E9E7-low.png)

    * *Select a circle, ellipse, arc, 2D-spline, or 2D-polyline.* Specifies the object to use for alignment.

Surface
:   Aligns the cutting plane with a surface.

    ![](../images/GUID-BECE6F43-F550-4782-BA8A-3A4A7C34E9E7-low.png)

    * *Select a surface.*Specifies a surface to be used for alignment.

      NOTE:You cannot select meshes created with the
      [EDGESURF](EDGESURF-Command.md),
      [REVSURF](REVSURF-Command.md),
      [RULESURF](RULESURF-Command.md), and
      [TABSURF](TABSURF-Command.md) commands.

      + [Point on desired side](SLICE-Command.md)
      + [Keep both sides](SLICE-Command.md)

Z axis
:   Defines the cutting plane by specifying a point on the plane and another point on the
    *Z* axis (normal) of the plane.

    ![](../images/GUID-0FEE5403-ACBF-4655-B70E-963053115AE4-low.png)

    * *Specify a point on the section plane.*Sets a point on the slicing plane.
    * *Specify a point on the Z-axis (normal) of the plane.* Specifies a point that defines the axis that is perpendicular to the slicing plane.
    * + [Point on desired side](SLICE-Command.md)
      + [Keep both sides](SLICE-Command.md)

View
:   Aligns the cutting plane with the current viewport's viewing plane. Specifying a point defines the location of the cutting
    plane.

    ![](../images/GUID-9ED12323-5019-44B9-A6B1-7EF059803831-low.png)

    * *Specify a point on the current view plane.* Sets a point on the object to start the slice.
    * + [Point on desired side](SLICE-Command.md)
      + [Keep both sides](SLICE-Command.md)

XY
:   Aligns the cutting plane with the
    *XY* plane of the current user coordinate system (UCS). Specifying a point defines the location of the cutting plane.

    ![](../images/GUID-100BFF43-E285-4438-AEB4-C080C1AB333C-low.png)

    * *Point on the XY-plane.*Sets the location of the slice.
    * + [Point on desired side](SLICE-Command.md)
      + [Keep both sides](SLICE-Command.md)

YZ
:   Aligns the cutting plane with the
    *YZ* plane of the current UCS. Specifying a point defines the location of the cutting plane.

    ![](../images/GUID-26D406B1-FE70-4514-AABF-7798EE700638-low.png)

    * *Point on the YZ-plane.*Sets the location of the slice.

ZX
:   Aligns the cutting plane with the
    *ZX* plane of the current UCS. Specifying a point defines the location of the cutting plane.

    * *Point on the ZX-plane.* Sets the location of the slice.

      If a single object is sliced into more than two objects, one solid or surface is created from the objects on one side of the
      plane and another solid or surface is created from the objects on the other side.

      ![](../images/GUID-9D424F0B-C274-47D6-A176-058AAC12694A-low.png)

      ![](../images/GUID-D5B88486-15D5-4123-8FD4-B014FBCB38B6-low.png)

3points
:   Defines the cutting plane using three points.

    ![](../images/GUID-6DAF2DBB-FF67-46A7-BAAE-37DE2D332FDB-low.png)

Point on desired side
:   Uses a point to determine which side of the sliced solids your drawing retains. The point cannot lie on the cutting plane.

    ![](../images/GUID-D5B88486-15D5-4123-8FD4-B014FBCB38B6-low.png)

Keep both sides
:   Retains both sides of the sliced solids. Slicing a single solid into two pieces creates two solids from the pieces on either
    side of the plane. SLICE never creates more than two new composite solids for each selected solid.

    ![](../images/GUID-DF99CD33-67F0-4697-BA06-A99C64CD1A13-low.png)

#### Related Concepts

* [About Slicing 3D Solids and Surfaces](About-Slicing-3D-Solids-and-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*