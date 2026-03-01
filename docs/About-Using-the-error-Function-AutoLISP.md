# About Using the \*error\* Function (AutoLISP)

The \*error\* function can ensure that AutoCAD returns to a particular state after an error occurs.

This user-definable function can assess the error condition and return an appropriate message to the user. If AutoCAD encounters
an error during evaluation, it prints a message in the following form:

Error: text

In this message, text describes the error. However, if the \*error\* function is defined (that is, if it is not nil), AutoLISP executes \*error\* instead of printing the message. The \*error\* function receives text as its single argument. If \*error\* is not defined or is nil, AutoLISP evaluation stops and displays a traceback of the calling function and its callers. It is beneficial to leave this
error handler in effect while you debug your program.

A code for the last error is saved in the system variable ERRNO, where you can retrieve it using the getvar function.

Before defining your own \*error\* function, save the current contents of \*error\* so that the previous error handler can be restored upon exit. When an error condition exists, AutoCAD calls the currently
defined \*error\* function and passes it one argument, which is a text string describing the nature of the error. Your \*error\* function should be designed to exit quietly after an Esc (cancel) or an exit function call. The standard way to accomplish this is to include the following statements in your error-handling routine.

```
(if
  (or
    (= msg "Function cancelled")
    (= msg "quit / exit abort")
  )
 (princ)
 (princ (strcat "\
Error: " msg))
)
```

This code evaluates the error message passed to it and ensures that the user is informed of the nature of the error. If the
user cancels the command or function while it is running, nothing is returned from this code. Likewise, if an error condition
is programmed into your code and the exit function is called, nothing is returned. It is presumed you have already explained the nature of the error by displaying
a message. Remember to include a terminating call to princ if you do not want a return value printed at the end of the \*error\* function.

The main caveat about error-handling routines is they are normal AutoLISP functions that can be canceled by the user. Keep
them as short and as fast as possible. This will increase the likelihood that an entire routine will execute if called.

You can also warn the user about error conditions by displaying an alert box, which is a small dialog box containing a message
supplied by your program and a single OK button. To display an alert box, call the alert function.

The following call to alert displays an alert box with the message File note found:

```
(alert "File not found")
```

#### Related Concepts

* [About Error Handling (AutoLISP)](About-Error-Handling-AutoLISP.md)
* [About Catching Errors and Continuing Program Execution (AutoLISP)](About-Catching-Errors-and-Continuing-Program-Execution-AutoLISP.md)
* [About Exiting a Function Quietly (AutoLISP)](About-Exiting-a-Function-Quietly-AutoLISP.md)
* [Error-Handling Functions Reference (AutoLISP)](Error-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*