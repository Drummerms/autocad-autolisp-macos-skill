# LAYOFF (Command)

Turns off the layer of a selected object.

## Access Methods

*Menu*:
Window ![](../images/ac.menuaro.gif) Properties Inspector ![](../images/ac.menuaro.gif) Layer Off.
![](../images/GUID-E9F7CCA6-6783-4D1C-A11B-787098E1D65E-low.png)

*Menu*:
Format
![](../images/ac.menuaro.gif) Layer Tools
![](../images/ac.menuaro.gif) Layer Off.

## Summary

Turning off the layer of a selected object makes that object invisible. This command is useful if you need an unobstructed
view when working in a drawing or if you don’t want to plot details such as reference lines.

## List of Prompts

The following prompts are displayed.

*Current settings*: Viewports=*current*, Block nesting level=*current*

[Select an object on the layer to be turned off](LAYOFF-Command.md)or [[Settings](LAYOFF-Command.md)/[Undo](LAYOFF-Command.md)]:
*Select an object,* *enter**s**, or enter**u*

Select an Object on the Layer to be Turned Off

Selects one or more objects whose layers you want to turn off.

Settings

Displays the Viewports and Block Definition setting types. The setting you choose persists from session to session.

Viewports
:   Displays the Viewports setting types.

    Returns the following prompt:

    * *Vpfreeze: In paper space, freezes the layer selected in the current viewport.*
    * *Off:* In paper space, turns off selected layers in all viewports.

Block Selection
:   Displays the Block Selection setting types, where you can freeze layers of selected objects.

    * *Block*: Turns off the layers of selected objects. If a selected object is nested in a block, the layer containing that block is
      turned off. If a selected object is nested in an xref, the layer of the object is turned off.
    * *Entity*: Turns off layers of selected objects even if they are nested in an xref or a block.
    * *None*: Turns off the layers of selected objects. If a block or an xref is selected, the layer containing that block or xref is
      turned off.

Undo

Cancels the previous layer selection.

#### Related Tasks

* [To Work with Layers](To-Work-with-Layers.md)
* [To Work with the Layer List in the Layers Palette](To-Work-with-the-Layer-List-in-the-Layers-Palette.md)

#### Related References

* [Commands for Layers](Commands-for-Layers.md)

#### Related Concepts

* [About Layers](About-Layers.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*