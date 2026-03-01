# vlax-curve-getArea (AutoLISP/ActiveX)

Returns the area inside the curve

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-curve-getArea curve-obj)
```

*curve-obj*
:   *Type:* VLA-object

    The object to be measured.

## Return Values

*Type:* Real or nil

A numeric value representing the area of the curve, if successful; otherwise
nil.

## Examples

Assume the curve being measured is the ellipse in the following drawing:

![](../images/GUID-72EE416E-A773-4477-8D39-7AD153DF816B-low.png)

Sample curve (ellipse) for
vlax-curve-getArea

The
ellipseObj variable points to the ellipse VLA-object.

The following command obtains the area of the curve:

```
(vlax-curve-getArea ellipseObj)
4.712393
```

#### Related References

* [vlax-curve-isClosed (AutoLISP/ActiveX)](vlax-curve-isClosed-AutoLISP-ActiveX.md)
* [vlax-curve-isPeriodic (AutoLISP/ActiveX)](vlax-curve-isPeriodic-AutoLISP-ActiveX.md)
* [vlax-curve-isPlanar (AutoLISP/ActiveX)](vlax-curve-isPlanar-AutoLISP-ActiveX.md)

#### Related Concepts

* [Curve Measurement Functions Reference (AutoLISP/ActiveX)](Curve-Measurement-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*