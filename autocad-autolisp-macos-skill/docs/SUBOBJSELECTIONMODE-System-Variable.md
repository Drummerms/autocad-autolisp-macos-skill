# SUBOBJSELECTIONMODE (System Variable)

Filters whether faces, edges, vertices or solid history subobjects are highlighted when you roll over them.

|  |  |
| --- | --- |
| Type: | Integer |
| Saved in: | Not-saved |
| Initial value: | 0 |

In busy 3D environments with many objects, it can be helpful to filter certain subobjects out of the selection highlighting.

| 0 | When subobject filtering is off, press Ctrl+click to select a face, edge, vertex or a history subobject. (Shift-F1) |
| 1 | Only vertices are available for selection (Shift-F2) |
| 2 | Only edges are available for selection. (Shift-F3) |
| 3 | Only faces are available for selection. (Shift-F4) |
| 4 | Only history subobjects of compound objects are available for selection. (Shift-F5) |

Turn off subobject filtering if you want to select the entire object. You can also press Ctrl-click to select faces, edges,
and vertices.

![](../images/GUID-CAB40E1E-5AC8-4B92-BE3C-2E9FFB788677-low.gif)

When filtering is set for vertices, you cannot select faces, edges, or history subobjects.

![](../images/GUID-04C95CD3-B29F-48C7-8674-1774E8CADA7D-low.gif)

When filtering is set for edges, you cannot select faces, vertices, or history subobjects.

![](../images/GUID-353E9B0D-25F8-45F5-81F8-718BD311118F-low.gif)

When filtering is set for faces, you cannot select edges, vertices, or history subobjects.

![](../images/GUID-01ACE0C2-0501-4D61-8BBD-092AB711049E-low.gif)

When filtering is set for history subobjects, you can only select the wireframe representations of portions of objects removed
during a union, subtract, or intersect operation.

![](../images/GUID-040240BF-2AF9-430C-8637-BE0B2B341BB4-low.gif)

## Subobject Selection Filter Cursors

When a subobject selection filter is set, the following images are displayed next to the cursor:

| ![](../images/GUID-52DDE51A-DE3C-4FCC-994A-6EE067594DEC-low.png) | Vertex filtering is on |
| ![](../images/GUID-44AF4139-BE48-4A37-9B7D-F88932E6A52E-low.png) | Edge filtering is on |
| ![](../images/GUID-6BF1DE74-70BD-4ABC-A521-92BF16A1157F-low.png) | Face filtering is on |
| ![](../images/GUID-41F62930-BC73-4682-AB8C-578830AC4CDB-low.png) | History subobject filtering is on |
| ![](../images/GUID-0CD52F12-7675-42FB-AB1E-987D47173D31-low.png) | Subobject not eligible for selection |

#### Related Concepts

* [About Cycling Through and Filtering Subobjects](About-Cycling-Through-and-Filtering-Subobjects.md)
* [About Selecting Subobjects](About-Selecting-Subobjects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*