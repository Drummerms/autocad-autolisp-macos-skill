# About Functions with Arguments (AutoLISP)

With AutoLISP, many functions require you to pass them values. These values are known as arguments.

There are functions that also accept no arguments, and some in which accept optional arguments. User-defined functions cannot
have optional arguments. When you call a user-defined function that accepts arguments, you must provide values for all arguments.

NOTE:You can define multiple user functions with the same name, but have each definition accept a different number or type of arguments.

The symbols used as arguments are defined in the argument list before the local variables. Arguments are treated as a special
type of local variable; argument variables are not available outside the function. You cannot define a function with multiple
arguments of the same name.

If you do use the same name for multiple arguments, the following error message is displayed at the AutoCAD Command prompt:

duplicate argument name:

The following code defines a function that accepts two arguments. The code expects the arguments to both be of the string
data type. The arguments are combined and returned as the resulting string.

```
(defun ARGTEST ( arg1 arg2 / ccc )
  (setq ccc "Constant string")
  (strcat ccc ", " arg1 ", " arg2)
)
ARGTEST
```

The ARGTEST function returns the desired value because AutoLISP always returns the results of the last expression it evaluates. The last
line in ARGTEST uses strcat to concatenate the strings, and the resulting value is returned. This is one example where you should not use the princ function to suppress the return value from your program.

This type of function can be used a number of times within an application to combine two variable strings with one constant
string in a specific order. Because it returns a value, you can save the value to a variable for use later in the application.

```
(setq newstr (ARGTEST "String 1" "String 2"))
"Constant string, String 1, String 2"
```

The newstr variable is now set to the value of the three strings combined.

Note that the ccc variable was defined locally within the ARGTEST function. Once the function runs to completion, AutoLISP recaptures the memory allocated to the variable. You can use the
following code to check the value assigned to ccc.

```
!ccc
nil
```

If string values are not passed to the ARGTEST function, the strcat function will return the following error:

; error: bad argument type: stringp 1

You can use the type function to verify the data type of an argument and respond appropriately. The vl-catch-apply-all function could also be helpful in catching the error returned by the strcat function. The following example code uses the type function to make sure that the ARGTEST function was passed two string values before trying to combine and return the resulting string.

```
(defun ARGTEST (arg1 arg2 / ccc retVal)
  (setq ccc "Constant string")

  (if (= (type arg1) 'STR)
    (if (= (type arg2) 'STR)
      (setq retVal (strcat ccc ", " arg1 ", " arg2))
      (prompt "bad argument: arg2 not a string\
")
    )
    (prompt "bad argument: arg1 not a string\
")
  )
  (if retVal
    retVal
    (princ)
  )
)
```

#### Topics in this section

* [About Special Forms (AutoLISP)](About-Special-Forms-AutoLISP.md)

  Certain AutoLISP functions are considered special forms because they evaluate arguments in a different manner than most AutoLISP
  function calls.

#### Related Concepts

* [About Function Syntax (AutoLISP)](About-Function-Syntax-AutoLISP.md)
* [About Expressions (AutoLISP)](About-Expressions-AutoLISP.md)
* [About Defining a Function (AutoLISP)](About-Defining-a-Function-AutoLISP.md)
* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*