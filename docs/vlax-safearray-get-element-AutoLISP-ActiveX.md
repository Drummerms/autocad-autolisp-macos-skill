# vlax-safearray-get-element (AutoLISP/ActiveX)

Returns an element from an array

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-safearray-get-element var element ...)
```

*var*
:   *Type:* Safearray

    A variable containing a safearray.

*element ...*
:   *Type:* Integer

    Numeric values specifying the indexes of the element to be retrieved. For an array with one dimension, specify a single integer.
    For multi-dimension arrays, specify as many indexes as there are dimensions.

## Return Values

*Type:* Integer, Real, String, VLA-object, Safearray, Variant, T, or nil

The value of the element.

## Examples

Create an array with two dimensions, each dimension starting at index 1:

```
(setq matrix (vlax-make-safearray vlax-vbString '(1 . 2) '(1 . 2) ))
#<safearray...>
```

Use
vlax-safearray-put-element to populate the array:

```
(vlax-safearray-put-element matrix 1 1 "a")
"a"

(vlax-safearray-put-element matrix 1 2 "b")
"b"

(vlax-safearray-put-element matrix 2 1 "c")
"c"

(vlax-safearray-put-element matrix 2 2 "d")
"d"
```

Use
vlax-safearray-get-element to retrieve the second element in the first dimension of the array:

```
(vlax-safearray-get-element matrix 1 2)
"b"
```

#### Related References

* [vlax-make-safearray (AutoLISP/ActiveX)](vlax-make-safearray-AutoLISP-ActiveX.md)
* [vlax-safearray->list (AutoLISP/ActiveX)](vlax-safearray-list-AutoLISP-ActiveX.md)
* [vlax-safearray-fill (AutoLISP/ActiveX)](vlax-safearray-fill-AutoLISP-ActiveX.md)
* [vlax-safearray-get-dim (AutoLISP/ActiveX)](vlax-safearray-get-dim-AutoLISP-ActiveX.md)
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