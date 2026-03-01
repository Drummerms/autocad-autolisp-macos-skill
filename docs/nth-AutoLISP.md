# nth (AutoLISP)

Returns the nth element of a list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(nth n lst)
```

*n*
:   *Type:* Integer

    The number of the element to return from the list (zero is the first element).

*lst*
:   *Type:* List

    The list with one or more elements.

## Return Values

*Type:* Integer, Real, String, List, Ename (entity name), T, or nil

The
*n*th element of
*lst*. If
*n* is greater than the highest element number of
*lst*,
nth returns
nil.

## Examples

```
(nth 3 '(a b c d e))
D

(nth 0 '(a b c d e))
A

(nth 5 '(a b c d e))
nil
```

#### Related References

* [car (AutoLISP)](car-AutoLISP.md)
* [cdr (AutoLISP)](cdr-AutoLISP.md)
* [list (AutoLISP)](list-AutoLISP.md)
* [member (AutoLISP)](member-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*