# vlax-curve-getPointAtParam (AutoLISP/ActiveX)

Returns the point at the specified parameter value along a curve

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-getPointAtParam curve-obj param)
```

*curve-obj*
:   *Type:* VLA-object

    The object to be measured.

*param*
:   *Type:* Integer or Real

    A number specifying a parameter on the curve.

## Return Values

*Type:* List or nil

A 3D point representing a point on the curve, if successful; otherwise
nil.

## Examples

For the following example, assume that
splineObj points to the spline shown in the example for
vlax-curve-getDistAtParam.

Obtain the start parameter of the curve:

```
(setq startSpline (vlax-curve-getStartParam splineObj))
0.0
```

Obtain the end parameter of the curve:

```
(setq endSpline (vlax-curve-getEndParam splineObj))
17.1546
```

Determine the point at the parameter midway along the curve:

```
(vlax-curve-getPointAtParam splineObj
   ( / (- endspline startspline) 2))
(6.71386 2.82748 0.0)
```

#### Related References

* [vlax-curve-getDistAtPoint (AutoLISP/ActiveX)](vlax-curve-getDistAtPoint-AutoLISP-ActiveX.md)
* [vlax-curve-getPointAtDist (AutoLISP/ActiveX)](vlax-curve-getPointAtDist-AutoLISP-ActiveX.md)
* [vlax-curve-getEndParam (AutoLISP/ActiveX)](vlax-curve-getEndParam-AutoLISP-ActiveX.md)
* [vlax-curve-getStartParam (AutoLISP/ActiveX)](vlax-curve-getStartParam-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*