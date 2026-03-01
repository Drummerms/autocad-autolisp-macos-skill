# To Work with Editing Attribute Definitions

How to modify and apply block attribute definitions.

## Edit Attributes Attached to a Block Definition

Use this procedure to edit attribute definitions, including tags, prompts, defaults, modes, text display, and other properties.

1. Click
   Drafting tab ![](../images/ac.menuaro.gif) Block panel ![](../images/ac.menuaro.gif) Block Attribute Manager.
   ![](../images/GUID-29956DF2-A40C-4FF8-943C-CA1DBA0F5B9D-low.png)
2. In the Block Attribute Manager, select a block from the Block list, or click Select Block and select a block in the drawing
   area.
3. In the list of attributes, double-click the attribute you want to edit, or select the attribute and click Edit.
4. In the Attribute Editor dialog box, make changes on the following tabs and click OK:
   * *Attribute tab.* Modify the tag, prompt, and default text and set the modes, such as whether the attribute is visible, a constant value, and
     so on.
   * *Text Options tab.* Modify how the text is displayed in the drawing.
   * *Properties tab.* Modify layer, linetype, lineweight, plot style, and color properties.
5. Select Synchronise Blocks if you want to update all instances of the selected block with the attribute properties currently
   defined.

   This does not affect any values assigned to attributes in each block.

## Apply Attribute Changes to All Block References (from Command Line)

Use this procedure to update all inserted block references to match the current attribute definition or to update block references
with attribute changes that are a result of redefining a block.

1. Click
   Drafting tab ![](../images/ac.menuaro.gif) Block panel ![](../images/ac.menuaro.gif) Synchronize Attributes.
   ![](../images/GUID-8D538B40-498B-441F-840B-D4D314A7F177-low.png)
2. At the prompt, do one of the following:
   * Enter
     *?* to view a list of blocks, and then enter
     *name*, followed by the name of the block.
   * Press Enter, and then use your pointing device to select a block in the drawing area.

     If a block you specify does not contain attributes or does not exist, an error message is displayed, and you are prompted
     to specify another block.

   ATTSYNC removes any format or property changes made with the ATTEDIT or EATTEDIT commands. It also deletes any extended data
   associated with the block, and might affect dynamic blocks and blocks created by third-party applications.

## Remove an Attribute from a Block Definition

1. Click
   Drafting tab ![](../images/ac.menuaro.gif) Block panel ![](../images/ac.menuaro.gif) Block Attribute Manager.
   ![](../images/GUID-29956DF2-A40C-4FF8-943C-CA1DBA0F5B9D-low.png)
2. In the Block Attribute Manager, select a block from the Block list, or click Select Block and select a block in the drawing
   area.
3. Select an attribute from the attribute list and click Remove. Removes the selected attribute from the block definition.
4. Click Synchronize Blocks . This removes the attribute from all instances of the block in the current drawing.
5. Type Regen in the command line to regenerate the drawing.

## Identify and Correct Duplicate Block Attribute Tags

Use this process to prevent unpredictable results that can occur when two or more tags have the same name.

1. Click
   Drafting tab ![](../images/ac.menuaro.gif) Block panel ![](../images/ac.menuaro.gif) Block Attribute Manager.
   ![](../images/GUID-29956DF2-A40C-4FF8-943C-CA1DBA0F5B9D-low.png)
2. In the Block Attribute Manager, the duplicate tags are highlighted in red.
3. Double-click the tag name to edit it in the Attribute Editor dialog box.
4. Type Regen in the command line to regenerate the drawing.

#### Related Concepts

* [About Modifying Block Definitions](About-Modifying-Block-Definitions.md)

#### Related Information

* [About Modifying Block Attribute Definitions](About-Modifying-Block-Attribute-Definitions.md)
* [To Work With Changing Prompt Order in Attribute Definitions](To-Work-With-Changing-Prompt-Order-in-Attribute-Definitions.md)
* [About Modifying the Data in Block Attributes](About-Modifying-the-Data-in-Block-Attributes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*