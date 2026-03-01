# About Modifying Block Definitions

You can modify a block definition using several methods.

## Modify a Block Definition

There are several methods for redefining a block definition. The method you choose depends on whether you want to make changes
in the current drawing only or in a source drawing also.

* *Modify the block definition in the current drawing.*

  The Block Editor provides the easiest way to modify a block in the current drawing. The changes you make and save in the Block
  Editor replace the existing block definition, and all references to that block in the drawing are immediately updated.

  An alternative way to modify a block definition is to create a new block definition, but enter the name of the existing block
  definition. You can insert and explode an instance of the original block and then use the resulting objects in creating the
  new block definition.
* *Modify the block definition in the source drawing and reinsert it into the current drawing.*

  Updating a block that was created in another drawing and then inserted into the current drawing does not trigger an automatic
  update (unlike inserting xrefs). To update a block that has been updated in another drawing, you must reinsert it.
* *Update a block definition that originated from an inserted drawing file.*

  Block definitions created in your current drawing by inserting a drawing file are not updated automatically when the original
  drawing is modified. You must insert the drawing again to update a block definition from the drawing file.
* *Update a block definition that originated in a library drawing (advanced).*

  Inserting a block using DesignCenter does not overwrite an existing block definition. To insert a block definition that has
  been updated in a block library, for example, use WBLOCK to save the block as a separate drawing. Then, insert the drawing
  to overwrite the outdated block definition.

  NOTE:Block descriptions are stripped off when using INSERT. Use the Clipboard to copy and paste a block description displayed in
  the Block Definition dialog box from one block definition to another.

## Remove a Block Definition

The block definition remains in the drawing, even when all references to that block are erased. In order to remove the block
definition, you need to purge it.

#### Related References

* [Commands for Basic Blocks](Commands-for-Basic-Blocks.md)

#### Related Information

* [To Update a Block Definition](To-Update-a-Block-Definition.md)
* [To Modify the Description of a Block](To-Modify-the-Description-of-a-Block.md)
* [To Open a Block Definition for Editing (Block Editor)](To-Open-a-Block-Definition-for-Editing-Block-Editor.md)
* [To Open a Drawing Saved as a Block (Block Editor)](To-Open-a-Drawing-Saved-as-a-Block-Block-Editor.md)
* [To Ensure Uniform Scaling in a Block Reference](To-Ensure-Uniform-Scaling-in-a-Block-Reference.md)
* [To Specify Whether a Block Reference Can Be Exploded](To-Specify-Whether-a-Block-Reference-Can-Be-Exploded.md)
* [To Save a Copy of a Block with a New Name (Block Editor)](To-Save-a-Copy-of-a-Block-with-a-New-Name-Block-Editor.md)
* [To Save a Block as a Drawing](To-Save-a-Block-as-a-Drawing.md)
* [To View Properties of a Block Definition (Block Editor)](To-View-Properties-of-a-Block-Definition-Block-Editor.md)
* [To Remove a Block Definition](To-Remove-a-Block-Definition.md)
* [About Modifying Block References](About-Modifying-Block-References.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*