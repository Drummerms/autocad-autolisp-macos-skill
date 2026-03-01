# UNDO (Command)

Reverses the effect of commands.

## Access Methods

*Toolbar*:
![](../images/GUID-26DE0636-9A19-4623-A5EC-D5317877FE4A-low.png)

*Menu*:
Edit ![](../images/ac.menuaro.gif) Undo.

*Shortcut Menu*: With no command active and no objects selected, right-click in the drawing area and click Undo.

*Command entry*: Cmd-Z

## Summary

UNDO displays the command or system variable name at the Command prompt to indicate that you have stepped past the point where
the command was used.

NOTE:UNDO has no effect on some commands and system variables, including those that open, close, or save a window or a drawing,
display information, change the graphics display, regenerate the drawing, or export the drawing in a different format.

## List of Prompts

The following prompts are displayed.

Enter the
[number](UNDO-Command.md) of operations to undo or [[Auto](UNDO-Command.md)/[Control](UNDO-Command.md)/[BEgin/End](UNDO-Command.md)/[Mark/Back](UNDO-Command.md)]:
*Enter a positive number, enter an option, or press*Enter *to undo a single operation*

Number

Undoes the specified number of preceding operations. The effect is the same as entering
*u*multiple times.

Auto

Groups the commands in a macro, such as a menu macro, into a single action, making them reversible by a single
[U](U-Command.md) command.

UNDO Auto is not available if the Control option has turned off or limited the UNDO feature.

Control

Limits or turns off UNDO.

All
:   Turns on the full UNDO command.

None
:   Turns off the U and UNDO commands and discards any UNDO command information saved earlier in the editing session. The Undo
    button on the Standard toolbar is unavailable.

    The Auto, Begin, and Mark options are not available when None or One is in effect. If you attempt to use UNDO while it is
    turned off, the following prompt is displayed:

    Enter an UNDO control option [All/None/One/Combine/Layer] <All>:

One
:   Limits UNDO to a single operation.

    The Auto, Begin, and Mark options are not available when None or One is in effect. The main prompt for the UNDO command changes
    to show that only a Control option or a single step of the UNDO command is available when the One option is in effect.

Combine
:   Controls whether multiple, consecutive zoom and pan commands are combined as a single operation for undo and redo operations.

    NOTE:Pan and zoom commands that are started from the menu are not combined, and always remain separate actions.

Layer
:   Controls whether the layer dialog operations are combined as a single undo operation.

Begin, End

Groups a sequence of actions into a set. After you enter the Begin option, all subsequent actions become part of this set
until you use the End option. Entering
*undo begin* while a group is already active ends the current set and begins a new one. UNDO and U treat grouped actions as a single action.

If you enter
*undo begin* without
*undo end*, using the Number option undoes the specified number of commands but does not back up past the begin point. If you want to
go back to before the begin point, you must use the End option, even if the set is empty. The same applies to the U command.
A mark placed by the Mark option disappears inside an UNDO group.

Mark, Back

Mark places a mark in the undo information. Back undoes all the work done back to this mark. If you undo one operation at
a time, you are informed when you reach the mark.

You can place as many marks as necessary. Back moves back one mark at a time, removing the mark. If no mark is found, Back
displays the following prompt:

This will undo everything. OK? <Y>:
*Enter* *y* *or* *n* *or press*Enter

Enter
*y* to undo all commands entered in the current session. Enter
*n* to ignore the Back option.

When you use the Number option to undo multiple actions, UNDO stops if it encounters a mark.

#### Related Concepts

* [About Correcting Mistakes](About-Correcting-Mistakes.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*