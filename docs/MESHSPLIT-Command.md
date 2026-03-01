# MESHSPLIT (Command)

Splits a mesh face into two faces.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Mesh panel ![](../images/ac.menuaro.gif) Split Mesh Face.
![](../images/GUID-0195482A-85D0-4E34-9B35-0BEB0F67C22D-low.png)

*Menu*:
Modify
![](../images/ac.menuaro.gif) Mesh Editing
![](../images/ac.menuaro.gif) Split Face.

## Summary

Split a face to add more definition to an area without having to refine it. Because you specify the start and endpoint of
the split, this method provides greater control over the location of the split.

![](../images/GUID-32E8BA1C-8BA7-4FEB-9A2F-64F7B2720010-low.gif)

For more precision in the placement of the split, you can specify that the split starts or ends at a vertex. The Vertex option
is useful for creating two triangular faces from a rectangular face. It provides the precision you need if you later want
to spin the new edge using
[MESHSPIN](MESHSPIN-Command.md).

## List of Prompts

The following prompts are displayed:

Face to split
:   In the drawing area, specifies which mesh face to split.

    * *First split point on face edge.* Sets the location on an edge of the mesh face to start the split.
      + *Second split point on face edge.* Sets a second location on an edge of the mesh face to define the path of the split.
      + *Vertex*

Vertex
:   Limits the first endpoint of the split to a mesh vertex.

    * *First vertex for the split.*Specifies a vertex on a mesh face.
      + *Second split point on face edge.* Sets the second location on an edge of the mesh face to define the path of the split.
      + *Vertex.*Limits the second endpoint so that it can only intersect with a vertex.
        - *Second vertex for the split.* Specifies a second vertex on the same mesh face.

#### Related Concepts

* [About Removing Faces and Closing Gaps in Mesh Objects](About-Removing-Faces-and-Closing-Gaps-in-Mesh-Objects.md)
* [About Modifying Meshes](About-Modifying-Meshes.md)
* [About Modifying Mesh Faces](About-Modifying-Mesh-Faces.md)

#### Related Information

* [About Working With Mesh Models](About-Working-With-Mesh-Models.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*