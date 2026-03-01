# vlax-curve-getClosestPointToProjection (AutoLISP/ActiveX)

Returns the closest point (in WCS) on a curve after projecting the curve onto a plane

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-getClosestPointToProjection curve-obj givenPnt normal [extend])
```

*curve-obj*
:   *Type:* VLA-object

    The object to be measured.

*givenPnt*
:   *Type:* List

    A point (in WCS) for which to find the nearest point on the curve.

*normal*
:   *Type:* List

    *A* normal vector (in WCS) for the plane to project onto.

*extend*
:   *Type:* T

    If specified and not
    nil,
    vlax-curve-getClosestPointToProjection extends the curve when searching for the nearest point.

## Return Values

*Type:* List or nil

A 3D point representing a point on the curve, if successful; otherwise
nil.

## Remarks

vlax-curve-getClosestPointToProjection projects the curve onto the plane defined by the
*givenPnt* and
*normal*, and then calculates the nearest point on that projected curve to
*givenPnt*. The resulting point is then projected back onto the original curve, and
vlax-curve-getClosestPointToProjection returns that projected point.

## Example

N/A

#### Related References

* [vlax-curve-getClosestPointTo (AutoLISP/ActiveX)](vlax-curve-getClosestPointTo-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*