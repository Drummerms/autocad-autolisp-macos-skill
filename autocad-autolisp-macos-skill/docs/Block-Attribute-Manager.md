# Block Attribute Manager

Manages the attribute definitions for blocks in the current drawing.

BATTMAN (Command)

*Tool Set*:
Drafting tab ![](../images/ac.menuaro.gif) Block panel ![](../images/ac.menuaro.gif) Block attribute Manager.
![](../images/GUID-29956DF2-A40C-4FF8-943C-CA1DBA0F5B9D-low.png)

![](../images/GUID-4E55EA39-9C88-4CE4-814D-6710F3F09879-low.png)

## Summary

You can edit the attribute definitions in blocks, remove attributes from blocks, and change the order in which you are prompted
for attribute values when inserting a block.

Attributes of the selected block are displayed in the attribute list. By default, Tag, Prompt, Default, Mode, and Annotative
attribute properties are displayed in the attribute list. For each selected block, a description below the attribute list
identifies the number of its instances in the current drawing and in the current layout.

You can specify which attribute properties you want displayed in the list by right-clicking over the attribute headers and
choosing the ones to display.

Double-click an attribute to display the
[Attribute Editor dialog box](GUID-16555B43-D4FA-4C8E-BDF5-4256E9166A6F.htm#WSC30CD3D5FAA8F6D8FC9944FFC2D5F5A4-7FF9), where you can modify attribute properties.

## List of Options

The following options are displayed.

Select Block
:   You can use your pointing device to select a block from the drawing area. When you choose Select Block, the dialog box closes
    until you select a block from the drawing or you cancel by pressing ESC.

    If you modify attributes of a block and then select a new block before you save the attribute changes you made, you are prompted
    to save the changes before selecting another block.

Block
:   Lists all block definitions in the current drawing that have attributes. Select the block whose attributes you want to modify.

List of Attributes
:   Displays the properties of each attribute in the selected block.

Remove
:   Removes the selected attribute from the block definition. If Synchronize Blocks is clicked and then Synchronize is clicked
    in the Synchronize Blocks dialog box, the attribute is removed from all instances of the block in the current drawing.

Found in Drawing
:   Reports the total number of instances of the selected block in the current drawing.

Found in Current Layout
:   Reports the number of instances of the selected block in the current model space or layout.

Synchronize Blocks
:   Updates all instances of the selected block with the attribute properties currently defined. This does not affect any values
    assigned to attributes in each block.

Update Blocks
:   Applies the changes made and closes the dialog box open.

#### Related References

* [BATTMAN (Command)](BATTMAN-Command.md)

#### Related Concepts

* [About Modifying Block Attribute Definitions](About-Modifying-Block-Attribute-Definitions.md)

#### Related Information

* [Attribute Editor Dialog Box](Attribute-Editor-Dialog-Box.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*