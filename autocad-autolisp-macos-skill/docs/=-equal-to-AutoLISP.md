# = (equal to) (AutoLISP)

Compares arguments for numerical equality

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(= numstr [numstr ...])
```

*numstr*
:   *Type:* Integer, Real, or String

    A number or string.

## Return Values

*Type:* T or nil

T, if all arguments are numerically equal; otherwise
nil. If only one argument is supplied,
T is returned.

## Examples

```
(= 4 4.0)
T

(= 20 388)
nil

(= 2.4 2.4 2.4)
T

(= 499 499 500)
nil

(= "me" "me")
T

(= "me" "you")
nil
```

#### Related References

* [eq (AutoLISP)](eq-AutoLISP.md)
* [equal (AutoLISP)](equal-AutoLISP.md)
* [/= (not Equal to) (AutoLISP)](=-not-Equal-to-AutoLISP.md)

#### Related Concepts

* [Equality and Conditional Functions Reference (AutoLISP)](Equality-and-Conditional-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*