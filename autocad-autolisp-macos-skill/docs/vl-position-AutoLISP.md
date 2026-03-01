# vl-position (AutoLISP)

Returns the index of the specified list item

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-position symbol list)
```

*symbol*
:   *Type:* Integer, Real, String, File, Symbol, Ename (entity name), T, or nil

    Any AutoLISP symbol.

*list*
:   *Type:* List

    A true list.

## Return Values

*Type:* Integer or nil

A numeric value containing the index position of
*symbol* in
*list*; otherwise
nil if
*symbol* does not exist in the list.

NOTE:The first list element is index 0, the second element is index 1, and so on.

## Examples

```
(setq stuff (list "a" "b" "c" "d" "e"))
("a" "b" "c" "d" "e")

(vl-position "c" stuff)
2
```

#### Related References

* [vl-member-if-not (AutoLISP)](vl-member-if-not-AutoLISP.md)
* [vl-member-if (AutoLISP)](vl-member-if-AutoLISP.md)
* [member (AutoLISP)](member-AutoLISP.md)
* [list (AutoLISP)](list-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*