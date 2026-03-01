# vlax-property-available-p (AutoLISP/ActiveX)

Determines if an object has a specified property

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-property-available-p obj prop [check-modify])
```

*obj*
:   *Type:* VLA-object

    An object.

*property*
:   *Type:* Symbol or String

    Name of the property to be checked.

*check-modify*
:   *Type:* T

    If
    T is specified for this argument,
    vlax-property-available-p also checks that the property can be modified.

## Return Values

*Type:* T or nil

T, if the object has the specified property; otherwise
nil. If
T is specified for the
*check-modify* argument,
vlax-property-available-p returns
nil if either the property is not available
*or* the property cannot be modified.

## Examples

The following examples apply to a LightweightPolyline object:

```
(vlax-property-available-p WhatsMyLine 'Color)
T

(vlax-property-available-p WhatsMyLine 'center)
nil
```

The following examples apply to a Circle object:

```
(vlax-property-available-p myCircle 'area)
T
```

Note how supplying the optional third argument changes the result:

```
(vlax-property-available-p myCircle 'area T)
nil
```

The function returns
nil because, although the circle has an “area” property, that property cannot be modified.

#### Related References

* [vlax-dump-object (AutoLISP/ActiveX)](vlax-dump-object-AutoLISP-ActiveX.md)
* [vlax-ename->vla-object (AutoLISP/ActiveX)](vlax-ename-vla-object-AutoLISP-ActiveX.md)
* [vlax-get-property (AutoLISP/ActiveX)](vlax-get-property-AutoLISP-ActiveX.md)
* [vlax-put-property (AutoLISP/ActiveX)](vlax-put-property-AutoLISP-ActiveX.md)

#### Related Concepts

* [About VLA-objects (AutoLISP/ActiveX)](About-VLA-objects-AutoLISP-ActiveX.md)
* [Property-Handling Functions Reference (AutoLISP/ActiveX)](Property-Handling-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*