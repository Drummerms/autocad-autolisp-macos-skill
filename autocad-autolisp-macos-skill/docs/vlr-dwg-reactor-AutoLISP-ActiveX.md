# vlr-dwg-reactor (AutoLISP/ActiveX)

Constructs an editor reactor object that notifies of a drawing event (for example, opening or closing a drawing file)

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-dwg-reactor data callbacks)
```

*data*
:   *Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

    Any AutoLISP data to be associated with the reactor object; otherwise
    nil if no data.

*callbacks*
:   *Type:* List

    A list of pairs of the following form:

    (*event-name . callback\_function*)

    * *event-name* is one of the following DWG reactor events:

      | DWG reactor events | |
      | Event name | Description |
      | :vlr-beginClose | The drawing database is to be closed. |
      | :vlr-databaseConstructed | A drawing database has been constructed. |
      | :vlr-databaseToBeDestroyed | The contents of the drawing database are about to be deleted from memory. |
      | vlr-beginDwgOpen | AutoCAD is about to open a drawing file. |
      | :vlr-endDwgOpen | AutoCAD has ended the open operation. |
      | :vlr-dwgFileOpened | A new drawing has been loaded into the AutoCAD window. |
      | vlr-beginSave | AutoCAD is about to save the drawing file. |
      | vlr-saveComplete | AutoCAD has saved the current drawing to disk. |
    * *callback\_function* is a symbol representing a function to be called when the event occurs. Each callback function accepts two arguments:

      *reactor\_object* -- The VLR object that called the callback function.

      *list* -- A list of extra data elements associated with the particular event. The contents of this list for particular events are
      shown in the “DWG reactor callback data” table.

      | DWG reactor callback data | | |
      | Name | List length | Parameters |
      | :vlr-beginClose  :vlr-databaseConstructed  :vlr-databaseToBeDestroyed | 0 |  |
      | :vlr-beginDwgOpen  :vlr-endDwgOpen  :vlr-dwgFileOpened | 1 | A string identifying the file to open. |
      | :vlr-beginSave | 2 | First parameter is the database object to save at.  Second parameter is a string containing the default file name for save, which may be changed by the user. |
      | :vlr-saveComplete | 2 | First parameter is the database object to save at.  Second parameter is a string containing the actual file name used for the save. |

## Return Values

*Type:* VLR object

The
*reactor\_object* argument from the
*callback\_function*.

## Examples

N/A

#### Related References

* [vlr-dxf-reactor (AutoLISP/ActiveX)](vlr-dxf-reactor-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*