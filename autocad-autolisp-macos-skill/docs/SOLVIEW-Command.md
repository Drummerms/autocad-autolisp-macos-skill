# SOLVIEW (Command)

Creates orthographic views, layers, and layout viewports automatically for 3D solids.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Modeling Setup drop-down ![](../images/ac.menuaro.gif) View Faces.
![](../images/GUID-1193C427-4FFD-43F7-AC42-0FAADFCB771E-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Setup ![](../images/ac.menuaro.gif) View.

## Summary

This command automates the manual process of creating views, layers, and layout viewports for 3D models. For ongoing work,
it is recommended that you create drawing template (DWT) files customized for 3D.

NOTE:SOLVIEW must be run on a layout tab. If the Model tab is current, the last active layout tab is made current.

## List of Prompts

The following prompts are displayed.

Enter an option [[Ucs](SOLVIEW-Command.md)/[Ortho](SOLVIEW-Command.md)/[Auxiliary](SOLVIEW-Command.md)/[Section](SOLVIEW-Command.md)]:
*Enter an option or press* Enter *to exit the command*

SOLVIEW places the viewport objects on the VPORTS layer, which it creates if it does not already exist. The view-specific
information that is saved with each viewport you create is used by
[SOLDRAW](SOLDRAW-Command.md) to generate the final drawing view.

SOLVIEW creates layers that SOLDRAW uses to place the visible lines and hidden lines for each view,
*view name*-VIS,
*view name*-HID,
*view name*-HAT, and a layer where you can place dimensions that are visible in individual viewports,
*view name*-DIM.

WARNING:The information stored on these layers is deleted and updated when you run
[SOLDRAW](SOLDRAW-Command.md). Do not place permanent drawing information on these layers.

UCS

Creates a profile view relative to a user coordinate system. If no viewports exist in your drawing, the UCS option is a good
way to create an initial viewport from which other views can be created. All other SOLVIEW options require an existing viewport.

You have the option of using the current UCS or a previously saved one as the profile plane. The viewport projection is created
parallel to the
*XY* plane of the UCS with the
*X* axis facing right and the
*Y* axis upward.

![](../images/GUID-F68444B4-F654-43A8-8AC4-971A142AB1FF-low.png)

Named
:   Uses the
    *XY* plane of a named UCS to create a profile view.

    Enter the name of the UCS you want to use and the scale of your view. Entering a scale is equivalent to zooming your viewport
    by a factor relative to paper space.

    The center is based on the current model space extents.

World
:   Uses the
    *XY* plane of the WCS to create a profile view.

    Enter the name of the UCS you want to use and the scale of your view. Entering a scale is equivalent to zooming your viewport
    by a factor relative to paper space.

    The center is based on the current model space extents.

?—List Named UCSs
:   Lists the names of existing user coordinate systems. The list is filtered using the wild-card combinations you enter (wild-card
    characters accepted by the UCS command are valid).

Current
:   Uses the
    *XY* plane of the current UCS to create a profile view.

    Enter the name of the UCS you want to use and the scale of your view. Entering a scale is equivalent to zooming your viewport
    by a factor relative to paper space.

    The center is based on the current model space extents.

Ortho

Creates a folded orthographic view from an existing view.

![](../images/GUID-173F8DFE-AA11-45D8-9F38-2A9BEF947B38-low.png)

Once you select the side of the viewport you want to use for projecting the new view, a rubber-band line perpendicular to
the side of the viewport helps you locate the center of the new view.

Auxiliary

Creates an auxiliary view from an existing view. An auxiliary view is one that is projected onto a plane perpendicular to
one of the orthographic views and inclined in the adjacent view.

![](../images/GUID-0585040F-2939-434B-A2D6-3DA4451BF744-low.png)

Two points define the inclined plane used for the auxiliary projection. Both points must be located in the same viewport.

A rubber-band line perpendicular to the inclined plane helps you select the center of the new viewport.

Section

Creates a drafting sectional view of solids, complete with cross-hatching. When you use
[SOLDRAW](SOLDRAW-Command.md) on a sectional view created with this option, it creates a temporary copy of the solids and uses
[SLICE](SLICE-Command.md) to perform the operation at the cutting plane that you define. SOLDRAW then generates a profile of the visible half of the
solids and discards the original copy. Finally SOLDRAW sections the solids. Solids not crossing the cutting plane are generated
as full profiles. Because drafting standards recommend not drawing hidden lines in sectional views, SOLVIEW freezes the
*View Name*-HID layer.

![](../images/GUID-60810E31-F86C-44CF-91B6-92EC8D7F41FE-low.png)

In the original viewport, specify two points to define the sectioning plane.

Define the viewing side by specifying a point on one side of the cutting plane.

Enter the scale of the new view. Entering a scale is equivalent to zooming your viewport by a factor relative to paper space.
The default value is a 1:1 scale, which is equivalent to
*zoom 1.0xp*.

At the next prompt, specify the center of the new viewport. If you accepted the default scale (by pressing Enter), a rubber-band
line perpendicular to the sectioning plane helps you locate the center of the new view. Otherwise, you can place the view
anywhere.

#### Related Concepts

* [About Flattened Views](About-Flattened-Views.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*