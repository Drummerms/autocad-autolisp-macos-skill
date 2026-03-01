# vlax-put-property (AutoLISP/ActiveX)

Sets the property of an ActiveX object

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-put-property obj property arg)
```

*obj*
:   *Type:* VLA-object

    An object.

*property*
:   *Type:* Symbol or String

    Name of the property to be set.

*arg*
:   *Type:* Integer, Real, String, VLA-object, Safearray, Variant, T, or nil

    The value to be set.

## Return Values

*Type:* nil or error

nil, if successful; otherwise, an error occurs.

## Remarks

This function was formerly known as
vlax-put.

## Examples

Color an object red:

```
(vlax-put-property vlaobj 'Color 1)
nil
```

#### Related References

* [vlax-dump-object (AutoLISP/ActiveX)](vlax-dump-object-AutoLISP-ActiveX.md)
* [vlax-ename->vla-object (AutoLISP/ActiveX)](vlax-ename-vla-object-AutoLISP-ActiveX.md)
* [vlax-get-property (AutoLISP/ActiveX)](vlax-get-property-AutoLISP-ActiveX.md)
* [vlax-property-available-p (AutoLISP/ActiveX)](vlax-property-available-p-AutoLISP-ActiveX.md)

#### Related Concepts

* [About VLA-objects (AutoLISP/ActiveX)](About-VLA-objects-AutoLISP-ActiveX.md)
* [Property-Handling Functions Reference (AutoLISP/ActiveX)](Property-Handling-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*