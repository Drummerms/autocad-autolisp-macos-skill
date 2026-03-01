# About Catching Errors and Continuing Program Execution (AutoLISP)

Programs should intercept and attempt to process errors instead of allowing control to pass to \*error\* when possible.

The vl-catch-all-apply function is designed to invoke any function, return a value from the function, and trap any error that may occur. The function
requires two arguments:

* A symbol identifying a function or lambda expression
* A list of arguments to be passed to the called function

The importance of vl-catch-all-apply is the ability to catch errors and allow your program to continue execution. The following example uses vl-catch-all-apply to divide two numbers:

```
(setq catchit (vl-catch-all-apply '/ '(50 5)))
10
```

The result from this example is the same as if you had used apply to perform the division or just used  */*  to divide the provided numbers.

The following example uses vl-catch-all-apply to divide two numbers, and one of the numbers being zero:

```
(setq catchit (vl-catch-all-apply '/ '(5 0)))
#<%catch-all-apply-error%>
```

The result from this example returns a VL-CATCH-ALL-APPLY-ERROR object which can be interpreted using vl-catch-all-error-message. You can use the type function to make sure you are working with an error object before calling vl-catch-all-error-message.

The following example checks for an error object and returns the error message:

```
(if (vl-catch-all-error-p catchit)
  (vl-catch-all-error-message catchit)
)
"divide by zero"
```

#### Topics in this section

* [To catch errors with vl-catch-all-apply (AutoLISP)](To-catch-errors-with-vl-catch-all-apply-AutoLISP.md)

  Errors caused by AutoLISP functions can result in a program ending unexpectedly, make sure to handle all known situations
  that could cause an error.

#### Related Tasks

* [To catch errors with vl-catch-all-apply (AutoLISP)](To-catch-errors-with-vl-catch-all-apply-AutoLISP.md)

#### Related Concepts

* [About Error Handling (AutoLISP)](About-Error-Handling-AutoLISP.md)
* [About Using the \*error\* Function (AutoLISP)](About-Using-the-error-Function-AutoLISP.md)
* [About Exiting a Function Quietly (AutoLISP)](About-Exiting-a-Function-Quietly-AutoLISP.md)
* [Error Codes Reference (AutoLISP)](Error-Codes-Reference-AutoLISP.md)
* [Error-Handling Functions Reference (AutoLISP)](Error-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*