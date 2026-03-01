# MESHCREASE (Command)

Sharpens the edges of selected mesh subobjects.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Mesh panel ![](../images/ac.menuaro.gif) Mesh Crease drop-down ![](../images/ac.menuaro.gif) Add Crease.
![](../images/GUID-F13194E5-3E58-4DB6-BC93-BE1026424C25-low.png)

*Menu*:
Modify
![](../images/ac.menuaro.gif) Mesh Editing
![](../images/ac.menuaro.gif) Crease.

## Summary

You can sharpen, or crease, the edges of mesh objects. Creasing deforms mesh faces and edges that are adjacent to the selected
subobject. Creases added to mesh that has no smoothness are not apparent until the mesh is smoothed.

![](../images/GUID-442E7A93-631A-4D94-A272-A7669F6B1DCB-low.gif)

You can also apply creases to mesh subobjects by changing the crease type and crease level in the
[Properties Inspector palette](Properties-Inspector.md).

## List of Prompts

The following prompts are displayed.

Select mesh subobjects to crease
:   Specifies the mesh subobjects to crease. Click mesh faces, edges, and vertices to crease their associated edges. Press Shift+click
    to remove a subobject from the selection set.

    * [Crease value](MESHCREASE-Command.md)
    * [Always](MESHCREASE-Command.md)

Crease value
:   Sets highest smoothing level at which the crease is retained. If the smoothing level exceeds this value, the crease is also
    smoothed.

    Enter a value of 0 to remove an existing crease.

Always
:   Specifies that the crease is always retained, even if the object or subobject is smoothed or refined. A crease value of -1
    is the same as Always.

#### Related Concepts

* [About Adding Creases to Meshes](About-Adding-Creases-to-Meshes.md)
* [About Modifying Meshes](About-Modifying-Meshes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*