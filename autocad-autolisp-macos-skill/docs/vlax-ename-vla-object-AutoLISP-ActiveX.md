# vlax-ename->vla-object (AutoLISP/ActiveX)

Transforms an entity to a VLA-object

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-ename->vla-object entname)
```

*entname*
:   *Type:* Ename (entity name)

    An entity name.

## Return Values

*Type:* VLA-object

The object that represents the ename.

## Examples

```
(setq e (car (entsel)))
<Entity name: 27e0540>

(vlax-ename->vla-object e)
#<VLA-OBJECT IAcadLWPolyline 03f713a0>
```

#### Related References

* [vlax-dump-object (AutoLISP/ActiveX)](vlax-dump-object-AutoLISP-ActiveX.md)
* [vlax-method-applicable-p (AutoLISP/ActiveX)](vlax-method-applicable-p-AutoLISP-ActiveX.md)
* [vlax-property-available-p (AutoLISP/ActiveX)](vlax-property-available-p-AutoLISP-ActiveX.md)
* [vlax-vla-object->ename (AutoLISP/ActiveX)](vlax-vla-object-ename-AutoLISP-ActiveX.md)

#### Related Concepts

* [About VLA-objects (AutoLISP/ActiveX)](About-VLA-objects-AutoLISP-ActiveX.md)
* [Object-Handling Functions Reference (AutoLISP/ActiveX)](Object-Handling-Functions-Reference-AutoLISP-ActiveX.md)
* [Drawing Object Functions Reference (AutoLISP/ActiveX)](Drawing-Object-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*