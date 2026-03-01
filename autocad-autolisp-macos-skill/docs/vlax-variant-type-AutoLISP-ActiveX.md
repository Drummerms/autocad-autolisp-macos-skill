# vlax-variant-type (AutoLISP/ActiveX)

Determines the data type of a variant

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-variant-type var)
```

*var*
:   *Type:* Variant

    A variable containing a variant.

## Return Values

*Type:* Integer

If
*var* contains a variant, one of the following numeric values is returned:

*0* -- Uninitialized (vlax-vbEmpty)

*1* -- Contains no valid data (vlax-vbNull)

*2* -- Integer (vlax-vbInteger)

*3* -- Long integer (vlax-vbLong)

*4* -- Single-precision floating-point number (vlax-vbSingle)

*5* -- Double-precision floating-point number (vlax-vbDouble)

*8* -- String (vlax-vbString)

*9* -- Object (vlax-vbObject)

*11* -- Boolean (vlax-vbBoolean)

*8192+**n* -- Safearray (vlax-vbArray) of some data type. For example, an array of doubles (vlax-vbDouble) returns 8197 (8192 + 5).

If
*var* does not contain a variant, an error results.

## Examples

Set a variant to
nil and display the variant's data type:

```
(setq varnil (vlax-make-variant nil))
#<variant 0 >

(vlax-variant-type varnil)
0
```

Set a variant to an integer value and explicitly define the variant as an integer data type:

```
(setq varint (vlax-make-variant 5 vlax-vbInteger))
#<variant 2 5>

(vlax-variant-type varint)
2
```

Set a variant to an integer value and display the variant's data type:

```
(setq varint (vlax-make-variant 5))
#<variant 3 5>

(vlax-variant-type varint)
3
```

Notice that without explicitly defining the data type to
vlax-variant-variant, an integer assignment results in a Long integer data type.

Set a variant to a string and display the variant's data type:

```
(setq varstr (vlax-make-variant "ghost"))
#<variant 8 ghost>

(vlax-variant-type varstr)
8
```

Create a safearray of doubles, assign the safearray to a variant, and display the variant's data type:

```
(setq 4dubs (vlax-make-safearray vlax-vbDouble '(0 . 3)))
#<safearray...>

(setq var4dubs (vlax-make-variant 4dubs))
#<variant 8197 ...>

(vlax-variant-type var4dubs)
8197
```

A variant type value greater than 8192 indicates that the variant contains some type of safearray. Subtract 8192 from the
return value to determine the data type of the safearray. In this example, 8197-8192=5 (vlax-vbDouble).

Assign a real value to a variable, then issue
vlax-variant-type to check the variable's data type:

```
(setq notvar 6.0)
6.0

(vlax-variant-type notvar)
; *** ERROR: bad argument type: variantp 6.0
```

This last example results in an error, because the variable passed to
vlax-variant-type does not contain a variant.

#### Related References

* [vlax-make-variant (AutoLISP/ActiveX)](vlax-make-variant-AutoLISP-ActiveX.md)
* [vlax-variant-change-type (AutoLISP/ActiveX)](vlax-variant-change-type-AutoLISP-ActiveX.md)
* [vlax-variant-value (AutoLISP/ActiveX)](vlax-variant-value-AutoLISP-ActiveX.md)

#### Related Concepts

* [Data Conversion Functions Reference (AutoLISP/ActiveX)](Data-Conversion-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*