# vlr-remove-all (AutoLISP/ActiveX)

Disables all reactors of the specified type

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-remove-all [reactor-type])
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

    If no
    *reactor-type* is specified,
    vlr-remove-all disables all reactors.

## Return Values

*Type:* List

A list of lists. The first element of each list identifies the type of reactor, and the remaining elements identify the disabled
reactor objects. The function returns
nil if there are no reactors active.

## Examples

The following function call disables all editor reactors:

```
(vlr-remove-all :vlr-editor-reactor)
((:VLR-Editor-Reactor #<VLR-Editor-Reactor>))
```

The following call disables all reactors:

```
(vlr-remove-all)
((:VLR-Object-Reactor #<VLR-Object-Reactor> #<VLR-Object-Reactor>
#<VLR-Object-Reactor>)(:VLR-Editor-Reactor#<VLR-Editor-Reactor>))
```

#### Related References

* [vlr-remove (AutoLISP/ActiveX)](vlr-remove-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*