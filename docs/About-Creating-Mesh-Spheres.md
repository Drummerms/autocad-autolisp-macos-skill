# About Creating Mesh Spheres

Create a mesh sphere using one of several methods.

![](../images/GUID-8D195E43-E855-4CCB-B114-E35CD7491E1E-low.png)

When you start with the center point, the central axis of the mesh sphere parallels the *Z* axis of the current user coordinate system (UCS).

Use the DIVMESHSPHEREAXIS and DIVMESHSPHEREHEIGHT system variables to set the default number of divisions for a mesh sphere.

After a mesh primitive is created, the current level of smoothness for the object can be modified.

## Mesh Sphere Creation Options

The Sphere option of the MESH command provides several methods for determining the size and rotation of the mesh spheres you
create.

* *Specify three points to set the size and plane of the circumference or radius.* Use the 3P (Three Points) option to define the size of the sphere anywhere in 3D space. The three points also define the
  plane of the circumference.
* *Specify two points to set the circumference or radius.* Use the 2P (Two Points) option to define the size of the sphere anywhere in 3D space. The plane of the circumference matches
  the Z value of the first point.
* *Set the location to be tangent to two objects.* Use the Ttr (Tangent, Tangent, Radius) option to define points on two objects. Depending on the radius distance, the sphere
  is located as near as possible to the tangent points you specify. You can set up tangency with circles, arcs, lines, and some
  3D objects. The tangency points are projected onto the current UCS. The appearance of tangency is affected by the current
  level of smoothness.

#### Related Tasks

* [To Work With Creating Mesh Spheres](To-Work-With-Creating-Mesh-Spheres.md)

#### Related Concepts

* [About Creating Meshes](About-Creating-Meshes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*