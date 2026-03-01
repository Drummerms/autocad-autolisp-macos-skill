# vlr-dxf-reactor (AutoLISP/ActiveX)

Constructs an editor reactor object that notifies of an event related to reading or writing a DXF file

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-dxf-reactor data callbacks)
```

*data*
:   *Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

    Any AutoLISP data to be associated with the reactor object; otherwise
    nil if no data.

*callbacks*
:   *Type:* List

    A list of pairs of the following form:

    (*event-name . callback\_function*)

    * *event-name* is one of the following DXF reactor events:

      | DXF reactor events | |
      | Event name | Description |
      | :vlr-beginDxfIn | The contents of a DXF file are to be appended to the drawing database. |
      | :vlr-abortDxfIn | The DXF import was not successful. |
      | :vlr-dxfInComplete | The DXF import was successful. |
      | :vlr-beginDxfOut | AutoCAD is about to export the drawing database into a DXF file. |
      | :vlr-abortDxfOut | The DXF export operation failed. |
      | :vlr-dxfOutComplete | The DXF export operation was successful. |
    * *callback\_function* is a symbol representing a function to be called when the event fires. Each callback function accepts two arguments:

      *reactor\_object* -- The VLR object that called the callback function.

      *list* -- A list of extra data elements associated with the particular event. The contents of this list for particular events are
      shown in the “DXF reactor callback data” table.

      | DXF reactor callback data | |
      | Name | List length |
      | :vlr-beginDxfIn  :vlr-abortDxfIn  :vlr-dxfInComplete,  :vlr-beginDxfOut  :vlr-abortDxfOut  :vlr-dxfOutComplete | 0 |

## Return Values

*Type:* VLR object

The
*reactor\_object* argument from the
*callback\_function*.

## Examples

N/A

#### Related References

* [vlr-dwg-reactor (AutoLISP/ActiveX)](vlr-dwg-reactor-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*