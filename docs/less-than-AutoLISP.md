# < (less than) (AutoLISP)

Returns
*T* if each argument is numerically less than the argument to its right; otherwise
*nil*

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(< numstr [numstr ...])
```

*numstr*
:   *Type:* Integer, Real, or String

    A number or string.

## Return Values

*Type:* T or nil

T, if each argument is numerically less than the argument to its right; otherwise returns
nil . If only one argument is supplied,
T is returned.

## Examples

```
(< 10 20)
T

(< "b" "c")
T

(< 357 33.2)
nil

(< 2 3 88)
T

(< 2 3 4 4)
nil
```

#### Related References

* [<= (less than or equal to) (AutoLISP)](=-less-than-or-equal-to-AutoLISP.md)
* [> (greater than) (AutoLISP)](greater-than-AutoLISP.md)

#### Related Concepts

* [Equality and Conditional Functions Reference (AutoLISP)](Equality-and-Conditional-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*