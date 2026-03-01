# caddr (AutoLISP)

Returns the third element of a list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(caddr list)
```

*list*
:   *Type:* List

    A list with three or more elements.

## Return Values

*Type:* Integer, Real, String, List, T or nil

The third element in
*list*; otherwise
nil, if the list is empty or contains fewer than three elements.

## Remarks

In AutoLISP,
caddr is frequently used to obtain the
*Z* coordinate of a 3D point (the third element of a list of three reals).

## Examples

```
(setq pt3 '(5.25 1.0 3.0))
(5.25 1.0 3.0)

(caddr pt3)
3.0

(caddr '(5.25 1.0))
nil
```

#### Related References

* [car (AutoLISP)](car-AutoLISP.md)
* [cdr (AutoLISP)](cdr-AutoLISP.md)
* [nth (AutoLISP)](nth-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*