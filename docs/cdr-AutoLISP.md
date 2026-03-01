# cdr (AutoLISP)

Returns a list containing all but the first element of the specified list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(cdr list)
```

*list*
:   *Type:* List

    A list with two or more elements.

## Return Values

*Type:* Integer, Real, String, List, T or nil

A list containing all the elements of
*list,* except the first element. If the list is empty,
cdr returns
nil.

NOTE:When the
*list* argument is a dotted pair,
cdr returns the second element without enclosing it in a list.

## Examples

```
(cdr '(a b c))
(B C)

(cdr '((a b) c))
(C)

(cdr '())
nil

(cdr '(a . b))
B

(cdr '(1 . "Text"))
"Text"
```

#### Related References

* [caddr (AutoLISP)](caddr-AutoLISP.md)
* [cadr (AutoLISP)](cadr-AutoLISP.md)
* [nth (AutoLISP)](nth-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*