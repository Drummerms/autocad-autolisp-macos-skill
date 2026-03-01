# Flatshot Dialog Box

Creates a 2D representation of all 3D objects based on the current view.

FLATSHOT (Command)

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Solid panel ![](../images/ac.menuaro.gif) Section Plan drop-down ![](../images/ac.menuaro.gif) Flatshot.
![](../images/GUID-64E3DC35-6542-45DB-87C3-DDEAD129B03C-low.png)

![](../images/GUID-972F85FA-E879-491E-82B2-C00B8AF36276-low.png)

## Summary

The edges of all 3D solids and surfaces are projected line-of-sight onto a plane parallel to the viewing plane. The 2D representations
of these edges are inserted as a block on the
*XY* plane of the UCS. This block can be exploded for additional changes. The result can also be saved as a separate drawing file.

## List of Options

The following options are displayed.

Destination

Controls where the flattened representation is created.

Insert As New Block
:   Specifies to insert the flattened representation as a block in the current drawing.

Replace Existing Block
:   Replaces an existing block in the drawing with the newly created block.

Select Block
:   Closes the dialog box temporarily while you select the block you are replacing in the drawing. When you finish selecting the
    block, press Enter to re-display the Flatshot dialog box.

Block Selected / No Block Selected
:   Indicates whether a block has been selected.

Export to a File
:   Saves the block to an external file.

Foreground Lines

Contains controls for setting the color and linetype of lines that are not obscured in the flattened view.

Color
:   Sets the color of lines that are not obscured in the flattened view.

Linetype
:   Sets the linetype of lines that are not obscured in the flattened view.

Obscured Lines

Controls whether lines that are obscured in the drawing are displayed in the flattened view, and sets the color and linetype
of these obscured lines.

Show
:   Controls whether obscured lines are shown in the flattened representation. When selected, the 2D flattened representation
    displays lines hidden by other objects.

Color
:   Sets the color of lines that lie behind geometry in the flattened view.

Linetype
:   Sets the linetype of lines that lie behind geometry in the flattened view.

Include Tangential Lines

Creates silhouette edges for curved surfaces.

Create

Creates the flattened view.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*