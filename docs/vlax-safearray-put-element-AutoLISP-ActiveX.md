# vlax-safearray-put-element (AutoLISP/ActiveX)

Adds an element to an array

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-safearray-put-element var index ... value)
```

*var*
:   *Type:* Safearray

    A variable containing a safearray.

*index ...*
:   *Type:* Integer

    A set of index values pointing to the element you are assigning a value to. For a single-dimension array, specify one index
    value; for a two-dimension array, specify two index values, and so on.

*value*
:   *Type:* Integer, Real, String, VLA-object, Safearray, Variant, T, or nil

    The value to assign the safearray element.

## Return Values

*Type:* Integer, Real, String, VLA-object, Safearray, Variant, T, or nil

The
*value* assigned to the element.

## Examples

Create a single-dimension array consisting of doubles:

```
(setq point (vlax-make-safearray vlax-vbDouble '(0 . 2)))
#<safearray...>
```

Use
vlax-safearray-put-element to populate the array:

```
(vlax-safearray-put-element point 0 100)
100

(vlax-safearray-put-element point 1 100)
100

(vlax-safearray-put-element point 2 0)
0
```

Create a two-dimension array consisting of strings:

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

Note that you can also populate arrays using the
vlax-safearray-fill function. The following function call accomplishes the same task as three
vlax-safearray-put-element calls:

```
(vlax-safearray-fill matrix '(("a" "b") ("c" "d")))
#<safearray...>
```

#### Related References

* [vlax-make-safearray (AutoLISP/ActiveX)](vlax-make-safearray-AutoLISP-ActiveX.md)
* [vlax-safearray->list (AutoLISP/ActiveX)](vlax-safearray-list-AutoLISP-ActiveX.md)
* [vlax-safearray-fill (AutoLISP/ActiveX)](vlax-safearray-fill-AutoLISP-ActiveX.md)
* [vlax-safearray-get-dim (AutoLISP/ActiveX)](vlax-safearray-get-dim-AutoLISP-ActiveX.md)
* [vlax-safearray-get-element (AutoLISP/ActiveX)](vlax-safearray-get-element-AutoLISP-ActiveX.md)
* [vlax-safearray-get-l-bound (AutoLISP/ActiveX)](vlax-safearray-get-l-bound-AutoLISP-ActiveX.md)
* [vlax-safearray-get-u-bound (AutoLISP/ActiveX)](vlax-safearray-get-u-bound-AutoLISP-ActiveX.md)
* [vlax-safearray-type (AutoLISP/ActiveX)](vlax-safearray-type-AutoLISP-ActiveX.md)
* [list (AutoLISP)](list-AutoLISP.md)

#### Related Concepts

* [Data Conversion Functions Reference (AutoLISP/ActiveX)](Data-Conversion-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*