# About Modifying Geometrically Constrained Objects

You can edit geometrically constrained objects using grips, editing commands, or by relaxing or applying geometric constraints.

By definition, geometric constraints that are applied to geometric objects limit the editing actions that you perform on
the objects.

## Modify Constrained Objects with Grips

You can modify constrained geometry using grip editing modes. The geometry will maintain all applied constraints.

For example, if a line object is constrained to remain tangent to a circle, you can rotate the line and change its length
and endpoints, but the line *or its extension* will remain tangent to the circle.

![](../images/GUID-1CDE3A5B-1AAA-41AE-83EE-44C09ED11ACE-low.png)

If the circle was an arc instead, the line *or its extension* would remain tangent to the arc *or its extension*.

The results of modifying underconstrained objects are based on what constraints have already been applied and the object types
involved. For example, if the Radius constraint had not been applied, the radius of the circle would have been modified instead
of the tangent point of the line.

![](../images/GUID-0854283E-3A06-47F4-AC63-B16C980BE969-low.png)

The CONSTRAINTSOLVEMODE system variable determines the way an object behaves when constraints are applied or when grips are
used to edit it.

Best Practice

You can limit unexpected changes by applying additional geometric or dimensional constraints such as coincident and fix constraints.

## Modify Constrained Objects

You can use commands such as MOVE, COPY, ROTATE, SCALE, and STRETCH to modify constrained geometry while maintaining the constraints
applied to the objects. Commands such as TRIM, EXTEND, BREAK, and JOIN can remove constraints in some circumstances.

NOTE:By default, if an editing command results in copying the constrained objects, the constraints applied to the original objects
will also be duplicated. This behavior is controlled by the PARAMETERCOPYMODE system variable. Using the copying technique,
you can save work by taking advantage of multiple instances of objects, bilateral symmetry, or radial symmetry. This feature
is not available in AutoCAD LT.

#### Related Tasks

* [To Modify Geometrically Constrained Objects Using Grips](To-Modify-Geometrically-Constrained-Objects-Using-Grips.md)
* [To Delete a Single Geometric Constraint From an Object](To-Delete-a-Single-Geometric-Constraint-From-an-Object.md)

#### Related Information

* [To Delete All Geometric Constraints From an Object](To-Delete-All-Geometric-Constraints-From-an-Object.md)
* [About Geometric Constraints](About-Geometric-Constraints.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*