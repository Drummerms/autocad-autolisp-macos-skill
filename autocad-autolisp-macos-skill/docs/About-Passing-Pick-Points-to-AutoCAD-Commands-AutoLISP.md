# About Passing Pick Points to AutoCAD Commands (AutoLISP)

Some AutoCAD commands (such as TRIM, EXTEND, and FILLET) require the user to specify a pick point as well as the object itself.

Object and point data can be passed to the command and command-s functions without the use of a PAUSE, but requires you to first store the values as variables. Points can be passed as strings within the command and command-s functions, or can be defined outside the function and passed as variables, as shown in the following example.

The following example code demonstrates one method of passing an entity name and a pick point to the command function.

```
(command "._circle" "5,5" "2")    ;Draws a circle
(command "._line" "3,5" "7,5" "") ;Draws a line
(setq el (entlast))               ;Gets the last entity
                                  ;  added to the drawing
(setq pt '(5 7))                  ;Sets the trim point
(command "._trim" el "" pt "")    ;Performs the trim
```

If AutoCAD is at an idle Command prompt when these statements are called, AutoCAD performs the following actions:

1. Draws a circle centered at (5,5) with a radius of 2.
2. Draws a line from (3,5) to (7,5).
3. Creates a variable el that is the name of the last object added to the database.
4. Creates a pt variable that is a point on the circle. (This point selects the portion of the circle to be trimmed.)
5. Performs the TRIM command by selecting the el object (the line) and by selecting the point specified by pt.

#### Related Concepts

* [About Accessing and Requesting User Input (AutoLISP)](About-Accessing-and-Requesting-User-Input-AutoLISP.md)
* [About Controlling User-Input Function Conditions (AutoLISP)](About-Controlling-User-Input-Function-Conditions-AutoLISP.md)
* [About Using AutoCAD Commands (AutoLISP)](About-Using-AutoCAD-Commands-AutoLISP.md)
* [About Pausing for User Input During an AutoCAD Command (AutoLISP)](About-Pausing-for-User-Input-During-an-AutoCAD-Command-AutoLISP.md)
* [About Arbitrary Keyboard Input (AutoLISP)](About-Arbitrary-Keyboard-Input-AutoLISP.md)
* [User Input Functions Reference (AutoLISP)](User-Input-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*