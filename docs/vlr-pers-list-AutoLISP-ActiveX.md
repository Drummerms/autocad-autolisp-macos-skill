# vlr-pers-list (AutoLISP/ActiveX)

Returns a list of persistent reactors in the current drawing document

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-pers-list [reactor])
```

*reactor*
:   *Type:* VLR object

    The reactor object to be listed. If
    *reactor* is not specified,
    vlr-pers-list lists all persistent reactors.

## Return Values

*Type:* List

A list of reactor objects.

## Examples

```
(vlr-pers-list)
(#<VLR-Object-Reactor> #<VLR-Object-Reactor> (#<VLR-Object-Reactor>)
```

#### Related References

* [vlr-pers-p (AutoLISP/ActiveX)](vlr-pers-p-AutoLISP-ActiveX.md)
* [vlr-pers (AutoLISP/ActiveX)](vlr-pers-AutoLISP-ActiveX.md)
* [vlr-pers-release (AutoLISP/ActiveX)](vlr-pers-release-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*