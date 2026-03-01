# About Changing Mesh Smoothness Levels

Increase the roundness of mesh objects by increasing the smoothness levels.

Mesh objects are made up of multiple subdivisions, or tessellations, which define the editable faces. Each face consists
of underlying facets. When you increase smoothness, you increase the number of facets to provide a smoother, more rounded
look.

![](../images/GUID-5D64B5D5-3833-4FE5-BF2F-AE714195F98F-low.png)

## Increase or Decrease Smoothness

As you work, you can increase and decrease the level of smoothness. The differences are apparent both in the wireframe and
conceptual visual styles and in the rendered output.

![](../images/GUID-1C8B676D-E881-4754-9BAE-9B9EF5F3442D-low.png)

The lowest level of smoothness, or baseline, is 0. By default, Level 0 has no smoothness. You can increase the smoothness
of any mesh object up to the current limits. However, you cannot decrease the smoothness of a mesh object whose level of smoothness
is zero.

If you have added creases to a mesh object, the effect of smoothing differs, depending on the crease setting. The effect of
creases added to mesh that has no smoothness (Level 0) is not apparent until the mesh is smoothed.

As you edit an object using gizmos or grips, you might create gaps in the mesh object. One way to close the gap is to smooth
the object or refine individual subobjects.

NOTE:Using hardware acceleration might also help resolve this problem.

## Limit Mesh Density

A mesh is created at the level of smoothness that you specify. The smoothness can range from None (0), to the default maximum
(6), or to a level that you specify. As an object is smoothed, the density of the mesh facet grid also increases. For best
results, create mesh objects at lower smoothness levels and increase the smoothness only after modeling is complete.

Dense meshes can result in subobjects that are difficult to select and edit. They can also affect performance. Therefore you
might want to set limits that prevent the mesh from becoming too dense.

* *Maximum level of smoothness at which a grid is displayed* (SMOOTHMESHGRID). Displays the effects of modeling without the complexity of the underlying facet grid. The default smoothness
  level is 3. The tessellation display becomes increasingly dense until the maximum level is exceeded. Beyond that level, the
  display reverts to the most basic level, even though the smoothing level can continue to increase.
* *Maximum number of faces in a drawing* (SMOOTHMESHMAXFACE). Sets the maximum number of mesh faces that are permitted in mesh objects.
* *Maximum level of smoothness* (SMOOTHMESHMAXLEV). Sets the maximum smoothness level permitted for mesh objects.

#### Related Tasks

* [To Work With Changing Mesh Object Smoothness](To-Work-With-Changing-Mesh-Object-Smoothness.md)
* [To Work With Setting Mesh Density](To-Work-With-Setting-Mesh-Density.md)
* [To Work With Refining Mesh Faces and Objects](To-Work-With-Refining-Mesh-Faces-and-Objects.md)
* [To Work With Mesh Creases](To-Work-With-Mesh-Creases.md)

#### Related Concepts

* [About Refining Mesh Objects or Subobjects](About-Refining-Mesh-Objects-or-Subobjects.md)
* [About Adding Creases to Meshes](About-Adding-Creases-to-Meshes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*