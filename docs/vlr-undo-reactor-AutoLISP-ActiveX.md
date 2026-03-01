# vlr-undo-reactor (AutoLISP/ActiveX)

Constructs an editor reactor object that notifies of an undo event

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-undo-reactor data callbacks)
```

*data*
:   *Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

    Any AutoLISP data to be associated with the reactor object; otherwise
    nil if no data.

*callbacks*
:   *Type:* List

    A list of pairs of the following form:

    (*event-name . callback\_function*)

    * *event-name* is one of the following Undo reactor events:

      | Undo reactor events | |
      | Event name | Description |
      | :vlr-undoSubcommandAuto | The UNDO command's Auto option has been executed. |
      | :vlr-undoSubcommandControl | The UNDO command's Control option has been executed. |
      | :vlr-undoSubcommandBegin | The UNDO command's BEGIN or GROUP option is being performed. BEGIN and GROUP mark the beginning of a series of commands that can be undone as one unit. |
      | :vlr-undoSubcommandEnd | The UNDO command's END option is being performed. UNDO/END marks the end of a series of commands that can be undone as one unit. |
      | :vlr-undoSubcommandMark | The UNDO command's MARK option is about to be executed. This places a marker in the undo file so UNDO/BACK can undo back to the marker. |
      | :vlr-undoSubcommandBack | The UNDO command's BACK option is about to be performed. UNDO/BACK undoes everything back to the most recent MARK marker or back to the beginning of the undo file if no MARK marker exists. |
      | :vlr-undoSubcommandNumber | The UNDO command's NUMBER option is about to be executed (the default action of the UNDO command). |
    * and
      *callback\_function* is a symbol representing a function to be called when the event fires. Each callback function accepts two arguments:

      *reactor\_object* -- The VLR object that called the callback function.

      *list* -- A list of extra data elements associated with the particular event. The contents of this list for particular events are
      shown in the “Undo reactor callback data” table.

      | Undo reactor callback data | | |
      | Name | List length | Parameters |
      | :vlr-undoSubcommandAuto | 2 | First parameter is an integer indicating the activity. The value is always 4, indicating that notification occurred after the operation was performed.  Second parameter is a symbol indicating the state of Auto mode. Value is T if Auto mode is turned on, nil if Auto mode is turned off. |
      | :vlr-undoSubcommandControl | 2 | First parameter is an integer indicating the activity. The value is always 4, indicating that notification occurred after the operation was performed.  Second parameter is an integer indicating the Control option selected. This can be one of the following:  0 -- NONE was selected  1 -- ONE was selected  2 -- ALL was selected |
      | :vlr-undoSubcommandBegin  :vlr-undoSubcommandEnd  :vlr-undoSubcommandMark  :vlr-undoSubcommandBack | 1 | An integer value of 0, indicating that notification occurs before the actual operation is performed. |
      | :vlr-undoSubcommandNumber | 2 | First parameter is an integer indicating the activity. The value is always 0, indicating that notification occurs before the actual operation is performed.  Second parameter is an integer indicating the number of steps being undone. |

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