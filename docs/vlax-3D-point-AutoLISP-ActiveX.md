# vlax-3D-point (AutoLISP/ActiveX)

Creates ActiveX-compatible (variant) 3D point structure

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-3D-point lst)

(vlax-3D-point x y [z])
```

*lst*
:   *Type:* List

    A list of two or three numbers, representing points.

*x*, *y*
:   *Type:* Integer or Real

    Numbers representing
    *X* and
    *Y* coordinates of a point.

*z*
:   *Type:* Integer or Real

    A number representing the
    *Z* coordinate of a point.

## Return Values

*Type:* Variant

A variant containing a three-element array of doubles.

## Examples

```
(vlax-3D-point 5 20)
#<variant 8197 ...>

(vlax-3D-point '(33.6 44.0 90.0))
<variant 8197 ...>
```

#### Related Concepts

* [Data Conversion Functions Reference (AutoLISP/ActiveX)](Data-Conversion-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*