# vlax-ldata-put (AutoLISP/ActiveX)

Stores LISP data in a drawing dictionary or an object

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-ldata-put dict key data [private])
```

*dict*
:   *Type:* VLA-object or String

    A object, an AutoCAD drawing entity object, or a string naming a global dictionary.

*key*
:   *Type:* String

    Dictionary key.

*data*
:   *Type:* Integer, Real, String, List, Ename (entity name), VLA-object, Variant, Safearray, T, or nil

    LISP data to be stored in the dictionary.

*private*
:   *Type:* T or nil

    If
    vlax-ldata-put is called from a separate-namespace VLX and a non-nil value is specified for
    *private*,
    vlax-ldata-put marks the data as retrievable only by the same VLX.

## Return Values

*Type:* Integer, Real, String, List, Ename (entity name), VLA-object, Variant, Safearray, T, or nil

The value of
*data*.

## Examples

```
(vlax-ldata-put "dict" "key" '(1))
(1)

(vlax-ldata-put "dict" "cay" "Gumbo jumbo")
"Gumbo jumbo"
```

#### Related References

* [vlax-ldata-delete (AutoLISP/ActiveX)](vlax-ldata-delete-AutoLISP-ActiveX.md)
* [vlax-ldata-get (AutoLISP/ActiveX)](vlax-ldata-get-AutoLISP-ActiveX.md)
* [vlax-ldata-list (AutoLISP/ActiveX)](vlax-ldata-list-AutoLISP-ActiveX.md)
* [vlax-ldata-test (AutoLISP/ActiveX)](vlax-ldata-test-AutoLISP-ActiveX.md)

#### Related Concepts

* [Dictionary Functions Reference (AutoLISP/ActiveX)](Dictionary-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*