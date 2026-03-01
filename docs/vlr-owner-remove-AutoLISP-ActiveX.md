# vlr-owner-remove (AutoLISP/ActiveX)

Removes an object from the list of owners of an object reactor

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-owner-remove reactor owner)
```

*reactor*
:   *Type:* VLR object

    An object.

*owner*
:   *Type:* VLA-object

    An object to be removed from the list of notifiers for this reactor.

## Return Values

*Type:* VLA-object

The object from which the reactor was removed.

## Examples

```
(vlr-owner-remove circleReactor archie)
#<VLA-OBJECT IAcadArc 03ad0bcc>
```

#### Related References

* [vlr-owner-add (AutoLISP/ActiveX)](vlr-owner-add-AutoLISP-ActiveX.md)
* [vlr-owners (AutoLISP/ActiveX)](vlr-owners-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*