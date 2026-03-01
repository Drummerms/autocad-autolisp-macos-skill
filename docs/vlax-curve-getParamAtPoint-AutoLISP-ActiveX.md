# vlax-curve-getParamAtPoint (AutoLISP/ActiveX)

Returns the parameter of the curve at the point

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-getParamAtPoint curve-obj point)
```

*curve-obj*
:   *Type:* VLA-object

    The object to be measured.

*point*
:   *Type:* List

    A 3D point (in WCS) on
    *curve-obj*.

## Return Values

*Type:* Real or nil

A number representing a parameter, if successful; otherwise
nil.

## Examples

Assuming that
ellipseObj points to the ellipse shown in the example for
vlax-curve-getArea, set OSNAP to tangent and select the point where the line is tangent to the ellipse:

```
(setq selPt (getpoint))
(7.55765 5.55066 0.0)
```

Get the parameter value at the selected point:

```
(vlax-curve-getParamAtPoint ellipseObj selPt)
4.58296
```

#### Related References

* [vlax-curve-getDistAtParam (AutoLISP/ActiveX)](vlax-curve-getDistAtParam-AutoLISP-ActiveX.md)
* [vlax-curve-getDistAtPoint (AutoLISP/ActiveX)](vlax-curve-getDistAtPoint-AutoLISP-ActiveX.md)
* [vlax-curve-getParamAtDist (AutoLISP/ActiveX)](vlax-curve-getParamAtDist-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*