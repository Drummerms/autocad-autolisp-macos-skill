# About Creating Mesh Cylinders

Create a mesh cylinder with a circular or elliptical base.

![](../images/GUID-E100E44F-5E8B-4B30-831E-31F6D4F2391B-low.png)

By default, the base of the mesh cylinder lies on the *XY* plane of the current UCS. The height of the cylinder is parallel to the *Z* axis.

Use theDIVMESHCYLAXIS, DIVMESHCYLBASE, and DIVMESHCYLBASE system variables to set the default number of divisions for a mesh
cylinder.

After a mesh primitive is created, the current level of smoothness for the object can be modified.

## Mesh Cylinder Creation Options

The Cylinder option of the MESH command provides several methods for determining the size and rotation of the mesh cylinders
you create.

* *Set rotation.* Use the Axis Endpoint option to set the height and rotation of the cylinder. The center point of the top plane of the cylinder
  is the axis endpoint, which can be located anywhere in 3D space.
* *Use three points to define the base.* Use the 3P (Three Points) option to define the base of the cylinder. You can set three points anywhere in 3D space.
* *Create an elliptical base.* Use the Elliptical option to create a cylinder base whose axes are different lengths.
* *Set the location to be tangent to two objects.* Use the Ttr (Tangent, Tangent, Radius) option to define points on two objects. Depending on the radius distance, the new cylinder
  is located as near as possible to the tangent points you specify. You can set up tangency with circles, arcs, lines, and some
  3D objects. The tangency points are projected onto the current UCS. The appearance of tangency is affected by the current
  level of smoothness.

#### Related Tasks

* [To Work With Creating Mesh Cylinders](To-Work-With-Creating-Mesh-Cylinders.md)

#### Related Concepts

* [About Creating Meshes](About-Creating-Meshes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*