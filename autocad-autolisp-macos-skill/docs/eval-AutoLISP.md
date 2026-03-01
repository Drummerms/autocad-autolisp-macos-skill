# eval (AutoLISP)

Returns the result of evaluating an AutoLISP expression

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(eval expr)
```

*expr*
:   *Type:* Integer, Real, String, List, Symbol, Ename (entity name), T, or nil

    The expression to be evaluated.

## Return Values

*Type:* Integer, Real, String, List, Symbol, Ename (entity name), T, or nil

The result of the expression, after evaluation.

## Examples

First, set some variables:

```
(setq a 123)
123

(setq b 'a)
A
```

Now evaluate some expressions:

```
(eval 4.0)
4.0

(eval (abs -10))
10

(eval a)
123

(eval b)
123
```

#### Related References

* [defun (AutoLISP)](defun-AutoLISP.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*