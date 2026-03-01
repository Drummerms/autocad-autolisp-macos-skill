# vlr-notification (AutoLISP/ActiveX)

Determines whether or not a reactor will fire if its associated namespace is not active

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-notification reactor)
```

*reactor*
:   *Type:* VLR object

    An object.

## Return Values

*Type:* Symbol

A symbol, which can be either
'all-documents (the reactor fires whether or not its associated document is active), or
'active-document-only (the reactor fires only if its associated document is active).

## Examples

N/A

#### Related References

* [vlr-set-notification (AutoLISP/ActiveX)](vlr-set-notification-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*