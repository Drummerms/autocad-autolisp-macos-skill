# About Constructing Solids and Surfaces From 2D Geometry

You can construct surfaces and 3D solids from 2D geometry by extruding, sweeping, lofting, and revolving.

## Methods for Constructing Surfaces or Solids From Other Geometry

When you extrude, sweep, loft, and revolve curves, you can create both solids and surfaces.

![](../images/GUID-7C53FA54-85AB-48D3-BAC9-4FD1A462F915-low.png)

Open curves always create surfaces, but closed curves can create either solids or surfaces depending on certain settings.

If you select a
*closed* curve and extrude, sweep, loft, or revolve an object, you create:

* A
  *solid* if the Mode option is set to Solid.
* A
  *surface* if the Mode option is set to Surface.

## About Surfaces Based on Other Objects

The type of surface depends on additional settings. For example, you create

* A
  *procedural surface* if the SURACEMODELINGMODE system variable is set to 0.
* A
  *NURBS surface* if the SURFACEMODELINGMODE system variable is set to 1.
* An
  *associative surface* if the SURFACEASSOCIATIVITY system variable is on.

In this illustration, the same profile creates a solid (left), a procedural surface (middle), and a NURBS surface (right).

![](../images/GUID-8BCE01D7-5238-45E3-B1C3-A78C68D0B90B-low.png)

## About Solids Based on Other Objects

You can also create 3D solids from 2D geometry or other 3D objects. For example, a 3D solid can also be the result of extruding
a 2D shape to follow a specified path in 3D space.

![](../images/GUID-B50A0B92-A21F-4EC6-9E49-B4978224CA7E-low.png)

The following methods are available:

* *Sweep.* Extends a 2D object along a path.
* *Extrusion.* Extends the shape of a 2D object in a perpendicular direction into 3D space.
* *Revolve.* Sweeps a 2D object around an axis.
* *Loft.*Extends the contours of a shape between one or more open or closed objects.
* *Slice.*Divides a solid object into two separate 3D objects.
* *Sculpting Surfaces.* Converts and trims a group of surfaces that enclose a watertight area into a solid.
* *Conversion.* Converts mesh objects and planar objects with thickness into solids and surfaces.

## Geometry That Can Be Used As Profiles and Guide Curves

The curves that you use as profile and guide curves when you extrude, sweep, loft, and revolve can be:

* Open or closed
* Planar or non-planar
* Solid and surface edges
* A single object (to extrude multiple lines, convert them to a single object with the JOIN command)
* A single region (to extrude multiple regions, convert them to a single object with the REGION command)

## Example: Use Splines to Create 3D NURBS Surfaces

Splines are one of the many 2D object types that can be lofted, extruded, swept, and revolved to create NURBS surfaces. Other
2D objects that can be used include lines, polylines, arcs, and circles. Splines, however, are the only 2D object customized
to create NURBS surfaces. Because they allow you to adjust tolerance, degree, and tangency, they are better suited than other
types of 2D profiles (such as lines, polylines, and circles) for surface modeling.

![](../images/GUID-BC88B0BC-B211-4A03-841B-7DCFEB445364-low.png)

Many of the same commands used with NURBS surfaces, can also be used with CV splines.

## Create Associative Surfaces

Surfaces can be associative while solids cannot. If surface associativity is on when a surface is created, the surface maintains
a relationship with the curve from which it is was generated (even if the curve is the subobject of another solid or surface).
If the curve is reshaped, the surface profile is also updated.

NOTE: To modify a surface that is associative, you must modify the generating curve and not the surface itself. If you reshape
the surface, its link to the generating curve will be broken and the surface will lose associativity and become a generic
surface.

## Deleting the Curves that Generate the Solid or Surface

The DELOBJ system variable controls whether the curves that generate an object are automatically deleted after the solid or
surface is created. However, if surface associativity is on, the DELOBJ setting is ignored and the generating curves are not
deleted.

#### Related Tasks

* [To Create a Solid by Lofting Through a Set of Cross-section Profiles](To-Create-a-Solid-by-Lofting-Through-a-Set-of-Cross-section-Profiles.md)
* [To Modify a Lofted Solid or Surface by Changing the Surface Normal Settings](To-Modify-a-Lofted-Solid-or-Surface-by-Changing-the-Surface-Normal-Settings.md)
* [To Revolve Objects About an Axis to Create a NURBS Surface](To-Revolve-Objects-About-an-Axis-to-Create-a-NURBS-Surface.md)
* [To Revolve Objects About an Axis to Create a Solid](To-Revolve-Objects-About-an-Axis-to-Create-a-Solid.md)

#### Related Concepts

* [About Creating a Solid or Surface by Extruding](About-Creating-a-Solid-or-Surface-by-Extruding.md)
* [About Creating a Solid or Surface by Sweeping](About-Creating-a-Solid-or-Surface-by-Sweeping.md)
* [About Creating a Solid or Surface by Lofting](About-Creating-a-Solid-or-Surface-by-Lofting.md)
* [About Creating a Solid or Surface by Revolving](About-Creating-a-Solid-or-Surface-by-Revolving.md)

#### Related Information

* [To Create a NURBS Surface by Extruding](To-Create-a-NURBS-Surface-by-Extruding.md)
* [To Create a 3D Solid by Extruding](To-Create-a-3D-Solid-by-Extruding.md)
* [To Create a Procedural Surface by Extruding Along a Path](To-Create-a-Procedural-Surface-by-Extruding-Along-a-Path.md)
* [To Create a Solid or Surface by Sweeping an Object Along a Path](To-Create-a-Solid-or-Surface-by-Sweeping-an-Object-Along-a-Path.md)
* [To Create a NURBS Surface by Conversion and Lofting](To-Create-a-NURBS-Surface-by-Conversion-and-Lofting.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*