# inters (AutoLISP)

Finds the intersection of two lines

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(inters pt1 pt2 pt3 pt4 [onseg])
```

*pt1*
:   *Type:* List

    One endpoint of the first line.

*pt2*
:   *Type:* List

    The other endpoint of the first line.

*pt3*
:   *Type:* List

    One endpoint of the second line.

*pt4*
:   *Type:* List

    The other endpoint of the second line.

*onseg*
:   *Type:* List or nil

    If specified as
    nil, the lines defined by the four
    *pt* arguments are considered infinite in length. If the
    *onseg* argument is omitted or is not
    nil, the intersection point must lie on both lines or
    inters returns
    nil.

## Return Values

*Type:* List or nil

If the
*onseg* argument is present and is
nil,
inters returns the point where the lines intersect, even if that point is off the end of one or both of the lines. If the
*onseg* argument is omitted or is not
nil, the intersection point must lie on both lines or
inters returns
nil. The
inters function returns
nil if the two lines do not intersect.

## Remarks

All points are expressed in terms of the current UCS. If all four point arguments are 3D,
inters checks for 3D intersection. If any of the points are 2D,
inters projects the lines onto the current construction plane and checks only for 2D intersection.

## Examples

```
(setq a '(1.0 1.0) b '(9.0 9.0))
(setq c '(4.0 1.0) d '(4.0 2.0)) (inters a b c d)
nil

(inters a b c d T)
nil

(inters a b c d nil)
(4.0 4.0)
```

#### Related References

* [osnap (AutoLISP)](osnap-AutoLISP.md)
* [polar (AutoLISP)](polar-AutoLISP.md)

#### Related Concepts

* [Geometric Functions Reference (AutoLISP)](Geometric-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*