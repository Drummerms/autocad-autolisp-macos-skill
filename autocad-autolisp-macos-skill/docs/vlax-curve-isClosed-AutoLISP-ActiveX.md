# vlax-curve-isClosed (AutoLISP/ActiveX)

Determines if the specified curve is closed (that is, the start point is the same as the endpoint)

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-isClosed curve-obj)
```

*curve-obj*
:   *Type:* VLA-object

    The object to be tested.

## Return Values

*Type:* T or nil

T if the curve is closed; otherwise
nil.

## Examples

Determine if the ellipse used to demonstrate
vlax-curve-getArea is closed:

```
(vlax-curve-isClosed ellipseObj)
T
```

Determine if the spline used to demonstrate
vlax-curve-getDistAtParam is closed:

```
(vlax-curve-isClosed splineObj)
nil
```

#### Related References

* [vlax-curve-isPeriodic (AutoLISP/ActiveX)](vlax-curve-isPeriodic-AutoLISP-ActiveX.md)
* [vlax-curve-isPlanar (AutoLISP/ActiveX)](vlax-curve-isPlanar-AutoLISP-ActiveX.md)
* [vlax-curve-getArea (AutoLISP/ActiveX)](vlax-curve-getArea-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*