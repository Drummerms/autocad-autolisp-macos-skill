# angle (AutoLISP)

Returns an angle in radians of a line defined by two endpoints

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(angle pt1 pt2)
```

*pt1*
:   *Type:* Integer or Real

    An endpoint.

*pt2*
:   *Type:* Integer or Real

    An endpoint.

## Return Values

*Type:* Real

An angle, in radians.

The angle is measured from the
*X* axis of the current construction plane, in radians, with angles increasing in the counterclockwise direction. If 3D points
are supplied, they are projected onto the current construction plane.

## Examples

```
(angle '(1.0 1.0) '(1.0 4.0))
1.5708

(angle '(5.0 1.33) '(2.4 1.33))
3.14159
```

#### Related References

* [distance (AutoLISP)](distance-AutoLISP.md)
* [getangle (AutoLISP)](getangle-AutoLISP.md)
* [getorient (AutoLISP)](getorient-AutoLISP.md)

#### Related Concepts

* [Geometric Functions Reference (AutoLISP)](Geometric-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*