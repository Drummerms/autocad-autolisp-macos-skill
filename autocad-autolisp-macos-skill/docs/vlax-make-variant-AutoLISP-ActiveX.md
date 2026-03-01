# vlax-make-variant (AutoLISP/ActiveX)

Creates a variant data type

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-make-variant [value [type]])
```

*value*
:   *Type:* Integer, Real, String, VLA-object, Safearray, T, or nil

    The value to be assigned to the variant. If omitted, the variant is created with the
    vlax-vbEmpty type (uninitialized).

*type*
:   *Type:* Integer

    The type of variant. This can be represented by one of the following constants:

    *vlax-vbEmpty*(0) -- Uninitialized (default value)

    *vlax-vbNull*(1) -- Contains no valid data

    *vlax-vbInteger*(2) -- Integer

    *vlax-vbLong*(3) -- Long integer

    *vlax-vbSingle*(4) -- Single-precision floating-point number

    *vlax-vbDouble*(5) -- Double-precision floating-point number

    *vlax-vbString*(8) -- String

    *vlax-vbObject*(9) -- Object

    *vlax-vbBoolean* (11) -- Boolean

    *vlax-vbArray* (8192) -- Array

    The integer shown in parentheses indicates the value to which the constant evaluates. It is recommended that you specify the
    constant in your argument, not the integer value, because the value may change in later releases of AutoCAD.

    If you do not specify a
    *type*,
    vlax-make-variant assigns a default data type based on the data type of the
    *value* it receives. The following list identifies the default variant data type assigned to each LISP data type:

    *nil* --
    vlax-vbEmpty

    *:vlax-null* --
    vlax-vbNull

    *integer* --
    vlax-vbLong

    *real* --
    vlax-vbDouble

    *string* --
    vlax-vbString

    *VLA-object* --
    vlax-vbObject

    *:vlax-true*/*:vlax-false* --
    vlax-vbBoolean

    *variant* -- Same as the type of initial value

    *vlax-make-safearray* --
    vlax-vbArray

## Return Values

*Type:* variant

The variant created.

## Examples

Create a variant using the defaults for
vlax-make-variant:

```
(setq varnil (vlax-make-variant))
#<variant 0 >
```

The function creates an uninitialized (vlax-vbEmpty) variant by default. You can accomplish the same thing explicitly with the following call:

```
(setq varnil (vlax-make-variant nil))
#<variant 0 >
```

Create an integer variant and set its value to 5:

```
(setq varint (vlax-make-variant 5 vlax-vbInteger))
#<variant 2 5>
```

Repeat the previous command, but omit the
*type* argument and see what happens:

```
(setq varint (vlax-make-variant 5))
#<variant 3 5>
```

By default,
vlax-make-variant assigned the specified integer value to a Long integer data type, not Integer, as you might expect. This highlights the importance
of explicitly stating the type of variant you want when working with numbers.

Omitting the
*type* argument for a string produces predictable results:

```
(setq varstr (vlax-make-variant "ghost"))
#<variant 8 ghost>
```

To create a variant containing arrays, you must specify type
vlax-vbArray, along with the type of data in the array. For example, to create a variant containing an array of doubles, first set a variable's
value to an array of doubles:

```
(setq 4dubs (vlax-make-safearray vlax-vbDouble '(0 . 3)))
#<safearray...>
```

Then take the array of doubles and assign it to a variant:

```
(vlax-make-variant 4dubs)
#<variant 8197 ...>
```

#### Related References

* [vlax-variant-change-type (AutoLISP/ActiveX)](vlax-variant-change-type-AutoLISP-ActiveX.md)
* [vlax-variant-type (AutoLISP/ActiveX)](vlax-variant-type-AutoLISP-ActiveX.md)
* [vlax-variant-value (AutoLISP/ActiveX)](vlax-variant-value-AutoLISP-ActiveX.md)

#### Related Concepts

* [Data Conversion Functions Reference (AutoLISP/ActiveX)](Data-Conversion-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*