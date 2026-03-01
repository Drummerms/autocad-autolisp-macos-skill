# vlax-curve-isPeriodic (AutoLISP/ActiveX)

Determines if the specified curve has an infinite range in both directions and there is a period value
*dT,* such that a point on the curve at (*u* +
*dT*) = point on curve (*u*), for any parameter
*u*

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-isPeriodic curve-obj)
```

*curve-obj*
:   *Type:* VLA-object

    The object to be tested.

## Return Values

*Type:* T or nil

T if the curve is periodic; otherwise
nil.

## Examples

Determine if the ellipse used to demonstrate
vlax-curve-getArea is periodic:

```
(vlax-curve-isPeriodic ellipseObj)
T
```

Determine if the spline used to demonstrate vlax-curve-getDistAtParam is periodic:

```
(vlax-curve-isPeriodic splineObj)
nil
```

#### Related References

* [vlax-curve-isClosed (AutoLISP/ActiveX)](vlax-curve-isClosed-AutoLISP-ActiveX.md)
* [vlax-curve-isPlanar (AutoLISP/ActiveX)](vlax-curve-isPlanar-AutoLISP-ActiveX.md)
* [vlax-curve-getArea (AutoLISP/ActiveX)](vlax-curve-getArea-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*