# About Creating Mesh Pyramids

Create a mesh pyramid with up to 32 sides.

![](../images/GUID-38EB4501-0B2C-4E05-876F-545553280AA4-low.png)

Create a pyramid that tapers to a point, or create a frustum of a pyramid, which tapers to a planar face.

Use the DIVMESHPYRBASE, DIVMESHPYRHEIGHT, and DIVMESHPYRLENGTH system variables to set the default number of divisions for
a mesh pyramid.

After a mesh primitive is created, the current level of smoothness for the object can be modified.

## Mesh Pyramid Creation Options

The Pyramid option of the MESH command provides several methods for determining the size and rotation of the mesh pyramids
you create.

* *Set the number of sides.* Use the Sides option to set the number of sides for the mesh pyramid.
* *Set the length of the edges.* Use the Edges option to specify the dimension of the sides at the base.
* *Create a frustum of a pyramid.* Use the Top Radius option to create a frustum, which tapers to a planar face. The frustum face is parallel to, and has the
  same number of sides as, the base.

  ![](../images/GUID-37994015-5C44-4AC8-8297-9532EDFD0879-low.png)
* *Set the height and rotation of the pyramid.* Use the Axis Endpoint option to specify the height and rotation of the pyramid. This endpoint is the top of the pyramid.
  The axis endpoint can be located anywhere in 3D space.
* *Set the perimeter to be inscribed or circumscribed.* Specify whether the pyramid base is drawn inside or outside of the radius.

  ![](../images/GUID-BDC3A63E-8473-407E-BCD4-00462C85A2B5-low.png)

#### Related Tasks

* [To Work With Creating Mesh Pyramids](To-Work-With-Creating-Mesh-Pyramids.md)

#### Related Concepts

* [About Creating Meshes](About-Creating-Meshes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*