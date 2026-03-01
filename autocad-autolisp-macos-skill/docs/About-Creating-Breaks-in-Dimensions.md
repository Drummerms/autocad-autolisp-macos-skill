# About Creating Breaks in Dimensions

With dimension breaks, you can keep the dimension, extension, or leader lines from appearing as if they are a part of the
design.

Dimension breaks can be added to a dimension or a multileader automatically or manually. The method that you choose to place
dimension breaks depends on the number of objects that intersect a dimension or multileader.

![](../images/GUID-5E7DF62F-7A6A-45F8-8B6E-2A6953D95B03-low.png)

You can add dimension breaks to the following dimension and leader objects:

* Linear dimensions, including aligned and rotated
* Angular dimensions, including 2- and 3-point
* Radial dimensions, including radius, diameter, and jogged
* Arc length dimensions
* Ordinate dimensions
* Multileaders that use straight-line leaders

You can also remove dimension breaks from dimensions or multileaders with the Remove option of DIMBREAK. When removing them,
*all* dimension breaks are removed from the selected dimension or multileader, but you can always add them back individually.

The following objects can be used as cutting edges when adding a dimension break:

* Dimension
* Leader
* Line
* Circle
* Arc
* Spline
* Ellipse
* Polyline
* Text
* Multiline text
* Blocks but limited to the previously mentioned objects in this list
* Xrefs but limited to the previously mentioned objects in this list

## Automatic Dimension Breaks

To create dimension breaks automatically, you select a dimension or multileader, and then use the Auto option of the DIMBREAK
command. Automatic dimension breaks are updated any time the dimension or multileader, or intersecting objects are modified.

## Dimension Break Gap Size

You control the size of dimension breaks in the Dimension Style dialog box, Symbols and Arrows tab. The specified size is
affected by the dimension break size, dimension scale, and current annotation scale for the current viewport.

## Dimension Break Created by Selecting an Object

Instead of placing a dimension break for each object that intersects a dimension or multileader, you can specify which of
the intersecting objects to use. Dimension breaks that are added by selecting individual intersecting objects are updated
any time the dimension or multileader, or intersecting objects are modified.

## Dimension Break Created by Picking Two Points

You can place a dimension break by picking two points on the dimension, extension, or leader line to determine the size and
placement of the break. Dimension breaks that are added manually by picking two points are not automatically updated if the
dimension or multileader, or intersecting object is modified.

So if a dimension or multileader with a manually added dimension break is moved or the intersecting object is modified, you
might have to restore the dimension or multileader, and then add the dimension break again. The size of a dimension break
that is created by picking two points is not affected by the current dimension scale or annotation scale value for the current
viewport.

## Exceptions and Limitations

The following dimension and leader objects do not support dimension breaks:

* Multileaders that use spline leaders
* Leaders created with the LEADER or QLEADER commands

Dimension breaks do not work or are not supported in the following cases:

| Dimension Break Exceptions | |
| Condition | Description |
| No break in xrefs or blocks | Dimension breaks on dimensions or multileaders in xrefs and blocks are not supported. However, the objects in an xref or block can be used as the cutting edges for dimension breaks on dimensions or multileaders that are not in an xref or block. |
| No break on arrowhead and dimension text | Dimension breaks cannot be placed on an arrowhead or the dimension text. If you want a break to appear at the dimension text, it is recommended to use the background mask option. If the intersecting point of an object and the dimension are at the arrowhead or dimension text, the break will not be displayed until the intersecting object, or dimension or multileader are moved. |
| No break on trans-spatial dimensions | Automatic breaks are not supported for objects and dimensions or multileaders that are in different spaces. In order to break a dimension or multileader that is in a different space, you need to use the Manual option of the DIMBREAK command. |

#### Related Tasks

* [To Create Dimension Breaks Automatically](To-Create-Dimension-Breaks-Automatically.md)
* [To Create a Dimension Break Manually](To-Create-a-Dimension-Break-Manually.md)
* [To Create a Single Dimension Break for an Intersecting Object](To-Create-a-Single-Dimension-Break-for-an-Intersecting-Object.md)
* [To Create Breaks for Multiple Dimensions or Multileaders Automatically](To-Create-Breaks-for-Multiple-Dimensions-or-Multileaders-Automatically.md)
* [To Remove all Breaks from a Dimension or Multileader](To-Remove-all-Breaks-from-a-Dimension-or-Multileader.md)
* [To Remove all Breaks From Multiple Dimensions or Multileaders](To-Remove-all-Breaks-From-Multiple-Dimensions-or-Multileaders.md)

#### Related Concepts

* [About Dimension Styles](About-Dimension-Styles.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*