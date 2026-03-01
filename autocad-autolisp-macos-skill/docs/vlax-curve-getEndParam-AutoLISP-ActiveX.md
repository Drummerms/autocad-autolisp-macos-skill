# vlax-curve-getEndParam (AutoLISP/ActiveX)

Returns the parameter of the endpoint of the curve

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-getEndParam curve-obj)
```

*curve-obj*
:   *Type:* VLA-object

    The object to be measured.

## Return Values

*Type:* Real or nil

A number representing an end parameter, if successful; otherwise
nil.

## Examples

The following function call returns the end parameter of the curve:

```
(vlax-curve-getendparam ellipseObj)
6.28319
```

The end parameter is 6.28319 (twice pi).

#### Related References

* [vlax-curve-getEndPoint (AutoLISP/ActiveX)](vlax-curve-getEndPoint-AutoLISP-ActiveX.md)
* [vlax-curve-getStartParam (AutoLISP/ActiveX)](vlax-curve-getStartParam-AutoLISP-ActiveX.md)
* [vlax-curve-getStartPoint (AutoLISP/ActiveX)](vlax-curve-getStartPoint-AutoLISP-ActiveX.md)
* [vlax-curve-getFirstDeriv (AutoLISP/ActiveX)](vlax-curve-getFirstDeriv-AutoLISP-ActiveX.md)
* [vlax-curve-getSecondDeriv (AutoLISP/ActiveX)](vlax-curve-getSecondDeriv-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*