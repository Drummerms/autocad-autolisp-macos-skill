# MESH (Command)

Creates a 3D mesh primitive object such as a box, cone, cylinder, pyramid, sphere, wedge, or torus.

## Access Methods

*Tool Set*:
Modeling tab ![](../images/ac.menuaro.gif) Mesh panel ![](../images/ac.menuaro.gif) Primitive drop-down.

*Menu*:
Draw
![](../images/ac.menuaro.gif) 3D Modeling ![](../images/ac.menuaro.gif) Meshes ![](../images/ac.menuaro.gif) Primitives.

## Summary

The basic mesh forms, known as mesh primitives, are the equivalent of the primitive forms for 3D solids.

You can reshape mesh objects by smoothing, creasing, refining, and splitting faces. You can also drag edges, faces, and vertices
to mold the overall form.

NOTE:By default, new mesh primitives are created with no smoothness. To change the default smoothness, enter
*mesh* at the Command prompt. Specify the Settings option before you specify the type of mesh primitive you want to create.

## List of Prompts

The following prompts are displayed.

Select primitive [[Box](MESH-Command.md)/[Cone](MESH-Command.md)/[CYlinder](MESH-Command.md)/[Pyramid](MESH-Command.md)/[Sphere](MESH-Command.md)/[Wedge](MESH-Command.md)/[Torus](MESH-Command.md)/[SEttings](MESH-Command.md)]

Box
![](../images/GUID-420D13B2-59AB-420C-A8A2-CFAE1D5EBC66-low.png)

Creates a 3D mesh box.

![](../images/GUID-9EB30727-30E7-4CCD-89B3-2D0F7F15B054-low.gif)

Specify the length of the sides.

First corner / Corner
:   Sets the first corner of the mesh box.

    * *Other corner.* Sets the opposite corner of the mesh box.
    * [Cube](MESH-Command.md)
    * [Length](MESH-Command.md)

Center
:   Sets the center of the mesh box.

    * *Corner.* Sets the opposite corner of the mesh box.
    * [Cube](MESH-Command.md)
    * [Length](MESH-Command.md)

Cube
:   Sets all edges of the box to be of equal length.

    * [Length](MESH-Command.md)

Length
:   Sets the length of the mesh box along the
    *X* axis.

    * [Width](MESH-Command.md) (not available for cubes)

Width
:   Sets the width of the mesh box along the
    *Y* axis.

    * [Height](MESH-Command.md)
    * [2Point (height)](MESH-Command.md)

Height
:   Sets the height of the mesh box along the
    *Z* axis.

2Point (height)
:   Sets the height based on the distance between two points:

    * *First point.*Sets the first point of a two-point distance.
    * *Second point.* Sets the second point of a two-point distance.

Cone
![](../images/GUID-F70FF188-E1DC-4FC3-B950-D161BEE677E9-low.png)

Creates a 3D mesh with a circular or elliptical base that tapers symmetrically to a point or to a planar face.

![](../images/GUID-646AA443-DF94-4578-B116-EDC2B7083A55-low.gif)

Specify the diameter and height.

Center point of base
:   Sets the center point of the base of the mesh cone.

    * [Base radius](MESH-Command.md)
    * [Diameter](MESH-Command.md)

3P (three points)
:   Sets the location, size, and plane of the mesh cone by specifying three points:

    * *First point.* Sets the first point on the circumference of the mesh cone base.
    * *Second point.*Sets a second point on the circumference of the mesh cone base.
    * *Third point.* Sets the size and planar rotation of the mesh cone base.
      + [Height](MESH-Command.md)
      + [2Point (height)](MESH-Command.md)
      + [Axis endpoint](MESH-Command.md)
      + [Top radius](MESH-Command.md)

2P (diameter)
:   Defines the base diameter of the mesh cone based on two points:

    * *First endpoint of diameter.* Sets the first location on the circumference of the mesh cone base.
    * *Second endpoint of diameter.* Determines the general location and size of the mesh cone base by setting the endpoint of the diameter.
      + [Height](MESH-Command.md)
      + [2Point (height)](MESH-Command.md)
      + [Axis endpoint](MESH-Command.md)
      + [Top radius](MESH-Command.md)

