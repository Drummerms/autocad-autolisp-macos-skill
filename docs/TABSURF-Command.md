# TABSURF (Command)

Creates a mesh from a line or curve that is swept along a straight path.

## Access Methods

*Tool Sets*:
Modeling tab ![](../images/ac.menuaro.gif) Mesh panel ![](../images/ac.menuaro.gif) Tabulated Surface.
![](../images/GUID-3F02A81B-8AA1-4EC0-91D6-7925BD1D2F9B-low.png)

*Menu*:
Draw ![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Meshes ![](../images/ac.menuaro.gif) Tabulated Mesh.

## Summary

Select a line, arc, circle, ellipse, or polyline to sweep in a straight path. Then select a line or polyline to determine
the first and last points of a vector that indicates the direction and length of the polygon mesh.

![](../images/GUID-B15E3A02-6FD9-4545-A31C-D210E795ECB3-low.gif)

The
[MESHTYPE](MESHTYPE-System-Variable.md) system variable sets which type of mesh is created. Mesh objects are created by default. Set the variable to 0 to create
legacy polyface or polygon mesh.

For polygon meshes, TABSURF constructs a 2 by
*n* mesh, where
*n* is determined by the
[SURFTAB1](SURFTAB1-System-Variable.md) system variable. The
*M* direction of the mesh is always 2 and lies along the direction vector. The
*N* direction lies along the path curve. If the path curve is a line, arc, circle, ellipse, or spline-fit polyline, tabulation
lines are drawn that divide the path curve into intervals of equal size set by SURFTAB1. If the path curve is a polyline that
has
*not* been spline fit, tabulation lines are drawn at the ends of straight segments, and each arc segment is divided into intervals
set by SURFTAB1.

![](../images/GUID-295C9A52-FCD8-4CAB-BD62-8CB3727DE4F8-low.png)

## List of Prompts

The following prompts are displayed.

Object for path curve
:   Specifies which object is swept along the path.

    The path curve defines the approximated surface of the polygon mesh. It can be a line, arc, circle, ellipse, or 2D or 3D polyline.
    The mesh is drawn starting at the point on the path curve closest to the selection point.

Object for direction vector.
:   Specifies a line or open polyline that defines the direction of the sweep.

    ![](../images/GUID-DBAF571B-6A8E-47E9-86E9-28DF34ED60A3-low.png)

    ![](../images/GUID-C0E7B7D2-7348-4892-B225-84D122ECD947-low.png)

    Only the first and last points on a polyline are considered, and intermediate vertices are ignored. The direction vector indicates
    the direction and length of the shape to be extruded. The end selected on the polyline or line determines the direction of
    the extrusion. The original path curve is drawn with wide lines to help you visualize how the direction vector dictates the
    construction of a tabulated mesh.

#### Related Concepts

* [About Constructing Meshes From Other Objects](About-Constructing-Meshes-From-Other-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*