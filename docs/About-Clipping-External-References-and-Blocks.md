# About Clipping External References and Blocks

You can specify clipping boundaries to display a limited portion of an external reference drawing or block reference.

You can clip external references such as raster images, PDF underlays, or block references. With a clipping boundary, you
can determine the portions of an external reference or block reference that you want to display by hiding the redundant parts
of the reference inside or outside the boundary.

![](../images/GUID-835A5C3A-66F0-4C6B-9E70-7DF6BF6FAE72-low.png)

The clipping boundary can be a polyline, rectangle, or a polygon with vertices within the boundaries of the image. You can
change the boundary of a clipped image. When you clip a boundary, the objects in the external reference or block are not altered;
only their display is changed.

With the XCLIP, PDFCLIP, and IMAGECLIP commands, you can control the following viewing options:

| Control the visibility of the clipped area of the external reference or block reference. | When clipping is turned off, the boundary is not displayed and the entire external reference or block is visible, provided that the objects are on layers that are turned on and thawed.  Clipping results can be turned on or off using the clipping commands, controlling whether clipped areas are hidden or displayed. |
| Control the visibility of clipping boundaries. | You can control the display of the clipping boundary with a clipping frame. The clipping system variable for XREF, images, PDF underlays are XCLIPFRAME, PDFFRAME, and IMAGEFRAME respectively. |
| Invert the area to be hidden, inside or outside the clipping boundary. | When you want the hidden parts of the clipped reference displayed or vice versa, use the grips to alter the display of the external reference or blocks. With grips located at the midpoint on the first edge of the clipping boundary, you can invert the display of the clipped reference inside or outside the boundary. |

![](../images/GUID-0FC876EE-97F9-46F1-B548-679514AC7515-low.png)

The grips are visible and can be used when the clipping system variable is turned on, the reference is selected, and clipped.

## Editing Options

After an external reference or block reference has been clipped, it can be moved, copied, or rotated just like an unclipped
external reference or block reference. The clipping boundary moves with the reference. If an xref contains nested clipped
xrefs, they appear clipped in the drawing. If the parent xref is clipped, the nested xrefs are also clipped.

## Resize Clipping Boundaries

If you want to change the shape or size of a clipping boundary for external references and block references, you can use grips
to edit the vertices just as you edit any object with grips.

In case of rectangular grip editing, you can maintain the closed four-sided rectangle or square shape of the rectangular clipping
boundary because two vertices of the same side of the rectangular clipping boundary are edited together.

NOTE: With Clipping boundaries, you cannot display self-intersecting polygonal boundaries. An error message is displayed and the
boundary reverts to the last boundary.

## Limitations for Clipping Boundaries

When clipping an referenced drawing or block the following limitations apply:

* A clipping boundary can be specified anywhere in 3D space, but it is always applied planar to the current UCS.
* If a polyline is selected, the clipping boundary is applied in the plane of that polyline.
* Images in external references or blocks are always clipped within the rectangular extents of the reference. When you apply
  polygonal clipping to images in externally referenced drawings, the clipping boundary is applied to the rectangular extents
  of the polygonal boundary, rather than to the polygon itself.

#### Related Concepts

* [About Nesting and Overlaying Referenced Drawings](About-Nesting-and-Overlaying-Referenced-Drawings.md)

#### Related Information

* [About Attaching and Detaching Referenced Drawings (Xrefs)](About-Attaching-and-Detaching-Referenced-Drawings-Xrefs.md)
* [To Clip an Xref](To-Clip-an-Xref.md)
* [To Invert a Clipped Reference](To-Invert-a-Clipped-Reference.md)
* [To Resolve External References (Xrefs) while Sharing Drawings Between Mac and Windows](To-Resolve-External-References-Xrefswhile-Sharing-Drawings-Between-Mac-and-Windows.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*