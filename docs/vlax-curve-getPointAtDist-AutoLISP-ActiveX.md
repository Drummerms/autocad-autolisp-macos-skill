# vlax-curve-getPointAtDist (AutoLISP/ActiveX)

Returns the point (in WCS) along a curve at the distance specified by the user

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-getPointAtDist curve-obj dist)
```

*curve-obj*
:   *Type:* VLA-object

    The object to be measured.

*dist*
:   *Type:* Real

    The distance along the curve from the beginning of the curve to the location of the specified point.

## Return Values

*Type:* List or nil

A 3D point representing a point on the curve, if successful; otherwise
nil.

## Examples

Assuming that
splineObj points to the spline shown in the example for
vlax-curve-getDistAtParam, determine the point at a distance of 1.0 from the beginning of the spline:

```
(vlax-curve-getPointAtDist splineObj 1.0)
(2.24236 2.99005 0.0)
```

#### Related References

* [vlax-curve-getDistAtPoint (AutoLISP/ActiveX)](vlax-curve-getDistAtPoint-AutoLISP-ActiveX.md)
* [vlax-curve-getPointAtParam (AutoLISP/ActiveX)](vlax-curve-getPointAtParam-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*