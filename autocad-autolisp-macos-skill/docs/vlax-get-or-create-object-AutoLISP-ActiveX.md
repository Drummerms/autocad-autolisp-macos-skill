# vlax-get-or-create-object (AutoLISP/ActiveX)

Returns a running instance of an application object, or creates a new instance if the application is not currently running

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(vlax-get-or-create-object prog-id)
```

*prog-id*
:   *Type:* String

    Programmatic identifier of the desired ActiveX object. The format of
    *prog-id* is

    <*Vendor*>.<*Component*>.<*Version*>

    For example:

    Excel.Application.16

## Return Values

*Type:* VLA-object

An object.

## Examples

```
(vlax-get-or-create-object "Excel.Application")
#<VLA-OBJECT _Application 0017bb5c>
```

#### Related References

* [vlax-create-object (AutoLISP/ActiveX)](vlax-create-object-AutoLISP-ActiveX.md)
* [vlax-get-object (AutoLISP/ActiveX)](vlax-get-object-AutoLISP-ActiveX.md)
* [vlax-release-object (AutoLISP/ActiveX)](vlax-release-object-AutoLISP-ActiveX.md)
* [vlax-get-property (AutoLISP/ActiveX)](vlax-get-property-AutoLISP-ActiveX.md)
* [vlax-invoke-method (AutoLISP/ActiveX)](vlax-invoke-method-AutoLISP-ActiveX.md)
* [vlax-method-applicable-p (AutoLISP/ActiveX)](vlax-method-applicable-p-AutoLISP-ActiveX.md)
* [vlax-property-available-p (AutoLISP/ActiveX)](vlax-property-available-p-AutoLISP-ActiveX.md)
* [vlax-put-property (AutoLISP/ActiveX)](vlax-put-property-AutoLISP-ActiveX.md)

#### Related Concepts

* [Drawing Object Functions Reference (AutoLISP/ActiveX)](Drawing-Object-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*