# 3D Polyline Selection (PEDIT)

If you select a 3D polyline, the following prompt is displayed:

## List of Prompts

The following prompts are displayed.

Enter an option [Close/Join/Edit vertex/Spline curve/Decurve/Reverse/Undo]:
*Enter an option or press*Enter

If the polyline you select is closed, Open replaces the Close option in the prompt.

Close

Creates the closing segment of the polyline, connecting the last segment with the first. The polyline is considered open unless
you close it with Close.

Open

Removes the closing segment of the polyline. The polyline is considered closed unless you open it with Open.

Join

Joins an open curve to the 3D polyline. The curve can be on a different plane, but must be contiguous with the 3D polyline.

Edit Vertex

Performs various editing tasks on one vertex of the polyline and segments that follow it.

Next

Moves the X marker to the next vertex. The marker does not wrap around from the end to the start of the polyline, even if
the polyline is closed.

Previous

Moves the X marker to the previous vertex. The marker does not wrap around from the start to the end of the polyline, even
if the polyline is closed.

Break

Saves the location of the marked vertex while you move the X marker to any other vertex.

* Next
* Previous

Go
:   Deletes any segments and vertices between the two vertices you specify and returns to Edit Vertex mode.

Exit
:   Exits Break and returns to Edit Vertex mode.

If one of the specified vertices is at an end of the polyline, the polyline is truncated. If both specified vertices are at
endpoints of the polyline, or if just one vertex is specified and it is at an endpoint, you cannot use Break mode.

Insert

Adds a new vertex to the polyline after the marked vertex.

Move

Moves the marked vertex.

Regen

Regenerates the polyline.

Straighten

Saves the location of the marked vertex while you move the X marker to any other vertex.

Next
:   Moves the X marker to the next vertex.

Previous
:   Moves the X marker to the previous vertex.

Go
:   Deletes any segments and vertices between the two vertices you select, replaces them with single straight line segments, and
    returns to Edit Vertex mode. If you specify only one vertex by entering
    *go* without moving the X marker, the segment following that vertex is made straight if it is an arc.

Exit
:   Exits Straighten and returns to Edit Vertex mode.

To remove an arc segment that connects two straight segments of a polyline and then to extend the straight segments until
they intersect, use the
[FILLET](FILLET-Command.md) command with a fillet radius of 0.

Exit

Exits Edit Vertex mode.

Spline Curve

Fits a 3D B-spline curve to its control points. The
 [SPLFRAME](SPLFRAME-System-Variable.md) system variable controls the accuracy and display of the control points for the 3D B-spline, whose curves can be approximated
only by line segments. Negative values for spline segments are ignored.

![](../images/GUID-90CBB7A9-4B0C-49FA-B6BD-ED201683961A-low.png)

Decurve

Removes extra vertices inserted by a fit or spline curve and straightens all segments of the polyline. Retains tangent information
assigned to the polyline vertices for use in subsequent fit curve requests. If you edit a spline-fit polyline with a command
such as
[BREAK](BREAK-Command.md) or
[TRIM](TRIM-Command.md), you cannot use the Decurve option.

Reverse

Reverses the order of vertices of the polyline. Use this option to reverse the direction of objects that use linetypes with
included text. For example, depending on the direction in which a polyline was created, the text in the linetype might be
displayed upside down.

Undo

Reverses operations as far back as the beginning of the PEDIT session.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*