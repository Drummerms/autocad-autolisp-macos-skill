# vlax-curve-getClosestPointTo (AutoLISP/ActiveX)

Returns the point (in WCS) on a curve that is nearest to the specified point

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-getClosestPointTo curve-obj givenPnt [extend])
```

*curve-obj*
:   *Type:* VLA-object

    The object to be measured.

*givenPnt*
:   *Type:* List

    A point (in WCS) for which to find the nearest point on the curve.

*extend*
:   *Type:* T

    If specified and not
    nil,
    vlax-curve-getClosestPointTo extends the curve when searching for the nearest point.

## Return Values

*Type:* List or nil

A 3D point representing a point on the curve, if successful; otherwise
nil.

## Examples

Assume that the curve being measured is the arc in the following drawing:

![](../images/GUID-0B949665-4928-48D2-A793-D7EBF686A45D-low.png)

Return the closest point on the arc to the coordinates 6.0, 0.5:

```
(vlax-curve-getClosestPointTo arcObj '(6.0 0.5 0.0))
(6.0 1.5 0.0)
```

Return the closest point on the arc to the coordinates 6.0, 0.5, after extending the arc:

```
(vlax-curve-getClosestPointTo arcObj '(6.0 0.5 0.0) T)
(5.7092 0.681753 0.0)
```

#### Related References

* [vlax-curve-getClosestPointToProjection (AutoLISP/ActiveX)](vlax-curve-getClosestPointToProjection-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*