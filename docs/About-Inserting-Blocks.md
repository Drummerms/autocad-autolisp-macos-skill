# About Inserting Blocks

Save time and control the drawing size by inserting references to a set of objects that have been combined to form a block.
When you insert a block, you create a block reference and specify its location, scale, and rotation.

## Why You Use Blocks in a Drawing

A block is one or more objects combined to create a single, named object. Using blocks provides the following advantages:

* You can ensure uniformity between identical copies of furniture, fixtures, parts, symbols, and title blocks in drawings.
* You can insert, rotate, scale, move, and copy blocks much faster than operating on selections of individual geometric objects.
* If you edit or redefine a block definition, all block references in that drawing are updated automatically.
* You can include data such as part numbers, costs, service dates, and performance values to blocks. The data is stored in
  *block attributes*.
* You can reduce the file size of a drawing by inserting multiple block references instead of duplicating object geometry.

## Sources of Block Definitions

You can insert blocks from these sources:

* Blocks defined in the current drawing
* Other drawing files inserted as blocks into the current drawing
* Blocks defined in other drawing files, called
  *block library drawings*, which can be inserted into the current drawing
* Blocks created by online vendors and services. These blocks are often associated with specific parts or products.

## Insert Blocks

When you insert a block reference, you specify its location, scale, and rotation. Subsequent references to that block definition
can be inserted in different locations, scales, and rotation angles.

NOTE:When a block is inserted into a drawing, it is scaled automatically according to the ratio of units defined in the drawing
to the units defined in the block. For example, if the unit of measurement is meters in the destination drawing and centimeters
in the block, the block is inserted at 1/100 scale. See
[About Block Insertion Units and Scale](About-Block-Units-and-Insertion-Scale.md) for more information.

Although a block reference is always inserted on the current layer, the block reference preserves the properties in the block
definition. This means, for example, that blocks can have multiple colors even when they are inserted on a layer set to red
or some other color.

Several methods are available for inserting blocks.

* *Blocks Palette.* The Blocks palette is designed for fast access to blocks from a variety of sources. This palette displays blocks organized
  into these categories: Current Drawing, Recent, and Block Libraries. You can access the Blocks palette with the CONTENT command
  or from the Window menu.

  A block library can be a drawing that contains blocks or a folder that contains drawing files. A block library stored on
  the cloud can be shared across devices and AutoCAD platforms. You can insert block definitions from a block library into your
  current drawing file.
* *Classic Insert Command.* Use the CLASSICINSERT command to select from a list of block definitions in the current drawing or browse to drawing file
  to insert as a block.
* *Finder.* You can drag a .dwg file from Finder in to the drawing canvas. The file is inserted as a block. Use the Properties Inspector
  to change block properties or EXPLODE as needed.

#### Related Tasks

* [To Insert a Block Using the Libraries Tab on the Blocks Palette](To-Insert-a-Block-Using-the-Libraries-Tab-on-the-Blocks-Palette.md)
* [To Insert a Block Using Automatic Placement](To-Insert-a-Block-Using-Automatic-Placement.md)

#### Related References

* [Blocks Palette](Blocks-Palette.md)
* [Commands for Basic Blocks](Commands-for-Basic-Blocks.md)

#### Related Concepts

* [About Smart Blocks](About-Smart-Blocks.md)

#### Related Information

* [Overview of Blocks](Overview-of-Blocks.md)
* [To Insert a Block Defined in the Current Drawing](To-Insert-a-Block-Defined-in-the-Current-Drawing.md)
* [To Insert a Drawing File as a Block by Dragging](To-Insert-a-Drawing-File-as-a-Block-by-Dragging.md)
* [To Change Properties of a Block Reference as You Insert It](To-Change-Properties-of-a-Block-Reference-as-You-Insert-It.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*