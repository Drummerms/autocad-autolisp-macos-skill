# vlax-object-released-p (AutoLISP/ActiveX)

Determines if an object has been released

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-object-released-p obj)
```

*obj*
:   *Type:* VLA-object

    An object.

## Return Values

*Type:* T or nil

T, if the object is released (no AutoCAD drawing object is attached to
*obj*);
nil if the object has not been released.

## Remarks

NOTE:Erasing a VLA-object (using
command with the AutoCAD ERASE command or
vla-erase) does not release the object. A VLA-object is not released until you invoke
vlax-release-object on the object, or normal AutoLISP garbage collection occurs, or the drawing database is destroyed at the end of the drawing
session.

## Examples

Attach a Microsoft Excel application to the current AutoCAD drawing:

```
(setq excelobj (vlax-get-object "Excel.Application"))
#<VLA-OBJECT _Application 00168a54>
```

Release the Excel object:

```
(vlax-release-object excelobj)
1
```

Issue
vlax-object-released-p to verify the object was released:

```
(vlax-object-released-p excelobj)
T
```

#### Related References

* [vlax-create-object (AutoLISP/ActiveX)](vlax-create-object-AutoLISP-ActiveX.md)
* [vlax-dump-object (AutoLISP/ActiveX)](vlax-dump-object-AutoLISP-ActiveX.md)
* [vlax-get-object (AutoLISP/ActiveX)](vlax-get-object-AutoLISP-ActiveX.md)
* [vlax-get-or-create-object (AutoLISP/ActiveX)](vlax-get-or-create-object-AutoLISP-ActiveX.md)
* [vlax-release-object (AutoLISP/ActiveX)](vlax-release-object-AutoLISP-ActiveX.md)

#### Related Concepts

* [About VLA-objects (AutoLISP/ActiveX)](About-VLA-objects-AutoLISP-ActiveX.md)
* [Object-Handling Functions Reference (AutoLISP/ActiveX)](Object-Handling-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*