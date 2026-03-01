# About Pausing Macros for User Input

Macros can be paused using a backslash (\) at the point where you want the user to provide some form of input.

In the following example, the CIRCLE command is paused and the user is prompted to specify the center point of the circle.
Note that there is no space after the backslash.

```
^C^C_.circle \1
```

In this example, the macro starts the -LAYER command and enters the Off option. The user is then prompted to enter a layer
name to turn off before the command exits.

```
^C^C_.-layer off \;
```

NOTE:The -LAYER command normally prompts for another operation and exits only if you press the Spacebar or Enter. In the macro,
the semicolon (;) is the equivalent of pressing Enter.

A macro typically resumes after one user input, such as a single point location. Therefore, you cannot construct a macro that
accepts a variable number of inputs (as in object selection) and then continues. However, an exception is made for the SELECT
command; a backslash (\) suspends the command until object selection has been completed. Consider the following example:

```
^C^C_.select \_.change previous ;properties color blue ;
```

In this macro, the SELECT command is used to select one or more objects (^C^C\_.select \). The macro then starts the CHANGE command, references the selection set using the Previous option, and changes the color
of all selected objects to blue (\_.change previous ;properties color blue ;).

NOTE:The backslash character (\) causes a macro to pause for user input. You cannot use a backslash for any other purpose in a
macro. When you need to specify a file path, use a forward slash (/) as the path delimiter: for example, /direct/file.

The following circumstances delay resumption of a macro after a pause:

* If input of a point location is expected, object snap modes may be used before the point is specified.
* If X/Y/Z point filters are used, the command remains suspended until the entire point has been accumulated.
* For the SELECT command only, the macro does not resume until object selection has been completed.
* If the user responds with a transparent command, the suspended macro remains suspended until the transparent command is completed
  and the originally requested input is received.
* If the user responds by choosing another command (to supply options or to execute a transparent command), the original macro
  is suspended, and the newly selected item is processed to completion. Then, the suspended macro is resumed.

NOTE:When command input comes from a command, the settings of the PICKADD and PICKAUTO system variables are assumed to be 1 and
0, respectively. This preserves compatibility with previous releases and makes customization easier because you are not required
to check the settings of these variables.

#### Related Tasks

* [To Create a Custom Command](To-Create-a-Custom-Command.md)
* [To Edit a Command](To-Edit-a-Command.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Command Macro Strings](About-Command-Macro-Strings.md)
* [About Special Control Characters in Command Macros](About-Special-Control-Characters-in-Command-Macros.md)
* [About Using Conditional Expressions in Macros](About-Using-Conditional-Expressions-in-Macros.md)
* [About Using AutoLISP in Macros](About-Using-AutoLISP-in-Macros.md)
* [About Command Customization](About-Command-Customization.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*