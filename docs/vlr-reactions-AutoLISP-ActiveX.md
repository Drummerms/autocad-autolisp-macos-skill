# vlr-reactions (AutoLISP/ActiveX)

Returns a list of pairs (*event-name . callback\_function*) for the reactor

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-reactions reactor)
```

*reactor*
:   *Type:* VLR object

    An object.

## Return Values

*Type:* List

List that contains the name of the event and callback function for the reactor object.

## Examples

```
(vlr-reactions circleReactor)
((:vlr-modified . PRINT-RADIUS))
```

#### Related References

* [vlr-reaction-name (AutoLISP/ActiveX)](vlr-reaction-name-AutoLISP-ActiveX.md)
* [vlr-reaction-set (AutoLISP/ActiveX)](vlr-reaction-set-AutoLISP-ActiveX.md)
* [vlr-reactors (AutoLISP/ActiveX)](vlr-reactors-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*