# set (AutoLISP)

Sets the value of a quoted symbol name to an expression

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(set sym expr)
```

*sym*
:   *Type:* Symbol

    The user-defined variable to assign
    *expr* to.

*expr*
:   *Type:* Integer, Real, String, List, Symbol, File, Ename (entity name), T, or nil

    An AutoLISP expression.

## Return Values

*Type:* Integer, Real, String, List, Symbol, File, Ename (entity name), T, or nil

The value of the expression.

## Remarks

The
set function is similar to
setq except that
set evaluates both of its arguments whereas
setq only evaluates its second argument.

## Examples

Each of the following commands sets symbol
a to 5.0:

```
(set 'a 5.0)
5.0

(set (read "a") 5.0)
5.0

(setq a 5.0)
5.0
```

Both
set and
setq expect a symbol as their first argument, but
set accepts an expression that returns a symbol, whereas
setq does not, as the following shows:

```
(set (read "a") 5.0)
5.0

(setq (read "a") 5.0)
; *** ERROR: syntax error
```

#### Related References

* [setq (AutoLISP)](setq-AutoLISP.md)
* [type (AutoLISP)](type-AutoLISP.md)

#### Related Concepts

* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*