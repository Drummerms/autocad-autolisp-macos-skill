# About Command Scripts

A script is a text file with command or a script call on each line.

You can invoke a script at startup or run a script using either the SCRIPT or the SCRIPTCALL command. The difference is that
the SCRIPTCALL command can execute nested scripts in addition to commands. With the SCRIPT command, if a script is currently
active when the SCRIPT command is invoked, the script is stopped.

You create script files outside the program using a text editor text editor that saves in ASCII format (for example, Notepad
on Windows or TextEdit on Mac OS). The file extension must be .*scr*.

Each line of a script contains a command, and each blank space in a script is significant because it is like pressing Enter
or the Spacebar. You must be familiar with the sequence of prompts for a command to provide an appropriate sequence of responses
in a script.

NOTE:Keep in mind that prompts and command names might change in future releases, so you might need to revise your scripts when
you upgrade to a later release of the program. For similar reasons, avoid the use of command aliases; future command aliases
might create ambiguities.

A script can execute any command at the Command prompt except a command that displays a dialog box. In most cases, a command
that displays a dialog box has an alternative version of the command that displays Command prompts instead of a dialog box.
Most alternative versions of a command start with a hypen (-). For example, use -INSERT instead of INSERT.

NOTE:On Windows, when using the -PLOT command to automate multiple plot jobs, set the BACKGROUNDPLOT system variable to 0 before
running the script.

Scripts can contain comments. Any line that begins with a semicolon (;) is considered a comment, and is ignored while the
script is being processed. The last line of the script must be blank.

All references to long file names that contain embedded spaces must be enclosed in double quotes. For example, to open the
drawing *my house.dwg* from a script, you must use the following syntax:

```
open "my house"
```

When command input comes from a script, it is assumed that the settings of the PICKADD and PICKAUTO system variables are 1
and 0, respectively; therefore, you do not have to change the settings of these variables.

A script is treated as a group, a unit of commands, reversible by a single U command. However, each command in the script
causes an entry in the undo log, which can slow the execution of a script. Changing the Control option of the UNDO command
to None will turn off undo recording, which will improve the performance of a script when executed. Remember to turn undo
recording back on (UNDO Control All) when the script is finished.

#### Topics in this section

* [To Create a Script that Changes Settings in a Drawing](To-Create-a-Script-that-Changes-Settings-in-a-Drawing.md)

#### Related Tasks

* [To Create a Script that Changes Settings in a Drawing](To-Create-a-Script-that-Changes-Settings-in-a-Drawing.md)
* [To Run a Script at Startup](To-Run-a-Script-at-Startup.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*