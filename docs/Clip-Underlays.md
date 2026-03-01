# Clip Underlays

You can use a clipping boundary to clip a PDF underlay.

You can define part of an underlay that you want to display and plot by setting up a clipping boundary with PDFCLIP IMAGECLIP,
VPCLIP, and XCLIP. The clipping boundary can be a closed polyline, rectangle or a polygon with vertices within the overall
extents of the underlay. Each instance of an underlay can only have one clipped boundary. Multiple instances of the same underlay
can have different boundaries.

Following is an example of an underlay with insets showing polygonal (l) and rectangular (r) clipping boundaries:

![](../images/GUID-2C81D2FD-E983-47C9-808F-9F5AA0791FE1-low.png)

When the clipping boundary is no longer needed, you can delete the clipped boundary from the underlay and the underlay is
displayed with its original boundary. You can also invert the area to be hidden inside or outside the clipping boundary. With
grips located at the midpoint on the first edge of the clipping boundary, you can invert the display of the clipped reference
inside or outside the boundary.

![](../images/GUID-0FC876EE-97F9-46F1-B548-679514AC7515-low.png)

You can control the way clipping boundaries and grips display with the clipping frame system variables. The clipping frame
system variable are FRAME, PDFFRAME, XCLIPFRAME, and IMAGEFRAME.

#### Related Concepts

* [About Underlays](About-Underlays.md)

#### Related Information

* [Use Object Snaps With PDF Underlays](Use-Object-Snaps-With-PDF-Underlays.md)
* [About Controlling the Display of Layers in an Underlay](About-Controlling-the-Display-of-Layers-in-an-Underlay.md)
* [To Clip a PDF Underlay](To-Clip-a-PDF-Underlay.md)
* [To Turn Layers on and off in an Underlay](To-Turn-Layers-on-and-off-in-an-Underlay.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*