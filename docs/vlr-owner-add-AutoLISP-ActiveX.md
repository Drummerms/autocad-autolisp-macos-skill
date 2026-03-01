# vlr-owner-add (AutoLISP/ActiveX)

Adds an object to the list of owners of an object reactor

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-owner-add reactor owner)
```

*reactor*
:   *Type:* VLR object

    An object.

*owner*
:   *Type:* VLA-object

    An object to be added to the list of notifiers for this reactor.

## Return Values

*Type:* VLA-object

The object to which the reactor has been added.

## Remarks

This function adds a new source of reactor events; the reactor will receive events from the specified object.

## Examples

In the following example, an arc object named “archie” is added to the owner list of reactor
circleReactor:

```
(vlr-owner-add circleReactor archie)
#<VLA-OBJECT IAcadArc 03ad0bcc>
```

#### Related References

* [vlr-owner-remove (AutoLISP/ActiveX)](vlr-owner-remove-AutoLISP-ActiveX.md)
* [vlr-owners (AutoLISP/ActiveX)](vlr-owners-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*