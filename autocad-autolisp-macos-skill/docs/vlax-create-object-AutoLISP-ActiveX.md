# vlax-create-object (AutoLISP/ActiveX)

Creates a new instance of an application object

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Syntax

```
(vlax-create-object prog-id)
```

*prog-id*
:   *Type:* String

    Programmatic identifier of the desired ActiveX object. The format of
    *prog-id* is

    <*Vendor*>.<*Component*>.<*Version*>

    For example:

    AutoCAD.AcCmColor.25

## Return Values

*Type:* VLA-object

The application object.

## Remarks

Use
vlax-create-object when you want a new instance of an application to be started, and an object of the type specified by <*Component*> (see the argument description) to be created. To use the current instance, use
vlax-get-object. However, if an application object has registered itself as a single-instance object, only one instance of the object is
created, no matter how many times you call
vlax-create-object.

## Examples

Create an instance of a Microsoft Excel application:

```
(vlax-create-object "Excel.Application")
#<VLA-OBJECT _Application 0017b894>
```

#### Related References

* [vlax-get-object (AutoLISP/ActiveX)](vlax-get-object-AutoLISP-ActiveX.md)
* [vlax-get-or-create-object (AutoLISP/ActiveX)](vlax-get-or-create-object-AutoLISP-ActiveX.md)
* [vlax-get-property (AutoLISP/ActiveX)](vlax-get-property-AutoLISP-ActiveX.md)
* [vlax-invoke-method (AutoLISP/ActiveX)](vlax-invoke-method-AutoLISP-ActiveX.md)
* [vlax-method-applicable-p (AutoLISP/ActiveX)](vlax-method-applicable-p-AutoLISP-ActiveX.md)
* [vlax-property-available-p (AutoLISP/ActiveX)](vlax-property-available-p-AutoLISP-ActiveX.md)
* [vlax-put-property (AutoLISP/ActiveX)](vlax-put-property-AutoLISP-ActiveX.md)
* [vlax-release-object (AutoLISP/ActiveX)](vlax-release-object-AutoLISP-ActiveX.md)

#### Related Concepts

* [Drawing Object Functions Reference (AutoLISP/ActiveX)](Drawing-Object-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*