# To Work With Setting Associativity for Surfaces

## Turn On Surface Associativity for New Surfaces

* At the command prompt, enter SURFACEASSOCIATIVITY and set the value to 1.

  Any new procedural surfaces will be associative.

  NOTE:NURBS surfaces cannot be associative.

## Display the Reference Surface of an Associated Surface

1. Select an associative surface.
2. In the Properties palette, under Surface Associativity, in the Show Associativity list, click Yes.
3. Press Esc to clear the selection.
4. Hover over or select the associative surface object.

   The reference surface is highlighted as well as the selected associated surface.

## Turn Off Associativity for a Surface Object

1. Select an associative surface.
2. In the Properties palette, under Surface Associativity, in the Maintain Associativity list, select None.

   The surface associativity is removed, and new surfaces will not be associated with this surface.

## Remove Associativity From a Surface

1. Select an associative surface.
2. In the Properties palette, under Surface Associativity, in the Maintain Associativity list, select Remove.

   The surface becomes a generic surface. You can no longer change surface properties in the Properties palette and the relationship
   with other objects is lost.

#### Related Tasks

* [To Create a Parallel Relationship Between Two Surfaces](To-Create-a-Parallel-Relationship-Between-Two-Surfaces.md)

#### Related References

* [Surface Types That Accept Mathematical Expressions Reference](Surface-Types-That-Accept-Mathematical-Expressions-Reference.md)

#### Related Concepts

* [About Creating Associative Surfaces](About-Creating-Associative-Surfaces.md)
* [About Creating Geometric Relationships Between Associative Surfaces](About-Creating-Geometric-Relationships-Between-Associative-Surfaces.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*