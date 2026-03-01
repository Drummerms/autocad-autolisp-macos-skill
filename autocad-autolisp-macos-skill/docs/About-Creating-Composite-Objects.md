# About Creating Composite Objects

Create composite 3D objects by combining, subtracting, or finding the intersecting mass of two or more 3D solids, surfaces,
or regions.

Composite solids are created from two or more solids, surfaces, or regions through any of the following commands: UNION, SUBTRACT,
and INTERSECT.

3D solids record a *history* of how they were created. This history allows you to see the original forms that make up composite solids.

## Methods for Creating Composite Objects

Three methods are available for creating composite solids, surfaces, or regions:

* *Combine two or more objects.*

  With UNION, you can combine the total volume or area of two or more objects.

  ![](../images/GUID-4710EAD8-4A2E-42EF-87F7-FC177C844799-low.png)
* *Subtract one set of solids from another.*

  With SUBTRACT, you can remove the common volume or area of one set of objects from another. For example, you can use SUBTRACT
  to create holes in a mechanical part by subtracting cylinders from the object.

  ![](../images/GUID-68ABB681-D6D2-4831-936F-150D51E02A93-low.png)
* *Find the common volume.*

  With INTERSECT, you can create a composite object from the common volume or area of two or more overlapping objects. INTERSECT
  removes the portions that do not overlap and creates a composite object from the remainder.

  ![](../images/GUID-45A375E6-B2A6-4359-88C7-F371ED5C243C-low.png)

## Create Composites from Mixed Object Types

In addition to creating composite objects from the same object types, you can also create composites from mixed surfaces and
solids.

* *Mixed intersections.* Combining a solid and a surface through intersection results in a surface.
* *Mixed subtractions.* Subtracting a 3D solid from a surface results in a surface. However, you cannot subtract a surface from a 3D solid object.
* *Mixed unions.* You cannot create a union between 3D solid and surface objects.

You cannot combine solids with mesh objects. However, you can convert them to 3D solids in order to combine them with solids.

If a selection set of mixed objects contains regions, the regions are ignored.

#### Related Tasks

* [To Work With Creating Composite Objects](To-Work-With-Creating-Composite-Objects.md)
* [To Work With Displaying Composite Object History](To-Work-With-Displaying-Composite-Object-History.md)
* [To Work With Selecting a Component of a Composite Solid](To-Work-With-Selecting-a-Component-of-a-Composite-Solid.md)
* [To Separate a Composite 3D Solid Into Individual Solids](To-Separate-a-Composite-3D-Solid-Into-Individual-Solids.md)

#### Related Concepts

* [About Displaying the Original Components of Composite Solids](About-Displaying-the-Original-Components-of-Composite-Solids.md)
* [About Modifying Composite Solids and Surfaces](About-Modifying-Composite-Solids-and-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*