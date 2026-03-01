# vlax-for (AutoLISP/ActiveX)

Iterates through a collection of objects, evaluating each expression

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-for symbol collection [expression1 [expression2 ...]])
```

*symbol*
:   *Type:* VLA-object

    A symbol to be assigned to each VLA-object in a collection.

*collection*
:   *Type:* VLA-object

    A VLA-object representing a collection object.

*expression1*, *expression2...*
:   *Type:* List, Subroutine, or Symbol

    The expressions to be evaluated.

## Return Values

*Type:* Integer, Real, String, List, VLA-object, Variant, Safearray, T, or nil

The value of the last expression evaluated for the last object in the collection.

## Examples

The following code issues
vlax-dump-object on every drawing object in the model space:

```
(vl-load-com)                        ; load ActiveX support
(vlax-for for-item
   (vla-get-modelspace
        (vla-get-activedocument (vlax-get-acad-object))
   )
  (vlax-dump-object for-item)        ; list object properties
)
```

#### Related References

* [vlax-dump-object (AutoLISP/ActiveX)](vlax-dump-object-AutoLISP-ActiveX.md)
* [vlax-map-collection (AutoLISP/ActiveX)](vlax-map-collection-AutoLISP-ActiveX.md)

#### Related Concepts

* [Collection Manipulation Functions Reference (AutoLISP/ActiveX)](Collection-Manipulation-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*