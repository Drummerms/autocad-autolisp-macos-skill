# vl-consp (AutoLISP)

Determines whether or not a list is nil

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-consp list-variable)
```

*list-variable*
:   *Type:* Integer, Real, String, List, Subroutine, Ename (entity name), T, nil, or catch-all-apply-error

    A list.

## Return Values

*Type:* T or nil

T, if
*list-variable* is a list and is not
nil; otherwise
nil.

## Remarks

The
vl-consp function determines whether a variable contains a valid list definition.

## Examples

```
(vl-consp nil)
nil

(vl-consp t)
nil

(vl-consp (cons 0 "LINE"))
T
```

#### Related References

* [cons (AutoLISP)](cons-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*