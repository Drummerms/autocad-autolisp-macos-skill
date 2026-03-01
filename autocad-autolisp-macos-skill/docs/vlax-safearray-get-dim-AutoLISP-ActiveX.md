# vlax-safearray-get-dim (AutoLISP/ActiveX)

Returns the number of dimensions in a safearray object

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-safearray-get-dim var)
```

*var*
:   *Type:* Safearray

    A variable containing a safearray.

## Return Values

*Type:* Integer or nil

A numeric value identifying the number of dimensions in
*var*. An error occurs if
*var* is not a safearray.

## Examples

Set
sa-int to a single-dimension safearray with one dimension:

```
(setq sa-int (vlax-make-safearray vlax-vbinteger '(1 . 4)))
#<safearray...>
```

Use
vlax-safearray-get-dim to return the number of dimensions in
sa-int:

```
(vlax-safearray-get-dim sa-int)
1
```

#### Related References

* [vlax-make-safearray (AutoLISP/ActiveX)](vlax-make-safearray-AutoLISP-ActiveX.md)
* [vlax-safearray->list (AutoLISP/ActiveX)](vlax-safearray-list-AutoLISP-ActiveX.md)
* [vlax-safearray-fill (AutoLISP/ActiveX)](vlax-safearray-fill-AutoLISP-ActiveX.md)
* [vlax-safearray-get-element (AutoLISP/ActiveX)](vlax-safearray-get-element-AutoLISP-ActiveX.md)
* [vlax-safearray-get-l-bound (AutoLISP/ActiveX)](vlax-safearray-get-l-bound-AutoLISP-ActiveX.md)
* [vlax-safearray-get-u-bound (AutoLISP/ActiveX)](vlax-safearray-get-u-bound-AutoLISP-ActiveX.md)
* [vlax-safearray-put-element (AutoLISP/ActiveX)](vlax-safearray-put-element-AutoLISP-ActiveX.md)
* [vlax-safearray-type (AutoLISP/ActiveX)](vlax-safearray-type-AutoLISP-ActiveX.md)
* [list (AutoLISP)](list-AutoLISP.md)

#### Related Concepts

* [Data Conversion Functions Reference (AutoLISP/ActiveX)](Data-Conversion-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*