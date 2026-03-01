# vlr-xref-reactor (AutoLISP/ActiveX)

Constructs an editor reactor object that notifies of an event related to attaching or modifying XREFs

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-xref-reactor data callbacks)
```

*data*
:   *Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

    Any AutoLISP data to be associated with the reactor object; otherwise
    nil if no data.

*callbacks*
:   *Type:* List

    A list of pairs of the following form:

    (*event-name . callback\_function*)

    * *event-name* is one of the following XREF reactor events:

      | XREF reactor events | |
      | Event name | Description |
      | :VLR-beginAttach | An xref is about to be attached. |
      | :VLR-otherAttach | An external reference is being added to the drawing database. This event occurs after objects are cloned, but before any translation. This callback function is sent just after beginDeepCloneXlation notification, but occurs only for the xref attach process. |
      | :VLR-abortAttach | An xref attach operation was terminated before successful completion. |
      | :VLR-endAttach | An xref attach operation completed successfully. |
      | :VLR-redirected | An object ID in the xref drawing is being modified to point to the associated object in the drawing being referenced. |
      | :VLR-comandeered | The object ID of the object is being appended to the symbol table of the drawing being xrefed into. |
      | :VLR-beginRestore | An existing xref is about to be resolved (typically when a drawing with xrefs is loading). |
      | :VLR-abortRestore | An xref unload or reload was terminated before successful completion. |
      | :VLR-endRestore | An existing xref has been resolved (typically when a drawing with xrefs has completed loading). |
      | :VLR-xrefSubcommandBindItem | The BIND subcommand of XREF was invoked, or a preexisting xref is being bound.  NOTE:The BIND subcommand is interactive and triggers multiple events. |
      | :VLR-xrefSubcommandAttachItem | The ATTACH subcommand of XREF was invoked, or a preexisting xref is being resolved.  NOTE:The ATTACH subcommand is interactive and triggers multiple events. |
      | :VLR-xrefSubcommandOverlayItem | The OVERLAY subcommand of XREF was invoked, or a preexisting xref is being resolved.  NOTE:The OVERLAY subcommand is interactive and triggers multiple events. |
      | :VLR-xrefSubcommandDetachItem | The DETACH subcommand of XREF was invoked.  NOTE:The DETACH subcommand is interactive and triggers multiple events. |
      | :VLR-xrefSubcommandPathItem | The PATH subcommand of XREF was invoked.  NOTE:The PATH subcommand is interactive and triggers multiple events. |
      | :VLR-xrefSubcommandReloadItem | The RELOAD subcommand of XREF was invoked, or a preexisting xref is being reloaded.  NOTE:The RELOAD subcommand is interactive and triggers multiple events. |
      | :VLR-xrefSubcommandUnloadItem | The UNLOAD subcommand of XREF was invoked, or a preexisting xref is being unloaded. |
    * *callback\_function* is a symbol representing a function to be called when the event fires. Each callback function accepts two arguments:

      *reactor\_object* -- The VLR object that called the callback function.

      *list* -- A list of extra data elements associated with the particular event. The contents of this list for particular events are
      shown in the “XREF reactor callback data” table.

      | XREF reactor callback data | | |
      | Name | List length | Parameters |
      | :VLR-beginAttach | 3 | First parameter is a VLA-object pointing to the target drawing database.  Second parameter is a string containing the file name of the xref being attached.  Third parameter is a VLA-object pointing to the drawing database that contains the objects being attached. |
      | :VLR-otherAttach | 2 | First parameter is a VLA-object pointing to the target drawing database.  Second parameter is a VLA-object pointing to the drawing database that contains the objects being attached. |
      | :VLR-abortAttach | 1 | A VLA-object pointing to the drawing database that contains the objects being attached. |
      | :VLR-endAttach | 1 | A VLA-object pointing to the target drawing database. |
      | :VLR-redirected | 2 | First parameter is an integer containing the object ID for the redirected symbol table record (STR) in the drawing being referenced.  Second parameter is an integer containing the object ID for the object in the xref drawing. |
      | :VLR-comandeered | 3 | First parameter is a VLA-object pointing to the database receiving the xref.  Second parameter is an integer containing the object ID of the object being commandeered.  Third parameter is a VLA-object pointing to the drawing database that contains the objects being attached. |
      | :VLR-beginRestore | 3 | First parameter is a VLA-object pointing to the database receiving the xref.  Second parameter is a string containing the xref block table record (BTR) name.  Third parameter is a VLA-object pointing to the drawing database that contains the objects being attached. |
      | :VLR-abortRestore  :VLR-endRestore | 1 | A VLA-object pointing to the target drawing database. |
      | :VLR-xrefSubcommandBindItem | 2 | First parameter is an integer indicating the activity the BIND is carrying out. Possible values are  0 -- BIND subcommand invoked.  2 -- xref with the indicated object ID is being bound.  3 -- xref with the indicated object ID was successfully bound.  4 -- BIND subcommand completed.  5 -- BIND operation is about to either terminate or fail to complete on the specified object ID.  6 -- BIND operation has either terminated or failed to complete on the specified object ID.  7 -- Sent for an XDep block bound by XBind.  8 -- Sent for all other symbols: Layers, Linetypes, TextStyles, and DimStyles.  Second parameter is an integer containing the object ID of the xref being bound, or 0 if not applicable. |
      | :VLR-xrefSubcommandAttachItem | 2 | First parameter is an integer indicating the activity the ATTACH is carrying out. Possible values are  0 -- BIND subcommand invoked.  2 -- xref with the indicated object ID is being bound.  3 -- xref with the indicated object ID was successfully bound.  4 -- BIND subcommand completed.  5 -- BIND operation is about to either terminate or fail to complete on the specified object ID.  6 -- BIND operation has either terminated or failed to complete on the specified object ID.  Second parameter is a string identifying the file being attached; otherwise nil if not applicable. |
      | :VLR-xrefSubcommandOverlayItem | 2 | First parameter is an integer indicating the activity the OVERLAY is carrying out. Possible values are  0 -- BIND subcommand invoked.  2 -- xref with the indicated object ID is being bound.  3 -- xref with the indicated object ID was successfully bound.  4 -- BIND subcommand completed.  5 -- BIND operation is about to either terminate or fail to complete on the specified object ID.  6 -- BIND operation has either terminated or failed to complete on the specified object ID.  Second parameter is a string identifying the file being overlaid; otherwise nil if not applicable. |
      | :VLR-xrefSubcommandDetachItem | 2 | First parameter is an integer indicating the activity the DETACH is carrying out. Possible values are  0 -- BIND subcommand invoked.  2 -- xref with the indicated object ID is being bound.  3 -- xref with the indicated object ID was successfully bound.  4 -- BIND subcommand completed.  5 -- BIND operation is about to either terminate or fail to complete on the specified object ID.  6 -- BIND operation has either terminated or failed to complete on the specified object ID.  Second parameter is an integer containing the object ID of the xref being detached, or 0 if not applicable. |
      | :VLR-xrefSubcommandPathItem | 3 | First parameter is an integer indicating the activity the DETACH is carrying out. Possible values are  0 -- BIND subcommand invoked.  2 -- xref with the indicated object ID is being bound.  3 -- xref with the indicated object ID was successfully bound.  4—BIND subcommand completed.  5 -- BIND operation is about to either terminate or fail to complete on the specified object ID.  6 -- BIND operation has either terminated or failed to complete on the specified object ID.  Second parameter is an integer containing the object ID of the xref being operated on, or 0 if not applicable.  Third parameter is a string identifying the new path name of the xref; otherwise nil if not applicable. |
      | :VLR-xrefSubcommandReloadItem | 2 | First parameter is an integer indicating the activity the RELOAD is carrying out. Possible values are  0 -- BIND subcommand invoked.  2 -- xref with the indicated object ID is being bound.  3 -- xref with the indicated object ID was successfully bound.  4 -- BIND subcommand completed.  5 -- BIND operation is about to either terminate or fail to complete on the specified object ID.  6 -- BIND operation has either terminated or failed to complete on the specified object ID.  Second parameter is an integer containing the object ID of the xref being reloaded, or 0 if not applicable. |
      | :VLR-xrefSubcommandUnloadItem | 2 | First parameter is an integer indicating the activity the UNLOAD is carrying out. Possible values are  0 -- BIND subcommand invoked.  2 -- xref with the indicated object ID is being bound.  3 -- xref with the indicated object ID was successfully bound.  4 -- BIND subcommand completed.  5 -- BIND operation is about to either terminate or fail to complete on the specified object ID.  6 -- BIND operation has either terminated or failed to complete on the specified object ID.  Second parameter is an integer containing the object ID of the xref being unloaded, or 0 if not applicable. |

## Return Values

*Type:* VLR object

The
*reactor\_object* argument from the
*callback\_function*.

## Examples

N/A

#### Related References

* [vlr-insert-reactor (AutoLISP/ActiveX)](vlr-insert-reactor-AutoLISP-ActiveX.md)
* [vlr-wblock-reactor (AutoLISP/ActiveX)](vlr-wblock-reactor-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*