# About Selecting Subobjects

Select faces, edges, and vertices on 3D objects.

## Subobject Selection Methods

A *subobject* is a face, edge or vertex of a 3D solid, surface, or mesh object. You can control which subobjects you select in several ways:

* *Set subobject filters.* The filters specify the default subobject that is selected when you click a 3D object. If no filter is selected, you select
  the entire object.
* *Press Ctrl as you click a 3D object.* If the selection set contains a mixture of subobject types, this method is useful because it overrides any subobject filters
  that have been set.

## Select Subobjects

Selected subobjects display different types of grips, depending on the subobject type.

![](../images/GUID-D57BBF8B-800A-495A-9F2A-492C7AF268C6-low.png)

You can select one or more subobjects on any number of 3D objects. The selection set can include more than one type of subobject.
Press and hold Ctrl to select subobjects at the selection prompts of the MOVE, ROTATE, SCALE, and ERASE commands.

![](../images/GUID-D91E6BE7-ABCC-469C-85E6-ECF00E9347CE-low.png)

You can remove an item from the selection set by pressing and holding Shift and selecting it again.

## Select Subobjects on Composite 3D Solids

Press and hold Ctrl to select faces, edges, and vertices on composite solids. If the History property of the composite solid
is set to Record (On), the first “pick” might select the *history subobject*. (The history subobject is the portion of the original object that was removed during the union, subtract, or intersect operation.)
Continue to hold Ctrl and pick again to select a face, edge, or vertex on the original form.

![](../images/GUID-DFE36D55-3016-488D-8E35-31339C973C3A-low.png)

If you set a subobject selection filter, you can select the face, edge, or vertex by clicking it once.

#### Related Tasks

* [To Work With Subobject Selection](To-Work-With-Subobject-Selection.md)
* [To Work With Selecting a Component of a Composite Solid](To-Work-With-Selecting-a-Component-of-a-Composite-Solid.md)
* [To Cycle Through and Select Overlapping Subobjects](To-Cycle-Through-and-Select-Overlapping-Subobjects.md)

#### Related Concepts

* [About Using Grips to Edit 3D Objects](About-Using-Grips-to-Edit-3D-Objects.md)
* [About Cycling Through and Filtering Subobjects](About-Cycling-Through-and-Filtering-Subobjects.md)
* [About Moving, Rotating, and Scaling Faces on 3D Solids and Surfaces](About-Moving,-Rotating,-and-Scaling-Faces-on-3D-Solids-and-Surfaces.md)
* [Modify Vertices on 3D Objects](Modify-Vertices-on-3D-Objects.md)

#### Related Information

* [About Modifying Edges on 3D Objects](About-Modifying-Edges-on-3D-Objects.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*