# vlax-ldata-get (AutoLISP/ActiveX)

Retrieves LISP data from a drawing dictionary or an object

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-ldata-get dict key [default-data [private]])
```

*dict*
:   *Type:* VLA-object or String

    An object, an AutoCAD drawing entity object, or a string naming a global dictionary.

*key*
:   *Type:* String

    Dictionary key.

*default-data*
:   *Type:* Integer, Real, String, List, Ename (entity name), VLA-object, Variant, Safearray, T, or nil

    LISP data to be returned if no matching key exists in the dictionary.

*private*
:   *Type:* T or nil

    If a non-nil value is specified for
    *private* and
    vlax-ldata-get is called from a separate-namespace VLX,
    vlax-ldata-get retrieves private LISP data from
    *dict*.

    If you specify
    *private*, you must also specify
    *default-data*; you can use
    nil for
    *default-data*.

## Return Values

*Type:* Integer, Real, String, List, Ename (entity name), VLA-object, Variant, Safearray, T, or nil

The value of the
*key* item.

## Remarks

Note that a separate-namespace VLX can store both private and non-private data using the same
*dict* and
*key*. The private data can be accessed only by the same VLX, but any application can retrieve the non-private data.

## Examples

```
(vlax-ldata-put "mydict" "mykey" "Mumbo Dumbo")
"Mumbo Dumbo"

(vlax-ldata-get "mydict" "mykey")
"Mumbo Dumbo"
```

#### Related References

* [vlax-ldata-delete (AutoLISP/ActiveX)](vlax-ldata-delete-AutoLISP-ActiveX.md)
* [vlax-ldata-list (AutoLISP/ActiveX)](vlax-ldata-list-AutoLISP-ActiveX.md)
* [vlax-ldata-put (AutoLISP/ActiveX)](vlax-ldata-put-AutoLISP-ActiveX.md)
* [vlax-ldata-test (AutoLISP/ActiveX)](vlax-ldata-test-AutoLISP-ActiveX.md)

#### Related Concepts

* [Dictionary Functions Reference (AutoLISP/ActiveX)](Dictionary-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*