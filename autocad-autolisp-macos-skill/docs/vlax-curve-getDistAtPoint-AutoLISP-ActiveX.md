# vlax-curve-getDistAtPoint (AutoLISP/ActiveX)

Returns the length of the curve's segment between the curve's start point and the specified point

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-getDistAtPoint curve-obj point)
```

*curve-obj*
:   *Type:* VLA-object

    The object to be measured.

*point*
:   *Type:* List

    A 3D point list (in WCS) on
    *curve-obj*.

## Return Values

*Type:* Real or nil

A number if successful; otherwise
nil.

## Examples

Set OSNAP to tangent and select the point where the line is tangent to the curve:

```
(setq selPt (getpoint))
(4.91438 6.04738 0.0)
```

Determine the distance from the start of the curve to the selected point:

```
(vlax-curve-getDistAtPoint splineObj selpt)
5.17769
```

#### Related References

* [vlax-curve-getDistAtParam (AutoLISP/ActiveX)](vlax-curve-getDistAtParam-AutoLISP-ActiveX.md)
* [vlax-curve-getParamAtDist (AutoLISP/ActiveX)](vlax-curve-getParamAtDist-AutoLISP-ActiveX.md)
* [vlax-curve-getParamAtPoint (AutoLISP/ActiveX)](vlax-curve-getParamAtPoint-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*