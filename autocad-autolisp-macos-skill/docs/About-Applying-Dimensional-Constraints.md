# About Applying Dimensional Constraints

Dimensional constraints maintain specified distances and angles between geometric objects or points on objects.

For example, you can specify that the length of a line should always remain at 6.00 units, that the vertical distance between
two points be maintained at 1.00 unit, and that a circle should always remain at 1.00 unit in diameter.

![](../images/GUID-BBFDC506-D34C-4F7C-9441-CD848CDA42D5-low.png)

When you apply a dimensional constraint to an object, a *constraint variable* is automatically created for maintaining the constraint value. By default, these are assigned names such as *d1* or *dia1*, but you can rename using Parameters command.

Dimensional constraints can be created in one of the following forms:

* Dynamic constraints
* Annotational constraints

The forms have different purposes. In addition, any dynamic or annotational constraint can be converted to a *reference parameter*.

## Dynamic Constraints

By default, dimensional constraints are *dynamic*. They are ideal for normal parametric drawing and design tasks.

Dynamic constraints have the following characteristics:

* Maintain the same size when zooming in or out
* Can easily be turned on or off globally in the drawing
* Display using a fixed, predefined dimension style
* Position the textual information automatically, and provide triangle grips with which you can change the value of a dimensional
  constraint
* Do not display when the drawing is plotted

If you need to control the dimension style of dynamic constraints, or if you need to plot dimensional constraints, use the
Properties Inspector to change dynamic constraints to annotational constraints.

## Annotational Constraints

Annotational constraints are useful when you want dimensional constraints to have the following characteristics:

* Change their size when zooming in or out
* Display individually with layers
* Display using the *current* dimension style
* Provide grip capabilities that are similar to those on dimensions
* Display when the drawing is plotted

NOTE:To display the text used in annotational constraints in the same format as used in dimensions, set the CONSTRAINTNAMEFORMAT
system variable to 1.

After plotting, you can use the Properties Inspector to convert annotational constraints back to dynamic constraints.

## Reference Parameters

A reference parameter is a *driven* dimensional constraint, either dynamic or annotational. This means that it does not control the associated geometry, but
rather reports a measurement similar to a dimension object.

You use reference parameters as a convenient way to display measurements that you would otherwise have to calculate. For example,
the width in the illustration is constrained by the diameter constraint, *dia1*, and the linear constraint, *d1*. The reference parameter, *d2*, displays the total width but does not constrain it. The textual information in reference parameters is always displayed
within parentheses.

![](../images/GUID-B85593DA-8E99-4684-98A7-CBCA67FE0CCC-low.png)

You can set the Reference property in the Properties Inspector to convert a dynamic or annotational constraint to a reference
parameter.

NOTE:

You cannot change a reference parameter back to a dimensional constraint if doing so would overconstrain the geometry.

#### Related Tasks

* [To Change the Display Format for All Dimensional Constraints](To-Change-the-Display-Format-for-All-Dimensional-Constraints.md)

#### Related Information

* [To Convert Associative Dimensions to Dimensional Constraints](To-Convert-Associative-Dimensions-to-Dimensional-Constraints.md)
* [About Dimensional Constraints](About-Dimensional-Constraints.md)
* [About Parametric Drawing](About-Parametric-Drawing.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*