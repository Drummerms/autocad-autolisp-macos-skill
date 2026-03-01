# vlr-type (AutoLISP/ActiveX)

Returns a symbol representing the reactor type

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-type reactor)
```

*reactor*
:   *Type:* VLR object

    An object.

## Return Values

*Type:* Symbol

Reactor type from the following table:

| Reactor types | |
| Reactor type | Description |
| :VLR-AcDb-Reactor | Database reactor. |
| :VLR-Command-Reactor | An editor reactor notifying of a command event. |
| :VLR-DeepClone-Reactor | An editor reactor notifying of a deep clone event. |
| :VLR-DocManager-Reactor | Document management reactor. |
| :VLR-DWG-Reactor | An editor reactor notifying of a drawing event (for example, opening or closing a drawing file). |
| :VLR-DXF-Reactor | An editor reactor notifying of an event related to reading or writing of a DXF file. |
| :VLR-Editor-Reactor | General editor reactor; maintained for backward compatibility. |
| :VLR-Insert-Reactor | An editor reactor notifying of an event related to block insertion. |
| :VLR-Linker-Reactor | Linker reactor. |
| :VLR-Lisp-Reactor | An editor reactor notifying of a LISP event. |
| :VLR-Miscellaneous-Reactor | An editor reactor that does not fall under any of the other editor reactor types. |
| :VLR-Mouse-Reactor | An editor reactor notifying of a mouse event (for example, a double-click). |
| :VLR-Object-Reactor | Object reactor. |
| :VLR-SysVar-Reactor | An editor reactor notifying of a change to a system variable. |
| :VLR-Toolbar-Reactor | An editor reactor notifying of a change to the bitmaps in a toolbar. |
| :VLR-Undo-Reactor | An editor reactor notifying of an undo event. |
| :VLR-Wblock-Reactor | An editor reactor notifying of an event related to writing a block. |
| :VLR-Window-Reactor | An editor reactor notifying of an event related to moving or sizing an AutoCAD window. |
| :VLR-XREF-Reactor | An editor reactor notifying of an event related to attaching or modifying XREFs. |

## Examples

```
(vlr-type circleReactor)
:VLR-Object-Reactor
```

#### Related References

* [vlr-types (AutoLISP/ActiveX)](vlr-types-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*