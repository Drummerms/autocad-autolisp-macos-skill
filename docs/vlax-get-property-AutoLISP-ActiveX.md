# vlax-get-property (AutoLISP/ActiveX)

Retrieves a VLA-object's property

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-get-property object property)
```

*object*
:   *Type:* VLA-object

    An object.

*property*
:   *Type:* Symbol or String

    Name of the property to be retrieved.

## Return Values

*Type:* Integer, Real, String, List, VLA-object, Variant, Safearray, T, or nil

The value of the object's property.

## Remarks

This function was formerly known as
vlax-get.

## Examples

Begin by retrieving a pointer to the root AutoCAD object:

```
(setq acadObject (vlax-get-acad-object))
#<VLA-OBJECT IAcadApplication 00a4b2b4>
```

Get the AutoCAD ActiveDocument property:

```
(setq acadDocument (vlax-get-property acadObject 'ActiveDocument))
#<VLA-OBJECT IAcadDocument 00302a18>
```

The function returns the current document object.

Get the ModelSpace property of the ActiveDocument object:

```
(setq mSpace (vlax-get-property acadDocument 'Modelspace))
#<VLA-OBJECT IAcadModelSpace 00c14b44>
```

The model space object of the current document is returned.

Convert a drawing entity to a VLA-object:

```
(setq vlaobj (vlax-ename->vla-object e))
#<VLA-OBJECT IAcadLWPolyline 0467114c>
```

Get the color property of the object:

```
(vlax-get-property vlaobj 'Color)
256
```

#### Related References

* [vlax-dump-object (AutoLISP/ActiveX)](vlax-dump-object-AutoLISP-ActiveX.md)
* [vlax-ename->vla-object (AutoLISP/ActiveX)](vlax-ename-vla-object-AutoLISP-ActiveX.md)
* [vlax-property-available-p (AutoLISP/ActiveX)](vlax-property-available-p-AutoLISP-ActiveX.md)
* [vlax-put-property (AutoLISP/ActiveX)](vlax-put-property-AutoLISP-ActiveX.md)

#### Related Concepts

* [Property-Handling Functions Reference (AutoLISP/ActiveX)](Property-Handling-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*