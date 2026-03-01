# progn (AutoLISP)

Evaluates each expression sequentially and returns the value of the last expression

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(progn [expr ...])
```

*expr*
:   *Type:* Integer, Real, String, List, Symbol, File, Ename (entity name), T, or nil

    One or more AutoLISP expressions.

## Return Values

*Type:* Integer, Real, String, List, Symbol, File, Ename (entity name), T, or nil

The result of the last evaluated expression.

## Remarks

You can use
progn to evaluate several expressions where only one expression is expected.

## Examples

The
if function normally evaluates one
*then* expression if the test expression evaluates to anything but
nil. The following example uses
progn to evaluate two expressions following
if:

```
(if (= a b)
  (progn
    (princ "\
A = B ")
    (setq a (+ a 10) b (- b 10))
  )
)
```

#### Related References

* [if (AutoLISP)](if-AutoLISP.md)

#### Related Concepts

* [Function-Handling Functions Reference (AutoLISP)](Function-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*