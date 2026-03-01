# lambda (AutoLISP)

Defines an anonymous function

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(lambda arguments expr ...)
```

*arguments*
:   *Type:* List

    Arguments passed to an expression.

*expr*
:   *Type:* List

    An AutoLISP expression.

## Return Values

*Type:* Integer, Real, String, List, Symbol, Ename (entity name), T, or nil

Value of the last
*expr*.

## Remarks

Use the
lambda function when the overhead of defining a new function is not justified. It also makes your intention more apparent by laying
out the function at the spot where it is to be used. This function returns the value of its last
*expr*, and is often used in conjunction with
apply and/or
mapcar to perform a function on a list.

## Examples

The following examples demonstrate the
lambda function:

```
(apply '(lambda (x y z)
          (* x (- y z))
        )
        '(5 20 14)
)
30

(setq counter 0)
(mapcar '(lambda (x)
          (setq counter (1+ counter))
          (* x 5)
        )
        '(2 4 -6 10.2)
)
0
(10 20 -30 51.0)
```

#### Related References

* [defun (AutoLISP)](defun-AutoLISP.md)
* [apply (AutoLISP)](apply-AutoLISP.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*