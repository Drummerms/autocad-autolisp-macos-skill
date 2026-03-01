# About Special Forms (AutoLISP)

Certain AutoLISP functions are considered special forms because they evaluate arguments in a different manner than most AutoLISP
function calls.

A typical function evaluates all arguments passed to it before acting on those arguments. Special forms either do not evaluate
all their arguments, or only evaluate some arguments under certain conditions.

The following AutoLISP functions are considered special forms:

* AND
* COMMAND
* COND
* DEFUN
* DEFUN-Q
* FOREACH
* FUNCTION
* IF
* LAMBDA
* OR
* PROGN
* QUOTE
* REPEAT
* SETQ
* TRACE
* UNTRACE
* VLAX-FOR
* WHILE

NOTE:The
VLAX-FOR function is not available on Mac OS and Web.

#### Related Concepts

* [About Defining a Function (AutoLISP)](About-Defining-a-Function-AutoLISP.md)
* [About Variables (AutoLISP)](About-Variables-AutoLISP.md)
* [Equality and Conditional Functions Reference (AutoLISP)](Equality-and-Conditional-Functions-Reference-AutoLISP.md)
* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)
* [Query and Command Functions Reference (AutoLISP)](Query-and-Command-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*