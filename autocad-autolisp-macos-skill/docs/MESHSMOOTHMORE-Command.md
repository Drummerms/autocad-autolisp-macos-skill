# MESHSMOOTHMORE (Command)

Increases the level of smoothness for mesh objects by one level.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Mesh panel ![](../images/ac.menuaro.gif) Smooth More.
![](../images/GUID-7909F658-4F28-43C8-BF76-4D7E770F26B6-low.png)

*Menu*:
Modify
![](../images/ac.menuaro.gif) Mesh Editing
![](../images/ac.menuaro.gif) Smooth More.

## Summary

Smoothing increases the number of facets in the mesh, resulting in a rounder object.

![](../images/GUID-609A911B-71F4-405C-A770-A1E29AABB7FC-low.gif)

Facets are the underlying components of each mesh face. You can increase the smoothness level up to the value of
[SMOOTHMESHMAXLEV](SMOOTHMESHMAXLEV-System-Variable.md) as long as the number of faces does not exceed the value in the
[SMOOTHMESHMAXFACE](SMOOTHMESHMAXFACE-System-Variable.md) system variable. If you select multiple objects with differing levels of smoothness, their respective levels are increased
by one.

You can only smooth mesh objects. However, you have the option of converting some types of objects to mesh during the smoothing
operation. You can also filter out ineligible objects that you do not want to convert. For a list of objects that can be converted,
see
[MESHSMOOTH](MESHSMOOTH-Command.md).

#### Related Concepts

* [About Changing Mesh Smoothness Levels](About-Changing-Mesh-Smoothness-Levels.md)
* [About Modifying Meshes](About-Modifying-Meshes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*