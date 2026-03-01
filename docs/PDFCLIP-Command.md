# PDFCLIP (Command)

Crops the display of a selected PDF underlay to a specified boundary.

## Access Methods

![](../images/ac.keyboard.gif) Command entry: PDF Underlay visor ![](../images/ac.menuaro.gif) Create the Clipping Boundary

Shortcut menu: Select a PDF underlay. Right-click in the drawing area and click Clip PDF.

## Summary

The clipping boundary determines the portion of an image outside the boundary that is hidden. The visibility of the clipping
boundary is controlled by the PDFFRAME and FRAME system variables.

The boundary you specify must be in a plane parallel to the PDF underlay.

TIP:Use the
[CLIP](CLIP-Command.md) command to clip any type of referenced file: images, external references, viewports, and PDF underlays.

## List of Prompts

The following prompts are displayed.

On

Turns on clipping and displays the PDF underlay clipped to the previously defined boundary.

Off

Turns off clipping and displays the entire PDF underlay and frame.

If you re-clip the PDF underlay while clipping is turned off, clipping is automatically turned back on. You are prompted to
delete the old boundary even when clipping is turned off and the clipping boundary is not visible.

Delete

Removes a predefined clipping boundary and displays the full original underlay.

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

NOTE:You can only create a new clipping boundary for a selected PDF underlay when the old boundary is deleted.

#### Related Concepts

* [Clip Underlays](Clip-Underlays.md)

#### Related Information

* [About Clipping External References and Blocks](About-Clipping-External-References-and-Blocks.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*