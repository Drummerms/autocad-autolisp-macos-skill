# About Parametric Drawing

*Parametric drawing* is a technology that is used for designing with constraints, which are associations and restrictions applied to 2D geometry.

There are two general types of constraints:

* *Geometric constraints* control the relationships of objects with respect to each other
* *Dimensional constraints* control the distance, length, angle, and radius values of objects

The following illustration displays geometric and dimensional constraints using the default format and visibility.

![](../images/GUID-DA97DEF7-0A59-44D2-B7B7-1D4EB4DD6765-low.png)

A blue cursor icon always displays when you move the cursor over an object that has constraints applied to it.

![](../images/GUID-7A6E7040-BBEE-4ABF-B147-38DF71B5F589-low.png)

In the design phase of a project, constraints provide a way to enforce requirements when experimenting with different designs
or when making changes. Changes made to objects can adjust other objects automatically, and restrict changes to distance and
angle values.

With constraints, you can

* Maintain design specifications and requirements by constraining the geometry within a drawing
* Apply multiple geometric constraints to objects instantly
* Include formulas and equations within dimensional constraints
* Make design changes quickly by changing the value of a variable

Best PracticeIt is recommended that you first apply geometric constraints to determine the *shape* of a design, and then apply dimensional constraints to determine the *size* of objects in a design.

## Designing with Constraints

When you work with constraints, a drawing will be in one of three states:

* *Unconstrained*. No constraints are applied to any geometry.
* *Underconstrained*. Some constraints are applied to the geometry.
* *Fully constrained*. All relevant geometric and dimensional constraints are applied to the geometry. A fully constrained set of objects also
  needs to include at least one Fix constraint to lock the location of the geometry.

Thus, there are two general methods for designing with constraints:

* You can work in an underconstrained drawing and make changes as you go, using a combination of editing commands, grips, and
  adding or changing constraints.
* You can create and fully constrain a drawing first, and then control the design exclusively by relaxing and replacing geometric
  constraints, and changing the values in dimensional constraints.

The method that you choose depends on your design practices and the requirements of your discipline.

NOTE:

The program prevents you from applying any constraints that result in an overconstrained condition.

## Remove or Relax Constraints

There are two ways to cancel the effects of constraints when you need to make design changes:

* Delete the constraints individually and later apply new constraints. While the cursor hovers over a geometric constraint icon,
  you can use the Delete key or the shortcut menu to delete the constraint.
* Relax the constraints temporarily on selected objects to make the changes. With a grip selected or when you specify options
  during an editing command, tap the Shift key to alternate between relaxing constraints and maintaining constraints.

Relaxed constraints are not maintained during editing. Constraints are restored automatically if possible when the editing
process is complete. Constraints that are no longer valid are removed.

NOTE:The DELCONSTRAINT command deletes all geometric and dimensional constraints from selected objects.

#### Related Information

* [About Dimensional Constraints](About-Dimensional-Constraints.md)
* [About Geometric Constraints](About-Geometric-Constraints.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*