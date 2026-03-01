# vlax-typeinfo-available-p (AutoLISP/ActiveX)

Determines whether TypeLib information is present for the specified type of object

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-typeinfo-available-p obj)
```

*obj*
:   *Type:* VLA-object

    An object.

## Return Values

*Type:* T or nil

T, if TypeLib information is available; otherwise
nil.

## Remarks

AutoLISP requires TypeLib information to determine whether a method or property is available for an object. Some objects may
not have TypeLib information (for example, AcadDocument).

## Examples

N/A

#### Related References

* [vlax-create-object (AutoLISP/ActiveX)](vlax-create-object-AutoLISP-ActiveX.md)
* [vlax-get-object (AutoLISP/ActiveX)](vlax-get-object-AutoLISP-ActiveX.md)
* [vlax-get-or-create-object (AutoLISP/ActiveX)](vlax-get-or-create-object-AutoLISP-ActiveX.md)
* [vlax-import-type-library (AutoLISP/ActiveX)](vlax-import-type-library-AutoLISP-ActiveX.md)

#### Related Concepts

* [Drawing Object Functions Reference (AutoLISP/ActiveX)](Drawing-Object-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*