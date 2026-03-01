# vlax-curve-getStartPoint (AutoLISP/ActiveX)

Returns the start point (in WCS) of the curve

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-getStartPoint curve-obj)
```

*curve-obj*
:   *Type:* VLA-object

    The object to be measured.

## Return Values

*Type:* List or nil

A 3D point representing the start point, if successful; otherwise
nil.

## Examples

Get the start point of the ellipse.

```
(vlax-curve-getStartPoint ellipseObj)
(2.0 2.0 0.0)
```

For an ellipse, the start points and endpoints are the same.

Obtain the start point of the spline used to demonstrate
vlax-curve-getDistAtParam:

```
(vlax-curve-getStartPoint splineObj)
(1.73962 2.12561 0.0)
```

#### Related References

* [vlax-curve-getEndParam (AutoLISP/ActiveX)](vlax-curve-getEndParam-AutoLISP-ActiveX.md)
* [vlax-curve-getEndPoint (AutoLISP/ActiveX)](vlax-curve-getEndPoint-AutoLISP-ActiveX.md)
* [vlax-curve-getStartParam (AutoLISP/ActiveX)](vlax-curve-getStartParam-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*