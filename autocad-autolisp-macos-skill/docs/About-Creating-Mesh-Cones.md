# About Creating Mesh Cones

Create a pointed or frustum mesh cone with a circular or elliptical base.

![](../images/GUID-2963639B-8FC9-4499-8C6C-614DA71A13C2-low.png)

By default, the base of the mesh cone lies on the *XY* plane of the current UCS and the height of the cone is parallel to the *Z* axis.

Use the DIVMESHCONEAXIS, DIVMESHCONEBASE, and DIVMESHCONEHEIGHT system variables to set the default number of divisions for
a mesh cone.

After a mesh primitive is created, the current level of smoothness for the object can be modified.

## Mesh Cone Creation Options

The Cone option of the MESH command provides several methods for determining the size and rotation of the mesh cones you create.

* *Set the height and orientation.* Use the Axis Endpoint option when you want to reorient the cone by placing the tip or axis endpoint anywhere in 3D space.
* *Create a frustum of a cone.* Use the Top Radius option to create a frustum of a cone, which tapers to an elliptical or planar face.
* *Specify circumference and base plane.* The 3P (Three Points) option defines the size and plane of the base of the cone anywhere in 3D space.
* *Create an elliptical base.* Use the Elliptical option to create a cone base whose axes are different lengths.
* *Set the location to be tangent to two objects.* Use the Ttr (Tangent, Tangent, Radius) option to define points on two objects. Depending on the radius distance, the new cone
  is located as near as possible to the tangent points you specify. You can set up tangency with circles, arcs, lines, and some
  3D objects. The tangency points are projected onto the current UCS. The appearance of tangency is affected by the current
  level of smoothness.

#### Related Tasks

* [To Work With Creating Mesh Cones](To-Work-With-Creating-Mesh-Cones.md)

#### Related Concepts

* [About Creating Meshes](About-Creating-Meshes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*