# cadr (AutoLISP)

Returns the second element of a list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(cadr list)
```

*list*
:   *Type:* List

    A list with two or more elements.

## Return Values

*Type:* Integer, Real, String, List, T or nil

The second element in
*list*; otherwise
nil, if the list is empty or contains only one element.

## Remarks

In AutoLISP,
cadr is frequently used to obtain the
*Y* coordinate of a 2D or 3D point (the second element of a list of two or three reals).

## Examples

```
(setq pt2 '(5.25 1.0))
(5.25 1.0)

(cadr pt2)
1.0

(cadr '(4.0))
nil

(cadr '(5.25 1.0 3.0))
1.0
```

#### Related References

* [car (AutoLISP)](car-AutoLISP.md)
* [cdr (AutoLISP)](cdr-AutoLISP.md)
* [nth (AutoLISP)](nth-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*