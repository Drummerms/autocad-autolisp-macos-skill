# Polyface Meshes (DXF)

A polyface mesh is represented in DXF as a variant of a polyline entity. The polyline header is identified as introducing
a polyface mesh by the presence of the 64 bit in the polyline flags (70) group. The 71 group specifies the number of vertices
in the mesh, and the 72 group specifies the number of faces. Although these counts are correct for all meshes created with
the PFACE command, applications are not required to place correct values in these fields. Following the polyline header is
a sequence of vertex entities that specify the vertex coordinates, followed by faces that compose the mesh.

The entity structure imposes a limit on the number of vertices that a given face entity can specify. You can represent more
complex polygons by decomposing them into triangular wedges. Their edges should be made invisible to prevent visible artifacts
of this subdivision from being drawn. The PFACE command performs this subdivision automatically, but when applications generate
polyface meshes directly, the applications must do this themselves. The number of vertices per face is the key parameter in
this subdivision process. The PFACEVMAX system variable provides an application with the number of vertices per face entity.
This value is read-only and is set to 4.

Polyface meshes created with the PFACE command are always generated with all the vertex coordinate entities first, followed
by the face definition entities. The code that processes polyface meshes requires this ordering. Programs that generate polyface
meshes in DXF should generate all the vertices, and then all the faces. However, programs that read polyface meshes from DXF
should be tolerant of odd vertex and face ordering.

#### Related References

* [POLYLINE (DXF)](POLYLINE-DXF.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*