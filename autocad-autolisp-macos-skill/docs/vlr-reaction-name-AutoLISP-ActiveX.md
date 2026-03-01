# vlr-reaction-name (AutoLISP/ActiveX)

Returns a list of all possible callback conditions for this reactor type

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-reaction-names reactor-type)
```

*reactor-type*
:   *Type:* Symbol

    One of the following:

    * :VLR-AcDb-Reactor
    * :VLR-Command-Reactor
    * :VLR-DeepClone-Reactor
    * :VLR-DocManager-Reactor
    * :VLR-DWG-Reactor
    * :VLR-DXF-Reactor
    * :VLR-Editor-Reactor
    * :VLR-Insert-Reactor
    * :VLR-Linker-Reactor
    * :VLR-Lisp-Reactor
    * :VLR-Miscellaneous-Reactor
    * :VLR-Mouse-Reactor
    * :VLR-Object-Reactor
    * :VLR-SysVar-Reactor
    * :VLR-Toolbar-Reactor
    * :VLR-Undo-Reactor
    * :VLR-Wblock-Reactor
    * :VLR-Window-Reactor
    * :VLR-XREF-Reactor

## Return Values

*Type:* List

A list of symbols indicating the possible events for the specified reactor type.

## Examples

```
(vlr-reaction-names :VLR-Editor-Reactor)
(:vlr-unknownCommand :vlr-commandWillStart :vlr-commandEnded....
```

#### Related References

* [vlr-reaction-set (AutoLISP/ActiveX)](vlr-reaction-set-AutoLISP-ActiveX.md)
* [vlr-reactions (AutoLISP/ActiveX)](vlr-reactions-AutoLISP-ActiveX.md)
* [vlr-reactors (AutoLISP/ActiveX)](vlr-reactors-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*