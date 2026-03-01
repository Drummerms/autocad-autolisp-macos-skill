# 3D Polygon Mesh Selection (PEDIT)

If you select a polygon mesh, the following prompt is displayed:

## List of Prompts

The following prompts are displayed.

Enter an option [Edit vertex/Smooth surface/Desmooth/Mclose/Nclose/Undo]:
*Enter an option or press*Enter
*to end the command*

Mclose and Nclose are replaced by Mopen and Nopen if the polygon mesh is currently closed in the
*M* or
*N* direction.

Edit Vertex

Edits individual vertices of a polygon mesh that can be seen as a rectangular
*M* by
*N* array, where
*M* and
*N* are the dimensions specified in 3DMESH. The SURFTAB1 and SURFTAB2 system variables store
*M* and
*N* values for RULESURF, TABSURF, REVSURF, and EDGESURF.

Pressing Enter accepts the current default, which is either Next or Previous.

![](../images/GUID-BCB0EEB0-6BBC-4113-A824-611DB34D80E6-low.png)

Next
:   Moves the X marker to the next vertex. The marker does not wrap around from the end to the start of the mesh, even if the
    mesh is closed.

Previous
:   Moves the X marker to the previous vertex. The marker does not wrap around from the start to the end of the mesh, even if
    the mesh is closed.

Left
:   Moves the X marker to the previous vertex in the
    *N* direction. The marker does not wrap around from the start to the end of the mesh, even if the mesh is closed.

Right
:   Moves the X marker to the next vertex in the
    *N* direction. The marker does not wrap around from the end to the start of the mesh, even if the mesh is closed.

Up
:   Moves the X marker to the next vertex in the
    *M* direction. The marker does not wrap around from the end to the start of the mesh, even if the mesh is closed.

Down
:   Moves the X marker to the previous vertex in the
    *M* direction. The marker does not wrap around from the start to the end of the mesh, even if the mesh is closed.

Move
:   Repositions the vertex and moves the editing mark.

Regen
:   Regenerates the polygon mesh.

Exit
:   Exits Edit Vertex mode.

Smooth Surface

Fits a smooth surface. The SURFTYPE system variable controls the type of surface this option fits. The types of surfaces include
quadratic B-spline, cubic B-spline, and Bezier.

![](../images/GUID-F6AB3DEF-4E59-4212-9F55-3CF0FD81C0E5-low.png)

Desmooth

Restores the original control-point polygon mesh.

Mclose

Closes the
*M*-direction polylines if the polygon mesh is open in the
*M* direction.

![](../images/GUID-713A17F1-35F1-4EA8-AF4C-CB4F1D36D0A9-low.png)

Mopen

Opens the
*M*-direction polylines if the polygon mesh is closed in the
*M* direction.

Nclose

Closes the
*N*-direction polylines if the polygon mesh is open in the
*N* direction.

![](../images/GUID-245836A3-84F9-471E-A1C0-5D41708AD3DF-low.png)

Nopen

Opens the
*N*-direction polylines if the polygon mesh is closed in the
*N* direction.

Undo

Reverses operations as far back as the beginning of the PEDIT session.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*