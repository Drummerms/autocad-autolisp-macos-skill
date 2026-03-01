# About Dimensional Constraints

Dimensional constraints control the size and proportions of a design. They can constrain the following:

* Distances between objects, or between points on objects
* Angles between objects, or between points on objects
* Sizes of arcs and circles

For example, the following illustration includes linear, aligned, angular, and diameter constraints.

![](../images/GUID-9F56C1A8-919E-4FEE-B96B-8D450FD8F04B-low.png)

If you change the value of a dimensional constraint, *all* the constraints on the object are evaluated, and the objects that are affected are updated automatically.

Also, constraints can be added directly to segments within a polyline as if they were separate objects.

NOTE:The number of decimal places displayed in dimensional constraints is controlled by the LUPREC and AUPREC system variables.

## Compare Dimensional Constraints with Dimension Objects

Dimensional *constraints* are different from dimension *objects* in the following ways:

* Dimensional constraints are used in the design phase of a drawing, but dimensions are typically created in the documentation
  phase
* Dimensional constraints *drive* the size or angle of objects, but dimensions *are driven* by objects
* By default, dimensional constraints are not objects, display with only a single dimension style, maintain the same size during
  zoom operations, and are not outputted to a device

If you need to output a drawing with dimensional constraints or use dimension styles, you can change the form of a dimensional
constraint from dynamic to annotational.

## Define Variables and Equations

The PARAMETERS command allows you to define custom user variables that you can reference from within dimensional constraints
and other user variables. The expressions that you define can include a variety of predefined functions and constants.

#### Related Information

* [About Applying Dimensional Constraints](About-Applying-Dimensional-Constraints.md)
* [About Parametric Drawing](About-Parametric-Drawing.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*