# -BSEARCH (Command)

At the Command prompt, finds matching instances of the selected object and provides options to convert them into blocks.

Stub topic for updated -BSEARCH command.

The following prompts are displayed.

### Objects to Convert to Blocks

Specifies the geometry to convert into blocks.

Instance to Remove or Add
:   Specifies instances that you want to remove or add to or from the set of searched objects.

    Click selected instances to remove from the set.

Source Objects Only
:   Converts only the source objects into blocks excluding any selected instances.

After choosing whether to convert the instances to an existing block or a new block, additional prompts are displayed.

* *New block*. Specifies the name and insertion point of the newly created block.
* *Pick.* Selects an existing block from the current drawing that you want to convert the selected instances into.
* *Enter block name.* Specifies a block that's already defined in the current drawing by entering its name.
* *Block from file.* Converts the selected instances based on a block from an external drawing file. Specify the file path and name of the block
  to be used for conversion.
* *File as block.* Converts the selected instances based on an external drawing file. Specify the file path and name of the new block to be
  used for conversion.

  NOTE:When converting the selected instances using this option, a new block definition is created.

After selecting a block for conversion, you can adjust the rotation and alignment of the block relative to the source geometry.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*