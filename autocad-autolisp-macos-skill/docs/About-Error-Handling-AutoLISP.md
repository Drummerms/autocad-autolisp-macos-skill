# About Error Handling (AutoLISP)

The AutoLISP language provides several functions for handling errors.

The proper handling of errors allows your program to exit gracefully and with an expected result. Using the error handling
functions of the AutoLISP programming language allows you to do the following:

* Provide information to users when an error occurs during the execution of a program.
* Restore the AutoCAD environment to a known state.
* Intercept errors and continue program execution.

The following functions are useful to handle errors encountered by your programs:

* \*error\* - A user-definable error-handling function.
* \*pop-error-mode\* - Error-handling function that ends the previous call to \*push-error-using-command\* or \*push-error-using-stack\*.
* \*push-error-using-command\* - Error-handling function that indicates the use of the command function within a custom \*error\* handler.
* \*push-error-using-stack\* - Error-handling function that indicates the use of variables from the AutoLISP stack within a custom \*error\* handler.
* vl-catch-all-apply - Passes a list of arguments to a specified function and traps any exceptions.

If your program contains more than one error in the same expression, you cannot depend on the order in which AutoLISP detects
the errors. For example, the inters function requires several arguments, each of which must be either a 2D or 3D point list. A call to inters like the following:

```
(inters 'a)
```

Two errors are encountered: too few arguments and invalid argument type. You will receive either of the following error messages:

```
; *** ERROR: too few arguments
; *** ERROR: bad argument type: 2D/3D point
```

Your program should be designed to handle either error.

NOTE:AutoLISP evaluates all arguments before checking the argument types. In earlier releases of AutoCAD, AutoLISP evaluated and
checked the type of each argument sequentially. To see the difference, look at the following code examples:

```
(defun foo ()
  (print "Evaluating foo")
  '(1 2))

(defun bar ()
  (print "Evaluating bar")
  'b)

(defun baz ()
  (print "Evaluating baz")
  'c)
```

Observe how an expression using the inters function is evaluated in AutoCAD:

Command: *(inters (foo) (bar) (baz))*

"Evaluating foo"

"Evaluating bar"

"Evaluating baz"

; \*\*\* ERROR: too few arguments

Each argument was evaluated successfully before AutoLISP passed the results to inters and discovered that too few arguments were specified.

In AutoCAD R14 and earlier, the same expression evaluated as follows:

Command: *(inters (foo) (bar) (baz))*

"Evaluating foo"

"Evaluating bar" error: bad argument type

AutoLISP evaluated (foo), then passed the result to inters. Since the result was a valid 2D point list, AutoLISP proceeds to evaluate (bar), where it determines that the evaluated result is a string, an invalid argument type for inters.

#### Topics in this section

* [About Using the \*error\* Function (AutoLISP)](About-Using-the-error-Function-AutoLISP.md)

  The \*error\* function can ensure that AutoCAD returns to a particular state after an error occurs.
* [About Catching Errors and Continuing Program Execution (AutoLISP)](About-Catching-Errors-and-Continuing-Program-Execution-AutoLISP.md)

  Programs should intercept and attempt to process errors instead of allowing control to pass to \*error\* when possible.

#### Related Concepts

* [About Using the \*error\* Function (AutoLISP)](About-Using-the-error-Function-AutoLISP.md)
* [About Catching Errors and Continuing Program Execution (AutoLISP)](About-Catching-Errors-and-Continuing-Program-Execution-AutoLISP.md)
* [About Exiting a Function Quietly (AutoLISP)](About-Exiting-a-Function-Quietly-AutoLISP.md)
* [About Displaying Messages (AutoLISP)](About-Displaying-Messages-AutoLISP.md)
* [Error Codes Reference (AutoLISP)](Error-Codes-Reference-AutoLISP.md)
* [Error-Handling Functions Reference (AutoLISP)](Error-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*