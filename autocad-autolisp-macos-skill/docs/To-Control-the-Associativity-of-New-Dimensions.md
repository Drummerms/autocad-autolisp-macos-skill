# To Control the Associativity of New Dimensions

By default, new dimensions are associative

1. At the Command prompt, enter DIMASSOC.
2. Do one of the following:
   * Enter 0, to create exploded and non-associative dimensions.

     There is no association between the various elements of the dimension. The lines, arcs, arrowheads, and text of a dimension
     are drawn as separate objects.
   * Enter 1, to create non-associative dimension objects

     The elements of the dimension are formed into a single object. If one of the definition points of the dimension moves, the
     dimension is updated.
   * Enter 2, to create associative dimension objects.

     The elements of the dimension are formed into a single object, and one or more definition points of the dimension are coupled
     with association points on geometric objects. If the association point on the geometric object moves, the dimension location,
     orientation, and value are updated.

DIMASSOC is not stored in a dimension style.

Drawings saved in a format previous to AutoCAD 2002 retain the setting of the DIMASSOC system variable. When the drawing
is reopened in AutoCAD 2002 or later, the dimension associativity setting is restored.

#### Related Concepts

* [About Changing Dimension Associativity](About-Changing-Dimension-Associativity.md)

#### Related Information

* [About Associative Dimensions](About-Associative-Dimensions.md)
* [To Work with the Annotation Monitor](To-Work-with-the-Annotation-Monitor.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*