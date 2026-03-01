# About Defining a Function (AutoLISP)

You can define your own functions.

Once defined, these functions can be used at the AutoCAD Command prompt, the Visual LISP Console prompt, or within other
AutoLISP expressions, just as you use the standard functions.

NOTE:The Visual LISP IDE is not available in AutoCAD LT for Windows and on Mac OS.

You can also create your own commands, because commands are just a special type of function. The
defun function combines a multiple expressions into a function or command. This function requires at least three arguments:

* Name of the function (symbol name)
* Argument list (a list of arguments and local variables used by the function). The argument list can be nil or an empty list
  ().
* AutoLISP expressions to execute with the function or command. There must be at least one expression in a function definition.

```
(defun symbol_name ( arguments / local_variables )
  expressions
)
```

The following example code defines a simple function that accepts no arguments and displays the message “bye” at the AutoCAD
Command prompt. Note that the argument list is defined as an empty list (()):

```
(defun DONE ( ) (prompt "\
bye! "))
DONE
```

Once the
DONE function is defined, you can use it as you would any other function. For example, the following code prints a message, then
says “bye” at the AutoCAD Command prompt:

```
(prompt "The value is 127.") (DONE) (princ)
The value is 127
bye!
```

Note how the previous example invokes the
princ function without an argument to suppress an ending nil and achieves a quiet exit.

Functions that accept no arguments may seem useless. However, you might use this type of function to query the state of certain
system variables or conditions and to return a value that indicates those values.

#### Topics in this section

* [About Compatibility of Defun with Earlier Releases of AutoCAD (AutoLISP)](About-Compatibility-of-Defun-with-Earlier-Releases-of-AutoCAD-AutoLISP.md)

  The internal implementation of defun changed in AutoCAD 2000.

#### Related Concepts

* [About Local and Global Variables (AutoLISP)](About-Local-and-Global-Variables-AutoLISP.md)
* [About Expressions (AutoLISP)](About-Expressions-AutoLISP.md)
* [About Function Syntax (AutoLISP)](About-Function-Syntax-AutoLISP.md)
* [About Symbols and Variables (AutoLISP)](About-Symbols-and-Variables-AutoLISP.md)
* [About Functions with Arguments (AutoLISP)](About-Functions-with-Arguments-AutoLISP.md)
* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*