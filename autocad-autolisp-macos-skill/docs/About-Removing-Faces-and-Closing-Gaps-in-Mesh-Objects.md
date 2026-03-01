# About Removing Faces and Closing Gaps in Mesh Objects

## Remove Mesh Faces

You can press Delete or use the ERASE command to remove mesh faces. The removal leaves a gap in the mesh.

* Deleting a face removes only the face.

  ![](../images/GUID-3F78E3C9-62B0-4BD7-A404-B094005AFF67-low.png)
* Deleting an edge removes each adjacent face.

  ![](../images/GUID-E76FC676-C227-4FE5-9907-3C08C3EC8DCF-low.png)
* Deleting a vertex removes all faces that are shared by the vertex.

  ![](../images/GUID-6F732602-AB1A-4358-A31A-9DC54FA8EAB5-low.png)

If removal of a mesh face creates a gap, the mesh object is not “watertight.” It can be converted to a surface object, but
not to a 3D solid object.

## Close Gaps in Mesh Objects

If a mesh object is not watertight due to gaps, or holes, in the mesh, you can make it watertight by closing the holes. The
cap, or new face, spans the boundary formed by the mesh edges that you specify (MESHCAP).

![](../images/GUID-7E42A962-6B11-4C9D-ADC8-61E4A7BE1EF6-low.png)

This process works best when all edges are on the same plane. The edges you select as boundaries cannot be shared by two faces.
For example, you cannot close the center hole in a mesh torus.

NOTE:You can sometimes close gaps in a mesh by smoothing it, by using MESHCOLLAPSE, or by splitting adjacent faces (MESHSPLIT).

#### Related Tasks

* [To Work With Reshaping Mesh Faces](To-Work-With-Reshaping-Mesh-Faces.md)
* [To Delete a Face From a Mesh Object](To-Delete-a-Face-From-a-Mesh-Object.md)
* [To Repair a Hole in a Mesh Object](To-Repair-a-Hole-in-a-Mesh-Object.md)

#### Related Concepts

* [About Modifying Mesh Faces](About-Modifying-Mesh-Faces.md)

#### Related Information

* [To Modify a Mesh Subobject in the Properties Inspector](To-Modify-a-Mesh-Subobject-in-the-Properties-Inspector.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*