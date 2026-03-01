# About Creating Associative Surfaces

Associative surfaces automatically adjust to changes made to other, related objects.

When surface associativity is on, surfaces are created with a relationship to the surface or profiles that created them.

Associativity allows you to:

* Reshape the generating profiles to automatically reshape the surface.
* Work with a group of surfaces as if they were one object. Just as reshaping one face of a solid box adjusts the entire box,
  reshaping one surface or edge in a group of associated surfaces adjusts the entire group.
* Use geometric constraints on the 2D profiles of a surface.
* Assign mathematical expressions to derive properties of surfaces, such as height and radius. For example, specify that the
  height of an extruded surface be equal to one half the length of another object.

As you add and edit objects, all objects become related and create a chain of dependency. Editing one object can affect all
associated objects. It is important to understand the chain of associativity because moving or deleting one of the links in
the chain can break the relationship between all the objects.

NOTE:To modify the shape of a surface that is generated from a curve or spline, you must select and modify the generating curve
or spline, not the surface itself. If you modify the surface itself, you will lose associativity.

When associativity is on, the DELOBJ system variable is ignored. If Surface Associativity and NURBS Creation are both on,
surfaces are created as NURBS surfaces, not associative surfaces.

Save time by planning your model ahead; you cannot go back and add associativity after the model has been created. Also, be
careful not to accidentally break associativity by dragging objects away from the group.

#### Related Tasks

* [To Work With Setting Associativity for Surfaces](To-Work-With-Setting-Associativity-for-Surfaces.md)
* [To Create a Parallel Relationship Between Two Surfaces](To-Create-a-Parallel-Relationship-Between-Two-Surfaces.md)

#### Related References

* [Surface Types That Accept Mathematical Expressions Reference](Surface-Types-That-Accept-Mathematical-Expressions-Reference.md)

#### Related Concepts

* [About Creating Geometric Relationships Between Associative Surfaces](About-Creating-Geometric-Relationships-Between-Associative-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*