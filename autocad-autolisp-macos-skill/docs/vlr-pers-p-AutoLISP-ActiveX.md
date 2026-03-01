# vlr-pers-p (AutoLISP/ActiveX)

Determines whether a reactor is persistent

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-pers-p reactor)
```

*reactor*
:   *Type:* VLR object

    An object.

## Return Values

*Type:* VLR object or nil

The specified reactor object, if it is persistent;
nil, if the reactor is transient.

## Examples

Make a reactor persistent:

```
(vlr-pers circleReactor)
#<VLR-Object-Reactor>
```

Verify that a reactor is persistent:

```
(vlr-pers-p circleReactor)
#<VLR-Object-Reactor>
```

Change the persistent reactor to transient:

```
(vlr-pers-release circleReactor)
#<VLR-Object-Reactor>
```

Verify that the reactor is no longer persistent:

```
(vlr-pers-p circleReactor)
nil
```

#### Related References

* [vlr-pers-list (AutoLISP/ActiveX)](vlr-pers-list-AutoLISP-ActiveX.md)
* [vlr-pers (AutoLISP/ActiveX)](vlr-pers-AutoLISP-ActiveX.md)
* [vlr-pers-release (AutoLISP/ActiveX)](vlr-pers-release-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*