Ttr (tangent, tangent, radius)
:   Defines the base of the mesh cone with a specified radius that is tangent to two objects:

    * *Point on object for first tangent.* Sets a point on an object to serve as the first tangent point.
    * *Point on object for second tangent.* Sets a point on an object to serve as the second tangent point.
    * *Radius of circle.* Sets the radius of the mesh cone base.
      + [Height](MESH-Command.md)
      + [2Point (height)](MESH-Command.md)
      + [Axis endpoint](MESH-Command.md)
      + [Top radius](MESH-Command.md)

      If the specified criteria can produce multiple results, the closest tangent points are used.

Elliptical
:   Specifies an elliptical base for the mesh cone.

    * *Endpoint of first axis.*Sets the start point for the first axis of the mesh cone base and then specifies the other axis endpoints:
      + *Other endpoint of first axis.* Sets the first axis endpoint.
      + *Endpoint of second axis.* Sets the second axis endpoint
    * *Center.* Specifies the method for creating an elliptical mesh cone base that starts with the center point of the base:
      + *Center point.* Sets the center of the mesh cone base.
      + *Distance to first axis.* Sets the radius of the first axis.
      + *Endpoint of second axis.* Sets the endpoint of the second axis.

Base radius
:   Sets the radius of the mesh cone base.

    * [Height](MESH-Command.md)
    * [2Point (height)](MESH-Command.md)
    * [Axis endpoint](MESH-Command.md)
    * [Top radius](MESH-Command.md)

Diameter
:   Sets the diameter for the base of the cone.

    * [Height](MESH-Command.md)
    * [2Point (height)](MESH-Command.md)
    * [Axis endpoint](MESH-Command.md)
    * [Top radius](MESH-Command.md)

Height
:   Sets the height of the mesh cone along an axis that is perpendicular to the plane of the base.

2Point (height)
:   Defines the height of the mesh cone by specifying the distance between two points:

    * *First point.*Sets the first point of a two-point distance.
    * *Second point.* Sets the second point of a two-point distance.

Axis endpoint
:   Sets the location of the top point of the cone or the center of the top face of a cone frustum. The orientation of the axis
    endpoint can be anywhere in 3D space.

Top radius
:   Specifies the top radius of the cone, creating a cone frustum.

    * [Height](MESH-Command.md)
    * [2Point (height)](MESH-Command.md)
    * [Axis endpoint](MESH-Command.md)

Cylinder
![](../images/GUID-B8CD7888-31AB-4E00-81DD-06A251748C47-low.png)

Creates a 3D mesh cylinder.

![](../images/GUID-3FCB8CAF-9257-4F9B-8DD6-6DBBE0746BE6-low.gif)

Specify the size of the base and height.

Center point of base
:   Sets the center point of the mesh cylinder base.

    * [Base Radius](MESH-Command.md)
    * [Diameter](MESH-Command.md)

3P (three points)
:   Sets the location, size, and plane of the mesh cylinder by specifying three points:

    * *First point.* Sets the first point on the circumference of the mesh cylinder base.
    * *Second point.*Sets a second point on the circumference of the mesh cylinder base.
    * *Third point.* Sets the size and planar rotation of the mesh cylinder base.
      + [Height](MESH-Command.md)
      + [2Point (height)](MESH-Command.md)
      + [Axis endpoint](MESH-Command.md)

2P (diameter)
:   Sets the diameter of the mesh cylinder base by specifying two points:

    * *First endpoint of diameter.*Sets the first point on the diameter of the mesh cylinder base.
    * *Second endpoint of diameter.* Sets the second point on the diameter of the mesh cylinder base.
      + [Height](MESH-Command.md)
      + [2Point (height)](MESH-Command.md)
      + [Axis endpoint](MESH-Command.md)

