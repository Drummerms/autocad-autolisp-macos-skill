# About Resizing or Reshaping Objects

You can resize objects to make them longer or shorter in only one direction or to make them proportionally larger or smaller.

You can also stretch certain objects by moving an endpoint, vertex, or control point.

## Lengthen Objects

With LENGTHEN, you can change the included angle of arcs and the length of the following objects:

* Lines
* Arcs
* Open polylines
* Elliptical arcs
* Open splines.

The results are similar to extending and trimming. You can

* Drag an object endpoint dynamically
* Specify a new length or angle as a percentage of the total length or angle
* Specify an incremental length or angle measured from an endpoint
* Specify the object's total absolute length or included angle

## Stretch Objects

With STRETCH, you relocate the endpoints of objects that lie across or within a crossing selection window.

* Objects that are partially enclosed by a crossing window are stretched.
* Objects that are completely enclosed within the crossing window, or that are selected individually, are moved rather than
  stretched.

You stretch an object by specifying a base point and then a point of displacement.

![](../images/GUID-AA752E3C-A802-4877-9372-2B1A18F367A3-low.png)

Use object snaps, grid snaps, and relative coordinate entry to stretch with precision.

## Scale Objects Using a Scale Factor

With SCALE, you can make an object uniformly larger or smaller. To scale an object, you specify a base point and a scale
factor. Alternatively, you can specify a length to be used as a scale factor based on the current drawing units.

A scale factor greater than 1 enlarges the object. A scale factor between 0 and 1 shrinks the object.

Scaling changes the size of all dimensions of the selected object. A scale factor greater than 1 enlarges the object. A scale
factor less than 1 shrinks the object.

![](../images/GUID-EA5D6584-9768-462D-AAC3-94E33AB55455-low.png)

NOTE:When you use the SCALE command with   objects, the position or location of the object is scaled relative to the base point of the scale operation, but the size
of the object is not changed.

## Scale Objects Using a Reference Distance

You can also scale by reference. Scaling by reference uses an existing distance as a basis for the new size. To scale by
reference, specify the current distance and then the new desired size. For example, if one side of an object is 4.8 units
long and you want to expand it to 7.5 units, use 4.8 as the reference length.

You can use the Reference option to scale an entire drawing. For example, use this option when the original drawing units
need to be changed. Select all objects in the drawing. Then use Reference to select two points and specify the intended distance.
All the objects in the drawing are scaled accordingly.

#### Related Information

* [To Extend an Object](To-Extend-an-Object.md)
* [To Lengthen an Object](To-Lengthen-an-Object.md)
* [To Stretch an Object](To-Stretch-an-Object.md)
* [To Trim an Object](To-Trim-an-Object.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*