# 3DMESH (Command)

Creates a free-form polygon mesh.

## Summary

The mesh density controls the number of facets, and is defined in terms of a matrix of
*M* and
*N* vertices, similar to a grid consisting of columns and rows. 3DMESH is a legacy method for creating mesh, designed primarily
for operation under program control rather than by manual entry.

To take advantage of smoothing, creasing, and refinement capabilities, use the MESH command.

## List of Prompts

The following prompts are displayed.

Size of mesh in M direction
:   Sets the
    *M* direction value. Enter a value between 2 and 256.

Size of mesh in N direction
:   Sets the
    *N* direction value. Enter a value between 2 and 256.

    *M* times
    *N* equals the number of vertices that you must specify.

    ![](../images/GUID-C49B3109-0B9D-47BA-AF75-DF75912D8570-low.png)

Location for vertex (0, 0)
:   Sets the coordinate location of the vertex. Enter a 2D or 3D coordinate.

    The location of each vertex in the mesh is defined by
    *m* and
    *n*, the row and column indices of the vertex. Defining vertices begins with vertex (0,0). You must supply the coordinate locations
    for each vertex in row
    *m* before specifying vertices in row
    *m* + 1.

    Vertices may be any distance from each other. The
    *M* and
    *N* orientation of a mesh depends on the position of its vertices.

    ![](../images/GUID-B0C8725C-3A14-4F92-ADF6-1DBF26D90DF4-low.png)

    3DMESH polygon meshes are always open in both
    *M* and
    *N* directions. You can close a mesh with the PEDIT command.

    ![](../images/GUID-6FBDC714-D282-4EA5-92FF-C515BCDD80F8-low.png)

#### Related References

* [MESH (Command)](MESH-Command.md)
* [PEDIT (Command)](PEDIT-Command.md)

#### Related Concepts

* [About Creating a Custom Mesh (Legacy)](About-Creating-a-Custom-Mesh-Legacy.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*