2Point (height)
:   Defines the height of the mesh cylinder by specifying the distance between two points:

    * *First point.*Sets the first point of a two-point distance.
    * *Second point.* Sets the second point of a two-point distance.

Ttr (tangent, tangent, radius)
:   Defines the base of the mesh cylinder with a specified radius that is tangent to two objects. If the specified criteria can
    produce multiple results, the closest tangent points are used.

    * *Point on object for first tangent.* Sets a point on an object to serve as the first tangent point.
    * *Point on object for second tangent.* Sets a point on an object to serve as the second tangent point.
    * *Radius of circle.* Sets the radius of the mesh cylinder base.
      + [Height](MESH-Command.md)
      + [2Point (height)](MESH-Command.md)
      + [Axis endpoint](MESH-Command.md)

Base Radius
:   Sets the radius of the mesh cylinder base.

    * [Height](MESH-Command.md)
    * [2Point (height)](MESH-Command.md)
    * [Axis endpoint](MESH-Command.md)

Diameter
:   Sets the diameter for the base of the cylinder.

    * [Height](MESH-Command.md)
    * [2Point (height)](MESH-Command.md)
    * [Axis endpoint](MESH-Command.md)

Height
:   Sets the height of the mesh cylinder along an axis that is perpendicular to the plane of the base.

Axis endpoint
:   Sets the location of the top face of the cylinder. The orientation of the axis endpoint can be anywhere in 3D space.

Elliptical
:   Specifies an elliptical base for the mesh cylinder.

    * *Endpoint of first axis.*Sets the start point for the first axis of the mesh cone base.
      + *Other endpoint of first axis.* Sets the first axis endpoint.
      + *Endpoint of second axis.* Sets the second axis endpoint.
    * *Center.* Specifies the method for creating an elliptical mesh cone base that starts with the center point of the base.
      + *Center point.* Sets the center of the mesh cone base.
      + *Distance to first axis.* Sets the radius of the first axis.
      + *Endpoint of second axis.* Sets the endpoint of the second axis.

Pyramid
![](../images/GUID-F08801A4-92D4-4D7B-8114-1AF30E29B08E-low.png)

Creates a 3D mesh pyramid.

![](../images/GUID-66B458DD-B1A3-4E6E-9E1C-A2ED9B5320CA-low.gif)

Specify the diameter and height.

Center point of base
:   Sets the center point of the mesh pyramid base.

    * [Base radius](MESH-Command.md)
    * [Inscribed](MESH-Command.md)

Edge
:   Sets the length of the one edge of the mesh pyramid base, as indicated by two points that you specify:

    * *First endpoint of edge.*Sets the first location of the edge of the mesh pyramid.
    * *Second endpoint of edge.* Sets the second location of the edge of the mesh pyramid.
      + [Height](MESH-Command.md)
      + [2Point (height)](MESH-Command.md)
      + [Axis endpoint](MESH-Command.md)
      + [Top radius](MESH-Command.md)

Sides
:   Sets the number of sides for the mesh pyramid. Enter a positive value from 3-32.

    * [Center point of base](MESH-Command.md)
    * [Edge](MESH-Command.md)
    * *Sides.*Resets the number of sides for the mesh pyramid.

Base radius
:   Sets the radius of the mesh pyramid base.

    * [Height](MESH-Command.md)
    * [2Point (height)](MESH-Command.md)
    * [Axis endpoint](MESH-Command.md)
    * [Top radius](MESH-Command.md)

Inscribed
:   Specifies that the base of the mesh pyramid is inscribed, or drawn within, the base radius.

    * [Base radius](MESH-Command.md)
    * [Circumscribed](MESH-Command.md)

Height
:   Sets the height of the mesh pyramid along an axis that is perpendicular to the plane of the base.

2Point (height)
:   Defines the height of the mesh cylinder by specifying the distance between two points:

    * *First point.*Sets the first point of a two-point distance.
    * *Second point.* Sets the second point of a two-point distance.

Axis endpoint
:   Sets the location of the top point of the pyramid or the center of the top face of a pyramid frustum. The orientation of the
    axis endpoint can be anywhere in 3D space.

