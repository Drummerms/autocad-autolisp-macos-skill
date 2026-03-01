# About Pressing or Pulling Areas, Objects, and Faces

Get visual feedback as you extrude closed objects and areas, and offset or extrude 3D solid faces.

The program responds differently, depending on the type of object or subobject you select to press or pull. Closed objects
or bounded areas create 3D solid objects. Open objects create surfaces.

## Press and Pull to Create Holes and Solid Extrusions

Press in or pull out bounded, or closed, areas or objects to create holes and 3D solid extrusions. You can click inside a
closed object, an area, or a face that is imprinted on a solid object and then drag it in or out. The following example shows
how you can press or pull a circle imprinted on the face of a solid box to create a hole or extrusion from the box.

![](../images/GUID-EC72AE31-1A56-4D72-B5E2-8FDB0D284D29-low.png)

In combination with imprinted faces, you can form complex shapes using press or pull operations to create extrusions and notches.
The following object was formed using press and pull operations on an imprinted pyramid

![](../images/GUID-FD41034F-46B4-40D4-A610-61E606C9D610-low.png)

## Press or Pull to Create Surfaces

Selecting an open object, such as a line, spline, or arc creates a surface.

![](../images/GUID-2464DDAD-6CEA-4924-B185-7345D3F9DE41-low.png)

## Press or Pull to Offset a 3D Solid Face

If you select a planar face of a 3D solid object, the press or pull operation modifies the size of the solid object based
on the offset distance you specify. You can select more than one face on the object. By pressing Ctrl as you drag the face,
you can preserve the angle of the adjacent faces. For best results, do not select adjacent faces that are filleted.

![](../images/GUID-CD9023E4-85DD-4346-9FF4-31E632FB9432-low.png)

## Methods for Press and Pull Modifications

To filter selection to include only 2D objects, faces or edges, press Ctrl as you move the cursor. Bounded areas and imprints
on solid objects are not detected.

You can also press Ctrl+Shift+E to initiate a press or pull operation. To limit the type of objects that can act as boundaries,
turn off the IMPLIEDFACE system variable. When the variable is off, only 3D faces and 3D solid faces can be extruded using
Ctrl+Shift+E. (This setting does not affect the PRESSPULL command.)

NOTE:If you alternatively use EXTRUDE to extend an existing face on a 3D solid, a separate extruded object is created.

#### Related Tasks

* [To Work With Pressing or Pulling Bounded Areas](To-Work-With-Pressing-or-Pulling-Bounded-Areas.md)
* [To Work with Pressing or Pulling 3D Solid Faces](To-Work-with-Pressing-or-Pulling-3D-Solid-Faces.md)
* [To Create a Surface by Pressing or Pulling an Open Curve](To-Create-a-Surface-by-Pressing-or-Pulling-an-Open-Curve.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*