# vlax-safearray-type (AutoLISP/ActiveX)

Returns the data type of a safearray

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-safearray-type var)
```

*var*
:   *Type:* Safearray

    A variable containing a safearray.

## Return Values

*Type:* Integer or error

If
*var* contains a safearray, one of the following numeric values is returned:

*2* -- Integer (vlax-vbInteger)

*3* -- Long integer (vlax-vbLong)

*4* -- Single-precision floating-point number (vlax-vbSingle)

*5* -- Double-precision floating-point number (vlax-vbDouble)

*8* -- String (vlax-vbString)

*9* -- Object (vlax-vbObject)

*11* -- Boolean (vlax-vbBoolean)

*12* -- Variant (vlax-vbVariant)

If
*var* does not contain a safearray, an error results.

## Examples

Create a single-dimension array of doubles and a two-dimension array of strings:

```
(setq point (vlax-make-safearray vlax-vbDouble '(0 . 2)))
#<safearray...>

(setq matrix (vlax-make-safearray vlax-vbString '(1 . 2) '(1 . 2) ))
#<safearray...>
```

Use
vlax-safearray-type to verify the data type of the safearrays:

```
(vlax-safearray-type point)
5

(vlax-safearray-type matrix)
8
```

#### Related References

* [vlax-make-safearray (AutoLISP/ActiveX)](vlax-make-safearray-AutoLISP-ActiveX.md)
* [vlax-safearray->list (AutoLISP/ActiveX)](vlax-safearray-list-AutoLISP-ActiveX.md)
* [vlax-safearray-fill (AutoLISP/ActiveX)](vlax-safearray-fill-AutoLISP-ActiveX.md)
* [vlax-safearray-get-dim (AutoLISP/ActiveX)](vlax-safearray-get-dim-AutoLISP-ActiveX.md)
* [vlax-safearray-get-element (AutoLISP/ActiveX)](vlax-safearray-get-element-AutoLISP-ActiveX.md)
* [vlax-safearray-get-l-bound (AutoLISP/ActiveX)](vlax-safearray-get-l-bound-AutoLISP-ActiveX.md)
* [vlax-safearray-get-u-bound (AutoLISP/ActiveX)](vlax-safearray-get-u-bound-AutoLISP-ActiveX.md)
* [vlax-safearray-put-element (AutoLISP/ActiveX)](vlax-safearray-put-element-AutoLISP-ActiveX.md)
* [list (AutoLISP)](list-AutoLISP.md)

#### Related Concepts

* [Data Conversion Functions Reference (AutoLISP/ActiveX)](Data-Conversion-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*