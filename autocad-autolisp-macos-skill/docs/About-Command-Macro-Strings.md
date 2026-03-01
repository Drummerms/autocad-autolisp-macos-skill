# About Command Macro Strings

Command macro strings are used to instruct AutoCAD which commands and system variables to execute along with any expected
input allowed at the Command prompt. Special characters, DIESEL expressions and AutoLISP programming code can also included
in a command macro string.

You can create custom command macro strings that allow help to:

* Reduce repetitive tasks
* Enforce CAD standards
* Simplify workflows

You define and edit command macro strings with the:

* Customize User Interface Editor (AutoCAD and AutoCAD LT for Windows)
* Command Macro Editor (AutoCAD for Windows only; not supported in AutoCAD-based toolsets or AutoCAD LT)
* Customize dialog box (AutoCAD for Mac OS only)

## Command Macro String Basics

A command macro string is defined as a series of commands and expected options and values with a specialized syntax, but is
similar to the input you enter at the AutoCAD Command prompt. When you interact with the program's user interface, such as
a clicking button on the ribbon or an item on a shortcut menu, you are executing a command macro string. The syntax of a command
macro can be as simple as a single command name (such as
CIRCLE) or more complex with the inclusion of special characters (such as
^C^C\_.circle \1). .

The following lists the most used special characters in command macro strings:

* *^C* – Represents pressing the Esc key.
* *. (period)* – Instructs AutoCAD to use the standard definition of a command. The behavior of commands can be altered with programming
  languages like AutoLISP and ObjectARX.
* *\_ (underscore)* – Lets AutoCAD know the command or option provided is the global/English name. This is required for macros to work correctly
  across multiple languages.
* *; (semi-colon)* – Represents pressing the Enter key.
* *\ (backslash)* – Represents a pause for user input; allows the user to enter a value, specify a point, or select objects.
* *(space)* – Represents pressing the Spacebar key.

NOTE:AutoLISP is not available in AutoCAD LT for Mac OS, and ObjectARX is not available in AutoCAD LT for Windows or Mac OS.

Here is what it looks like to start the CIRCLE command and draw a circle with a radius of 5 at the AutoCAD Command prompt
and how that same input looks as a command macro string:

| Command Prompt Sequence | Macro String Syntax Equivalent |
| ``` Command: CIRCLE Specify center point for circle or [3P/2P/Ttr (tan tan radius)]: Specify radius of circle or [Diameter] <2.5000>: 5 ``` | ``` CIRCLE; \ 5; ``` |

Here is what the final command macro string might look:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](../images/GUID-306ADDE0-0A5B-48AD-8794-42B456765F86-low.png) | | Item | Syntax | Description | | 1 | ^C^C | ^C^C means to press Esc twice before executing the macro | | 2 | .\_CIRCLE; | Starts the CIRCLE command, independent of the current AutoCAD language pack | | 3 | \ | Prompts for the center point at which the circle is to be drawn | | 4 | 5; | Specifies the radius of the circle and exits the CIRCLE command | |

The previous macro string could have also be written as the following without the semi-colons since a space in a macro is
like pressing the Spacebar at the AutoCAD Command prompt:

```
^C^C_.circle \5
```

NOTE:The use of semi-colons in a macro string makes it easier to read and know when an Enter is supposed to occur since a space
can indicate an actual space in the input provided to the previous command or system variable.

Here is another example of using the
MOCORO command to copy and then rotate those copied objects at the AutoCAD Command prompt and how the command sequence would look
as a command macro string:

| Command Prompt Sequence | Macro String Syntax Equivalent |
| ``` Command: MOCORO Select objects: Specify opposite corner: Select objects: Base point: [Move/Copy/Rotate/Scale/Base/Undo]<eXit>: C Second point of displacement/Undo/<eXit>: Second point of displacement/Undo/<eXit>:  [Move/Copy/Rotate/Scale/Base/Undo]<eXit>: R Second Point or Rotation angle: [Move/Copy/Rotate/Scale/Base/Undo]<eXit>: ``` | ``` MOCORO; \ \ ; \ C; \ ;  R; \ ; ``` |

Here is what the final command macro string might look:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](../images/GUID-F70398FA-E894-4040-BE59-FE3657330C49-low.png) | | Item | Syntax | Description | | 1 | ^C^C | ^C^C means to press Esc twice before executing the macro | | 2 | .\_MOCORO; | Starts the MOCORO command, independent of the current AutoCAD language pack | | 3 | \\; | Prompts for object selection; two backslashes here allow for specifying two points for window or crossing selection | | 4 | \ | Prompts for the base point that should be used to copy the selected objects | | 5 | \_C; | Uses the Copy option | | 6 | \; | Prompts for the second point of displacement | | 7 | \_R; | Uses the Rotate option | | 8 | \ | Prompts for the angle of rotation | | 9 | ; | Exits the MOCORO command | |

## Cancel the Active Command

When a button in the user interface is clicked, the macro assigned to it is executed in the current context of the program.
This means that the macro will attempt to provide responses to the current prompt. If you want to make sure that no command
is currently active when the macro is executed, prefix your macro with the
^C command sequence. Although a single
^C cancels most commands,
^C^C is required to return to the command prompt from a dimensioning command and
^C^C^C is required based on the current option of the -LAYER command.
^C^C handles canceling out of most command sequences and is the recommended sequence to use.

