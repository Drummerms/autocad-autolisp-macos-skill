# About Pausing for User Input During an AutoCAD Command (AutoLISP)

The PAUSE symbol can be used in the command function to interrupt the execution of an AutoCAD command and have the user provide
input.

If an AutoCAD command is in progress and the predefined symbol PAUSE is encountered as an argument to command, the command is suspended to allow direct user input (usually point selection or dragging). This is similar to the backslash
pause mechanism provided for menus.

The PAUSE symbol is defined as a string consisting of a single backslash. When you use a backslash ( *\* ) in a string, you must precede it by another backslash ( *\\* ).

NOTE:You can use two backslashes ( *\\* ) instead of the PAUSE symbol. However, it is recommended that you always use the PAUSE symbol rather than the explicit use of two backslashes. Also, if the command function is invoked from a menu item, the backslash
suspends the reading of the menu item, which results in partial evaluation of the AutoLISP expression.

For example, the following code begins the CIRCLE command, sets the center point at (5,5), and then pauses to let the user
drag the circle's radius. When the user specifies the desired point (or types in the desired radius), the function resumes,
and a line is drawn from (5,5) to (7,5), as follows:

```
(command "._circle" "5,5" pause "._line" "5,5" "7,5" "")
```

If PAUSE is encountered when a command is expecting input of a text string or an attribute value, AutoCAD pauses for input
only if the AutoCAD TEXTEVAL system variable is nonzero. Otherwise, AutoCAD does not pause for user input but uses the value
of the PAUSE symbol (a single backslash).

When the command function pauses for user input, the function is considered active, so the user cannot enter another AutoLISP
expression to be evaluated.

The following example code uses the PAUSE symbol to allow the user to specify the block’s insertion point. The layer NEW\_LAY and block MY\_BLOCK must exist in the drawing
prior to testing this code.

```
(setq blk "MY_BLOCK")
(setq old_lay (getvar "clayer"))
(command "._-layer" "set" "NEW_LAY" "")
(command "._-insert" blk PAUSE "" "" PAUSE)
(command "._-layer" "set" old_lay "")
```

The preceding code fragment sets the current layer to NEW\_LAY, pauses for an insertion point for the block MY\_BLOCK (which
is inserted with *X* and *Y* scale factors of 1), and pauses again for a rotation angle. The current layer is then reset to the previous layer.

If the command function specifies a PAUSE with the AutoCAD SELECT command and the AutoCAD PICKFIRST system variable set is active, the SELECT command obtains the objects
selected before the command is executed and does not pause for the user to select objects.

NOTE:The Radius and Diameter subcommands of the AutoCAD DIM command issue additional prompts in some situations. This can cause
a failure of AutoLISP programs written prior to Release 11 that use these subcommands.

## Using Transparent Commands

If you issue a transparent command while a command function is suspended, the command function remains suspended. Therefore, users can 'ZOOM and 'PAN while a command is at a pause. The pause remains in effect
until AutoCAD gets valid input, and transparent command ends.

The following shows the results of using the ZOOM command transparently when the command function allows the user to provide
a radius for the circle:

Command: *(command ".\_circle" "5,5" PAUSE ".\_line" "5,5" "7,5" "")*

circle

Specify center point for circle or [3P/2P/Ttr (tan tan radius)]: 5,5

Specify radius of circle or [Diameter]: *'zoom*

>>Specify corner of window, enter a scale factor (nX or nXP), or [All/Center/Dynamic/Extents/Previous/Scale/Window/Object]
<real time>:

>>Press ESC or ENTER to exit, or right-click to display shortcut menu.

Resuming CIRCLE command.

Specify radius of circle or [Diameter]:

Command: line

Specify first point: 5,5

Specify next point or [Undo]: 7,5

Specify next point or [Undo]:

Command: nil

## Accepting Menu Input

Menu input is not suspended when PAUSE is used by the command function. If a menu item is active when the command function pauses for input, that input request can be satisfied by the menu. If you want the menu item to be suspended as
well, you must provide a backslash in the menu item. When valid input is provided, both the command function and the menu item resume.

#### Related Concepts

* [About Accessing and Requesting User Input (AutoLISP)](About-Accessing-and-Requesting-User-Input-AutoLISP.md)
* [About Passing Pick Points to AutoCAD Commands (AutoLISP)](About-Passing-Pick-Points-to-AutoCAD-Commands-AutoLISP.md)
* [About Controlling User-Input Function Conditions (AutoLISP)](About-Controlling-User-Input-Function-Conditions-AutoLISP.md)
* [About Arbitrary Keyboard Input (AutoLISP)](About-Arbitrary-Keyboard-Input-AutoLISP.md)
* [About Using AutoCAD Commands (AutoLISP)](About-Using-AutoCAD-Commands-AutoLISP.md)
* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*