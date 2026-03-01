# vlax-curve-getDistAtParam (AutoLISP/ActiveX)

Returns the length of the curve's segment from the curve's beginning to the specified parameter

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-getDistAtParam curve-obj param)
```

*curve-obj*
:   *Type:* VLA-object

    The object to be measured.

*param*
:   *Type:* Integer or Real

    A number specifying a parameter on the curve.

## Return Values

*Type:* Real or nil

A number that is the length up to the specified parameter, if successful; otherwise
nil.

## Examples

Assume that
splineObj points to the spline in the following drawing:

![](../images/GUID-67719031-9AAC-43F2-87D1-34D4740C5EA1-low.png)

Sample curve (spline) for
vlax-curve-getDistAtParam

Obtain the start parameter of the curve:

```
(setq startSpline (vlax-curve-getStartParam splineObj))
0.0
```

The curve starts at parameter 0.

Obtain the end parameter of the curve:

```
(setq endSpline (vlax-curve-getEndParam splineObj))
17.1546
```

The curve's end parameter is 17.1546.

Determine the distance to the parameter midway along the curve:

```
(vlax-curve-getDistAtParam splineObj
   ( / (- endspline startspline) 2))
8.99417
```

The distance from the start to the middle of the curve is 8.99417.

#### Related References

* [vlax-curve-getDistAtPoint (AutoLISP/ActiveX)](vlax-curve-getDistAtPoint-AutoLISP-ActiveX.md)
* [vlax-curve-getParamAtDist (AutoLISP/ActiveX)](vlax-curve-getParamAtDist-AutoLISP-ActiveX.md)
* [vlax-curve-getParamAtPoint (AutoLISP/ActiveX)](vlax-curve-getParamAtPoint-AutoLISP-ActiveX.md)
* [vlax-curve-getEndParam (AutoLISP/ActiveX)](vlax-curve-getEndParam-AutoLISP-ActiveX.md)
* [vlax-curve-getStartParam (AutoLISP/ActiveX)](vlax-curve-getStartParam-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*