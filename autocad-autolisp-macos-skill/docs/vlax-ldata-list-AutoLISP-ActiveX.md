# vlax-ldata-list (AutoLISP/ActiveX)

Lists AutoLISP data in a drawing dictionary

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-ldata-list dict [private])
```

*dict*
:   *Type:* VLA-object or String

    An object, an AutoCAD drawing entity object, or a string naming a global dictionary.

*private*
:   *Type:* T or nil

    If
    vlax-ldata-list is called from a separate-namespace VLX and a non-nil value is specified for
    *private*,
    vlax-ldata-list retrieves only private data stored by the same VLX.

## Return Values

*Type:* List

An associative list consisting of pairs (key . value).

## Examples

Use
vlax-ldata-put to store LISP data in a dictionary:

```
(vlax-ldata-put "dict" "cay" "Mumbo Jumbo ")
"Mumbo Jumbo"

(vlax-ldata-put "dict" "say" "Floobar ")
"Floobar"
```

Use
vlax-ldata-list to display the LISP data stored in “dict”:

```
 (vlax-ldata-list "dict")
(("say" . "Floobar") ("cay" . "Mumbo Jumbo"))
```

#### Related References

* [vlax-ldata-delete (AutoLISP/ActiveX)](vlax-ldata-delete-AutoLISP-ActiveX.md)
* [vlax-ldata-get (AutoLISP/ActiveX)](vlax-ldata-get-AutoLISP-ActiveX.md)
* [vlax-ldata-put (AutoLISP/ActiveX)](vlax-ldata-put-AutoLISP-ActiveX.md)
* [vlax-ldata-test (AutoLISP/ActiveX)](vlax-ldata-test-AutoLISP-ActiveX.md)

#### Related Concepts

* [Dictionary Functions Reference (AutoLISP/ActiveX)](Dictionary-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*