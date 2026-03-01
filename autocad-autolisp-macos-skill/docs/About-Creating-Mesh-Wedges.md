# About Creating Mesh Wedges

Create a mesh wedge with rectangular or cubical faces.

![](../images/GUID-FE936F2A-48D2-451A-BB67-1D7D73352E12-low.png)

The base of the wedge is drawn parallel to the *XY* plane of the current UCS with the sloped face opposite the first corner. The height of the wedge is parallel to the *Z* axis.

Use the DIVMESHWEDGEBASE, DIVMESHWEDGEHEIGHT, DIVMESHWEDGESLOPE, DIVEMESHWEDGEWIDTH, and DIVMESHWEDGELENGTH system variables
to set the default number of divisions for a mesh wedge.

After a mesh primitive is created, the current level of smoothness for the object can be modified.

## Mesh Wedge Creation Options

The Wedge option of the MESH command provides several methods for determining the size and rotation of the mesh wedges you
create.

* *Create a wedge with sides of equal length.* Use the Cube option.
* *Specify rotation.* Use the Cube or Length option if you want to set the rotation of the mesh wedge in the XY plane.
* *Start from the center point.* Use the Center Point option.

#### Related Concepts

* [About Creating Meshes](About-Creating-Meshes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*