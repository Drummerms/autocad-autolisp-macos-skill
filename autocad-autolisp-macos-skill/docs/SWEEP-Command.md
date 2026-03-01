# SWEEP (Command)

Creates a 3D solid or 3D surface by sweeping a 2D object or subobject along an open or closed path.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Modeling drop-down ![](../images/ac.menuaro.gif) Sweep.
![](../images/GUID-C86F5BE9-D23A-4E26-BF0D-DB9C1A521E0B-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Sweep.

Open-ended objects create 3D surfaces, while objects that enclose an area can be set to create either 3D solids or 3D surfaces.

You can use the following objects and paths when creating a swept solid or surface:

| Objects that Can Be Swept | Objects that Can Be Used as a Sweep Path |
| 2D and 3D splines | 2D and 3D splines |
| 2D polylines | 2D and 3D polylines |
| 2D solids | Solid, surface and mesh edge subobjects |
| 3D solid face subobjects | Helices |
| Arcs | Arcs |
| Circles | Circles |
| Ellipses | Ellipses |
| Elliptical arcs | Elliptical arcs |
| Lines | Lines |
| Regions |  |
| Solid, surface and mesh edge subobjects |  |
| Trace |  |

NOTE: Select face and edge subobjects by pressing Ctrl while you select them.

To automatically delete the original geometry used to create the object, use the DELOBJ system variable. For associative surfaces,
the DELOBJ system variable is ignored and the originating geometry is not deleted.

The following prompts are displayed.

Objects to Sweep
:   Specifies an object to use as the sweep profile.

Sweep Path
:   Specifies the sweep path based on the object you select.

Mode
:   Controls whether the sweep action creates a solid or a surface. Surfaces are swept as either NURBS surfaces or procedural
    surfaces, depending on the SURFACEMODELINGMODE system variable.

Alignment
:   Specifies whether the profile is aligned to be normal to the tangent direction of the sweep path.

    If the profile is not perpendicular (normal) to the tangent of the start point of the path, then the profile automatically
    aligns. Enter No at the alignment prompt to prevent this.

Base Point
:   Specifies a base point for the objects to be swept.

Scale
:   Specifies a scale factor for a sweep operation. The scale factor is uniformly applied to the objects that are swept from the
    start to the end of the sweep path.

    * *Reference.* Scales the selected objects based on the length you reference by picking points or entering values.

Twist
:   Sets a twist angle for the objects being swept. The twist angle specifies the amount of rotation along the entire length of
    the sweep path.

    * *Bank.* Specifies whether the curve(s) being swept will naturally bank (rotate) along a 3D sweep path (3D polyline, spline, or helix).

#### Related Concepts

* [About Creating a Solid or Surface by Sweeping](About-Creating-a-Solid-or-Surface-by-Sweeping.md)
* [About Modeling 3D Objects](About-Modeling-3D-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*