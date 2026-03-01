# To catch errors with vl-catch-all-apply (AutoLISP)

Errors caused by AutoLISP functions can result in a program ending unexpectedly, make sure to handle all known situations
that could cause an error.

1. Wrap each function that could throw an error with
   vl-catch-all-apply.
2. Evaluate the value returned by
   vl-catch-all-apply with
   vl-catch-all-error-p to see if an error object or a value was returned.
3. Use
   vl-catch-all-error-message to get the message associated with the returned error object.
4. Load, run, and test the code.

## Example

The following defines a function named catch-me-if-you-can. This function accepts two number arguments and uses
vl-catch-all-apply to divide the first number by the second number. The
vl-catch-all-error-p function determines whether the return value from
vl-catch-all-apply is an error object. If the return value is an error object, catch-me-if-you-can invokes
vl-catch-all-error-message to obtain the message from the error object.

1. At the AutoCAD Command prompt, enter the following code:

   ```
   (defun catch-me-if-you-can (dividend divisor / errobj)
     (setq errobj (vl-catch-all-apply '/ (list dividend divisor)))
     (if (vl-catch-all-error-p errobj)
       (progn
         (print (strcat "An error occurred: " (vl-catch-all-error-message errobj)))
         (initget "Yes No")
         (setq ans (getkword "Do you want to continue? [Y/N]: "))
         (if (equal (strcase ans) "YES")
           (print "Okay, I'll keep going")
         )
       )
       (print errobj)
     )
    (princ)
   )
   ```

   NOTE:You can also add the example code to an existing or create a new LSP file. Then load the LSP file with the APPLOAD command.
2. Enter the following code:

   ```
   (catch-me-if-you-can 50 2)
   ```

   The function returns 25.
3. Enter the following code:

   ```
   (catch-me-if-you-can 50 0)
   ```

   The function issues the following prompt:

   "An error occurred: divide by zero" Do you want to continue? [Y/N]:

   If you enter y (or yes), catch-me-if-you-can indicates that it will continue processing. Try modifying this example by changing
   vl-catch-all-apply to
   apply. Load and run the example with a divide by zero again. When apply results in an error, execution immediately halts and \*error\*
   is called, resulting in an error message.

   The
   vl-catch-\* functions are especially important when you use ActiveX with AutoLISP. Many of the AutoCAD ActiveX automation methods are
   designed to be used in the “programming by exception” style. This means they either return useful values if they succeed,
   or raise an exception if they fail (instead of returning an error value). If your program uses ActiveX methods, you must prepare
   it to catch exceptions, otherwise the program halts, leaving the user at a Command prompt.

   NOTE:ActiveX is not supported on Mac OS and Web.

#### Related Concepts

* [About Catching Errors and Continuing Program Execution (AutoLISP)](About-Catching-Errors-and-Continuing-Program-Execution-AutoLISP.md)
* [About Error Handling (AutoLISP)](About-Error-Handling-AutoLISP.md)
* [About Using the \*error\* Function (AutoLISP)](About-Using-the-error-Function-AutoLISP.md)
* [About Exiting a Function Quietly (AutoLISP)](About-Exiting-a-Function-Quietly-AutoLISP.md)
* [Error Codes Reference (AutoLISP)](Error-Codes-Reference-AutoLISP.md)
* [Error-Handling Functions Reference (AutoLISP)](Error-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*