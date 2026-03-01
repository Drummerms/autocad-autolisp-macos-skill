# or (AutoLISP)

Returns the logical OR of a list of expressions

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(or [expr ...])
```

*expr*
:   *Type:* Integer, Real, String, List, Subroutine, Ename (entity name), T, or nil

    The expressions to be evaluated.

## Remarks

The
or function evaluates the expressions from left to right, looking for a non-nil expression.

## Return Values

*Type:* T or nil

T, if a non-nil expression is found; otherwise
nil, if all of the expressions are
nil or no arguments are supplied.

Note that
or accepts an atom as an argument and returns
T if one is supplied.

## Examples

```
(or nil 45 '())
T

(or nil '())
nil
```

#### Related References

* [and (AutoLISP)](and-AutoLISP.md)

#### Related Concepts

* [Equality and Conditional Functions Reference (AutoLISP)](Equality-and-Conditional-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*