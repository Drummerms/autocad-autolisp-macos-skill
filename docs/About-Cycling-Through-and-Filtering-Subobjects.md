# About Cycling Through and Filtering Subobjects

Filter and select faces, edges, and vertices on 3D objects.

## Cycle Through Multiple Subobjects

In 3D views, some objects or subobjects (faces, edges, and vertices) might be hidden behind other geometry. You can press
Ctrl+Spacebar to cycle through the hidden subobjects until the object you want to select is highlighted.

For example, when you select faces on a 3D solid box, the face in the foreground is detected first. To cycle through the hidden
faces, press Ctrl+Spacebar repeatedly. When the face you want to select is highlighted, continue to hold Ctrl and select the
face.

![](../images/GUID-C28EE859-2858-408A-B813-0482CE487C87-low.png)

## Turn on Subobject Selection Filters

Selecting a specific type of subobject can be difficult on complex objects, such as meshes. You can limit the selection to
a face, edge, vertex, or history subobject by setting a subobject selection filter on the status bar.

![](../images/GUID-6E873D4F-47C2-46BF-82B7-B6B3E0A0F2E5-low.png)

When a subobject selection filter is on, you do not need to press and hold Ctrl to select the face, edge, or vertex of a 3D
model. However, you need to turn off the filter to select the entire object. The current subobject filter setting is stored
in the SUBOBJSELECTIONMODE system variable.

When a subobject filter is turned on, the following icons are displayed near the cursor:

| *Icon* | *Filter* | *Keyboard Shortcut* |
| ![](../images/GUID-52DDE51A-DE3C-4FCC-994A-6EE067594DEC-low.png) | Vertex | Fn + Shift + F2 |
| ![](../images/GUID-44AF4139-BE48-4A37-9B7D-F88932E6A52E-low.png) | Edge | Fn + Shift + F3 |
| ![](../images/GUID-6BF1DE74-70BD-4ABC-A521-92BF16A1157F-low.png) | Face | Fn + Shift + F4 |
| ![](../images/GUID-41F62930-BC73-4682-AB8C-578830AC4CDB-low.png) | History subobject | Fn + Shift + F5 |
|  | None | Fn + Shift + F1 |

#### Related Tasks

* [To Work With Selecting a Component of a Composite Solid](To-Work-With-Selecting-a-Component-of-a-Composite-Solid.md)
* [To Cycle Through and Select Overlapping Subobjects](To-Cycle-Through-and-Select-Overlapping-Subobjects.md)
* [To Work With Subobject Selection](To-Work-With-Subobject-Selection.md)

#### Related Concepts

* [About Selecting Subobjects](About-Selecting-Subobjects.md)
* [About Using Grips to Edit 3D Objects](About-Using-Grips-to-Edit-3D-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*