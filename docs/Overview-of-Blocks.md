# Overview of Blocks

A block can be composed of objects drawn on several layers with various properties. You can use several methods to create
blocks.

## How Blocks are Stored and Referenced

A block can be composed of objects drawn on several layers with various colors, linetypes, and lineweight properties. Whenever
you create a block or insert a drawing as a block, all block information (including geometry, layers, colors, and linetypes)
is stored in a behind-the-scenes table of definitions. Every block you insert is actually a *reference* to a block definition. Although a block is always inserted on the current layer, the block reference preserves information
about the original layer, color, and linetype properties of the objects that are contained in the block. You can control whether
objects in a block retain their original properties or inherit their properties from the current layer, color, linetype, or
lineweight settings.

Each rectangle below represents a separate drawing file and is divided into two parts:

* The block definition table
* The objects in the drawing

![](../images/GUID-115FBDC4-ECD0-44E0-92AD-354B3125FEC2-low.png)

When you insert a block you are inserting a block reference. The information is not copied from the block definition to the
drawing area. Instead, a link is established between the block reference and the block definition. Therefore, if the block
definition is changed, all references are updated automatically.

Using blocks has the following advantages:

* If you redefine a block definition, all references in that drawing are updated automatically.
* You help control the drawing size by inserting references instead of object geometry.

You remove a block reference by erasing it. However, the corresponding block definition remains. To reduce the size of a drawing,
you must also remove any unused block definitions by purging them.

## Annotative Blocks

You can also create annotative blocks. For more information about creating and working with an annotative blocks, see Create
Annotative Blocks and Attributes.

#### Related References

* [Commands for Basic Blocks](Commands-for-Basic-Blocks.md)

#### Related Information

* [About Inserting Blocks](About-Inserting-Blocks.md)
* [To Insert a Block Defined in the Current Drawing](To-Insert-a-Block-Defined-in-the-Current-Drawing.md)
* [To Insert a Drawing File as a Block by Dragging](To-Insert-a-Drawing-File-as-a-Block-by-Dragging.md)
* [To Change Properties of a Block Reference as You Insert It](To-Change-Properties-of-a-Block-Reference-as-You-Insert-It.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*