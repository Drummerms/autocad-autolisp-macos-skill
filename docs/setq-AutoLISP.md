# setq (AutoLISP)

Sets the value of a symbol or symbols to associated expressions

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(setq sym expr [sym expr] ...)
```

*sym*
:   *Type:* Symbol

    The user-defined variable to assign
    *expr* to. This argument is not evaluated.

*expr*
:   *Type:* Integer, Real, String, List, File, Ename (entity name), T, or nil

    An expression.

## Return Values

*Type:* Integer, Real, String, List, File, Ename (entity name), T, or nil

The result of the last
*expr* evaluated.

## Remarks

This is the basic assignment function in AutoLISP. The
setq function can assign multiple symbols in one call to the function.

## Examples

The following function call sets variable
a to 5.0:

```
(setq a 5.0)
5.0
```

Whenever
a is evaluated, it returns the real number 5.0.

The following command sets two variables,
b and
c:

```
(setq b 123 c 4.7)
4.7
```

setq returns the value of the last variable set.

In the following example,
s is set to a string:

```
(setq s "it")
"it"
```

The following example assigns a list to
x:

```
(setq x '(a b))
(A B)
```

#### Related References

* [set (AutoLISP)](set-AutoLISP.md)
* [type (AutoLISP)](type-AutoLISP.md)
* [vl-bb-set (AutoLISP)](vl-bb-set-AutoLISP.md)
* [vl-propagate (AutoLISP)](vl-propagate-AutoLISP.md)
* [vl-doc-set (AutoLISP)](vl-doc-set-AutoLISP.md)

#### Related Concepts

* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*