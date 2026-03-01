# CLIP (Command)

Crops a selected external reference, image, viewport, or PDF underlay to a specified boundary.

## Summary

The clipping boundary determines a portion of an image, PDF underlay, viewport, or external reference to hide. The visibility
of the clipping boundary is controlled by the FRAME system variable.

## List of Prompts

The list of prompts varies depending on whether you are clipping a PDF underlay, image, external reference, or viewport.

PDF Underlay and Image Prompts

The following prompts are displayed.

On
:   Turns on clipping and displays the PDF underlay or image clipped to the previously defined boundary.

Off
:   Turns off clipping and displays the entire PDF underlay or image, and frame.

    If you clip the PDF underlay or image again while clipping is off, clipping automatically turns on. You are prompted to delete
    the old boundary even when clipping is off and the clipping boundary is not visible.

Delete
:   Removes a predefined clipping boundary and redisplays the full original PDF underlay or image.

New Boundary
:   Defines a rectangular or polygonal clipping boundary, or generates a polygonal clipping boundary from a polyline.

    NOTE:You can only create a new clipping boundary for a PDF underlay or image when the old boundary is deleted.

Select Polyline
:   Defines the boundary with the selected polyline. The polyline can be open but must consist of straight line segments and cannot
    intersect itself.

Polygonal
:   Defines a polygonal clipping boundary with three or more points that you specify for the vertices of a polygon.

Rectangular
:   Defines a rectangular boundary with the points that you specify for opposite corners.

Invert Clip
:   Inverts the mode of the clipping boundary: objects are clipped either outside the boundary or inside the boundary.

External Reference Prompts

The following prompts are displayed.

On
:   Displays the clipped portion of the external reference or block in the current drawing.

Off
:   Displays all of the geometry of the external reference or block in the current drawing, ignoring the clipping boundary.

Clipdepth
:   Sets the front and back clipping planes on an xref or block. Objects outside the volume defined by the boundary and the specified
    depth are not displayed. Regardless of the current UCS, the clip depth is applied parallel to the clipping boundary.

    * *Front Clip Point.* Creates a clipping plane passing through and perpendicular to the clipping boundary.
    * *Distance.* Creates a clipping plane the specified distance from and parallel to the clipping boundary.
    * *Remove.* Removes both the front and back clipping planes.

Delete
:   Removes a clipping boundary for the selected xref or block. To temporarily turn off a clipping boundary, use the Off option.
    Delete erases the clipping boundary and the clipdepth. The ERASE command cannot be used to delete clipping boundaries.

Generate Polyline
:   Automatically draws a polyline coincident with the clipping boundary. The polyline assumes the current layer, linetype, lineweight,
    and color settings. Use this option when you want to modify the current clipping boundary using PEDIT and then redefine the
    clipping boundary with the new polyline. To see the entire xref while redefining the boundary, use the Off option.

New Boundary
:   Defines a rectangular or polygonal clipping boundary, or generates a polygonal clipping boundary from a polyline.

    NOTE:You can only create a new clipping boundary for a selected external reference when the old boundary is deleted.

    * *Select Polyline.* Defines the boundary with the selected polyline. The polyline can be open but must consist of straight line segments and
      cannot intersect itself.
    * *Polygonal.* Defines a polygonal clipping boundary with three or more points that you specify for the vertices of a polygon.
    * *Rectangular.* Defines a rectangular boundary with the points that you specify for opposite corners.
    * *Invert Clip.* Inverts the mode of the clipping boundary: objects are clipped either outside the boundary or inside the boundary.

Viewport Prompts

NOTE:You cannot clip a viewport in model space. You must be in paper space on a named layout.

Clipping Object
:   Select the viewport to clip.

Polygonal
:   Draws a clipping boundary. You can draw line segments or arc segments by specifying points.

    The descriptions of the Next Point, Arc, Close, Length, and Undo options match the descriptions of the corresponding options
    in the PLINE command.

Delete
:   Deletes the clipping boundary of a selected viewport. This option is available only if the selected viewport has already been
    clipped. If you clip a viewport that has been previously clipped, the original clipping boundary is deleted, and the new clipping
    boundary is applied.

#### Related Concepts

* [About Clipping External References and Blocks](About-Clipping-External-References-and-Blocks.md)
* [About Clipping Raster Images](About-Clipping-Raster-Images.md)

#### Related Information

* [Clip Underlays](Clip-Underlays.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*