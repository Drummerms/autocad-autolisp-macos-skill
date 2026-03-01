# vl-list-length (AutoLISP)

Calculates list length of a true list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-list-length list-or-cons-object)
```

*list-or-cons-object*
:   *Type:* List or nil

    A true or dotted list.

## Return Values

*Type:* Integer or nil

An integer containing the list length if the argument is a true list; otherwise
nil if
*list-or-cons-object* is a dotted list.

Compatibility note: The
vl-list-length function returns
nil for a dotted list, while the corresponding Common LISP function issues an error message if the argument is a dotted list.

## Examples

```
(vl-list-length nil)
0

(vl-list-length '(1 2))
2

(vl-list-length '(1 2 . 3))
nil
```

#### Related References

* [length (AutoLISP)](length-AutoLISP.md)
* [cons (AutoLISP)](cons-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*