Top radius
:   Specifies the top radius of the mesh pyramid, creating a pyramid frustum.

    * [Height](MESH-Command.md)
    * [2Point (height)](MESH-Command.md)
    * [Axis endpoint](MESH-Command.md)

Circumscribed
:   Specifies that the base of the pyramid is circumscribed, or is drawn around, the base radius.

    * [Base radius](MESH-Command.md)
    * [Inscribed](MESH-Command.md)

Sphere
![](../images/GUID-D22E5B03-04EA-4FE6-BB76-3890875E68AE-low.png)

Creates a 3D mesh sphere.

:   ![](../images/GUID-19325786-2B9F-4392-BBFF-7169618268A5-low.gif)

    Specify the size of the sphere (diameter or radius).

Center point
:   Sets the center point of the sphere.

    * *Radius.*Creates a mesh sphere based on a specified radius.
    * *Diameter.* Creates a mesh sphere based on a specified diameter.

3P (three points)
:   Sets the location, size, and plane of the mesh sphere by specifying three points:

    * *First point.* Sets the first point on the circumference of the mesh sphere.
    * *Second point.*Sets a second point on the circumference of the mesh sphere.
    * *Third point.* Sets the size and planar rotation of the mesh sphere.

2P (diameter)
:   Sets the diameter of the mesh sphere by specifying two points:

    * *First endpoint of diameter.*Sets the first point on the diameter of the mesh sphere.
    * *Second endpoint of diameter.* Sets the opposite point on the diameter of the mesh sphere.

Ttr (tangent, tangent, radius)
:   Defines a mesh sphere with a specified radius that is tangent to two objects:

    * *Point on object for first tangent.* Sets a point on an object to serve as the first tangent point.
    * *Point on object for second tangent.* Sets a point on an object to serve as the second tangent point.
    * *Radius of circle.* Sets the radius of the mesh sphere.

    If the specified criteria can produce multiple results, the closest tangent points are used.

Wedge
![](../images/GUID-F6A5C919-B3D7-499C-BA7A-94645FE0AEAB-low.png)

Creates a 3D mesh wedge.

![](../images/GUID-B17BCA29-3101-409B-9812-F4F277D86725-low.gif)

Specify the length and width of the base and the height.

First corner
:   Sets the first corner of the mesh wedge base.

    * *Other corner.*Sets the opposite corner of the mesh wedge base, located on the
      *X,Y*plane.
      + [Height](MESH-Command.md)
      + [2Point (height)](MESH-Command.md)
    * [Cube](MESH-Command.md)
    * [Length](MESH-Command.md)

Center
:   Sets the center point of the mesh wedge base.

    * *Corner.*Sets one corner of the mesh wedge base.
      + [Height](MESH-Command.md)
      + [2Point (height)](MESH-Command.md)
    * [Cube](MESH-Command.md)
    * [Length](MESH-Command.md)

Cube
:   Sets all edges of the mesh wedge base to be of equal length.

    * [Length](MESH-Command.md)

Length
:   Sets the length of the mesh wedge base along the X axis.

    * [Width](MESH-Command.md) (not available for Cube)

Width
:   Sets the width of the mesh box along the Y axis.

    * [Height](MESH-Command.md)
    * [2Point (height)](MESH-Command.md)

Height
:   Sets the height of the mesh wedge. Enter a positive value to draw the height along the positive
    *Z* axis of the current UCS. Enter a negative value to draw the height along the negative
    *Z* axis.

2Point (height)
:   Defines the height of the mesh wedge by specifying the distance between two points:

    * *First point.*Sets the first point of a two-point distance.
    * *Second point.* Sets the second point of a two-point distance.

Torus
![](../images/GUID-3CDF7085-3645-4BD2-B3E0-995327BB666D-low.png)

Creates a 3D mesh primitive torus.

![](../images/GUID-6224A340-1506-45CB-8C80-1A334F7DEAE1-low.gif)

Specify two values: the size of the tube and the distance from the center of the torus to the center of the tube.

