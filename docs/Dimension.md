# Dimension

Create several types of dimensions and save dimension settings by name.

Here is an example of several types of dimensions using an architectural dimension style with imperial units.

![](../images/GUID-07CEDC0F-BDA0-4D79-82A8-9D8310FB4195-low.png)

## Linear Dimensions

You can create horizontal, vertical, aligned, and radial dimensions with the DIM command. The type of dimension depends on
the object that you select and the direction that you drag the dimension line.

![](../images/GUID-426D04C8-90C0-4E9E-9A66-EE4778507149-low.png)

The following illustration demonstrates one method for using the DIM command. Once you enter the command, select the line
(1), and then click the location of the dimension line (2).

![](../images/GUID-D91F663A-56C6-4B78-B3BF-F0C3D4F539F2-low.png)

For the 8'-0" dimension below, you use another method. You enter the DIM command, click two endpoints (1 and 2) and then the
location of the dimension line (3). To line up the dimension lines, point 3 was snapped to the endpoint of the previously
created dimension line.

![](../images/GUID-5DCA5272-49C3-438A-82B3-E1FD90031DB7-low.png)

TIP:If points 1 and 2 are not on the same horizontal line, press Shift to force the dimension line to be horizontal. In addition,
if the building or part being dimensioned is at an angle, enter DIMROTATED for that case.

Use the DIM command to create dimensions that are parallel to an object by dragging the dimension line at an angle rather
than horizontally or vertically.

![](../images/GUID-48991C8A-0C74-42C6-BA21-7120F4F3FB45-low.png)

TIP:Because it is easy to accidentally snap to the wrong feature or to part of a dimension object, be sure to zoom in closely
enough to avoid confusion.

## Modify Dimensions

For simple adjustments to dimensions, nothing is faster than using grips.

In this example, you select the dimension to display its grips. Next, click the grip on the dimension text and drag it to
a new location, or click one of the grips at the end of the dimension line and drag the dimension line.

![](../images/GUID-466F530A-2E55-4589-9FBC-35B8F203E734-low.png)

TIP:If the changes are more complicated than this, it might be faster simply to delete and then recreate the dimension.

## Dimension Styles

Dimension styles help establish and enforce drafting standards. There are many dimension variables that can be set with the
DIMSTYLE command to control virtually every nuance of the appearance and behavior of dimensions. All these settings are stored
in each dimension style.

The default dimension style is named either Standard (imperial) or ISO-25 (metric). It is assigned to all dimensions until
you set another style as the current dimension style.

The current dimension style name, Hitchhiker in this case, is displayed in the drop-down list of the Properties Inspector
when no objects are selected.

![](../images/GUID-031579EC-0165-4959-9BBF-20F9658D5275-low.png)

Use the Dimension Style Manager to create and modify dimension styles.

![](../images/GUID-ABD85A70-727E-40F2-9F51-2E196A732B3A-low.png)

You can create dimension styles that match nearly any standard, but you will need to invest time to specify them completely.
For this reason, you should save any dimension styles that you create in one or more drawing template files.

![](../images/GUID-618251A5-29E3-4CAF-8006-2F90ECA09184-low.png)

## Recommendations

* When you save a dimension style, choose a descriptive name.
* If applicable, check with your CAD manager regarding existing dimension style standards and drawing template files.

**Parent topic:** [The Hitchhiker's Guide to AutoCAD for Mac](GUID-8B0F08A3-1B25-4E87-8CDA-5BFBC126DC6C.htm "If you're new to AutoCAD for Mac or AutoCAD LT for Mac, this guide introduces you to the essential commands that you need to create 2D drawings. It's also a great place to refresh your memory if you just completed your initial training or if you use AutoCAD for Mac only occasionally.
  ")

**Previous topic:** [Annotate](GUID-9DB2D622-DFF9-4197-8936-CDE269371BD4.htm " Create notes, labels, bubbles, and callouts. Save and restore style settings by name.
")

**Next topic:** [Print](GUID-B25DF865-4276-4905-B627-D67BB7B87151.htm " Output a drawing layout to a printer, a plotter, or a file. Save and restore the printer settings for each layout.
")

#### Related References

* [DIM (Command)](DIM-Command.md)
* [DIMROTATED (Command)](DIMROTATED-Command.md)
* [Dimension Style Manager](Dimension-Style-Manager.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*