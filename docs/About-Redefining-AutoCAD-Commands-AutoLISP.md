# About Redefining AutoCAD Commands (AutoLISP)

Using AutoLISP, you can undefine and replace the functionality of a built-in AutoCAD command.

The UNDEFINE command allows you to disable a built-in AutoCAD command, and then using AutoLISP it can be replaced by defining
a user-defined command of the same name with the defun function. A command remains undefined for the current editing session only. The built-in definition of a command can be restored
with the REDEFINE command.

You can execute the built-in definition of a command after it has been undefined by specifying its name prefixed with a period
(.). For example, if you undefine QUIT, you can access the command by entering *.quit* at the AutoCAD Command prompt. This is also the syntax that should be used within the AutoLISP command function to make sure
your user-defined functions and commands work predictably even if a built-in command has been undefined.

It is recommended that you protect your menus, scripts, and AutoLISP programs by using the period-prefixed forms of all commands.
This ensures that your applications use the built-in command definitions rather than a redefined command.

Consider the following example. Whenever you use the LINE command, you want AutoCAD to remind you about using the PLINE command.
You can define the AutoLISP function C:LINE to substitute for the normal LINE command as follows:

```
(defun C:LINE ( )
  (princ "Shouldn't you be using PLINE?\
")
  (command ".LINE")
 (princ)
)
C:LINE
```

In this example, the function C:LINE is designed to issue its message and then to execute the standard LINE command (using .LINE with the command function). Before
AutoCAD can use your definition of the LINE command, you must undefine the built-in LINE command. Enter the following to undefine
the built-in LINE command:

```
(command ".undefine" "line")
```

After undefining the command and entering line at the AutoCAD Command prompt, AutoCAD uses the C:LINE AutoLISP function:

Command: *line*

Shouldn't you be using PLINE?

.LINE Specify first point: Specify first point:

The previous code example assumes the CMDECHO system variable is set to 1 (On). If CMDECHO is set to 0 (Off), AutoCAD does
not echo prompts during a command function call. The following code uses the CMDECHO system variable to prevent the LINE command prompt from repeating:

```
(defun C:LINE ( / cmdsave )
  (setq cmdsave (getvar "cmdecho"))
  (setvar "cmdecho" 0)
  (princ "Shouldn't you be using PLINE?\
")
  (command ".LINE")
  (setvar "cmdecho" cmdsave)
 (princ)
)
C:LINE
```

Now if you enter line at the AutoCAD Command prompt, the following text is displayed:

Shouldn't you be using PLINE?

Specify first point:

You can undefined and redefine commands to create a drawing management system, for example. You can redefine the NEW, OPEN,
and QUIT commands to write billing information to a log file after a drawing is created and before you terminate an editing
session.

#### Related Concepts

* [About Defining Commands (AutoLISP)](About-Defining-Commands-AutoLISP.md)
* [About Defining a Function (AutoLISP)](About-Defining-a-Function-AutoLISP.md)
* [About Using AutoCAD Commands (AutoLISP)](About-Using-AutoCAD-Commands-AutoLISP.md)
* [About Undoing Changes Made by a Routine (AutoLISP)](About-Undoing-Changes-Made-by-a-Routine-AutoLISP.md)
* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*