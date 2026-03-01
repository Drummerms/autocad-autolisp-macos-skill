# null (AutoLISP)

Verifies that an item is bound to nil

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(null item)
```

*item*
:   *Type:* Integer, Real, String, List, Ename (entity name), T, or nil

    An AutoLISP expression.

## Return Values

*Type:* T or nil

T if
*item* evaluates to
nil; otherwise
nil.

## Examples

```
(setq a 123 b "string" c nil)
nil

(null a)
nil

(null b)
nil

(null c)
T

(null '())
T
```

#### Related References

* [not (AutoLISP)](not-AutoLISP.md)
* [boundp (AutoLISP)](boundp-AutoLISP.md)
* [if (AutoLISP)](if-AutoLISP.md)

#### Related Concepts

* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*