# Insert Block Dialog Box

Specifies the name and position of the block or drawing to insert.

CLASSICINSERT (Command)

![](../images/GUID-427BD456-BC9A-4302-B2B0-4C26BA9103DF-low.png)

## Summary

The position of the inserted block depends on the orientation of the UCS.

## Name

Specifies the name of a block to insert, or the name of a file to insert as a block.

Browse
:   Opens the Select Drawing File dialog box (a standard file selection dialog box) where you can select a block or drawing file
    to insert.

Path
:   Specifies the path to the block.

Explode Block
:   Explodes the block and inserts the individual parts of the block. When Explode is selected, you can specify a uniform scale
    factor only.

    Component objects of a block drawn on layer 0 remain on that layer. Objects having color BYBLOCK are white. Objects with linetype
    BYBLOCK have the CONTINUOUS linetype.

Description
:   Displays the description that was saved with the block.

Preview
:   Displays a preview of the specified block to insert. A lightning bolt icon in the lower-right corner of the preview indicates
    that the block is dynamic. A![](../images/GUID-B3D4A80D-2642-4C17-BD2D-BF5CA00B4D3F-low.png) icon indicates that the block is annotative.

## Show\Hide Insertion Options

Expands or collapses the Insertion Options section to allow you to specify the insertion point, rotation and scale for the
block reference being created.

## Insertion Point

Specifies the insertion point for the block.

Specify On-Screen
:   Specifies the insertion point of the block using the pointing device.

X
:   Sets the
    *X* coordinate value.

Y
:   Sets the
    *Y* coordinate value.

Z
:   Sets the
    *Z* coordinate value.

## Scale

Specifies the scale for the inserted block. Specifying negative values for the
*X*,
*Y*, and
*Z* scale factors inserts a mirror image of a block.

Specify On-Screen
:   Specifies the scale of the block using the pointing device.

X
:   Sets the
    *X* scale factor.

Y
:   Sets the
    *Y* scale factor.

Z
:   Sets the
    *Z* scale factor.

Uniform Scale
:   Specifies a single scale value for
    *X*,
    *Y*, and
    *Z* coordinates.

## Rotation

Specifies the rotation angle for the inserted block in the current UCS.

Specify On-Screen
:   Specifies the rotation of the block using the pointing device.

Angle
:   Sets a rotation angle for the inserted block.

## Block Unit

Displays information about the block units.

Unit
:   Specifies the
    [INSUNITS](INSUNITS-System-Variable.md) value for the inserted block.

Factor
:   Displays the unit scale factor, which is calculated based on the
    [INSUNITS](INSUNITS-System-Variable.md) value of the block and the drawing units.

#### Related Tasks

* [To Insert a Block Defined in the Current Drawing](To-Insert-a-Block-Defined-in-the-Current-Drawing.md)
* [To Insert a Drawing File as a Block by Dragging](To-Insert-a-Drawing-File-as-a-Block-by-Dragging.md)
* [To Change Properties of a Block Reference as You Insert It](To-Change-Properties-of-a-Block-Reference-as-You-Insert-It.md)

#### Related References

* [INSERT (Command)](INSERT-Command.md)

#### Related Concepts

* [Insert Block Dialog Box](Insert-Block-Dialog-Box.md)
* [-INSERT (Command)](INSERT-Command-2.md)
* [About Modifying Block Definitions](About-Modifying-Block-Definitions.md)

#### Related Information

* [To Work with Blocks in a Table Cell](To-Work-with-Blocks-in-a-Table-Cell.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*