# PFACE (Command)

Creates a 3D polyface mesh vertex by vertex.

## List of Prompts

The following prompts are displayed.

Specify location for vertex 1:
*Specify a point*

Specify location for vertex 2 or <define faces>:
*Specify a point or press*Enter

Specify location for vertex
*n* or <define faces>:
*Specify a point or press* Enter

Vertex Location

You specify all vertices used in the mesh. The vertex numbers displayed in the prompts are the numbers used to reference each
vertex. The prompt is repeated until you press Enter. If you press Enter on a blank line, you are prompted for the vertices
to be assigned to each face.

Define Faces

Vertex Number
:   You define each face by entering vertex numbers for all the vertices of that face. The mesh is drawn after you have defined
    the last face and pressed Enter after the prompt.

    To make an edge invisible, you can enter a negative vertex number for the beginning vertex of the edge.

    You can create polygons with any number of edges. PFACE automatically breaks them into multiple face objects with the appropriate
    invisible edges. Faces with one or two vertices behave like point or line objects without the special properties of Point
    Display modes or linetypes. You can use them to embed wireframe images within a mesh. Use Endpoint object snap to snap to
    a face composed of one or two vertices. All object snap modes that apply to line objects work with visible edges of polyface
    meshes. You cannot use
    [PEDIT](PEDIT-Command.md) to edit polyface meshes.

Color
:   Faces created with PFACE adopt the current layer and color. Unlike polyline vertices, polyface mesh faces can be created with
    layer and color properties different from their parent object.

    You can enter a color from the AutoCAD Color Index (a color name or number), a true color, or a color from a color book.

Layer
:   Faces created with PFACE adopt the current layer and color. Unlike polyline vertices, polyface mesh faces can be created with
    layer and color properties different from their parent object. Layer visibility behaves normally on faces of a polyface mesh.
    However, if you create a polyface mesh on a frozen layer, the program does not generate any of its faces, including those
    on non-frozen layers.

#### Related Concepts

* [About Creating a Custom Mesh (Legacy)](About-Creating-a-Custom-Mesh-Legacy.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*