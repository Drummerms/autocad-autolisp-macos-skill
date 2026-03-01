# vlax-get-object (AutoLISP/ActiveX)

Returns a running instance of an application object

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(vlax-get-object prog-id)
```

*prog-id*
:   *Type:* String

    Identifies the desired application object. The format of
    *prog-id* is:

    *appname.objecttype*

    where
    *appname* is the name of the application and
    *objecttype* is the application object. The
    *objecttype* may be followed by a version number.

    NOTE:You can usually find the
    *prog-id* for an application in that application's Help.

## Return Values

*Type:* VLA-object or nil

The application object; otherwise
nil, if there is no instance of the specified object currently running.

## Examples

Obtain the application object for the Excel program:

```
(vlax-get-object "Excel.Application")
#<VLA-OBJECT _Application 0017bb5c>
```

#### Related References

* [vlax-create-object (AutoLISP/ActiveX)](vlax-create-object-AutoLISP-ActiveX.md)
* [vlax-get-or-create-object (AutoLISP/ActiveX)](vlax-get-or-create-object-AutoLISP-ActiveX.md)
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