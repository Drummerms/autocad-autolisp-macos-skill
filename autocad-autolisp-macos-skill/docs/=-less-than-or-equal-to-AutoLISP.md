# <= (less than or equal to) (AutoLISP)

Returns
*T* if each argument is numerically less than or equal to the argument to its right; otherwise returns
*nil*

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(<= numstr [numstr ...])
```

*numstr*
:   *Type:* Integer, Real, or String

    A number or string.

## Return Values

*Type:* T or nil

T, if each argument is numerically less than or equal to the argument to its right; otherwise returns
nil. If only one argument is supplied,
T is returned.

## Examples

```
(<= 10 20)
T

(<= "b" "b")
T

(<= 357 33.2)
nil

(<= 2 9 9)
T

(<= 2 9 4 5)
nil
```

#### Related References

* [< (less than) (AutoLISP)](less-than-AutoLISP.md)
* [>= (greater than or equal to) (AutoLISP)](=-greater-than-or-equal-to-AutoLISP.md)

#### Related Concepts

* [Equality and Conditional Functions Reference (AutoLISP)](Equality-and-Conditional-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*