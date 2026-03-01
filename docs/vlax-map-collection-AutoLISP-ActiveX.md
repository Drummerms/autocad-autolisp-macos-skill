# vlax-map-collection (AutoLISP/ActiveX)

Applies a function to all objects in a collection

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-map-collection obj function)
```

*obj*
:   *Type:* VLA-object

    An object representing a collection.

*function*
:   *Type:* Subroutine or Symbol

    A symbol or lambda expression to be applied to
    *obj*.

## Return Values

*Type:* Integer, Real, String, VLA-object, Variant, Safearray, T, or nil

The
*obj* first argument.

## Examples

```
(vlax-map-collection (vla-get-ModelSpace acadDocument) 'vlax-dump-object)
; IAcadLWPolyline: AutoCAD Lightweight Polyline Interface
; Property values:
;   Application (RO) = #<VLA-OBJECT IAcadApplication 00a4ae24>
;   Area (RO) = 2.46556
;   Closed = 0
;   Color = 256
;   ConstantWidth = 0.0
;   Coordinate = ...Indexed contents not shown...
;   Coordinates = (8.49917 7.00155 11.2996 3.73137 14.8 5.74379 ... )
;   Database (RO) = #<VLA-OBJECT IAcadDatabase 01e3da44>
;   Elevation = 0.0
;   Handle (RO) = "53"
;   HasExtensionDictionary (RO) = 0
;   Hyperlinks (RO) = #<VLA-OBJECT IAcadHyperlinks 01e3d7d4>
;   Layer = "0"
;   Linetype = "BYLAYER"
;   LinetypeGeneration = 0
;   LinetypeScale = 1.0
;   Lineweight = -1
;   Normal = (0.0 0.0 1.0)
;   ObjectID (RO) = 28895576
;   ObjectName (RO) = "AcDbPolyline"
;   PlotStyleName = "ByLayer"
;   Thickness = 0.0
;   Visible = -1
T
```

#### Related References

* [vlax-dump-object (AutoLISP/ActiveX)](vlax-dump-object-AutoLISP-ActiveX.md)
* [vlax-for (AutoLISP/ActiveX)](vlax-for-AutoLISP-ActiveX.md)

#### Related Concepts

* [Collection Manipulation Functions Reference (AutoLISP/ActiveX)](Collection-Manipulation-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*