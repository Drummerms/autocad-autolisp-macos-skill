# vl-remove (AutoLISP)

Removes elements from a list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-remove element-to-remove lst)
```

*element-to-remove*
:   *Type:* Integer, Real, String, List, File, Ename (entity name), T, or nil

    The value of the element to be removed; may be any LISP data type.

*lst*
:   *Type:* List

    Any list.

## Return Values

*Type:* List or nil

The
*lst* with all elements except those equal to
*element-to-remove*.

## Examples

```
(vl-remove pi (list pi t 0 "abc"))
(T 0 "abc")
```

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)
* [vl-remove-if (AutoLISP)](vl-remove-if-AutoLISP.md)
* [vl-remove-if-not (AutoLISP)](vl-remove-if-not-AutoLISP.md)
* [vl-member-if (AutoLISP)](vl-member-if-AutoLISP.md)
* [vl-member-if-not (AutoLISP)](vl-member-if-not-AutoLISP.md)
* [member (AutoLISP)](member-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*