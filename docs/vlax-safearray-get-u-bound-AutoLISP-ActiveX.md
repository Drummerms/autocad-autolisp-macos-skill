# vlax-safearray-get-u-bound (AutoLISP/ActiveX)

Returns the upper boundary (end index) of a dimension of an array

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-safearray-get-u-bound var dim)
```

*var*
:   *Type:* Safearray

    A variable containing a safearray.

*dim*
:   *Type:* Integer

    A dimension of the array. The first dimension is dimension 1.

## Return Values

*Type:* Integer

A numeric value representing the upper boundary (end index) of the dimension. If
*var* is not an array, or
*dim* is invalid (for example, 0, or a number greater than the number of dimensions in the array), an error results.

## Examples

The following examples evaluate a safearray defined as follows:

```
(vlax-make-safearray vlax-vbString '(1 . 2) '(0 . 1) ))
```

Get the end index value of the array's first dimension:

```
(vlax-safearray-get-u-bound tmatrix 1)
2
```

The first dimension ends with index 2.

Get the end index value of the second dimension of the array:

```
(vlax-safearray-get-u-bound tmatrix 2)
1
```

The second dimension starts with index 1.

#### Related References

* [vlax-make-safearray (AutoLISP/ActiveX)](vlax-make-safearray-AutoLISP-ActiveX.md)
* [vlax-safearray->list (AutoLISP/ActiveX)](vlax-safearray-list-AutoLISP-ActiveX.md)
* [vlax-safearray-fill (AutoLISP/ActiveX)](vlax-safearray-fill-AutoLISP-ActiveX.md)
* [vlax-safearray-get-dim (AutoLISP/ActiveX)](vlax-safearray-get-dim-AutoLISP-ActiveX.md)
* [vlax-safearray-get-element (AutoLISP/ActiveX)](vlax-safearray-get-element-AutoLISP-ActiveX.md)
* [vlax-safearray-get-l-bound (AutoLISP/ActiveX)](vlax-safearray-get-l-bound-AutoLISP-ActiveX.md)
* [vlax-safearray-put-element (AutoLISP/ActiveX)](vlax-safearray-put-element-AutoLISP-ActiveX.md)
* [vlax-safearray-type (AutoLISP/ActiveX)](vlax-safearray-type-AutoLISP-ActiveX.md)
* [list (AutoLISP)](list-AutoLISP.md)

#### Related Concepts

* [Data Conversion Functions Reference (AutoLISP/ActiveX)](Data-Conversion-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*