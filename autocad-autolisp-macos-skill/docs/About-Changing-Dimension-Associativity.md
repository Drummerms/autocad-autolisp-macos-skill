# About Changing Dimension Associativity

You may need to change the associativity of dimensions in several circumstances including adding associativity to dimensions
created in previous releases.

You may need to change the associativity of dimensions in several circumstances such as the following:

* Redefine the associativity of dimensions in drawings that have been edited significantly.
* Add associativity to dimensions that have been partially disassociated.
* Add associativity to dimensions in legacy drawings.
* Remove associativity from dimensions in drawings that will be used by people working in releases prior to AutoCAD 2002-based
  products, but who do not want any proxy objects in the drawings.

## Reassociate Dimensions to Different Objects

With DIMREASSOCIATE, you can select one or more dimensions and step through the extension-line origin points of each dimension.
For each extension-line origin point, you can specify a new
*association point* on a geometric object. Association points determine the attachment of extension lines to locations on geometric objects.

When you create or modify associative dimensions, it is important to locate their association points carefully so that if
you make a future design change, the geometric objects that you change will also change the dimensions associated with them.

When you use the DIMREASSOCIATE command, a marker is displayed that indicates whether each successive extension line origin
point of the dimension is associative or nonassociative. A square with an X in it means that the point is associated with
a location on an object, while an X without the square means that the point is not associated with an object. Use an object
snap to specify the new association for the extension-line origin point or press Enter to skip to the next extension-line
origin point.

NOTE:The marker disappears if you pan or zoom.

## Change Non-associative Dimensions to Associative

You can change all the non-associative dimensions in a drawing to associative. Select all non-associative dimensions, and
then use DIMREASSOCIATE to step through the dimensions, associating each one with locations on geometric objects.

## Change Associative Dimensions to Non-associative

You can change all associative dimensions in a drawing to nonassociative dimensions. Select all associative dimensions, and
then use DIMDISASSOCIATE to convert them into nonassociative dimensions.

#### Related Tasks

* [To Associate or Reassociate a Dimension](To-Associate-or-Reassociate-a-Dimension.md)
* [To Disassociate a Dimension](To-Disassociate-a-Dimension.md)

#### Related Concepts

* [About Associative Dimensions](About-Associative-Dimensions.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*