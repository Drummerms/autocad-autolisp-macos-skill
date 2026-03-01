# To Modify Polylines With PEDIT

1. Click
   Modify
   ![](../images/ac.menuaro.gif) Object ![](../images/ac.menuaro.gif) Polyline.
2. Select the polyline to modify.

   NOTE:To select a single arc or line segment, press Ctrl while clicking the segment.
3. If the selected object is a spline, line, or an arc, the following prompt is displayed:

   Object selected is not a polyline.

   Do you want it to turn into one? <Y>:
   *Enter**y* *or**n**, or press Enter*

   If you enter
   *y*, the object is converted into a single-segment 2D polyline that you can edit.

   Before the selected spline is converted to a polyline, the following prompt is displayed:

   Specify a precision <10>:
   *Enter a new precision value or press* Enter.

   The PLINECONVERTMODE system variable determines whether the polylines are created with linear or arc segments. When the PEDITACCEPT
   system variable is set to 1, this prompt is suppressed, and the selected object is automatically converted to a polyline.
4. Edit the polyline by entering one or more of the following options:
   * Enter
     *c* (Close) to create a closed polyline.
   * Enter
     *j* (Join) to join contiguous lines, splines, arcs, or polylines.
   * Enter
     *w* (Width) to specify a new uniform width for the entire polyline.
   * Enter
     *e* (Edit Vertex) to edit a vertex.
   * Enter
     *f* (Fit) to create an arc-fit polyline, a smooth curve consisting of arcs joining each pair of vertices
   * Enter
     *s* (Spline) to create an approximation of a spline.
   * Enter
     *d* (Decurve) to remove extra vertices inserted by a fit or spline curve and to straighten all segments of the polyline.
   * Enter
     *L* (Ltype Gen) to generate the linetype in a continuous pattern through the vertices of the polyline.
   * Enter
     *r* (Reverse) to reverse the order of vertices of the polyline.
   * Enter
     *u* (Undo) to reverse actions back to the start of PEDIT.
5. Enter
   *x* (Exit) to end a command option. Press Enter to exit the PEDIT command.

#### Related Tasks

* [To Modify Polylines With Grips](To-Modify-Polylines-With-Grips.md)

#### Related References

* [Commands for Editing Specific Objects](Commands-for-Editing-Specific-Objects.md)

#### Related Concepts

* [About Polylines](About-Polylines.md)
* [About Exploding Compound Objects](About-Exploding-Compound-Objects.md)

#### Related Information

* [To Delete a Vertex in a Polyline](To-Delete-a-Vertex-in-a-Polyline.md)
* [To Taper the Width of Individual Polyline Segments](To-Taper-the-Width-of-Individual-Polyline-Segments.md)
* [To Reverse Lines, Polylines, Splines, or Helixes](To-Reverse-Lines,-Polylines,-Splines,-or-Helixes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*