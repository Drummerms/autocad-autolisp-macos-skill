# listp (AutoLISP)

Verifies that an item is a list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(listp item)
```

*item*
:   *Type:* Integer, Real, String, List, Ename (entity name), T, or nil

    Any atom, list, or expression.

## Return Values

*Type:* T or nil

T if
*item* is a list; otherwise
nil. Because
nil is both an atom and a list, the
listp function returns
T when passed
nil.

## Examples

```
(listp '(a b c))
T

(listp 'a)
nil

(listp 4.343)
nil

(listp nil)
T

(listp (setq v1 '(1 2 43)))
T
```

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*