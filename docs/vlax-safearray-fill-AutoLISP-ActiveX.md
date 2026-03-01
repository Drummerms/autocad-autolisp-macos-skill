# vlax-safearray-fill (AutoLISP/ActiveX)

Stores data in the elements of a safearray

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-safearray-fill var 'element-values)
```

*var*
:   *Type:* Safearray

    A variable containing a safearray.

*'element-values*
:   *Type:* List

    Values to be stored in the array. You can specify as many values as there are elements in the array. If you specify fewer
    values than there are elements, the remaining elements retain their current value.

    For multi-dimension arrays,
    *element-values* must be a list of lists, with each list corresponding to a dimension of the array.

## Return Values

*Type:* List or nil

Value provided in the
*var* argument.

## Examples

Create a single-dimension array of doubles:

```
(setq sa (vlax-make-safearray vlax-vbdouble '(0 . 2)))
#<safearray...>
```

Use
vlax-safearray-fill to populate the array:

```
(vlax-safearray-fill sa '(1 2 3))
#<safearray...>
```

List the contents of the array:

```
(vlax-safearray->list sa)
(1.0 2.0 3.0)
```

Use
vlax-safearray-fill to set the first element in the array:

```
(vlax-safearray-fill sa '(-66))
#<safearray...>
```

List the contents of the array:

```
(vlax-safearray->list sa)
(-66.0 2.0 3.0)
```

Notice that only the first element in the array has been changed; the remaining elements are unaffected and retain the value
you previously set them to. If you need to change the second or third element and leave the first element unaffected, use
vlax-put-element.

Instruct
vlax-safearray-fill to set four elements in an array that contains only three elements:

```
(vlax-safearray-fill sa '(1 2 3 4))
Error: Assertion failed: safearray-fill failed. Too many elements.
```

The
vlax-safearray-fill function returns an error if you specify more elements than the array contains.

To assign values to a multi-dimensional array, specify a list of lists to
vlax-safearray-fill, with each list corresponding to a dimension. The following command creates a two-dimension array of strings containing three
elements in each dimension:

```
(setq mat2 (vlax-make-safearray vlax-vbString '(0 . 1) '(1 . 3)))
#<safearray...>
```

Use
vlax-safearray-fill to populate the array:

```
(vlax-safearray-fill mat2 '(("a" "b" "c") ("d" "e" "f")))
#<safearray...>
```

Call the
vlax-safearray->list function to confirm the contents of
mat2:

```
(vlax-safearray->list mat2)
(("a" "b" "c") ("d" "e" "f"))
```

#### Related References

* [vlax-make-safearray (AutoLISP/ActiveX)](vlax-make-safearray-AutoLISP-ActiveX.md)
* [vlax-safearray->list (AutoLISP/ActiveX)](vlax-safearray-list-AutoLISP-ActiveX.md)
* [vlax-safearray-get-dim (AutoLISP/ActiveX)](vlax-safearray-get-dim-AutoLISP-ActiveX.md)
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