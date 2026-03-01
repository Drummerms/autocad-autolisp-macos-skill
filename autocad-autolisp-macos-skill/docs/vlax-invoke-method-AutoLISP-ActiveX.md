# vlax-invoke-method (AutoLISP/ActiveX)

Calls the specified ActiveX method

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-invoke-method obj method arg [arg ...])
```

*obj*
:   *Type:* VLA-object

    An object.

*method*
:   *Type:* Symbol or String

    A symbol or string naming the method to be called.

*arg*
:   *Type:* Integer, Real, String, List, VLA-object, Variant, Safearray, T, or nil

    Argument to be passed to the method called. No argument type checking is performed.

## Return Values

*Type:* Integer, Real, String, List, VLA-object, Variant, Safearray, T, or nil

Depends on the method invoked.

## Remarks

This function was known as
vlax-invoke prior to AutoCAD 2000.

## Examples

The following example uses the
AddCircle method to draw a circle in the current AutoCAD drawing.

The first argument to AddCircle specifies the location of the center of the circle. The method requires the center to be specified
as a variant containing a three-element array of doubles. You can use
vlax-3d-point to convert an AutoLISP point list to the required variant data type:

```
(setq circCenter (vlax-3d-point '(3.0 3.0 0.0)))
#<variant 8197 ...>
```

Now use
vlax-invoke-method to draw a circle with the
AddCircle method:

```
(setq mycircle (vlax-invoke-method mspace 'AddCircle circCenter 3.0))
#<VLA-OBJECT IAcadCircle 00bfd6e4>
```

#### Related References

* [vlax-dump-object (AutoLISP/ActiveX)](vlax-dump-object-AutoLISP-ActiveX.md)
* [vlax-ename->vla-object (AutoLISP/ActiveX)](vlax-ename-vla-object-AutoLISP-ActiveX.md)
* [vlax-get-property (AutoLISP/ActiveX)](vlax-get-property-AutoLISP-ActiveX.md)
* [vlax-method-applicable-p (AutoLISP/ActiveX)](vlax-method-applicable-p-AutoLISP-ActiveX.md)
* [vlax-put-property (AutoLISP/ActiveX)](vlax-put-property-AutoLISP-ActiveX.md)

#### Related Concepts

* [About VLA-objects (AutoLISP/ActiveX)](About-VLA-objects-AutoLISP-ActiveX.md)
* [Method Invocation Functions Reference (AutoLISP/ActiveX)](Method-Invocation-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*