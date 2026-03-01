# MESHMERGE (Command)

Merges adjacent faces into a single face.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Mesh panel ![](../images/ac.menuaro.gif) Merge Face.
![](../images/GUID-A097062B-4D0C-4849-8067-C5C2F959499A-low.png)

*Menu*:
Modify
![](../images/ac.menuaro.gif) Mesh Editing
![](../images/ac.menuaro.gif) Merge Face.

## Summary

You can merge two or more adjacent mesh faces to form a single face.

![](../images/GUID-BCD59C98-EC87-44F6-ADF5-23EB330CFEE3-low.gif)

The merge operation is performed only on mesh faces that are adjacent. Other types of subobjects are removed from the selection
set.

Merging mesh faces that wrap a corner can have unintended results when you try to edit the mesh or convert it to other types
of solid objects. For example, the mesh might no longer be watertight. For best results, restrict mesh merging to faces that
are on the same plane.

## List of Prompts

The following prompts are displayed.

Select adjacent faces to merge
:   Specifies the mesh faces to combine. Click each face to select it.

#### Related Concepts

* [About Modifying Meshes](About-Modifying-Meshes.md)
* [About Modifying Mesh Faces](About-Modifying-Mesh-Faces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*