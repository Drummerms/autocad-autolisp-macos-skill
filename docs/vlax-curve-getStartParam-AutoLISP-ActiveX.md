# vlax-curve-getStartParam (AutoLISP/ActiveX)

Returns the start parameter on the curve

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-getStartParam curve-obj)
```

*curve-obj*
:   *Type:* VLA-object

    The object to be measured.

## Return Values

*Type:* Real or nil

A number representing the start parameter, if successful; otherwise
nil.

## Examples

Assuming that
ellipseObj points to the ellipse shown in the example for
vlax-curve-getArea, determine the start parameter of the curve:

```
(vlax-curve-getstartparam ellipseObj)
0.0
```

#### Related References

* [vlax-curve-getEndParam (AutoLISP/ActiveX)](vlax-curve-getEndParam-AutoLISP-ActiveX.md)
* [vlax-curve-getEndPoint (AutoLISP/ActiveX)](vlax-curve-getEndPoint-AutoLISP-ActiveX.md)
* [vlax-curve-getStartPoint (AutoLISP/ActiveX)](vlax-curve-getStartPoint-AutoLISP-ActiveX.md)
* [vlax-curve-getFirstDeriv (AutoLISP/ActiveX)](vlax-curve-getFirstDeriv-AutoLISP-ActiveX.md)
* [vlax-curve-getSecondDeriv (AutoLISP/ActiveX)](vlax-curve-getSecondDeriv-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*