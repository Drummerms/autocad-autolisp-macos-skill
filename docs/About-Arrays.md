# About Arrays

You can create copies of selected objects to be arranged in a pattern called an array.

After you select the objects that you want to duplicate, which are called the
*source objects*, you choose the arrangement pattern. There are three types of arrays:

* Rectangular
* Path
* Polar

Here's what these arrays might look like when applied to arranging display tables:

![](../images/GUID-D57DC9F8-5FD1-4877-9C5C-DDC89EA6CD36-low.png)

Each element of the array is called an
*array item*, which can be composed of several objects. You can also specify a block to be the source object of an array.

NOTE: With a path array, you also need a line, polyline, 3D polyline, spline, helix, arc, circle, or ellipse to serve as the path.

## Associative and Non-Associative Arrays

You can choose whether an array by default is associative and non-associative in an option in the ARRAY command.

* Associative arrays have the advantage that they can be easily modified later. Array items are contained in a single array
  object, similar to a block. You can change the number of these items and their spacing in an associative array. You can edit
  the array properties, such as the spacing or number of items using either the grips on the array or the Properties palette.
* Non-associative arrays become independent objects after you exit the ARRAY command.

NOTE:Quick Select does not select or count blocks nested in associative array objects.

## Modify the Items in an Associative Array

With associative arrays, you can perform edits directly using grips, with grip menu options that appear when you hover over
a grip, or by using the ARRAYEDIT command from the contextual tab or at the Command prompt. For example, here are the primary
controls for a rectangular array of chairs. Path arrays and polar arrays have similar controls.

![](../images/GUID-635DD7C4-C3E2-4566-B416-12B278778CD8-low.png)

After an associative array is created, you can still modify the items in the array as follows:

* Edit a source item of the array. All instances of the source item will be updated automatically.
* Remove one or more items in the array.
* Replace one or more items in the array with selected objects. You can also add or delete objects associated with the array
  item.

In the example, the first column of display tables was replaced by a shorter version, and two of the tables in the top row
were deleted.

![](../images/GUID-BA9A01F3-266C-4BC8-ADB6-6EE9F64F1324-low.png)

Even after these changes, the array remains associative, and the spacing and angles between the items can still be changed
dynamically in a single operation.

TIP:If you need to convert an associative array to individual objects, simply use the EXPLODE command on the array.

#### Related Information

* [To Work With Path Arrays](To-Work-With-Path-Arrays.md)
* [To Work With Polar Arrays](To-Work-With-Polar-Arrays.md)
* [To Work With Rectangular Arrays](To-Work-With-Rectangular-Arrays.md)
* [About Editing Associative Arrays](About-Editing-Associative-Arrays.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*