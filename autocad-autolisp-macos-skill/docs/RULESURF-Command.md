# RULESURF (Command)

Creates a mesh that represents the surface between two lines or curves.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Mesh panel ![](../images/ac.menuaro.gif) Modeling, Meshes, Ruled Surface.
![](../images/GUID-362C6D83-E86B-42FF-A45B-4E91BE875016-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Meshes ![](../images/ac.menuaro.gif) Ruled Mesh.

## Summary

Select two edges that define the mesh. The edges can be lines, arcs, splines, circles, or polylines. If one of the edges is
closed, then the other edge must also be closed. You can also use a point as one edge for either an open or a closed curve.

![](../images/GUID-B5490077-85E4-408F-B9E9-D03752FA9AE5-low.gif)

The
[MESHTYPE](MESHTYPE-System-Variable.md) system variable sets which type of mesh is created. Mesh objects are created by default. Set the variable to 0 to create
legacy polyface or polygon mesh.

For closed curves, the selection does not matter. If the curve is a circle, the ruled mesh begins at the 0-degree quadrant
point, as determined by the current
*X* axis plus the current value of the
[SNAPANG](SNAPANG-System-Variable.md) system variable. For closed polylines, the ruled mesh starts at the last vertex and proceeds backward along the segments
of the polyline. Creating a ruled mesh between a circle and a closed polyline can be confusing. Substituting a closed semicircular
polyline for the circle might be preferable.

![](../images/GUID-1CB73C0E-AC96-41AB-B648-14D4D6612EA4-low.png)

The ruled mesh is constructed as a 2 by
*N* polygon mesh. RULESURF places half the mesh vertices at equal intervals along one defining curve, and the other half at equal
intervals along the other curve. The number of intervals is specified by the
[SURFTAB1](SURFTAB1-System-Variable.md) system variable. It is the same for each curve; therefore, the distance between the vertices along the two curves differs
if the curves are of different lengths.

The
*N* direction of the mesh is along the boundary curves. If both boundaries are closed, or if one is closed and the other is a
point, the resulting polygon mesh is closed in the
*N* direction and
*N* equals SURFTAB1. If both boundaries are open,
*N* equals SURFTAB1 + 1, because division of a curve into
*n* parts requires
*n* + 1 tabulations.

The 0,0 vertex of the mesh is the endpoint of the first selected curve nearest the point you used to select that curve.

Selecting objects at the same ends creates a polygon mesh.

![](../images/GUID-53057B5D-3A2E-4984-B3BA-90A09A21005E-low.png)

Selecting objects at opposite ends creates a self-intersecting polygon mesh.

![](../images/GUID-417FADAC-D5BB-4E25-9BF7-C0C9BF6D09EB-low.png)

## List of Prompts

The following prompts are displayed.

First defining curve
:   Specifies an object and start point for the new mesh object.

Second defining curve
:   Specifies an object and start point for the sweep of the new mesh object.

#### Related Concepts

* [About Constructing Meshes From Other Objects](About-Constructing-Meshes-From-Other-Objects.md)
* [About Creating Meshes](About-Creating-Meshes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*