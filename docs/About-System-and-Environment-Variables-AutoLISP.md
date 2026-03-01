# About System and Environment Variables (AutoLISP)

AutoLISP applications can inspect and change the value of AutoCAD system variables with the getvar and setvar functions.

These functions use a string to specify the variable name. The setvar function requires a second argument that specifies the new value the system variable. AutoCAD system variables accept and
return various data types: integers, reals, strings, 2D points, and 3D points.

Values supplied as arguments to setvar must be of the expected type. If an invalid type is supplied, an AutoLISP error is generated.

The following example code demonstrates how to get and set the value of the AutoCAD FILLETRAD system variable:

```
(if (< (getvar "filletrad") 1)
  (setvar "filletrad" 1)
)
```

Additional functions, getenv and setenv, provide AutoLISP routines with access to the currently defined operating system environment variables. Unlike system variable
names, environment variable names are case specific. For example, MaxHatch and MAXHATCH are not the same. When using the setenv function, you always supply the new value as a string even if it might be a numeric value.

The following example code demonstrates how to set the MaxHatch environment variable:

```
(setq curMaxHatch (getenv "MaxHatch"))
(prompt (strcat "\
Current value of MaxHatch: " curMaxHatch))
(setenv "MaxHatch" "50000")
(prompt (strcat "\
New value of MaxHatch: " (getenv "MaxHatch")))
(setenv "MaxHatch" curMaxHatch)
```

#### Related Concepts

* [About Configuration Files (AutoLISP)](About-Configuration-Files-AutoLISP.md)
* [About Local and Global Variables (AutoLISP)](About-Local-and-Global-Variables-AutoLISP.md)
* [Windows Registry and Property List File Functions Reference (AutoLISP)](Windows-Registry-and-Property-List-File-Functions-Reference-AutoLISP.md)
* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*