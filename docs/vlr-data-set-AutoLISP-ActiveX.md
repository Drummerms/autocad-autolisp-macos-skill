# vlr-data-set (AutoLISP/ActiveX)

Overwrites application-specific data associated with a reactor

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-data-set obj data)
```

*obj*
:   *Type:* VLR object

    A object representing the reactor object whose data is to be overwritten.

*data*
:   *Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

    Any AutoLISP data.

## Return Values

*Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

The
*data* argument.

## Remarks

NOTE:The
vlr-data-set function should be used with care to avoid creation of circular structures.

## Examples

Return the application-specific data value attached to a reactor:

```
(vlr-data circleReactor)
"Circle Reactor"
```

Replace the text string used to identify the reactor:

```
(vlr-data-set circleReactor "Circle Area Reactor")
"Circle Area Reactor"
```

Verify the change:

```
(vlr-data circleReactor)
"Circle Area Reactor"
```

#### Related References

* [vlr-data (AutoLISP/ActiveX)](vlr-data-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*