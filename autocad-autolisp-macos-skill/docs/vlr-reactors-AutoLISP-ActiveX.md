# vlr-reactors (AutoLISP/ActiveX)

Returns a list of existing reactors

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-reactors [reactor-type...])
```

*reactor-type*
:   *Type:* Symbol

    One or more of the following:

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

A list of reactor lists; otherwise
nil, if there are no reactors of any specified type. Each reactor list begins with a symbol identifying the reactor type, followed
by pointers to each reactor of that type.

## Remarks

If you specify
*reactor-type* arguments,
vlr-reactors returns lists of the reactor types you specified. If you omit
*reactor-type*,
vlr-reactors returns all existing reactors.

## Examples

List all reactors in a drawing:

```
(vlr-reactors)
((:VLR-Object-Reactor #<VLR-Object-Reactor>) (:VLR-Editor-Reactor #<VLR-Editor-Reactor>))
```

List all object reactors:

```
(vlr-reactors :vlr-object-reactor)
((:VLR-Object-Reactor #<VLR-Object-Reactor>))
```

vlr-reactors returns a list containing a single reactor list.

List all database reactors:

```
(vlr-reactors :vlr-acdb-reactor)
nil
```

There are no database reactors defined.

List all DWG reactors:

```
(vlr-reactors :vlr-dwg-reactor)
((:VLR-DWG-Reactor #<VLR-DWG-Reactor> #<VLR-DWG-Reactor>))
```

vlr-reactors returns a list containing a list of DWG reactors.

#### Related References

* [vlr-reaction-name (AutoLISP/ActiveX)](vlr-reaction-name-AutoLISP-ActiveX.md)
* [vlr-reaction-set (AutoLISP/ActiveX)](vlr-reaction-set-AutoLISP-ActiveX.md)
* [vlr-reactions (AutoLISP/ActiveX)](vlr-reactions-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*