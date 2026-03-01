# About Defining Blocks

You can create blocks by associating objects and giving them a name or by creating a drawing to be used as a block.

## Block Definitions

Whenever you create a block or insert a drawing as a block, all of the block information in the
*block definition*, which includes its geometry, layers, colors, linetypes, and block attribute objects, is stored within the drawing file as
non-graphic information. Every block you insert is a
*block reference* to a block definition. Block references are often simply called blocks.

Blocks can be created and saved in several places:

* Within a drawing file intended for use only within that drawing
* Within a drawing template file intended for use by any drawing that starts with it
* As separate drawing files intended to be inserted into other drawings as blocks
* As multiple blocks within a drawing file intended to serve as a
  *block library* drawing to be accessed from other drawings
* As online block definitions provided by one of several vendors and services. These blocks are often associated with specific
  parts or products.

## Create a Block Within a Drawing

A block definition typically includes the following information:

* The block name
* Objects that are included
* A base point that's used for placing the block in a drawing
* Optionally, block attribute objects used to store data such as the part number, vendor name, service information, and so on.

## Create Drawing Files for Use as Blocks

You can create drawing files for the purpose of inserting them into other drawings as blocks. Individual drawing files are
easy to create and manage as the source of block definitions. Related drawings can be stored in a folder as a library of blocks.

* *Specify the name of the block*

  The drawing name serves as the name of the block.
* *Specify the base point of the drawing*

  By default, the WCS (world coordinate system) origin (0,0,0) is used as the base point for drawing files inserted as blocks.
  You can reset the base point to specify a different base point for insertion using the BASE command.
* *Create the objects*

  These objects typically include geometric objects, text, and block attribute objects. When you're finished, save the drawing
  in a folder with other drawings that you intend to use as blocks.

There are several methods of creating blocks so that they inherit one or more properties such as layers, colors, or linetypes
from the current setting.

NOTE:Objects in paper space are not included when you insert a drawing as a block. To transfer paper space objects to another drawing,
save the objects as a block or save them in a separate drawing file, and then insert the block or drawing file into the other
drawing.

## Work with a Block Library Drawing

You can create collections of related blocks with the BLOCK command and stored them in a dedicated drawing file called a
*block library* drawing. You can then insert these blocks individually from any other drawing. If you insert the entire block library drawing
file into the current drawing, all of its block definitions are added automatically to the current drawing.

## Create Nested Blocks

Block references that are included in a block definition are called
*nested blocks*. Using blocks within blocks can simplify the organization of a complex block definition.

![](../images/GUID-3299D5DE-E6F0-4287-B037-569D1AF46CB1-low.png)

NOTE:Blocks that try to reference themselves are called
*circular references* and are not allowed.

## Work with Commercial Blocks

With online access, you can download AutoCAD drawing files from the web sites of commercial vendors and suppliers. This option
can save you a significant amount of time creating the blocks yourself, but always check to make sure that these drawings
are drawn correctly and to scale.

#### Related References

* [Block Object Properties Reference](Block-Object-Properties-Reference.md)
* [Commands for Basic Blocks](Commands-for-Basic-Blocks.md)

#### Related Concepts

* [About Working With the Block Editor](About-Working-With-the-Block-Editor.md)

#### Related Information

* [To Define a New Block (Block Editor)](To-Define-a-New-Block-Block-Editor.md)
* [To Define a Block for the Current Drawing](To-Define-a-Block-for-the-Current-Drawing.md)
* [To Create a New Drawing File From Selected Objects](To-Create-a-New-Drawing-File-From-Selected-Objects.md)
* [About Organizing Blocks](About-Organizing-Blocks.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*