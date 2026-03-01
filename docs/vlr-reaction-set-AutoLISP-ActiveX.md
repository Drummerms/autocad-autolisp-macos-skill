# vlr-reaction-set (AutoLISP/ActiveX)

Adds or replaces a callback function in a reactor

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-reaction-set reactor event function)
```

*reactor*
:   *Type:* VLR object

    An object.

*event*
:   *Type:* Symbol

    A symbol denoting one of the event types available for this reactor type.

*function*
:   *Type:* Symbol

    A symbol representing the AutoLISP function to be added or replaced.

## Return Values

*Type:* Symbol

The value of the
*function* argument.

## Examples

The following command changes the
circleReactor reactor to call the
print-area function when an object is modified:

```
(vlr-reaction-set circleReactor :vlr-modified 'print-area)
PRINT-AREA
```

#### Related References

* [vlr-reaction-name (AutoLISP/ActiveX)](vlr-reaction-name-AutoLISP-ActiveX.md)
* [vlr-reactions (AutoLISP/ActiveX)](vlr-reactions-AutoLISP-ActiveX.md)
* [vlr-reactors (AutoLISP/ActiveX)](vlr-reactors-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*