# About Modifying Block Attribute Definitions

You can edit the values and other properties of attributes that are attached to a block and inserted in a drawing.

## Modify Attribute Definitions With the Block Attribute Manager

You can modify attributes in block definitions with the Block Attribute Manager. For example, you can do the following:

* *Modify tags, prompts, and default values.* These changes do not affect the values entered when existing block references were inserted. For example, if you change an
  attribute tag from "Cost" to "Unit Cost," a value entered at the prompt (such as 19.99) is unaffected.
* *Reset the attribute modes.* Modes control tag visibility, whether the value is a constant or a variable, the use of multiple-line text, the verification
  requirement, and position locking.
* *Change the attribute text display.* You can modify alignment, style, height, rotation, width (for multiple-line text), and whether it uses annotative scaling.
* *Set properties that define the layer, color, lineweight, and linetype of the attribute.*
* *Change the order of display for attribute prompts.* The order in which you select the attributes when you define a block determines the order in which you are prompted for attribute
  values when you insert the block reference. You can change the order of prompts that request attribute values.
* *Identify duplicate tag names.* Because duplicate tag names can lead to unpredictable results, you can set the Block Attribute Manager to highlight duplicate
  tags so that you can change them.
* *Remove attributes.* You can remove attributes from block definitions and from all existing block references in the current drawing. You cannot
  remove all attributes from a block; at least one attribute must remain. If you need to remove all attributes, redefine the
  block.

If constant attributes or nested attributed blocks are affected by your changes, use REGEN to update the display of those
blocks in the drawing area.

## Modify Attribute Definitions With the Block Editor

You can also use the Properties Inspector within the Block Editor to update the definition of a selected attribute. You can
modify many of the same properties that you can change in the Block Attribute Manager, but cannot change the order of the
prompts, or how the definition update is applied.

## Apply Attribute Definition Changes to Block References

As you modify an attribute, you can specify whether the change is applied only to new insertions, or also to all existing
block references in the current drawing (the default). If you elect not to apply changes to existing references, you update,
or synchronize, the references later using the Sync button in the block Attribute Manager or the ATTSYNC command.

#### Related Concepts

* [About Modifying Block Definitions](About-Modifying-Block-Definitions.md)

#### Related Information

* [To Work with Editing Attribute Definitions](To-Work-with-Editing-Attribute-Definitions.md)
* [To Work With Changing Prompt Order in Attribute Definitions](To-Work-With-Changing-Prompt-Order-in-Attribute-Definitions.md)
* [About Modifying the Data in Block Attributes](About-Modifying-the-Data-in-Block-Attributes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*