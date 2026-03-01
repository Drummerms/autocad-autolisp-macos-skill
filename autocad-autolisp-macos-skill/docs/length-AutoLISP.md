# length (AutoLISP)

Returns an integer indicating the number of elements in a list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(length lst)
```

*lst*
:   *Type:* List

    An empty list or a list with one or more elements.

## Return Values

*Type:* Integer

A numeric value.

## Examples

```
(length '(a b c d))
4

(length '(a b (c d)))
3

(length '())
0
```

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)
* [nth (AutoLISP)](nth-AutoLISP.md)
* [vl-list-length (AutoLISP)](vl-list-length-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*