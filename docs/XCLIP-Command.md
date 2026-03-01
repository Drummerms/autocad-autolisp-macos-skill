# XCLIP (Command)

Crops the display of a selected external reference or block reference to a specified boundary.

## Access Methods

*Menu*:
Modify ![](../images/ac.menuaro.gif) Clip ![](../images/ac.menuaro.gif) Xref.

*Shortcut menu*: Select an xref. Right-click in the drawing area and click Clip Xref.

## Summary

The clipping boundary determines the portion of an xref or block instance that is hidden, either outside or inside the boundary.
The visibility of the clipping boundary is controlled by the
[XCLIPFRAME](XCLIPFRAME-System-Variable.md) system variable.

TIP:Use the
[CLIP](CLIP-Command.md) command to clip any type of referenced file: images, external references, viewports, and PDF underlays.

## List of Options

The following options are displayed.

On

Displays the clipped portion of the external reference or block in the current drawing.

Off

Displays all of the geometry of the external reference or block in the current drawing, ignoring the clipping boundary.

Clipdepth

Sets the front and back clipping planes on an xref or block. Objects outside the volume defined by the boundary and the specified
depth are not displayed. Regardless of the current UCS, the clip depth is applied parallel to the clipping boundary.

Front Clip Point
:   Creates a clipping plane passing through and perpendicular to the clipping boundary.

Distance
:   Creates a clipping plane the specified distance from and parallel to the clipping boundary.

Remove
:   Removes both the front and back clipping planes.

Delete

Removes a clipping boundary for the selected xref or block. To temporarily turn off a clipping boundary, use the Off option.
Delete erases the clipping boundary and the clipdepth. The
[ERASE](ERASE-Command.md) command cannot be used to delete clipping boundaries.

Generate Polyline

Automatically draws a polyline coincident with the clipping boundary. The polyline assumes the current layer, linetype, lineweight,
and color settings. Use this option when you want to modify the current clipping boundary using
[PEDIT](PEDIT-Command.md) and then redefine the clipping boundary with the new polyline. To see the entire xref while redefining the boundary, use
the Off option.

New Boundary

Defines a rectangular or polygonal clipping boundary, or generates a polygonal clipping boundary from a polyline.

Select Polyline
:   Defines the boundary with the selected polyline. The polyline can be open but must consist of straight line segments and cannot
    intersect itself.

Polygonal
:   Defines a polygonal clipping boundary with three or more points that you specify for the vertices of a polygon.

Rectangular
:   Defines a rectangular boundary with the points that you specify for opposite corners.

Invert Clip
:   Inverts the mode of the clipping boundary: objects are clipped either outside the boundary or inside the boundary.

NOTE:You can only create a new clipping boundary for a selected XREF underlay when the old boundary is deleted.

#### Related Concepts

* [About Clipping External References and Blocks](About-Clipping-External-References-and-Blocks.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*