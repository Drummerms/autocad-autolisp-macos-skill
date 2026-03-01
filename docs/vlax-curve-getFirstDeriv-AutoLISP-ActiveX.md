# vlax-curve-getFirstDeriv (AutoLISP/ActiveX)

Returns the first derivative (in WCS) of a curve at the specified location

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-getFirstDeriv curve-obj param)
```

*curve-obj*
:   *Type:* VLA-object

    The object to be measured.

*param*
:   *Type:* Integer or Real

    A number specifying a parameter on the curve.

## Return Values

*Type:* List or nil

A 3D vector, if successful; otherwise
nil.

## Examples

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

Determine the first derivative at the parameter midway along the curve:

```
 (vlax-curve-getFirstDeriv splineObj
   ( / (- endspline startspline) 2))
(0.422631 -1.0951 0.0)
```

#### Related References

* [vlax-curve-getEndParam (AutoLISP/ActiveX)](vlax-curve-getEndParam-AutoLISP-ActiveX.md)
* [vlax-curve-getStartParam (AutoLISP/ActiveX)](vlax-curve-getStartParam-AutoLISP-ActiveX.md)
* [vlax-curve-getSecondDeriv (AutoLISP/ActiveX)](vlax-curve-getSecondDeriv-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*