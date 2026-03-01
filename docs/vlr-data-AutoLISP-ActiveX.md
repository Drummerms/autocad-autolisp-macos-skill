# vlr-data (AutoLISP/ActiveX)

Returns application-specific data associated with a reactor

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-data obj)
```

*obj*
:   *Type:* VLR object

    A object representing the reactor object from which to extract data.

## Return Values

*Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

The application-specific data obtained from the reactor object.

## Examples

The following example obtains a string associated with the
circleReactor VLR object:

```
(vlr-data circleReactor)
"Circle Reactor"
```

#### Related References

* [vlr-data-set (AutoLISP/ActiveX)](vlr-data-set-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*