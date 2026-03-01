# function (AutoLISP/Visual LISP IDE)

Tells the Visual LISP compiler to link and optimize an argument as if it were a built-in function

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(function symbol | lambda-expr)
```

*symbol*
:   *Type:* Symbol

    A symbol naming a function.

*lambda-expr*
:   *Type:* Subroutine or List

    An expression of the following form:

    (LAMBDA
    *arguments {S-expression}\**)

## Return Values

The result of the evaluated expression.

## Remarks

The
function function is identical to the
quote function, except it tells the Visual LISP compiler to link and optimize the argument as if it were a built-in function or
defun.

Compiled
lambda expressions that are quoted by
function will contain debugging information when loaded into the Visual LISP IDE.

## Examples

The Visual LISP compiler cannot optimize the quoted
lambda expression in the following code:

```
(mapcar
  '(lambda (x) (* x x))
       '(1 2 3))
```

After adding the
function function to the expression, the compiler can optimize the
lambda expression. For example:

```
(mapcar
   (function (lambda (x) (* x x)))
      '(1 2 3))
```

#### Related References

* [apply (AutoLISP)](apply-AutoLISP.md)
* [defun (AutoLISP)](defun-AutoLISP.md)
* [lambda (AutoLISP)](lambda-AutoLISP.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*