# LAYISO (Command)

Hides or locks all layers except those of the selected objects.

## Access Methods

*Menu*:
Window ![](../images/ac.menuaro.gif) Properties Inspector ![](../images/ac.menuaro.gif) Isolate Layer.
![](../images/GUID-77621964-AAA3-4B86-8EAA-DCA17A18C21C-low.png)

*Menu*:
Format
![](../images/ac.menuaro.gif) Layer Tools
![](../images/ac.menuaro.gif) Isolate Layer.

## Summary

All layers except the layers of the selected objects are either turned off, frozen in the current layout viewport, or locked,
depending on the current setting. The layers that remain visible and unlocked are called isolated.

## List of Prompts

The following prompts are displayed.

Current setting: <*current settings*>

Select objects on the layer(s) to be isolated or [Settings]:
*Select objects or enter**s*

Select Objects on the Layer(s) to be Isolated

After selecting one or more objects, all layers
*except* the layers of the selected objects are either turned off, frozen in the current layout viewport, or locked, depending on
the current setting. The layers that remain visible and unlocked are termed
*isolated*.

NOTE:Locked layers are faded by default. You can specify the percent of the fading from the Lock option in this command. You can
later change the value with the
[LAYLOCKFADECTL](LAYLOCKFADECTL-System-Variable.md) system variable.

If you make changes to layers within a session and you want to restore the layers to the state they were in immediately before
you entered the LAYISO command, use the
[LAYUNISO](LAYUNISO-Command.md) command.

Settings

Controls whether layers are turned off, frozen in the current layout viewports, or locked.

Off
:   Turns off or freezes all layers
    *except* the layers of the selected objects.

Vpfreeze
:   In a layout, freezes all but the selected layers in the current layout viewport only. Other layout viewports in the drawing
    are unchanged.

    If not in a layout, all other layers are turned off instead.

Off
:   Turns off all but the selected layers in all viewports.

Lock and Fade

Locks all layers
*except* the layers of the selected objects, and sets the fading for locked layers.

#### Related Tasks

* [To Work with Layers](To-Work-with-Layers.md)
* [To Work with the Layer List in the Layers Palette](To-Work-with-the-Layer-List-in-the-Layers-Palette.md)

#### Related References

* [Commands for Layers](Commands-for-Layers.md)

#### Related Concepts

* [About Layers](About-Layers.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*