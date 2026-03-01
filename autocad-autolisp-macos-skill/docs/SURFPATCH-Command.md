# SURFPATCH (Command)

Creates a new surface by fitting a cap over a surface edge that forms a closed loop.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Surface panel ![](../images/ac.menuaro.gif) Surface Creation drop-down ![](../images/ac.menuaro.gif) Surface Patch.
![](../images/GUID-D5D5C09C-ED89-48F7-B6EA-0F7A7B93AB9D-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Surfaces ![](../images/ac.menuaro.gif) Patch.

## Summary

You can also add an additional curve over the closed loop to constrain and guide the patch surface.

![](../images/GUID-D8E63FA4-C1C2-4363-BE14-F951BC580190-low.gif)

When you create a patch surface, you can specify surface continuity and bulge magnitude. If the SURFACEASSOCIATIVITY system
variable is set to 1, associativity is maintained between the patch surface and the originating edges or curves.

## List of Prompts

The following prompts are displayed.

Select
[Surface Edges](SURFPATCH-Command.md) to patch or [[Chain](SURFPATCH-Command.md)/[Curves](SURFPATCH-Command.md)] <CUrves>:

Surface Edges
:   Selects individual surface edges and adds them to the selection set.

Chain
:   Selects contiguous edges of connected but separate surface objects.

Curves
:   Selects curves rather than edges.

Select one or more closed surface edges (not the surface itself), a chain of edges, or one or more curves. You cannot choose
both edges and curves at the same time.

## List of Options

Once you have defined the surface edges to patch, the following options are displayed.

Press Enter to accept the patch surface or [[Continuity](SURFPATCH-Command.md)/[Bulge Magnitude](SURFPATCH-Command.md)/[Guides](SURFPATCH-Command.md)]:

Continuity
:   Measures how smoothly surfaces flow into each other. The default is G0. Select a value or use the grip to change the continuity.

Bulge Magnitude
:   For best results, enter a value between 0 and 1 to set the roundness of the patch surface edge where it meets the originating
    surface. The default is 0.5.

Guides
:   Uses additional guide curves to shape the patch surface. Guide curves can be curves or points.

#### Related Concepts

* [About Creating Procedural Surfaces](About-Creating-Procedural-Surfaces.md)
* [About Patching Surfaces](About-Patching-Surfaces.md)
* [About Creating 3D Surfaces](About-Creating-3D-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*