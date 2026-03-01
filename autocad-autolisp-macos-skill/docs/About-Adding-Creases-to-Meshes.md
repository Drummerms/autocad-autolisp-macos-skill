# About Adding Creases to Meshes

Add creases to sharpen mesh edges.

You can add creases to mesh objects that have a smoothing level of 1 or higher.

![](../images/GUID-2650E3DE-6F8D-40A2-BFBA-0954D65BB5A6-low.png)

## Add Creases to Different Subobjects

The result of creasing differs, depending on what type of subobject you select.

* *Edge*. The selected edge is sharpened. The adjacent faces are deformed to accommodate the new crease angle.
* *Face*. The selected face is flattened and all edges that bound that face are sharpened. Adjacent faces are deformed to accommodate
  the new shape of the face.
* *Vertex*. The point of the vertex and all intersecting edges are sharpened. Adjacent faces are deformed to accommodate the new vertex
  angle.

## Assign a Crease Value to the Edge

As you apply a crease, you set a crease value that determines how the crease is affected by smoothing. A value of Always ensures
that the crease is always retained, even when the mesh is repeatedly smoothed. Higher crease values ensure that the crease
is retained through several smoothing processes. (During smoothing, the assigned crease value is decreased by the value of
the original level of smoothing.)

You can add a crease to a mesh that has not been smoothed. However, the effect is not visible unless you smooth the object.

## Remove a Crease

You can restore a crease to a smoothed state that corresponds to the smoothing level for the object. If you remove a crease
that is adjacent to other creased subobjects, their contours are adjusted.

#### Related Tasks

* [To Work With Changing Mesh Object Smoothness](To-Work-With-Changing-Mesh-Object-Smoothness.md)
* [To Work With Setting Mesh Density](To-Work-With-Setting-Mesh-Density.md)
* [To Work With Refining Mesh Faces and Objects](To-Work-With-Refining-Mesh-Faces-and-Objects.md)
* [To Work With Mesh Creases](To-Work-With-Mesh-Creases.md)

#### Related Concepts

* [About Changing Mesh Smoothness Levels](About-Changing-Mesh-Smoothness-Levels.md)
* [About Refining Mesh Objects or Subobjects](About-Refining-Mesh-Objects-or-Subobjects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*