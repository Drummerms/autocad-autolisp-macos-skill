# About Imprinting Facets on Faces

Subdivide faces into additional facets on 3D solids and surfaces by imprinting other objects, such as arcs and circles on
them.

With the IMPRINT command, you can add a new facet to a 3D solid by imprinting a coplanar object that overlaps a face. Imprinting
provides additional edges that you can use to reshape the 3D object.

For example, if a circle overlaps the face of a box, you can imprint it on the solid.

![](../images/GUID-4E8EED6B-6960-4955-9C87-99AE60BFD5EE-low.png)

You can delete or retain the original object when you imprint it.

Objects that can be imprinted on 3D solids include arcs, circles, lines, 2D and 3D polylines, ellipses, splines, regions,
bodies, and other 3D solids.

## Edit Imprinted Objects

You can edit imprinted objects and subobjects in many of the same ways that you can edit other faces. For example, you can
Ctrl+click to select a new edge and drag it to a new location, or you can use PRESSPULL on the facet.

The following limitations exist for imprinted objects:

* You can move the edges of the imprinted face only within the plane of a face.
* You might be unable to move, rotate, or scale some subobjects.
* Imprinted edges and faces might be lost when some subobjects are moved, rotated, or scaled.

Subobjects with editing limitations include

* Faces with imprinted edges or faces
* Edges or vertices with adjacent faces that contain imprinted edges or faces

#### Related Tasks

* [To Imprint a 3D Solid](To-Imprint-a-3D-Solid.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*