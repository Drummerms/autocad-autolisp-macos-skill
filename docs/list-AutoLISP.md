# list (AutoLISP)

Takes any number of expressions and combines them into one list

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(list [expr ...])
```

*expr*
:   *Type:* Integer, Real, String, List, Ename (entity name), T, or nil

    An AutoLISP expression.

## Return Values

*Type:* List or nil

A list, unless no expressions are supplied, in which case
list returns
nil.

## Remarks

This function is frequently used to define a 2D or 3D point variable (a list of two or three reals).

## Examples

```
(list 'a 'b 'c)
(A B C)

(list 'a '(b c) 'd)
(A (B C) D)

(list 3.9 6.7)
(3.9 6.7)
```

As an alternative to using the
list function, you can explicitly quote a list with the
quote function if there are no variables or undefined items in the list. The single quote character (') is defined as the quote function.

```
'(3.9 6.7) means the same as (list 3.9 6.7)
```

This can be useful for creating association lists and defining points.

#### Related References

* [length (AutoLISP)](length-AutoLISP.md)
* [append (AutoLISP)](append-AutoLISP.md)
* [listp (AutoLISP)](listp-AutoLISP.md)
* [vl-every (AutoLISP)](vl-every-AutoLISP.md)
* [vl-list\* (AutoLISP)](vl-list-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*