# vlax-ldata-delete (AutoLISP/ActiveX)

Erases LISP data from a drawing dictionary

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-ldata-delete dict key [private])
```

*dict*
:   *Type:* VLA-object or String

    An object, AutoCAD drawing entity object, or a string naming a global dictionary.

*key*
:   *Type:* String

    Dictionary key.

*private*
:   *Type:* T or nil

    If a non-nil value is specified for
    *private* and
    vlax-ldata-delete is called from a separate-namespace VLX,
    vlax-ldata-delete deletes private LISP data from
    *dict*.

## Return Values

*Type:* T or nil

T, if successful; otherwise
nil (for example, the data did not exist).

## Examples

Add LISP data to a dictionary:

```
(vlax-ldata-put "dict" "key" '(1))
(1)
```

Use
vlax-ldata-delete to delete the LISP data:

```
(vlax-ldata-delete "dict" "key")
T
```

If
vlax-ldata-delete is called again to remove the same data, it returns
nil because the data does not exist in the dictionary:

```
(vlax-ldata-delete "dict" "key")
nil
```

#### Related References

* [vlax-ldata-get (AutoLISP/ActiveX)](vlax-ldata-get-AutoLISP-ActiveX.md)
* [vlax-ldata-list (AutoLISP/ActiveX)](vlax-ldata-list-AutoLISP-ActiveX.md)
* [vlax-ldata-put (AutoLISP/ActiveX)](vlax-ldata-put-AutoLISP-ActiveX.md)
* [vlax-ldata-test (AutoLISP/ActiveX)](vlax-ldata-test-AutoLISP-ActiveX.md)

#### Related Concepts

* [Dictionary Functions Reference (AutoLISP/ActiveX)](Dictionary-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*