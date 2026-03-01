# -INSERT (Command)

Inserts a block or drawing into the current drawing.

## List of Prompts

The following prompts are displayed.

Enter block name or [?] <*last*>: *Enter a name, enter**?*,
*enter**~**, or press*Enter

Units: <[INSUNITS](INSUNITS-System-Variable.md) *specified for inserted block>* Conversion:
*<conversion scale>*

Specify insertion point or [Basepoint/Scale/X/Y/Z/Rotate]: *Specify a point or enter an option*

Block Name

Entering a tilde (*~*) displays the Select Drawing File dialog box (a
[standard file selection dialog box](Standard-File-Selection-Dialog-Boxes.md)).

You can control block insertion behavior in response to the Enter Block Name prompt by following the listed examples.

* *Inserting Exploded Blocks:*Preceding the name of the block with an asterisk (\*) explodes the block and inserts the individual parts of it. The block
  definition is not added to the drawing.
* *Updating a Block Path:* If you enter a block name without a path name, INSERT searches the current drawing data for an existing block definition
  by that name. You can replace an existing block definition with an external file by entering the following at the Enter Block
  Name prompt:

  *block name=file name*
* *Updating a Block Definition:* If you make changes to a block file that is inserted in your drawing and you want to change the existing block definition
  without creating a new block insertion, enter the following at the Specify Insertion Point prompt (following the Enter Block
  Name prompt):

  *block name=*

  If you enter
  *=* after the block name, the following prompt is displayed:

  Block "current" already exists. Redefine it? [Yes/No] <No>:
  *Enter* *y**, enter**n**, or press* Enter

  If you choose to redefine the block, the existing block definition is replaced with the new block definition. The drawing
  is regenerated, and the new definition is applied to all existing insertions of the block definition. Press Esc when prompted
  for the insertion point if you do not want to insert a new block into the drawing.

NOTE:Grouped objects in an inserted drawing are inserted as unnamed groups. You can list unnamed groups with the
[GROUP](GROUP-Command.md) command.

?—List Block Names

Lists the blocks currently defined in the drawing.

Insertion Point

Specifies a location for the block or drawing.

Scale Factor
:   All
    *X* and
    *Y* dimensions of the block or drawing are multiplied by the
    *X* and
    *Y* scale factors. The block or drawing is rotated by the specified angle, using the insertion point as the center of rotation.

Corner
:   Defines the
    *X* and
    *Y* scale factors at the same time, using the insertion point and another point as the corners of a box. The
    *X* and
    *Y* dimensions of the box become the
    *X* and
    *Y* scale factors. The insertion point is the first corner.

XYZ
:   Sets
    *X*,
    *Y*, and
    *Z* scale factors.

    * *X Scale Factor:* Defines
      *X*,
      *Y*, and
      *Z* scale factors for the block or drawing.
    * *Corner:* Defines the
      *X* and
      *Y* scales at the same time, using the insertion point and another point as the corners of a box, and then defines the
      *Z* scale.

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

Sets the angle of insertion for the block.

#### Related Tasks

* [To Insert a Block Defined in the Current Drawing](To-Insert-a-Block-Defined-in-the-Current-Drawing.md)
* [To Insert a Drawing File as a Block by Dragging](To-Insert-a-Drawing-File-as-a-Block-by-Dragging.md)

#### Related References

* [Insert Block Dialog Box](Insert-Block-Dialog-Box.md)

#### Related Concepts

* [About Inserting Blocks](About-Inserting-Blocks.md)

#### Related Information

* [To Work with Blocks in a Table Cell](To-Work-with-Blocks-in-a-Table-Cell.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*