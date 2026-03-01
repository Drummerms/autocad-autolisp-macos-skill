# vlax-variant-change-type (AutoLISP/ActiveX)

Returns the value of a variant after changing it from one data type to another

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-variant-change-type var type)
```

*var*
:   *Type:* Variant

    A variable containing a variant.

*type*
:   *Type:* Integer

    The type of variant to return, using the value of
    *var* (the value of
    *var* is unchanged). The
    *type* value can be represented by one of the following constants:

    *vlax-vbEmpty* (0) -- Uninitialized

    *vlax-vbNull* (1) -- Contains no valid data

    *vlax-vbInteger* (2) -- Integer

    *vlax-vbLong* (3) -- Long integer

    *vlax-vbSingle* (4) -- Single-precision floating-point number

    *vlax-vbDouble* (5) -- Double-precision floating-point number

    *vlax-vbString* (8) -- String

    *vlax-vbObject* (9) -- Object

    *vlax-vbBoolean* (11) -- Boolean

    *vlax-vbArray* (8192) -- Array

    The integer shown in parentheses indicates the value to which the constant evaluates. It is recommended that you specify the
    constant in your argument, not the integer value, in case the value changes in later releases of AutoCAD.

## Return Values

*Type:* Integer, Real, String, VLA-object, safearray, T, or nil

The value of
*var*, after converting it to the specified variant type; otherwise
nil, if
*var* could not be converted to the specified type.

## Remarks

The
vlax-variant-change-type function returns the value of the specified variable after converting that value to the specified variant type.

## Examples

Set a variable named
varint to a variant value:

```
(setq variant (vlax-make-variant 5))
#<variant 3 5>
```

Set a variable named
variantStr to the value contained in
variant, but convert that value to a string:

```
(setq variantStr (vlax-variant-change-type variant vlax-vbstring))
#<variant 8 5>
```

Check the value of
variantStr:

```
(vlax-variant-value variantStr)
"5"
```

This confirms that
variantStr contains a string.

#### Related References

* [vlax-make-variant (AutoLISP/ActiveX)](vlax-make-variant-AutoLISP-ActiveX.md)
* [vlax-variant-type (AutoLISP/ActiveX)](vlax-variant-type-AutoLISP-ActiveX.md)
* [vlax-variant-value (AutoLISP/ActiveX)](vlax-variant-value-AutoLISP-ActiveX.md)

#### Related Concepts

* [Data Conversion Functions Reference (AutoLISP/ActiveX)](Data-Conversion-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*