Center point
:   Sets the center point of the mesh torus.

    * [Radius (torus)](MESH-Command.md)
    * [Diameter (torus)](MESH-Command.md)

3P (three points)
:   Sets the location, size, and rotation of the mesh torus by specifying three points. The path of the tube passes through the
    specified points:

    * *First point.*Sets the first point on the path of the tube.
    * *Second point.* Sets the second point on the path of the tube.
    * *Third point.* Sets the third point on the path of the tube.
      + [Tube radius](MESH-Command.md)
      + [2Point (tube radius)](MESH-Command.md)
      + [Diameter (tube)](MESH-Command.md)

2P (torus diameter)
:   Sets the diameter of the mesh torus by specifying two points. The diameter is calculated from the center point of the torus
    to the center point of the tube.

    * *First endpoint of diameter.* Sets the first point used to specify the torus diameter distance.
    * *Second endpoint of diameter.*Sets the second point used to specify the torus diameter distance.
      + [Tube radius](MESH-Command.md)
      + [2Point (tube radius)](MESH-Command.md)
      + [Diameter (tube)](MESH-Command.md)

Ttr (tangent, tangent, radius)
:   Defines a mesh torus radius that is tangent to two objects. The specified tangent points are projected into the current UCS:

    * *Point on object for first tangent.* Sets a point on an object to serve as the first tangent point.
    * *Point on object for second tangent.* Sets a point on an object to serve as the second tangent point.
    * *Radius of circle.* Sets the radius of the mesh torus.

    If the specified criteria can produce multiple results, the closest tangent points are used.

Radius (torus)
:   Sets the radius of the mesh torus, measured from the center point of the torus to the center point of the tube.

    * [Tube radius](MESH-Command.md)
    * [2Point (tube radius)](MESH-Command.md)
    * [Diameter (tube)](MESH-Command.md)

Diameter (torus)
:   Sets the diameter of the mesh torus, measured from the center point of the torus to the center point of the tube.

    * [Tube radius](MESH-Command.md)
    * [2Point (tube radius)](MESH-Command.md)
    * [Diameter (tube)](MESH-Command.md)

Tube radius
:   Sets the radius of the profile that is swept around the mesh torus path.

2Point (tube radius)
:   Sets the radius of the profile of the tube based on the distance between two points that you specify:

    * *First point.*Sets the first point of a two-point distance.
    * *Second point.* Sets the second point of a two-point distance.

Tube diameter
:   Sets the diameter of the profile of the mesh torus tube.

Settings

Modifies the smoothness and tessellation values for the new mesh object.

Level of smoothness
:   Sets the initial degree of smoothness, or roundness, to be applied to the mesh. Enter
    *0* to eliminate smoothness. Enter a positive integer up to 4 for increased degrees of smoothness. The value is retained for
    the current drawing session.

    This smoothness value is limited by the value of
    [SMOOTHMESHMAXLEV](SMOOTHMESHMAXLEV-System-Variable.md).

Tessellation
:   Enter a tessellation values (the number of faces) for each dimension of a mesh primitive option.

#### Related Concepts

* [About Creating Meshes](About-Creating-Meshes.md)
* [About Creating Mesh Boxes](About-Creating-Mesh-Boxes.md)
* [About Creating Mesh Cones](About-Creating-Mesh-Cones.md)
* [About Creating Mesh Cylinders](About-Creating-Mesh-Cylinders.md)
* [About Creating Mesh Pyramids](About-Creating-Mesh-Pyramids.md)
* [About Creating Mesh Spheres](About-Creating-Mesh-Spheres.md)
* [About Creating Mesh Tori](About-Creating-Mesh-Tori.md)
* [About Creating Mesh Wedges](About-Creating-Mesh-Wedges.md)
* [About Modifying Meshes](About-Modifying-Meshes.md)
* [About Changing Mesh Smoothness Levels](About-Changing-Mesh-Smoothness-Levels.md)
* [About Modifying Mesh Faces](About-Modifying-Mesh-Faces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*