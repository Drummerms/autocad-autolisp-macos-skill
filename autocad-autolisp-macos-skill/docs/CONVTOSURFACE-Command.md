# CONVTOSURFACE (Command)

Converts objects to 3D surfaces.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Surface panel ![](../images/ac.menuaro.gif) Convert to Surface.
![](../images/GUID-4EC93940-F904-40DA-9989-C51F3CD39C26-low.png)

*Menu*:
Modify ![](../images/ac.menuaro.gif) 3D Operations ![](../images/ac.menuaro.gif) Convert to Surface.

## Summary

As you convert objects to surfaces, you can specify whether the resulting object is smooth or faceted.

![](../images/GUID-5A0B4BE8-5A3E-4C75-AEC3-D492478F4C1A-low.gif)

When you convert a mesh, the smoothness and number of faces of the resulting surface are controlled by the
[SMOOTHMESHCONVERT](SMOOTHMESHCONVERT-System-Variable.md) system variable. Whereas the previous example shows a conversion to a smooth, optimized surface, the following example shows
a conversion to a faceted surface in which the faces are not merged, or optimized.

![](../images/GUID-4A57095A-E7F6-462C-B615-8394F89DB976-low.gif)

With the CONVTOSURFACE command, you can convert the following objects into surfaces:

Objects That Can Be Converted to 3D Surfaces

| Objects |
| 2D solids |
| 3D solids |
| Regions |
| Open, zero-width polylines with thickness |
| Lines with thickness |
| Arcs with thickness |
| Mesh objects |
| Planar 3D faces |

![](../images/GUID-0C8F9FCF-E4DA-49B9-BFFE-589573C2E973-low.png)

objects converted to surfaces

You can select the objects to convert before you start the command.

NOTE:You can create surfaces from 3D solids with curved faces, such as a cylinder, with the
[EXPLODE](EXPLODE-Command.md) command.

The
[DELOBJ](DELOBJ-System-Variable.md) system variable controls whether the geometry used to create 3D objects is automatically deleted when the new object is created
or whether you are prompted to delete the objects.

## List of Prompts

The following prompts are displayed.

Select objects
:   Specifies one or more objects to convert to surfaces.

    If one or more objects in the selection set are invalid for the command, you will be prompted again to select objects.

#### Related Concepts

* [To Convert Objects to Procedural Surfaces](To-Convert-Objects-to-Procedural-Surfaces.md)
* [About Creating Procedural Surfaces](About-Creating-Procedural-Surfaces.md)
* [About Creating 3D Surfaces](About-Creating-3D-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*