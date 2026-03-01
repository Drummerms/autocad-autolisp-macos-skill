# vlr-owners (AutoLISP/ActiveX)

Returns the list of owners of an object reactor

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-owners reactor)
```

*reactor*
:   *Type:* VLR object

    An object.

## Return Values

*Type:* List

A list of objects that notify the specified reactor.

## Examples

```
(vlr-owners circleReactor)
(#<VLA-OBJECT IAcadCircle 01db98f4> #<VLA-OBJECT IAcadCircle 01db9724>
#<VLA-OBJECT IAcadCircle 01db93d4> #<VLA-OBJECT IAcadCircle 01db9084>)
```

#### Related References

* [vlr-owner-add (AutoLISP/ActiveX)](vlr-owner-add-AutoLISP-ActiveX.md)
* [vlr-owner-remove (AutoLISP/ActiveX)](vlr-owner-remove-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*