## Use Standard Commands in Macros

Commands that are part of AutoCAD or AutoCAD-based products should be prefixed with a period character (.). The period character
allows the standard command to be used even if it has been undefined with the UNDEFINE command. This precaution makes the
macro predicable when it is used on other computers that share the same customization (CUI/CUIx) file.

NOTE:Starting with AutoCAD LT 2024, commands can be undefined.

## Verify Macro Characters

Every character in a macro has a significant meaning, even a blank space. A space is interpreted as a press of the Spacebar,
which can result in a space character in the input provided or as if you pressed the Enter key. The result is the same as
if you were using the command or system variable at the Command prompt.

NOTE:When you place a space at the end of the macro, it is interpreted as if you had pressed Enter to complete the command.

## International Support for Macros

When you first create a macro, you commonly create it using the command names and option values in the language of the product
which you are familiar. Each command and option has a local and global name that allows your macros to be used by other languages
of the product. Non-English support does not require much additional work on your part, you precede each command or option
with the underscore character (\_). The underscore character signals to the program that the command name or option value should
be translated into the local language of the product before it is executed.

## Use Single Object Selection Mode

Single Object Selection mode cancels the normal repetition of the Select Objects prompt in editing commands. After you select
one object and respond to any other prompts, the command ends.

Consider the macro in the following example:

```
^C^C._erase single
```

This macro terminates the current command and starts the ERASE command in Single Object Selection mode. After the macro is
started, you can either select a single object, or click a blank area in the drawing and specify window/crossing selection.
Any objects selected using these methods are erased.

## Repeat Commands in Macros

Once you have created a macro, you might want to repeat it several times before moving to a different command. In a macro,
use a leading asterisk (\*) to indicate that the command in a macro should be repeated until you press Esc or start another
macro that begins with
^C.

The macros in the following examples repeat the commands:

```
*^C^C._move Single
*^C^C._copy Single
*^C^C._erase Single
*^C^C._stretch Single Crossing
*^C^C._rotate Single
*^C^C._scale Single
```

NOTE:You cannot use this feature to choose options, or for macros in image tile menus.

## Terminate Macros

Some macros require special terminators. For example, the TEXT command requires you to press Enter rather than Spacebar to
terminate the command and some commands require more than one press of the Spacebar or Enter to complete.

Two special conventions resolve these problems.

* A semicolon (;) in a macro is equivalent to pressing Enter.
* If a line ends with a control character, a backslash (\) or a semicolon (;), a blank space is not added after it.

Compare the following macros:

```
ucs
ucs ;
```

The first example starts the UCS command and, because the line ends with a space, the pressing of the Spacebar is simulated.
The following prompt is displayed:

Specify origin of UCS or [Face/NAmed/OBject/Previous/View/World/X/Y/Z/ZAxis] <World>:

The second example starts the UCS command, simulates the pressing of the Spacebar, and then a press of the Enter is simulated
which accepts the default value (World).

## Suppress Echoes and Prompts in Macros

Characters in a macro appear at the Command prompt as though you had typed the characters from the keyboard. This display
duplication is called
*echoing*. You can suppress macro echoing with the MENUECHO system variable. If echoes and prompts from item input are turned on, a
^P in front of the macro will temporarily turn them off. You can also use
^Q in a macro to suppresses the display of all prompts and input from the Command Line history.

#### Topics in this section

* [About Special Control Characters in Command Macros](About-Special-Control-Characters-in-Command-Macros.md)

  Command macro strings support the use of special characters that are equivalent to pressing a key on the keyboard or for pausing
  for user input.
* [About Pausing Macros for User Input](About-Pausing-Macros-for-User-Input.md)

  Macros can be paused using a backslash (\) at the point where you want the user to provide some form of input.
* [About Using Conditional Expressions in Macros](About-Using-Conditional-Expressions-in-Macros.md)

  You can add conditional expressions to a macro by using a command that introduces macro expressions written in DIESEL (Direct
  Interpretively Evaluated String Expression Language).
* [About Using AutoLISP in Macros](About-Using-AutoLISP-in-Macros.md)

  Creating commands that use AutoLISP is a more advanced way to use the program's customization feature.
* [About Controlling the Display of Menu Items](About-Controlling-the-Display-of-Menu-Items.md)

  The way a menu item is displayed indicates its availability in the program.

#### Related Tasks

* [To Create a Custom Command](To-Create-a-Custom-Command.md)
* [To Edit a Command](To-Edit-a-Command.md)

#### Related References

* [Commands for Customization](Commands-for-Customization-2.md)

#### Related Concepts

* [About Special Control Characters in Command Macros](About-Special-Control-Characters-in-Command-Macros.md)
* [About Pausing Macros for User Input](About-Pausing-Macros-for-User-Input.md)
* [About Using Conditional Expressions in Macros](About-Using-Conditional-Expressions-in-Macros.md)
* [About Using AutoLISP in Macros](About-Using-AutoLISP-in-Macros.md)
* [About Command Customization](About-Command-Customization.md)
* [About Customization](About-Customization.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*