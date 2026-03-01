# boundp (AutoLISP)

Verifies if a value is bound to a symbol

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(boundp sym)
```

*sym*
:   *Type:* Symbol

    A symbol.

## Return Values

*Type:* T or nil

T if
*sym* has a value bound to it. If no value is bound to
*sym*, or if it has been bound to
nil,
boundp returns
nil. If
*sym* is an undefined symbol, it is automatically created and is bound to
nil.

## Examples

```
(setq a 2 b nil)
nil

(boundp 'a)
T

(boundp 'b)
nil
```

The
atoms-family function provides an alternative method of determining the existence of a symbol without automatically creating the symbol.

#### Related References

* [null (AutoLISP)](null-AutoLISP.md)

#### Related Concepts

* [Symbol-Handling Functions Reference (AutoLISP)](Symbol-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*