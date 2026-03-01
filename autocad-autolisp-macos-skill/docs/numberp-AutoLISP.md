# numberp (AutoLISP)

Verifies that an item is a real number or an integer

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(numberp item)
```

*item*
:   *Type:* Integer, Real, String, List, Subroutine, Ename (entity name), T, or nil

    An AutoLISP expression.

## Return Values

*Type:* T or nil

T if
*item* evaluates to a real or an integer; otherwise
nil.

## Examples

```
(setq a 123 b 'a)
A

(numberp 4)
T

(numberp 3.8348)
T

(numberp "Howdy")
nil

(numberp a)
T

(numberp b)
nil

(numberp (eval b))
T
```

#### Related References

* [not (AutoLISP)](not-AutoLISP.md)
* [boundp (AutoLISP)](boundp-AutoLISP.md)
* [zerop (AutoLISP)](zerop-AutoLISP.md)
* [if (AutoLISP)](if-AutoLISP.md)

#### Related Concepts

* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*