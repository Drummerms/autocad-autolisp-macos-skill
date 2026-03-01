# vlax-make-safearray (AutoLISP/ActiveX)

Creates a safearray

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-make-safearray type '(l-bound . u-bound) ['(l-bound . u-bound) ...)]
```

*type*
:   *Type:* Integer

    The type of safearray. Specify one of the following constants:

    *vlax-vbInteger* (2) -- Integer

    *vlax-vbLong* (3) -- Long integer

    *vlax-vbSingle* (4) -- Single-precision floating-point number

    *vlax-vbDouble* (5) -- Double-precision floating-point number

    *vlax-vbString* (8) -- String

    *vlax-vbObject* (9) -- Object

    *vlax-vbBoolean* (11) -- Boolean

    *vlax-vbVariant* (12) -- Variant

    The integer shown in parentheses indicates the value to which the constant evaluates. It is recommended that you specify the
    constant in your argument, not the integer value, in case the value changes in later releases of AutoCAD.

*'(l-bound . u-bound)*
:   *Type:* Integer

    Lower and upper index boundaries of a dimension.

## Return Values

*Type:* Safearray

The safearray created.

## Remarks

A maximum of 16 dimensions can be defined for an array. The elements in the array are initialized as follows:

Numbers
:   0

Strings
:   Zero-length string.

Booleans
:   :vlax-false

Object
:   nil

Variant
:   Uninitialized (vlax-vbEmpty)

## Examples

Create a single-dimension safearray consisting of doubles, beginning with index 0:

```
(setq point (vlax-make-safearray vlax-vbDouble '(0 . 3)))
#<safearray...>
```

Use the
vlax-safearray->list function to display the contents of the safearray as a list:

```
(vlax-safearray->list point)
(0.0 0.0 0.0 0.0)
```

The result shows each element of the array was initialized to zero.

Create a two-dimension array of strings, with each dimension starting at index 1:

```
(setq matrix (vlax-make-safearray vlax-vbString '(1 . 2) '(1 . 2) ))
#<safearray...>
```

#### Related References

* [vlax-safearray->list (AutoLISP/ActiveX)](vlax-safearray-list-AutoLISP-ActiveX.md)
* [vlax-safearray-fill (AutoLISP/ActiveX)](vlax-safearray-fill-AutoLISP-ActiveX.md)
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