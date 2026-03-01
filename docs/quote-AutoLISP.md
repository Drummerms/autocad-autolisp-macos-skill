# quote (AutoLISP)

Returns an expression without evaluating it

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(quote expr)
```

*expr*
:   *Type:* Integer, Real, String, List, Symbol, File, Subroutine, Ename (entity name), T, or nil

    An AutoLISP expression.

## Return Values

*Type:* Integer, Real, String, List, Symbol, File, Subroutine, Ename (entity name), T, or nil

The
*expr* argument.

## Examples

```
(quote a)
A
```

The previous expression can also be written as
'a. For example:

```
!'a
A

(quote (a b))
(A B)
```

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)

#### Related Concepts

* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*