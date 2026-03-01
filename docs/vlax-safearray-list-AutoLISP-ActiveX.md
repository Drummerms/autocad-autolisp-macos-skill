# vlax-safearray->list (AutoLISP/ActiveX)

Returns the elements of a safearray in list form

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlax-safearray->list var)
```

*var*
:   *Type:* Safearray

    A variable containing a safearray.

## Return Values

*Type:* List or nil

A list containing the elements of the safearray.

## Examples

Create a single-dimension array of doubles:

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

Convert the array to a list:

```
(setq pointlist (vlax-safearray->list point))
(100.0 100.0 0.0)
```

The following example demonstrates how a two-dimension array of strings is displayed by
vlax-safearray->list:

```
(vlax-safearray->list matrix)
(("a" "b") ("c" "d"))
```

#### Related References

* [vlax-make-safearray (AutoLISP/ActiveX)](vlax-make-safearray-AutoLISP-ActiveX.md)
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