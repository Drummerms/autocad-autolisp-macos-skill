# vlax-ldata-test (AutoLISP/ActiveX)

Determines if data can be saved over a session boundary

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-ldata-test data)
```

*data*
:   *Type:* Integer, Real, String, List, Ename (entity name), VLA-object, Variant, Safearray, T, or nil

    Any LISP data to be tested.

## Return Values

*Type:* T or nil

T, if the data can be saved and restored over the session boundary; otherwise
nil.

## Examples

Determine if a string can be saved as ldata over a session boundary:

```
(vlax-ldata-test "Gumbo jumbo")
T
```

Determine if a function can be saved as ldata over a session boundary:

```
(vlax-ldata-test yinyang)
nil
```

#### Related References

* [vlax-ldata-delete (AutoLISP/ActiveX)](vlax-ldata-delete-AutoLISP-ActiveX.md)
* [vlax-ldata-get (AutoLISP/ActiveX)](vlax-ldata-get-AutoLISP-ActiveX.md)
* [vlax-ldata-list (AutoLISP/ActiveX)](vlax-ldata-list-AutoLISP-ActiveX.md)
* [vlax-ldata-put (AutoLISP/ActiveX)](vlax-ldata-put-AutoLISP-ActiveX.md)

#### Related Concepts

* [Dictionary Functions Reference (AutoLISP/ActiveX)](Dictionary-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*