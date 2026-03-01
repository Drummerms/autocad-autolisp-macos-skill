# About Modifying Mesh Faces

Split, extrude, merge, collapse, or spin mesh faces to modify their shapes.

### Split a Mesh Face

You can split a mesh face to make custom subdivisions. Use this method to prevent deforming a larger area for small modifications.

![](../images/GUID-3CEBB50C-F526-4AAB-AC46-DB5652D6904E-low.png)

Because you specify the start point and end point of the split, this method also gives you control over the shape of the two
new faces. Use the Vertex option to snap automatically to the vertices of the face. If you plan to split a face to create—and
then spin the edge of—two triangular faces (MESHSPIN), use the Vertex option to ensure precision.

## Extrude Mesh Faces

You can add definition to a 3D object by extruding a mesh face. Extruding other types of objects creates a separate 3D solid
object. However extruding a mesh face extends, or deforms, the existing object and subdivides the extruded face.

![](../images/GUID-546F7002-47EB-4C43-9B05-64EB9DC80D00-low.png)

You can use the same methods for extrusion of the faces of 3D solids and meshes as you use for other types of objects. For
example, you can specify an extrusion direction, a path, or a taper angle. However, when you extrude mesh faces, the MESHEXTRUDE
command provides an option that sets whether adjacent faces are extruded individually or whether their shared edges remained
joined.

![](../images/GUID-66BE0E19-6EA1-40C5-92BC-D6E14EA5FEC4-low.png)

You cannot create joined extrusions for mesh faces in which only the vertices are shared.

## Reconfigure Adjacent Mesh Faces

You can extend your editing options by reconfiguring adjacent faces. Several options are available:

* *Merge adjacent faces.* Combine adjacent faces to form a single face. Merging works best with faces that are on the same plane.

  ![](../images/GUID-AF54E709-C5D2-425E-8B9C-D59F7E447EB7-low.png)

  Although you can merge faces that wrap a corner, additional modifications to the resulting mesh object can have unexpected
  results.
* *Collapse the mesh vertices.* Merge adjacent vertices of surrounding faces form a single point. The selected face is removed.

  ![](../images/GUID-9B9F5C88-0712-432B-A8EB-23455FF40A45-low.png)
* *Spin edges of triangular faces.* Rotate an edge that is shared by two triangular faces. The shared edge spins to extend from the opposite vertices. This activity
  works best when the adjoined triangles form a rectangular, not a triangular, shape.

  ![](../images/GUID-919D9BDC-D157-4BA9-AD06-968D591F3651-low.png)

#### Related Tasks

* [To Work With Reshaping Mesh Faces](To-Work-With-Reshaping-Mesh-Faces.md)
* [To Delete a Face From a Mesh Object](To-Delete-a-Face-From-a-Mesh-Object.md)
* [To Repair a Hole in a Mesh Object](To-Repair-a-Hole-in-a-Mesh-Object.md)

#### Related Concepts

* [About Creating Meshes](About-Creating-Meshes.md)
* [About Creating Meshes by Conversion](About-Creating-Meshes-by-Conversion.md)
* [About Removing Faces and Closing Gaps in Mesh Objects](About-Removing-Faces-and-Closing-Gaps-in-Mesh-Objects.md)
* [About Changing Mesh Smoothness Levels](About-Changing-Mesh-Smoothness-Levels.md)

#### Related Information

* [To Modify a Mesh Subobject in the Properties Inspector](To-Modify-a-Mesh-Subobject-in-the-Properties-Inspector.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*