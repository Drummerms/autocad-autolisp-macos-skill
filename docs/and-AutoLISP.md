# and (AutoLISP)

Returns the logical AND of the supplied arguments

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(and [expr ...])
```

*expr*
:   *Type:* Symbol, Integer, Real, String, T, or nil

    Any expression.

## Return Values

*Type:* T or nil

nil, if any of the expressions evaluate to
nil; otherwise
T. If
 and is issued without arguments, it returns
T.

## Examples

```
(setq a 103 b nil c "string")
"string"

(and 1.4 a c)
T

(and 1.4 a b c)
nil
```

#### Related References

* [or (AutoLISP)](or-AutoLISP.md)

#### Related Concepts

* [Equality and Conditional Functions Reference (AutoLISP)](Equality-and-Conditional-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*