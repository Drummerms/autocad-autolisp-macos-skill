# SOLDRAW (Command)

Generates profiles and sections in layout viewports created with SOLVIEW.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Modeling Setup drop-down ![](../images/ac.menuaro.gif) Drawing.
![](../images/GUID-F3EFB6F4-3848-436F-A251-158619383626-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Seup ![](../images/ac.menuaro.gif) Drawing.

## Summary

After using SOLVIEW, visible and hidden lines representing the silhouette and edges of solids in the viewport are created
and then projected to a plane perpendicular to the viewing direction.

## List of Prompts

The following prompts are displayed.

Select viewports to draw ...

Select objects:
*Select the viewports to be drawn*

SOLDRAW can only be used in viewports that have been created with
[SOLVIEW](SOLVIEW-Command.md).

Visible and hidden lines representing the silhouette and edges of solids in the viewport are created and then projected to
a plane perpendicular to the viewing direction. Silhouettes and edges are generated for all solids and portions of solids
behind the cutting plane. For sectional views, cross-hatching is created using the current values of the
[HPNAME](HPNAME-System-Variable.md),
[HPSCALE](HPSCALE-System-Variable.md), and
[HPANG](HPANG-System-Variable.md) system variables.

Any existing profiles and sections in the selected viewport are deleted, and new ones are generated. All layers, except those
required to display the profile or section, are frozen in each viewport.

WARNING:Do not place permanent drawing information on the
*view name*-VIS,
*view name*-HID, and *view name*-HAT layers. The information stored on these layers is deleted and updated when SOLDRAW is run.

To undo a viewport drawn by SOLDRAW, you must use the Back option of
[UNDO](UNDO-Command.md).

#### Related Concepts

* [About Flattened Views](About-Flattened-Views.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*