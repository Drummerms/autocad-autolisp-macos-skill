# zerop (AutoLISP)

Verifies that a number evaluates to zero

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(zerop number)
```

*number*
:   *Type:* Integer or Real

    A numeric value.

## Return Values

*Type:* T or nil

T if
*number* evaluates to zero; otherwise
nil.

## Examples

```
(zerop 0)
T

(zerop 0.0)
T

(zerop 0.0001)
nil
```

#### Related References

* [numberp (AutoLISP)](numberp-AutoLISP.md)
* [boundp (AutoLISP)](boundp-AutoLISP.md)
* [not (AutoLISP)](not-AutoLISP.md)
* [null (AutoLISP)](null-AutoLISP.md)

#### Related Concepts

* [Arithmetic Functions Reference (AutoLISP)](Arithmetic-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*