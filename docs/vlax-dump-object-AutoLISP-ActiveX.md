# vlax-dump-object (AutoLISP/ActiveX)

Lists an object's properties, and optionally, the methods that apply to the object

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-dump-object obj [flag])
```

*obj*
:   *Type:* VLA-object

    An object.

flag
:   *Type:* T or nil

    If specified and not
    nil,
    vlax-dump-object also lists all methods that apply to
    *obj*.

## Return Values

*Type:* T or error

T, if successful. If an invalid object name is supplied,
vlax-dump-object displays an error message.

## Examples

```
(setq aa (vlax-get-acad-object))
#<VLA-OBJECT IAcadApplication 00b3b91c>

(vlax-dump-object aa)
; IAcadApplication: AutoCAD Application Interface
; Property values:
;   ActiveDocument (RO) = #<VLA-OBJECT IAcadDocument 01b52fac>
;   Application (RO) = #<VLA-OBJECT IAcadApplication 00b3b91c>
;   Caption (RO) = "AutoCAD - [Drawing.dwg]"
.
.
.
T
```

List an object's properties and the methods that apply to the object:

```
(vlax-dump-object aa T)
; IAcadApplication: AutoCAD Application Interface
; Property values:
;   ActiveDocument (RO) = #<VLA-OBJECT IAcadDocument 01b52fac>
;   Application (RO) = #<VLA-OBJECT IAcadApplication 00b3b91c>
;   Caption (RO) = "AutoCAD - [Drawing.dwg]"
.
.
.
; Methods supported:
;   EndUndoMark ()
;   Eval (1)
;   GetInterfaceObject (1)
;   ListAds ()
;   ListArx ()
.
.
.
T
```

#### Related References

* [vlax-method-applicable-p (AutoLISP/ActiveX)](vlax-method-applicable-p-AutoLISP-ActiveX.md)
* [vlax-property-available-p (AutoLISP/ActiveX)](vlax-property-available-p-AutoLISP-ActiveX.md)
* [vlax-ename->vla-object (AutoLISP/ActiveX)](vlax-ename-vla-object-AutoLISP-ActiveX.md)

#### Related Concepts

* [About VLA-objects (AutoLISP/ActiveX)](About-VLA-objects-AutoLISP-ActiveX.md)
* [Object-Handling Functions Reference (AutoLISP/ActiveX)](Object-Handling-Functions-Reference-AutoLISP-ActiveX.md)
* [Drawing Object Functions Reference (AutoLISP/ActiveX)](Drawing-Object-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*