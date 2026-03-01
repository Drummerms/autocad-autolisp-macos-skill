# About Associative Dimensions

Dimensions can be associative, nonassociative, or exploded. Associative dimensions adjust to changes in the geometric objects
that they measure.

Dimension associativity defines the relationship between geometric objects and the dimensions that give their distance and
angles. There are three types of associativity between geometric objects and dimensions.

* *Associative dimensions* *.* Automatically adjust their locations, orientations, and measurement values when the geometric objects associated with them
  are modified. Dimensions in a layout may be associated to objects in model space. These are created when the DIMASSOC system
  variable is set to 2.
* *Non-associative dimensions* *.* Selected and modified with the geometry they measure. Non-associative dimensions do not change when the geometric objects
  they measure are modified. These are created when the DIMASSOC system variable is set to 1.
* *Exploded dimensions* *.* Contain a collection of separate objects rather than a single dimension object. These are created when the DIMASSOC system
  variable is set to 0.

You can determine whether a dimension is associative or non-associative by selecting the dimension and doing one of the following:

* Use Properties Inspector to display the properties of the dimension.
* Use the LIST command to display the properties of the dimension.

A dimension is considered partially associative when only one end of the dimension is associated with a geometric object.
You can use the DIMREASSOCIATE command to reassociate non-associative dimensions.

## Annotation Monitor

Associativity between a dimension and an object may be lost for several reasons. For example:

* Associativity is not maintained between a dimension and a block reference if the block is redefined such that the edge the
  dimension is associated with moves.
* Associativity is not maintained between a dimension and a model documentation drawing view, when an update or edit event removes
  the dimensioned edge.

You can use the annotation monitor to track leader associativity. When the annotation monitor is on, it flags dimensions that
lose associativity by displaying a badge on the dimension.

![](../images/GUID-96ECDCB5-8A32-4CCF-A79C-77D026E44144-low.png)

Before update event

![](../images/GUID-34A2D503-4763-4621-B08D-8E1A6D632CCB-low.png)

After update event

Clicking a badge, displays a menu that contains options specific to the corresponding disassociated annotation. The menu on
a dimension that has lost associativity provides access to the DIMREASSOCIATE and ERASE commands.

## Special Situations and Limitations

You might need to use DIMREGEN to update associative dimensions after panning or zooming, after opening a drawing that was
modified with an earlier release, or after opening a drawing with external references that have been modified.

Associative dimensions support most object types that you would expect to dimension. They do not support objects such as

* Hatches
* Images
* Underlays
* Multiline objects
* 2D solids
* Objects with a nonzero 3D thickness property

Dimensions associated to model drawing views may lose their associativity if the drawing is opened and re-saved in a pre-2012
release of AutoCAD.

#### Related Tasks

* [To Control the Associativity of New Dimensions](To-Control-the-Associativity-of-New-Dimensions.md)

#### Related Concepts

* [About the Parts of a Dimension](About-the-Parts-of-a-Dimension.md)
* [About Changing Dimension Associativity](About-Changing-Dimension-Associativity.md)

#### Related Information

* [To Work with the Annotation Monitor](To-Work-with-the-Annotation-Monitor.md)
* [About Dimensioning](About-Dimensioning.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*