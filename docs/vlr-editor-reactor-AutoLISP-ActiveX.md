# vlr-editor-reactor (AutoLISP/ActiveX)

Constructs an editor reactor object

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-editor-reactor data callbacks)
```

*data*
:   *Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

    Any AutoLISP data to be associated with the reactor object; otherwise
    nil if no data.

*callbacks*
:   *Type:* List

    A list of pairs of the following form:

    (*event-name . callback\_function*)

    * *event-name* is one of the following Editor reactor events:

      | Editor reactor events | |
      | Event name | Description |
      | :vlr-beginClose | The drawing database is to be closed. |
      | :vlr-beginDxfIn | The contents of a DXF file are to be appended to the drawing database. |
      | :vlr-abortDxfIn | The DXF import was not successful. |
      | :vlr-dxfInComplete | The DXF import completed successfully. |
      | :vlr-beginDxfOut | AutoCAD is about to export the drawing database into a DXF file. |
      | :vlr-abortDxfOut | DXF export operation failed. |
      | :vlr-dxfOutComplete | DXF export operation completed successfully. |
      | :vlr-databaseToBeDestroyed | The contents of the drawing database are about to be deleted from memory. |
      | :vlr-unknownCommand | A command not known to AutoCAD was issued. |
      | :vlr-commandWillStart | An AutoCAD command has been called. |
      | vlr-commandEnded | An AutoCAD command has completed. |
      | :vlr-commandCancelled | An AutoCAD command has been canceled. |
      | :vlr-commandFailed | An AutoCAD command failed to complete. |
      | :vlr-lispWillStart | An AutoLISP expression is to be evaluated. |
      | :vlr-lispEnded | Evaluation of an AutoLISP expression has completed. |
      | :vlr-lispCancelled | Evaluation of an AutoLISP expression has been canceled. |
      | :vlr-beginDwgOpen | AutoCAD is about to open a drawing file. |
      | :vlr-endDwgOpen | AutoCAD has ended the open operation. |
      | :vlr-dwgFileOpened | A new drawing has been loaded into the AutoCAD window. |
      | :vlr-beginSave | AutoCAD is about to save the drawing file. |
      | :vlr-saveComplete | AutoCAD has saved the current drawing to disk. |
      | :vlr-sysVarWillChange | AutoCAD is about to change the value of a system variable. |
      | :vlr-sysVarChanged | The value of a system variable has changed. |
    * *callback\_function* is a symbol representing a function to be called when the event fires. Each callback function accepts two arguments:

      *reactor\_object* -- The VLR object that called the callback function.

      *list* -- A list of extra data elements associated with the particular event. The contents of this list for particular events are
      shown in the “Editor reactor callback data” table.

      | Editor reactor callback data | | |
      | Name | List length | Parameters |
      | :vlr-lispEnded  :vlr-lispCancelled  :vlr-beginClose  :vlr-beginDxfIn  :vlr-abortDxfIn  :vlr-dxfInComplete  :vlr-beginDxfOut  :vlr-abortDxfOut  :vlr-dxfOutComplete  :vlr-databaseToBeDestroyed | 0 |  |
      | :vlr-unknownCommand  :vlr-commandWillStart  :vlr-commandEnded  :vlr-commandCancelled  :vlr-commandFailed | 1 | A string containing the command name. |
      | :vlr-lispWillStart | 1 | A string containing the first line of the AutoLISP expression to evaluate. |
      | :vlr-beginDwgOpen  :vlr-endDwgOpen  :vlr-dwgFileOpened | 1 | A string identifying the file to open. |
      | :vlr-beginSave | 2 | First parameter is the database object to save at.  Second parameter is a string containing the default file name for save, which may be changed by the user. |
      | :vlr-saveComplete | 2 | First parameter is the database object to save at.  Second parameter is a string containing the actual file name used for the save. |
      | :vlr-sysVarWillChange | 1 | A string naming the system variable. |
      | :vlr-sysVarChanged | 2 | First parameter is a string naming the system variable.  Second parameter is an integer indicating whether the change was successful (1 = success, 0 = failed). |

## Return Values

*Type:* VLR object

The
*reactor\_object* argument from the
*callback\_function*.

## Examples

N/A

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*