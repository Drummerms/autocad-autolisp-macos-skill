# vlax-curve-getParamAtDist (AutoLISP/ActiveX)

Returns the parameter of a curve at the specified distance from the beginning of the curve

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-getParamAtDist curve-obj dist)
```

*curve-obj*
:   *Type:* VLA-object

    The object to be measured.

*dist*
:   *Type:* Integer or Real

    A number specifying the distance from the beginning of the curve.

## Return Values

*Type:* Real or nil

A number representing a parameter, if successful; otherwise
nil.

## Examples

```
(vlax-curve-getParamAtDist splineObj 1.0)
0.685049
```

#### Related References

* [vlax-curve-getDistAtParam (AutoLISP/ActiveX)](vlax-curve-getDistAtParam-AutoLISP-ActiveX.md)
* [vlax-curve-getDistAtPoint (AutoLISP/ActiveX)](vlax-curve-getDistAtPoint-AutoLISP-ActiveX.md)
* [vlax-curve-getParamAtPoint (AutoLISP/ActiveX)](vlax-curve-getParamAtPoint-AutoLISP-ActiveX.md)
* [vlax-curve-getEndParam (AutoLISP/ActiveX)](vlax-curve-getEndParam-AutoLISP-ActiveX.md)
* [vlax-curve-getStartParam (AutoLISP/ActiveX)](vlax-curve-getStartParam-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*