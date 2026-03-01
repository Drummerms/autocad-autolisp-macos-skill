# vlr-set-notification (AutoLISP/ActiveX)

Defines whether a reactor's callback function will execute if its associated namespace is not active

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-set-notification reactor 'range)
```

*reactor*
:   *Type:* VLR object

    An object.

*'range*
:   *Type:* Symbol

    The
    *range* argument is a symbol that can be either
    *'all-documents* (execute the callback regardless of whether the reactor is associated with the active document), or
    *'active-document-only* (execute the callback only if the reactor is associated with the active document).

## Return Values

*Type:* VLR object

A reactor object.

## Examples

Set a reactor to execute its callback function even if its associated namespace is not active:

```
(vlr-set-notification circleReactor 'all-documents)
#<VLR-Object-Reactor>
```

#### Related References

* [vlr-notification (AutoLISP/ActiveX)](vlr-notification-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*