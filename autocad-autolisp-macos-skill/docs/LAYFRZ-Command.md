# LAYFRZ (Command)

Freezes the layer of selected objects.

## Access Methods

*Menu*:
Window ![](../images/ac.menuaro.gif) Properties Inspector ![](../images/ac.menuaro.gif) Freeze Layer.
![](../images/GUID-A85B6AF0-169D-4F7E-B5E9-66D91C34CCF1-low.png)

*Menu*:
Format
![](../images/ac.menuaro.gif) Layer Tools
![](../images/ac.menuaro.gif) Freeze Layer.

## Summary

Objects on frozen layers are invisible. In large drawings, freezing unneeded layers speeds up operations involving display
and regeneration. In a layout, you can freeze layers in individual layout viewports.

## List of Prompts

The following prompts are displayed.

Current settings: Viewports=*current*, Block nesting level=*current*

[Select an object on a layer to be frozen](LAYFRZ-Command.md) or [[Settings](LAYFRZ-Command.md)/[Undo](LAYFRZ-Command.md)]:
*Select an object or enter**s* *or**u*

Layer <*layer name*> has been frozen.

Select an Object on a Layer to be Frozen

Specifies the layer to be frozen.

Layer “<*layer name*>” has been frozen.

Settings

Displays settings for viewports and block definitions. The setting you choose persists from session to session.

Enter setting type for [Viewports/Block selection]:

Viewports
:   Displays settings for viewports.

    In paper space viewport use [Freeze/Vpfreeze] <Vpfreeze>:
    *Enter* *f* *to freeze objects in all viewports or* *v* *to freeze an object in the current viewport only*

Block Selection
:   Displays settings for block definitions.

    * *Block.* If a selected object is nested in a block, freezes the layer of that block. If a selected object is nested in an xref, freezes
      the layer of the object.
    * *Entity.* Freezes the layers of selected objects even if they are nested in an xref or a block.
    * *None.*If a block or an xref is selected, freezes the layer containing that block or xref.

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