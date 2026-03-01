# vlax-variant-value (AutoLISP/ActiveX)

Returns the value of a variant

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-variant-value var)
```

*var*
:   *Type:* Variant

    A variable containing a variant.

## Return Values

*Type:* Integer, Real, String, VLA-object, Safearray, T, or nil

The value of the variable. If the variable does not contain a variant, an error occurs.

## Examples

```
(vlax-variant-value varstr)
"ghost"

(vlax-variant-value varint)
5

(vlax-variant-value notvar)
; *** ERROR: bad argument type: variantp 6.0
```

The last example results in an error, because
notvar does not contain a variant.

#### Related References

* [vlax-make-variant (AutoLISP/ActiveX)](vlax-make-variant-AutoLISP-ActiveX.md)
* [vlax-variant-change-type (AutoLISP/ActiveX)](vlax-variant-change-type-AutoLISP-ActiveX.md)
* [vlax-variant-type (AutoLISP/ActiveX)](vlax-variant-type-AutoLISP-ActiveX.md)

#### Related Concepts

* [Data Conversion Functions Reference (AutoLISP/ActiveX)](Data-Conversion-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*