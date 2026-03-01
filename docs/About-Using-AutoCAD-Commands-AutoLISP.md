# About Using AutoCAD Commands (AutoLISP)

AutoLISP can execute a built-in AutoCAD command or one that is defined in a loaded ObjectARX or Managed .NET application.

NOTE:ObjectARX is not supported in AutoCAD LT, and Managed .NET is not supported in AutoCAD LT for Windows or on Mac OS.

The
command and
command-s functions allow you to start and pass values to an AutoCAD command. The
command and
command-s functions have a variable-length argument list. The first argument of these functions must be the command you want to execute.
All other arguments must correspond to the types and values expected by that command's prompt sequence; these may be strings,
real values, integers, points, entity names, or selection set names. Data such as angles, distances, and points can be passed
either as strings or as the values themselves (as integer or real values, or as point lists). An empty string ("") is equivalent to pressing the Spacebar or Enter on the keyboard.

The
command-s function is faster and more efficient than the
command function, but the command being executed within the
command-s function must be completed within the same statement. This means that an argument must be provided for each of the command’s
prompts, and that it cannot execute any more AutoLISP statements until the function has completed. Unlike the
command-s function, you can use AutoLISP functions within the
command function and the command that is being executed does not need to be completed to continue execution of the program.

There are some restrictions on the commands that you can use with the
command and
command-s functions.

The following code fragment shows representative calls to
command.

```
(defun c:CircC ()
  (command "._circle" "0,0" "3,3")
  (command "._thickness" 1)
  (command "._circle" PAUSE PAUSE)
 (princ)
)
```

When the
CircC command is loaded and executed at the AutoCAD Command prompt, the following actions occur:

1. The first call to
   command passes points to the CIRCLE command as strings (draws a circle centered at 0.0,0.0 and passes through 3.0,3.0).
2. The second call to command passes an integer to the THICKNESS system variable (changes the current thickness to 1.0).
3. The last call to command prompts the user for a center point and then the radius of the circle.

The following code fragment shows representative calls to
command-s.

```
(defun c:CircCS ( / p1 rad)
  (command-s "._circle" "0,0" "3,3")
  (command-s "._thickness" 1)
  (setq p1 (getpoint "\
Enter a center point: "))
  (setq rad (getdist p1 "\
Enter a radius: "))
  (command-s "._circle" p1 rad)
 (princ)
)
```

The
CircCS command is similar to
CircC except it prompts the user for a center point and radius before making the last call to the
command-s function. With the
command-s function, you should avoid the use of the PAUSE token.

#### Topics in this section

* [About Foreign Language or International Support (AutoLISP)](About-Foreign-Language-or-International-Support-AutoLISP.md)

  AutoLISP programs can be used in an AutoCAD release that supports a language other than the original language the program
  was developed for.
* [About Pausing for User Input During an AutoCAD Command (AutoLISP)](About-Pausing-for-User-Input-During-an-AutoCAD-Command-AutoLISP.md)

  The PAUSE symbol can be used in the command function to interrupt the execution of an AutoCAD command and have the user provide
  input.
* [About Passing Pick Points to AutoCAD Commands (AutoLISP)](About-Passing-Pick-Points-to-AutoCAD-Commands-AutoLISP.md)

  Some AutoCAD commands (such as TRIM, EXTEND, and FILLET) require the user to specify a pick point as well as the object itself.
* [About Undoing Changes Made by a Routine (AutoLISP)](About-Undoing-Changes-Made-by-a-Routine-AutoLISP.md)

  Grouping multiple AutoLISP statements together under a single UNDO group allows you to rollback all the actions performed
  by using either the AutoCAD U or UNDO commands.

#### Related Concepts

* [About Defining Commands (AutoLISP)](About-Defining-Commands-AutoLISP.md)
* [About Pausing for User Input During an AutoCAD Command (AutoLISP)](About-Pausing-for-User-Input-During-an-AutoCAD-Command-AutoLISP.md)
* [About Passing Pick Points to AutoCAD Commands (AutoLISP)](About-Passing-Pick-Points-to-AutoCAD-Commands-AutoLISP.md)
* [About Variables (AutoLISP)](About-Variables-AutoLISP.md)
* [About Defining a Function (AutoLISP)](About-Defining-a-Function-AutoLISP.md)
* [About Undoing Changes Made by a Routine (AutoLISP)](About-Undoing-Changes-Made-by-a-Routine-AutoLISP.md)
* [About Foreign Language or International Support (AutoLISP)](About-Foreign-Language-or-International-Support-AutoLISP.md)
* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*