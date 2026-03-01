# About Variables (AutoLISP)

Variables are used to store a value or list of values in memory.

The data type of a variable is determined when a value is assigned. Variables retain their value until a new value is assigned
or the variable goes out of scope. The scope of a variable can either be global or local. Global variables are accessible
by any AutoLISP program that is loaded into a drawing, while local variables are only available within a specific function
or command. You use the AutoLISP
setq function to assign values to variables.

The syntax of the
setq function is as follows:

```
(setq variable_name1 value1 [variable_name2 value2 ...])
```

The
setq function assigns the specified value to the variable name given, and returns the last assigned value as its function result.
The following example creates two variables:
val and
abc.
val is assigned the value of 3, while
abc is assigned the value of 3.875.

```
(setq val 3 abc 3.875)
3.875
```

The following example creates a variable named
layr and assigns it the value of “EXTERIOR-WALLS”.

```
(setq layr "EXTERIOR-WALLS")
"EXTERIOR-WALLS"
```

## Using a Variable with a Function

Once a value is assigned to a variable, it can be used in an expression as the value for an argument of a function. The following
uses two of the previously created variables in a few AutoLISP expressions to create a layer and draw a line with a specific
length at 0 degrees.

```
(command "_.-layer" "_make" layr "")
(command "_.line" PAUSE (strcat "@" (itoa val) "<0") "")
```

## Checking the Value of a Variable

You can use the following methods to determine the current value of a variable:

* At the AutoCAD Command prompt, add an
   *!*  (exclamation point) in front of the variable and press Enter.

  Command:
  *(setq val 3 abc 3.875)*

  3.875

  Command:
  *!val*

  3
* At the Visual LISP Console Window prompt, enter the name of the variable and press Enter. (AutoCAD for Windows only; not available
  in AutoCAD LT for Windows).

  \_$
  *(setq val 3 abc 3.875)*

  3.875

  \_$
  *val*

  3
* At the AutoCAD Command prompt or Visual LISP Console Window prompt (AutoCAD for Windows only; not available in AutoCAD LT
  for Windows), or in an AutoLISP program, create an expression that uses the
  princ function and pass it the name of the variable. You should also follow the first expression with a second expression that
  uses the
  princ function, but do not pass it an argument to suppress the return value of the first
  princ function.

  Command:
  *(setq val 3 abc 3.875)*

  3.875

  Command:
  *(princ val)(princ)*

  3

  NOTE:If you do not add the second expression in the above example, a value of 33 appears to be returned. The first 3 is the desired
  output of the
  princ function, while the second 3 is the result of the value returned by the
  princ function. Remember that AutoLISP returns the value of the last function evaluated. In the previous example, no value is returned
  by the second
  princ because no argument was provided.

#### Topics in this section

* [About Nil Variables (AutoLISP)](About-Nil-Variables-AutoLISP.md)

  A variable that has not been assigned a value has a default value of nil.
* [About Predefined Variables (AutoLISP)](About-Predefined-Variables-AutoLISP.md)

  AutoLISP has several predefined variables that can be used with your custom functions and commands.

#### Related Tasks

* [To declare local variables (AutoLISP)](To-declare-local-variables-AutoLISP.md)

#### Related Concepts

* [About Local and Global Variables (AutoLISP)](About-Local-and-Global-Variables-AutoLISP.md)
* [About Symbols and Variables (AutoLISP)](About-Symbols-and-Variables-AutoLISP.md)
* [About Predefined Variables (AutoLISP)](About-Predefined-Variables-AutoLISP.md)
* [About Nil Variables (AutoLISP)](About-Nil-Variables-AutoLISP.md)
* [About Referencing Variables in Document Namespaces (AutoLISP)](About-Referencing-Variables-in-Document-Namespaces-AutoLISP.md)
* [About Sharing Data Between Namespaces (AutoLISP)](About-Sharing-Data-Between-Namespaces-AutoLISP.md)
* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*