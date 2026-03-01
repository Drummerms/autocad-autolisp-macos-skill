# car (AutoLISP)

Returns the first element of a list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(car list)
```

*list*
:   *Type:* List

    A list with one or more elements.

## Return Values

*Type:* Integer, Real, String, List, T or nil

The first element in
*list*; otherwise
nil, if the list is empty.

## Remarks

In AutoLISP,
car is frequently used to obtain the
*X* coordinate of a 2D or 3D point (the first element of a list of two or three reals).

## Examples

```
(car '(a b c))
A

(car '((a b) c))
(A B)

(car '())
nil
```

#### Related References

* [caddr (AutoLISP)](caddr-AutoLISP.md)
* [cadr (AutoLISP)](cadr-AutoLISP.md)
* [nth (AutoLISP)](nth-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*