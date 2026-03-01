# About Checking 3D Models for Interferences

Identifies where 3D solids or surfaces intersect or overlap.

Use the INTERFERE command to check for interference within a set of 3D solid or surface objects. Interference checking creates
temporary solid or surface objects and highlights where the models intersect. You can compare two sets of objects or check
all 3D solids and surfaces in a drawing file. In the following example, selecting the duct (1) in the first set of objects,
and the brace (2) in the second set of objects reveals the interference.

![](../images/GUID-97B96A73-64CF-4EB3-8856-3A92A0A5C927-low.png)

During the checking operation, you can use the Interference Checking dialog box to cycle through and zoom to interference
objects. You can also specify whether to delete the temporary objects that are created during interference checking.

## Notes

* If the selection set contains both 3D solids and surfaces, the resulting interference object is a surface.
* You cannot check interference for mesh objects. However, if you select mesh objects, you can choose to convert them to a solid
  or surface object and continue the operation.
* You can select 3D solid or surface objects that are nested in blocks and external references (xrefs) and compare them against
  other objects in the selection set.

#### Related Tasks

* [To Check for Interferences Within a Solid or Surface Model](To-Check-for-Interferences-Within-a-Solid-or-Surface-Model.md)
* [To Change the Display for Interference Checking](To-Change-the-Display-for-Interference-Checking.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*