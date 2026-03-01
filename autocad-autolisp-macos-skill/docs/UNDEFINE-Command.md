# UNDEFINE (Command)

Allows an application-defined command to override an internal command.

## List of Prompts

The following prompts are displayed.

Enter command name:

Enter a command name to suppress that command. The suppressed command name can then be redefined to perform some other function.

You can undefine only built-in AutoCAD commands. You cannot undefine commands defined by AutoLISP ® . This includes ObjectARX™ application commands registered by
*acedDefun()*. You also cannot undefine external commands and aliases defined in the
*acad.pgp* file.

If an AutoLISP or ObjectARX application has redefined a command with the same name as a built-in AutoCAD command, the application-defined
command is active.

You can restore an undefined command with
[REDEFINE](REDEFINE-Command.md).

You can always access a built-in AutoCAD command by preceding the command name with a period (.).

ObjectARX application commands that are registered by
*acedRegCmd* can be accessed by preceding the command name with a period (.), followed by the command's group name, followed by another
period (.). For example, the MTEXT command can be accessed with
*.acad\_mtext.mtext*.

To determine command names and groups of an ObjectARX application, use the
[ARX](ARX-Command.md) command, and choose the Commands option to see a listing of all currently loaded ObjectARX commands and their group names.

#### Related Concepts

* [About ObjectARX Applications](About-ObjectARX-Applications.md)
* [About AutoLISP Applications](About-AutoLISP-Applications.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*