# About C:XXX Functions (AutoLISP)

If an AutoLISP function is defined with a name of the form
C:*xxx*, it can be issued at the AutoCAD Command prompt in the same manner as a built-in AutoCAD command.

This is true regardless of whether you define and load the function in Visual LISP or at the AutoCAD Command prompt. You
can use this feature to add new commands to AutoCAD or to redefine existing commands.

NOTE:The Visual LISP IDE is not available in AutoCAD LT for Windows and on Mac OS.

To use functions as AutoCAD commands, be sure they adhere to the following rules:

* The function name must use the form
  C:*xxx* (upper- or lowercase characters). The
  C: portion of the name must always be present; the
   *XXX*  portion is a command name of your choice.
  C:*xxx* functions can be used to override built-in AutoCAD commands. (See About Redefining AutoCAD Commands [AutoLISP].)
* The function must be defined with no arguments. However, local variables are permitted and it is a good programming practice
  to use them.

A function defined in this manner can be issued transparently from within any prompt of any built-in AutoCAD command, provided
the function issued transparently does not call the
command function. When issuing a
C:*xxx* defined command transparently, you must precede the
 *XXX*  portion with a single quotation mark (*'*).

You can issue a built-in command transparently while a
C:*xxx* command is active by preceding it with a single quotation mark (*'*), as you would with all commands that are issued transparently. However, you cannot issue a
C:*xxx* command transparently while a
C:*xxx* command is active.

NOTE:When calling a function defined as a command from the code of another AutoLISP function, you must use the whole name, including
the parentheses; for example,
(C:HELLO). You also must use the whole name and the parentheses when you invoke the function from the VLISP Console prompt.

#### Topics in this section

* [About Defining Commands (AutoLISP)](About-Defining-Commands-AutoLISP.md)

  New commands can be defined with the
  defun function and by prefixing a function name with
  c:.
* [About Redefining AutoCAD Commands (AutoLISP)](About-Redefining-AutoCAD-Commands-AutoLISP.md)

  Using AutoLISP, you can undefine and replace the functionality of a built-in AutoCAD command.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*