# About Accessing and Assigning Help to a Command (AutoLISP)

The help and setfunhelp functions provide access to the product and your custom help files.

The Help facility supports:

* HyperText Markup Language (.htm/.html) files - Windows and Mac OS
* Microsoft Compiled HTML Help (.chm) files - Windows only
* Windows Help (.hlp) files - Windows only

You can use the help function to display a Help file. Depending on the Help file's extension, the help function displays the
appropriate viewer for the specified file. The following example code displays the LINE commands topic in the default AutoCAD
Help file.

```
(help "" "line")
```

You can create a custom Help file that provides information about your applications and display it with the help function.
The following example code displays a custom help file named *abcindoorcad.chm*:

```
(defun C:ABCINDOORCADHELP ()
  (help "abcindoorcad.chm")
 (princ)
)
```

The setfunhelp function provides contextual help for user-defined commands. After the definition of a new command defined with AutoLISP,
add a call to setfunhelp and associate a specific help topic to the command. The following example assigns the help topic “MyCommand” in the *abcindoorcad.chm* file to the user-defined MYCOMMAND command:

```
(defun C:MYCOMMAND ( )
  ..
  Command definition
  ..
)
(setfunhelp "c:mycommand" "abcindoorcad.chm" "mycommand")
```

#### Related Concepts

* [About Defining Commands (AutoLISP)](About-Defining-Commands-AutoLISP.md)
* [About Defining a Function (AutoLISP)](About-Defining-a-Function-AutoLISP.md)
* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*