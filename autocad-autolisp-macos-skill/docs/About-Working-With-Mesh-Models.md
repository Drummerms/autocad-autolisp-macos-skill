# About Working With Mesh Models

Learn some best practices for mesh modeling.

Mesh modeling, with its enhanced modeling capabilities, offers a way to create more fluid, free-form designs. Keep these
tips in mind as you work.

Model a mesh before you smooth it.

Mesh modeling is a powerful way to design, but higher levels of smoothness increase complexity and can affect performance.
You can work more efficiently if you complete editing operations such as gizmo editing, extrusion, and face splitting, on
mesh objects that have not been smoothed. (That is, their level of smoothness is 0.)

![](../images/GUID-C1437147-68A6-4B38-8A46-DF755F61A700-low.png)

mesh sphere modeled by grip editing and extrusion, then smoothed

You can quickly switch between the levels of smoothness in the Properties window to get a preview of how your activities affect
the smoothed mesh.

Refine or split a face instead of refining the entire mesh.

Refinement is a powerful way to subdivide faces. However, by increasing the number of faces, you add to the overall complexity
of the model. In addition, refining an entire mesh object resets the base level of smoothness to 0. This change can result
in a dense grid that can no longer be simplified. For best results, avoid refining the object, and refine or split only the
individual faces that require more detailed modeling.

![](../images/GUID-B3285E50-3248-4297-A75F-1AB7B699E0D5-low.png)

mesh box, refined mesh box, and mesh box with one face refined

Refining individual faces does not reset the level of smoothness for the object.

Crease edges to help limit distortion when the mesh is smoothed.

Creased edges can be set to maintain their sharpness, no matter how much the mesh is smoothed. You may also need to crease
the edges in surrounding faces to obtain the result you want.

![](../images/GUID-2B3865FA-005F-4B50-97F8-A1AE9A26DB37-low.png)

extruded faces on mesh torus, creased and not creased

Creasing set to Always retains its sharpness after smoothing. If you set a crease value, the creased edge becomes smoother
at the equivalent level of smoothness.

Use gizmos to model faces, edges, and vertices.

The 3D Move, 3D Rotate, and 3D Scale gizmos can be used to modify entire mesh objects, or specific subobjects such as one
or more selected faces.

![](../images/GUID-A67A1239-F373-43DF-A434-0763DC2930AE-low.png)

By constraining the modifications to a specified axis or plane, gizmos help you avoid unexpected results. The default gizmo
is displayed whenever you select an object in a view that uses a 3D visual style. (You can also suppress this display.) Therefore,
you do not have to explicitly start the 3D Move, 3D Rotate, or 3D Scale command to initiate these activities. You just need
to select an object.

When a gizmo is selected, you can use the shortcut menu to switch to a different gizmo.

Use subobject selection filters to narrow the available selection candidates.

In a smoothed mesh, trying to select a subobject can be difficult unless you turn on subobject selection (shortcut menu).
By specifying that the selection set is limited to faces, edges, vertices, or even solid history subobjects, you can restrict
which subobject type is available for selection.

![](../images/GUID-2B0A736B-D749-4A0B-B597-AA8A52F98241-low.png)

mesh faces selected when the face subobject selection filter is on

A filter is valuable for selecting mesh vertices, which are not highlighted as you move over them.

To select the entire mesh object, turn off the subselection filters.

Model by extruding faces.

A key difference between gizmo editing and extrusion occurs in the way each face is modified. With gizmo editing, if you
select and drag a set of faces, adjacent faces are stretched to accommodate the modification. When the object is smoothed,
the adjacent faces adapt to the new location of the face.

![](../images/GUID-D9EF8585-F75A-451B-AAFB-452FF429D0CC-low.png)

mesh faces extended using 3D Move gizmo

Mesh extrusion, however, inserts additional faces to close the gap between the extruded face and its original surface. With
mesh extrusion, you can set whether adjacent faces are extruded as a unit (joined) or separately (unjoined).

![](../images/GUID-BBCD3203-6AB2-41FC-B3AC-E917E5D4E315-low.png)

mesh faces extruded, then smoothed

If you are working on an object that has not been smoothed, try smoothing it periodically to see how the extrusion is affected.

Convert between mesh and 3D solids or surfaces.

Mesh modeling is powerful, but it cannot do everything that solid modeling can do. If you need to edit mesh objects through
intersection, subtraction, or union, you can convert a mesh to a 3D solid or surface. Similarly, if you need to apply creasing
or smoothing to a 3D solid or surface, you can convert it to a mesh.

Keep in mind that not all conversions retain complete fidelity to the shape of the original object. Avoid switching between
object types more than once, if possible. If you notice that the conversion modifies the shape of the object in an unacceptable
way, undo the conversion and try again with different settings.

The SMOOTHMESHCONVERT system variable sets whether the mesh objects that you convert to 3D solids or surfaces are smoothed
or faceted, and whether their co-planar faces are optimized (merged).

You might have trouble converting some non-primitive mesh to solid objects due to the following problems:

* *Gaps in the mesh.* If you notice gaps, you can sometimes close them by smoothing the mesh or by refining the faces that are adjacent to the
  gap.

  ![](../images/GUID-A1A3AC4E-89E6-411A-A7F3-58672BAA20D2-low.png)

  mesh torus that has been twisted using 3D Rotate at various smoothing levels

  You can also close holes by using MESHCAP.

  In some cases, you can also obtain better results by using hardware acceleration to improve your graphics system.
* *Intersecting mesh faces.* Be especially careful not to create *self-intersections* as you move, rotate, or scale subobjects. (You create self-intersections when you cause one or more faces to cross or intersect
  other faces in the same mesh model.) View the mesh from several viewpoints to ensure you create a viable model.

  ![](../images/GUID-BB717E46-8C74-4402-BE0E-593F134B206D-low.png)

  mesh wedge with front faces dragged past the back faces

Mesh objects that cannot be converted to solids can often be converted to surfaces instead.

Avoid merging faces that wrap a corner

When you merge faces, you can create a mesh configuration in which the merged face wraps a corner. If a resulting face has
a vertex that has two edges and two faces, you cannot convert the mesh to a smooth 3D solid object.

![](../images/GUID-84E46191-1065-4CEF-A523-303B9BF5A9D8-low.png)

One way to resolve this problem is to convert the mesh to a faceted solid instead of a smooth solid. You might also be able
to repair the problem by splitting the adjacent faces, starting at the shared vertex (MESHSPLIT).

#### Related Concepts

* [About Modifying Meshes](About-Modifying-Meshes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*