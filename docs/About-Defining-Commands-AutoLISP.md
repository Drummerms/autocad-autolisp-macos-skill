# About Defining Commands (AutoLISP)

New commands can be defined with the
defun function and by prefixing a function name with
c:.

Functions prefixed with
c: can be accessed directly from the AutoCAD Command prompt and used to redefine an AutoCAD command.

Functions that are defined as commands should not accept arguments directly, instead input for a command should be obtained
using one of the
get*XXX* functions.

The following defines a function named
HELLO. This function displays a simple message.

```
(defun HELLO () (princ "\
Hello world.") (princ))
HELLO
```

Functions can be issued from the AutoCAD Command prompt or an AutoLISP program. The
HELLO function can be called from the AutoCAD Command prompt by entering the following:

Command:
*(hello)*

Hello world.

The
HELLO function must be wrapped in parentheses since it is not defined as a command. Entering
HELLO without the parentheses at the AutoCAD Command prompt, returns the following error message:

Unknown command "HELLO". Press F1 for help.

Adding c: to the front of the
HELLO function name results in the function being declared as a command, and can then be entered at the AutoCAD Command prompt
without being wrapped with parentheses. For example:

```
(defun C:HELLO () (princ "\
Hello world.") (princ))
C:HELLO
```

While
HELLO is declared as a command, it is also an AutoLISP function as well. The command can now be entered at the AutoCAD Command
prompt, as follows:

Command:
*hello*

Hello world.

The
HELLO command can also be used transparently because it does not make a call the command function. At the AutoCAD Command prompt,
you could do the following:

Command:
*line*

From point:
*'hello*

Hello world.

From point:

If an AutoLISP function is declared as a command, you can call the command from an AutoLISP program by wrapping the whole
function name with parentheses. For example:

```
(c:hello)
```

NOTE:If you are using the Visual LISP Editor, the Console window does not recognize AutoCAD commands. You must wrap the function
name with parentheses. The Visual LISP IDE is not available in AutoCAD LT for Windows and on Mac OS.

You cannot usually use an AutoLISP statement to respond to prompts from an AutoLISP-implemented command. However, if your
AutoLISP routine makes use of the
initget function, you can use arbitrary keyboard input with certain functions. This allows an AutoLISP-implemented command to accept
an AutoLISP statement as a response. Also, the values returned by a DIESEL expression can perform some evaluation of the current
drawing and return these values to AutoLISP.

#### Related Concepts

* [About Expressions (AutoLISP)](About-Expressions-AutoLISP.md)
* [About Function Syntax (AutoLISP)](About-Function-Syntax-AutoLISP.md)
* [About Defining a Function (AutoLISP)](About-Defining-a-Function-AutoLISP.md)
* [About Using AutoCAD Commands (AutoLISP)](About-Using-AutoCAD-Commands-AutoLISP.md)
* [About Undoing Changes Made by a Routine (AutoLISP)](About-Undoing-Changes-Made-by-a-Routine-AutoLISP.md)
* [About Redefining AutoCAD Commands (AutoLISP)](About-Redefining-AutoCAD-Commands-AutoLISP.md)
* [About Accessing and Assigning Help to a Command (AutoLISP)](About-Accessing-and-Assigning-Help-to-a-Command-AutoLISP.md)
* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*