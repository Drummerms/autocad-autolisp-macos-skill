# SOLPROF (Command)

Creates 2D profile images of 3D solids for display in a layout viewport.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Modeling Setup drop-down ![](../images/ac.menuaro.gif) Profile Faces.
![](../images/GUID-BB92D1A7-0095-42E1-9DD8-3EA14C6331BD-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) Setup ![](../images/ac.menuaro.gif) Profile.

## Summary

The selected 3D solids are projected onto a 2D plane parallel with the current layout viewport. The resulting 2D objects are
generated on separate layers for hidden and visible lines and are displayed only in that viewport.

## List of Prompts

The following prompts are displayed.

Select objects:
*Use an object selection method*

Display hidden profile lines on separate layer? [[Yes](SOLPROF-Command.md)/[No](SOLPROF-Command.md)] <Y>:
*Enter* *y* *or* *n**, or press*Enter

Yes
:   Generates only two blocks: one for the visible lines and one for the hidden lines of the entire selection set. When you generate
    hidden lines, solids can partially or completely hide other solids. The visible profile block is drawn in the BYLAYER linetype,
    and the hidden profile block is drawn in the HIDDEN linetype (if loaded). The visible and hidden profile blocks are placed
    on uniquely named layers using the following naming conventions:

    PV-viewport handle for the visible profile layer

    PH-viewport handle for the hidden profile layer

    For example, if you create a profile in a viewport whose handle is 4B, the blocks containing the visible lines are inserted
    on layer PV-4B, and the block containing the hidden lines (if requested) is inserted on layer PH-4B. If these layers do not
    exist, the command creates them. If the layers do exist, the blocks are added to the information already on the layers.

    NOTE:To determine the handle of a viewport, select the viewport while in paper space and use the
    [LIST](LIST-Command.md) command. Choose a layout tab to move from model space to paper space.

    SOLPROF does not change the display of layers; if you want to view only the profile lines that you have created, turn off
    the layer containing the original solid (usually the current layer).

No
:   Treats all profile lines as visible lines and creates a block for the profile lines of each selected solid. All profile lines
    for each solid in the selection set are generated, even if a solid is partially or completely obscured by another solid. The
    visible profile blocks are drawn in the same linetype as the original solid and placed on a uniquely named layer using the
    naming convention described under the Yes option.

    ![](../images/GUID-C9C72FEE-9DE6-4356-92CA-91EA2C79C70C-low.png)

    NOTE:Solids that overlap each other (share some common volume) produce dangling edges if you request hidden-line removal. This
    happens because the edges must be broken at the point where they enter another solid to separate them into visible and hidden
    portions. You can eliminate dangling edges by combining the overlapping solids (using
    [UNION](UNION-Command.md)) before generating a profile.

Yes
:   Creates the profile lines with 2D objects.

    The 3D profile is projected onto a plane normal to the viewing direction and passing through the origin of the UCS. SOLPROF
    cleans up the 2D profile by eliminating lines that are parallel to the viewing direction and by converting arcs and circles
    that are viewed on edge into lines.

No
:   Creates the profile lines with 3D objects.

    The next prompt determines whether tangential edges are displayed. A tangential edge is the transition line between two tangent
    faces. It's the imaginary edge at which two faces meet and are tangent. For example, if you fillet the edge of a box, tangential
    edges are created where the cylindrical face of the fillet blends into the planar faces of the box. Tangential edges are not
    shown for most drafting applications.

    ![](../images/GUID-068DD517-0DF7-4629-8008-1FED75B66978-low.png)

#### Related Concepts

* [About Flattened Views](About-Flattened-Views.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*