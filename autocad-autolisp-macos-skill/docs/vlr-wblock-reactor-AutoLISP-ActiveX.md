# vlr-wblock-reactor (AutoLISP/ActiveX)

Constructs an editor reactor object that notifies of an event related to writing a block

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-wblock-reactor data callbacks)
```

*data*
:   *Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

    Any AutoLISP data to be associated with the reactor object; otherwise
    nil if no data.

*callbacks*
:   *Type:* List

    A list of pairs of the following form:

    (*event-name . callback\_function*)

    * *event-name* is one of the following Wblock reactor events:

      | Wblock reactor events | |
      | Event name | Description |
      | :VLR-wblockNotice | A wblock operation is about to start. |
      | :VLR-beginWblockPt | A wblock operation is being performed on a set of entities. |
      | :VLR-beginWblockId | A wblock operation is being performed on a specified block. |
      | :VLR-beginWblock | A wblock operation is being performed on an entire database. Notification does not occur until all the entities in the source database's model space are copied into the target database. |
      | :VLR-endWblock | A wblock operation completed successfully. |
      | :VLR-beginWblockObjects | wblock has just initialized the object ID translation map. |
    * *callback\_function* is a symbol representing a function to be called when the event fires. Each callback function accepts two arguments:

      *reactor\_object* -- The VLR object that called the callback function.

      *list* -- A list of extra data elements associated with the particular event. The contents of this list for particular events are
      shown in the “Wblock reactor callback data” table.

      | Wblock reactor callback data | | |
      | Name | List length | Parameters |
      | :VLR-wblockNotice | 1 | Database object (VLA-object) from which the block will be created. |
      | :VLR-beginWblockPt | 3 | First parameter is the target database object (VLA-object).  Second parameter is the source database object (VLA-object) containing the objects being wblocked.  Third parameter is a 3D point list (in WCS) to be used as the base point in the target database. |
      | :VLR-beginWblockId | 3 | First parameter is the target database object (VLA-object).  Second parameter is the source database object (VLA-object) containing the objects being wblocked.  Third parameter is the object ID of the BlockTableRecord being wblocked. |
      | :VLR-beginWblock  :VLR-otherWblock | 2 | First parameter is the target database object (VLA-object).  Second parameter is the source database object (VLA-object) containing the objects being wblocked. |
      | :VLR-abortWblock  :VLR-endWblock | 1 | The target database object (VLA-object). |
      | :VLR-beginWblockObjects | 2 | First parameter is the source database object (VLA-object) containing the objects being wblocked.  Second parameter is an ID map. |

## Return Values

*Type:* VLR object

The
*reactor\_object* argument from the
*callback\_function*.

## Examples

N/A

#### Related References

* [vlr-insert-reactor (AutoLISP/ActiveX)](vlr-insert-reactor-AutoLISP-ActiveX.md)
* [vlr-xref-reactor (AutoLISP/ActiveX)](vlr-xref-reactor-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*