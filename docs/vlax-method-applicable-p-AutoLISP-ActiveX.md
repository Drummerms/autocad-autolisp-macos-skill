# vlax-method-applicable-p (AutoLISP/ActiveX)

Determines if an object supports a particular method

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-method-applicable-p obj method)
```

*obj*
:   *Type:* VLA-object

    An object.

*method*
:   *Type:* Symbol or String

    A symbol or string containing the name of the method to be checked.

## Return Values

*Type:* T or nil

T, if the object supports the method; otherwise
nil.

## Examples

The following commands are issued against a LightweightPolyline object:

```
(vlax-method-applicable-p WhatsMyLine 'copy)
T

(vlax-method-applicable-p WhatsMyLine 'AddBox)
nil
```

#### Related References

* [vlax-dump-object (AutoLISP/ActiveX)](vlax-dump-object-AutoLISP-ActiveX.md)
* [vlax-ename->vla-object (AutoLISP/ActiveX)](vlax-ename-vla-object-AutoLISP-ActiveX.md)
* [vlax-get-property (AutoLISP/ActiveX)](vlax-get-property-AutoLISP-ActiveX.md)
* [vlax-invoke-method (AutoLISP/ActiveX)](vlax-invoke-method-AutoLISP-ActiveX.md)
* [vlax-put-property (AutoLISP/ActiveX)](vlax-put-property-AutoLISP-ActiveX.md)

#### Related Concepts

* [About VLA-objects (AutoLISP/ActiveX)](About-VLA-objects-AutoLISP-ActiveX.md)
* [Method Invocation Functions Reference (AutoLISP/ActiveX)](Method-Invocation-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*