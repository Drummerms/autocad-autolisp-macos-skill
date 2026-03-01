# EDGESURF (Command)

Creates a mesh between four contiguous edges or curves.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Mesh panel ![](../images/ac.menuaro.gif) Edge Surface.
![](../images/GUID-E7AD75AE-7E1B-4D78-9754-83655FB966D4-low.png)

*Menu*:
Draw
![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Meshes ![](../images/ac.menuaro.gif) Edge Mesh.

## Summary

Select four adjoining edges that define the mesh. The edges can be lines, arcs, splines, or open polylines. The edges must
touch at their endpoints to form a single, closed loop.

![](../images/GUID-88ABBF06-A520-41B1-9CB8-86BDA68080AB-low.gif)

You can select the four edges in any order. The first edge ([SURFTAB1](SURFTAB1-System-Variable.md)) determines the
*M* direction of the generated mesh, which extends from the endpoint closest to the selection point to the other end. The two
edges that touch the first edge form the
*N* edges ([SURFTAB2](SURFTAB2-System-Variable.md)) of the mesh.

![](../images/GUID-8CA0D1A1-7221-4BA9-A136-0D13C40437F4-low.png)

The
[MESHTYPE](MESHTYPE-System-Variable.md) system variable sets which type of mesh is created. Mesh objects are created by default. Set the variable to 0 to create
legacy polyface or polygon mesh.

## List of Prompts

The following prompts are displayed.

Object 1 for surface edge
:   Specifies the first edge to be used as a boundary.

Object 2 for surface edge
:   Specifies the second edge to be used as a boundary.

Object 3 for surface edge
:   Specifies the third edge to be used as a boundary.

Object 4 for surface edge
:   Specifies the final edge to be used as a boundary.

#### Related Concepts

* [About Constructing Meshes From Other Objects](About-Constructing-Meshes-From-Other-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*