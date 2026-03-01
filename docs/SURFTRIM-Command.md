# SURFTRIM (Command)

Trims portions of a surface where it meets another surface or type of geometry.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Surface panel ![](../images/ac.menuaro.gif) Surface Trim drop-down ![](../images/ac.menuaro.gif) Surface Trim.
![](../images/GUID-AECA87E8-0EE6-46D7-BEF6-452AA122AAE8-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Surface Editing ![](../images/ac.menuaro.gif) Trim.

## Summary

Trims portions of a surface where it meets or bisects a curve, region, or another surface.

![](../images/GUID-D4B7421E-6825-4B09-9114-10CDC66B5479-low.gif)

If the
[SURFACEASSOCIATIVITY](SURFACEASSOCIATIVITY-System-Variable.md) system variable is set to 1, the trimmed surface updates whenever the trimming edges are modified.

## List of Prompts

The following prompts are displayed.

Select Surfaces or Regions to Trim
:   Select one or more surfaces or regions to trim.

Select Cutting Curves, Surfaces, or Regions
:   The curves that can be used as a trimming edge includes lines, arc, circles, ellipses, 2D polylines, 2D spline fit polylines,
    2D curve fit polylines, 3D polylines, 3D spline-fit polylines, splines, and helixes. You can also use surfaces and regions
    as trimming boundaries.

Select Area to Trim
:   Select one or more regions on a surface to remove.

Extend
:   Controls whether the cutting surface is trimmed to meet the edge of the trimmed surface.

Projection Direction
:   The cutting geometry is projected onto the surface. Controls the projection angle as follows:

    | Automatic | * When trimming a surface or region in plan, parallel view (for example, the default Top, Front, and Right view), the cutting   geometry is projected onto the surface in the view direction. * When trimming a surface or region with a planar curve in an angled parallel or perspective view, the cutting geometry is projected   onto the surface in a direction perpendicular to the curve plane. * When trimming a surface or region with a 3D curve in an angled, parallel or perspective view (for example, the default perspective   view), the cutting geometry is projected onto the surface in a direction parallel to the   *Z* direction of the current UCS. |
    | View | Projects the geometry based on the current view. |
    | UCS | Projects the geometry in the +*Z*and -*Z* axis of the current UCS. |
    | None | The surface will only be trimmed if the cutting curve lies on the surface. |

#### Related Concepts

* [About Trimming Surfaces](About-Trimming-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*