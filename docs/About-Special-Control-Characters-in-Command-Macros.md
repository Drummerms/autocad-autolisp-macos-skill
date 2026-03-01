# About Special Control Characters in Command Macros

Command macro strings support the use of special characters that are equivalent to pressing a key on the keyboard or for pausing
for user input.

For example, the backslash (\) in the following macro pauses for user input and the semicolon (;) represents pressing the Enter key.

```
^C^C_.text \.4 0 DRAFT Inc;;;Main St.;;;City, State;
```

The macro starts the TEXT command, pauses so the user can specify an insertion point, and then enters the address on three
lines. In the triple semicolon (;;;) sequence, the first semicolon ends the text string, the second repeats the TEXT command, and the third accepts the default
placement below the previous line.

Macros can use the special characters listed in the following table.

| Special characters used in macros | |
| Character | Description |
| [blank space] | Enters a space; a blank space in command sequences is equivalent to pressing the Spacebar. |
| ; | Issues Enter. |
| \ | Pauses for user input (cannot be used with accelerators). |
| . | Allows you to access a standard command even if it was undefined using the UNDEFINE command. |
| \_ | Translates commands and options that follow from the localized name to the global name. |
| ' | Invokes the command transparently. |
| =\* | Displays the current top-level pull-down, shortcut, or image tile menu. (Windows only) |
| \* | Repeats a command until another command is started or the current command is ended. |
| $ | Introduces a conditional DIESEL macro expression ($M=). |
| ^] | Prompts the user to select objects, if no objects are already selected. The selected objects are assigned to the Previous selection set.  Use the Previous selection option at the Select objects prompt to use the selected objects.  Equivalent to .\_SELECT;$M=$(if,$(eq,$(getvar,cmdnames),SELECT),\,)  NOTE:Support was added with AutoCAD 2023. |
| ^B | Turns Snap on or off; equivalent to Ctrl+B (Windows) or Control-B (Mac OS). |
| ^C | Cancels the active command or command option; equivalent to pressing Esc. |
| ^D | Turns Dynamic UCS on or off; equivalent to Ctrl+D (Windows) or Control-D (Mac OS). |
| ^E | Sets the next isometric plane; equivalent to Ctrl+E (Windows). (No equivalent key press on Mac OS) |
| ^G | Turns Grid on or off; equivalent to Ctrl+G (Windows) or Control-G (Mac OS). |
| ^H | Enters a Backspace. |
| ^I | Issues Tab. |
| ^M | Issues Enter. |
| ^O | Turns Ortho on or off. |
| ^P | Turns MENUECHO on or off. |
| ^Q | Suppresses the display of all prompts and input from the Command Line history for the macro. |
| ^R | Turns command versioning on or off. Command versioning is required for some commands to ensure the command macro written in an older release works properly in the latest release. |
| ^T | Turns the tablet on or off; equivalent to Ctrl+T. (Windows only) |
| ^V | Changes the current viewport. |
| ^Z | Null character that suppresses the automatic addition of a space being added to the end of the macro. |

NOTE:Several of these control characters operate differently when entered directly from the keyboard, including ^Q (Quit) , ^R
(cycle through viewports), and ^V (paste from the clipboard).

#### Related Tasks

* [To Create a Custom Command](To-Create-a-Custom-Command.md)
* [To Edit a Command](To-Edit-a-Command.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Command Macro Strings](About-Command-Macro-Strings.md)
* [About Pausing Macros for User Input](About-Pausing-Macros-for-User-Input.md)
* [About Using Conditional Expressions in Macros](About-Using-Conditional-Expressions-in-Macros.md)
* [About Using AutoLISP in Macros](About-Using-AutoLISP-in-Macros.md)
* [About Command Customization](About-Command-Customization.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*