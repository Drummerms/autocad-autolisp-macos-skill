# LOFT (Command)

Creates a 3D solid or surface in the space between several cross sections.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Modeling drop-down ![](../images/ac.menuaro.gif) Loft.
![](../images/GUID-E0E3CB70-083C-41D2-BEE5-8613DB266A8E-low.png)

*Menu*:
Draw
![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Loft.

## Summary

Creates a 3D solid or surface by specifying a series of cross sections. The cross sections define the shape of the resulting
solid or surface. You must specify at least two cross sections.

![](../images/GUID-3B8A5849-217C-4CCA-8BB0-839F4E28FAFC-low.png)

Loft profiles can be open or closed, planar or non-planar, and can also be edge subobjects. Use the mode option to select
whether to create a surface or a solid.

![](../images/GUID-3A522E1D-0A42-4700-85B1-E980A104A1B2-low.gif)

When creating surfaces, use
[SURFACEMODELINGMODE](SURFACEMODELINGMODE-System-Variable.md) to control whether the surface is a NURBS surface or a procedural surface. Use
[SURFACEASSOCIATIVITY](SURFACEASSOCIATIVITY-System-Variable.md) to control whether procedural surfaces are associative.

You can use the following objects and subobjects with LOFT:

| Objects That Can Be Used as Cross Sections | Objects That Can Be Used as a Loft Path | Objects That Can Be Used as Guides |
| 2D polyline | Spline | 2D spline |
| 2D solid |  |  |
| 2D spline | Helix | 3D spline |
| Arc | Arc | Arc |
| Circle | Circle | 2D polyline  NOTE: 2D polylines can be used as guides if they contain only 1 segment. |
| Edge sub-objects | Edge subobjects | Edge subobjects |
| Ellipse | Ellipse | 3D polyline |
| Elliptical arc | Elliptical arc | Elliptical arc |
| Helix | 2D polyline |  |
| Line | Line | Line |
| Planar or non-planar face of solid |  |  |
| Planar or non-planar surface |  |  |
| Points (first and last cross section only) | 3D polyline |  |
| Region |  |  |
| Trace |  |  |

To automatically delete the cross sections, guides, and paths, use
[DELOBJ](DELOBJ-System-Variable.md). If
[surface associativity](SURFACEASSOCIATIVITY-System-Variable.md) is on, DELOBJ is ignored and the originating geometry is not deleted.

## List of Prompts

The following prompts are displayed.

Cross Sections in Lofting Order
:   Specifies open or closed curves in the order in which the surface or solid will pass through them.

Point
:   If you select the Point option, you must also select a closed curve.

Join Multiple Curves
:   Joins multiple, end-to-end curves as one cross section.

Mode
:   Controls whether the lofted object is a solid or a surface.

Options
:   * [Guides](LOFT-Command.md)
    * [Path](LOFT-Command.md)
    * [Cross sections only](LOFT-Command.md)
    * [Settings](LOFT-Command.md)

Continuity
:   This option only displays if the
    [LOFTNORMALS](LOFTNORMALS-System-Variable.md) system variable is set to 1 (smooth fit). Specifies whether the continuity is G0, G1, or G2 where the surfaces meet.

    ![](../images/GUID-990B8BC1-9022-4CCC-80FD-DD76485C0486-low.png)

Bulge Magnitude
:   This option only displays if the
    [LOFTNORMALS](LOFTNORMALS-System-Variable.md) system variable is set to 1 (smooth fit). Specifies a bulge magnitude value for objects that have a continuity of G1 or G2.

    ![](../images/GUID-531D8DEC-A088-4C9D-AF69-17E1C49ECA3F-low.png)

Guides

:   Specifies guide curves that control the shape of the lofted solid or surface. You can use guide curves to control how points
    are matched up on corresponding cross sections to prevent undesired results, such as wrinkles in the resulting solid or surface.

    ![](../images/GUID-0278A51B-7E9D-429C-9639-5D909171BD1E-low.png)

    * Intersects each cross section
    * Starts on the first cross section
    * Ends on the last cross section

    Select any number of guide curves for the lofted surface or solid and press Enter.

Path

:   Specifies a single path for the lofted solid or surface.

    ![](../images/GUID-2E83D4EC-7A63-408F-81FF-E16C6120BE0F-low.png)

    The path curve must intersect all planes of the cross sections.

Cross Sections Only

:   Creates lofted objects without using guides or paths.

Settings

:   Displays the
    [Loft Settings dialog box](Loft-Settings-Dialog-Box.md).

#### Related Concepts

* [About Using Grips to Edit 3D Objects](About-Using-Grips-to-Edit-3D-Objects.md)
* [About Creating a Solid or Surface by Lofting](About-Creating-a-Solid-or-Surface-by-Lofting.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*