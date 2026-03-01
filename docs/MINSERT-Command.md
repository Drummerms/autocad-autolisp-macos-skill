# MINSERT (Command)

Inserts multiple instances of a block in a rectangular array.

## Summary

Options at the insertion point preset the scale and rotation of a block before you specify its position. Presetting is useful
for dragging a block using a scale factor and a rotation other than 1 or 0. If you enter one of the options, respond to the
prompts by specifying a distance for the scale options or an angle for rotation.

Blocks inserted using MINSERT cannot be exploded.

You cannot use MINSERT with annotative blocks.

## List of Prompts

The following prompts are displayed.

Enter block name or [?]: *Enter a name, enter**?* *to list the currently defined blocks in the drawing, or enter**~* *to display the Select Drawing File dialog box*

NOTE:You cannot precede the name of a block with an asterisk to explode the block's objects during insertion, as you can with
[INSERT](INSERT-Command.md).

Specify insertion point or [Basepoint/Scale/X/Y/Z/Rotate]*: Specify a point or enter an option*

Insertion Point

Specifies a location for the blocks.

Enter X scale factor, specify opposite corner, or [Corner/XYZ] <1>: *Enter a value, enter an option, or press*Enter

X Scale Factor
:   Sets
    *X*and *Y*scale factors.

Specify Rotation Angle
:   The rotation angle sets the angle of the individual block inserts and also sets the angle of the entire array.

Number of Rows/Columns
:   Specifies the number of rows and columns in the array.

Distance Between Rows
:   Specifies the distance (in units) between rows. You can use the pointing device to specify the distance between rows, or specify
    two points to define a box whose width and height represent the distance between rows and between columns.

Distance Between Columns
:   Specifies the distance (in units) between columns.

Corner
:   Sets the scale factor by using the block insertion point and the opposite corner.

XYZ
:   Sets
    *X*,
    *Y*, and
    *Z* scale factors.

Basepoint

Temporarily drops the block in the drawing where it is currently positioned and allows you to specify a new base point for
the block reference as it is dragged into position. This does not affect the actual base point defined for the block reference.

Scale

Sets the scale factor for the
*X*,
*Y*, and
*Z* axes. The scale for the
*Z* axis is the absolute value of the specified scale factor.

X

Sets the
*X* scale factor.

Y

Sets the
*Y* scale factor.

Z

Sets the
*Z* scale factor.

Rotate

Sets the angle of insertion for both the individual blocks and the entire array.

Preview Scale

Sets the scale factor for the
*X*,
*Y*, and
*Z* axes to control the display of the block as it is dragged into position.

Preview X

Sets the scale factor for the
*X* axis to control the display of the block as it is dragged into position.

Preview Y

Sets the scale factor for the
*Y* axis to control the display of the block as it is dragged into position.

Preview Z

Sets the scale factor for the
*Z* axis to control the display of the block as it is dragged into position.

Preview Rotate

Sets the rotation angle of the block as it is dragged into position.

#### Related Concepts

* [About Arrays](About-Arrays.md)

#### Related Information

* [About Inserting Blocks](About-Inserting-Blocks.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*