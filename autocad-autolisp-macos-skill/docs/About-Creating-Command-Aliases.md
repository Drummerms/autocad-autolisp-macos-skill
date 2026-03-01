# About Creating Command Aliases

A command alias is an abbreviation of a command name, which you can enter at the Command prompt instead of entering the entire
command name.

For example, you can enter
*c* instead of
*circle* to start the CIRCLE command.

NOTE:A command alias is not the same as a keyboard shortcut, which is a combination of keystrokes, such as CTRL+S for SAVE.

The program parameters (PGP) file is used to store command alias definitions. You can change existing command aliases or add
new ones.

* *Windows*: Edit
  *acad.pgp* (*acadlt.pgp* in AutoCAD LT) using an ASCII text editor (such as Notepad). In addition to command aliases, you can also add comment lines
  to add descriptive information. Start comment lines with a semicolon (;).
* *Mac OS*: Click
  Tools menu ![](../images/ac.menuaro.gif) Customize ![](../images/ac.menuaro.gif) Edit Command Aliases (PGP). Changes to the command aliases are saved to the
  *acaduser.pgp* file (or
  *acadltuser.pgp* for AutoCAD LT).

A command alias has the following syntax:

```
abbreviation,*command
```

*abbreviation*
:   Command alias that you enter at the Command prompt.

*command*
:   AutoCAD command name being abbreviated.

    You must enter an asterisk (\*) before the command name to identify the line as a command alias definition.

You can create command aliases that include the special hyphen (-) prefix, such as the following example, to access the version
of a command that displays command prompts instead of a dialog box.

```
-LA, *-LAYER
-CH, *-CHANGE
```

NOTE:You cannot use command aliases in script files, and they are not recommended for use in macros used by the user interface.

If you edit the PGP file while the program is running, use the RE-INIT system variable or RENIT command to reload the revised
file (on Windows only). Restarting the program will automatically reload the PGP file.

## AutoCorrect Entries and Synonyms

In addition to loading the aliases found in the default file, the product also loads the aliases defined in the following
two files:

* *AutoCorrectUserDB.pgp* - Library of suggestions for commonly mistyped commands and system variables. New entries are added automatically over time
  based on repeatedly mistyping commands and system variables. The Input Search AutoCorrect feature must be enabled with the
  INPUTSEARCHOPTIONS command. (The Input Search AutoCorrect feature is not available on Mac OS.)
* *acadSynonymsGlobalDB.pgp* - Library of command synonyms that are installed with the product.

NOTE:It is not recommended to edit the
*AutoCorrectUserDB.pgp* and
*acadSynonymsGlobalDB.pgp* files directly.

#### Topics in this section

* [To Manage Command Aliases](To-Manage-Command-Aliases.md)

  A command alias is an abbreviation of a command name, which you can enter at the Command prompt instead of entering the entire
  command name. Edit the Program Parameters (PGP) File to manage command aliases.

#### Related Tasks

* [To Manage Command Aliases](To-Manage-Command-Aliases.md)
* [To Customize Shortcut Keys](To-Customize-Shortcut-Keys.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)
* [Aliases Tab (Customize Dialog Box)](Aliases-Tab-Customize-Dialog-Box.md)

#### Related Concepts

* [About Customization](About-Customization.md)
* [AutoLISP and Visual LISP (AutoLISP)](AutoLISP-and-Visual-LISP-AutoLISP.md)
* [About Creating and Customizing of Shortcut Keys](About-Creating-and-Customizing-of-Shortcut-Keys.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*