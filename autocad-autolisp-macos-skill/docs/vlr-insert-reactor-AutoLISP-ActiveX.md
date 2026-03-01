# vlr-insert-reactor (AutoLISP/ActiveX)

Constructs an editor reactor object that notifies of an event related to block insertion

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-insert-reactor data callbacks)
```

*data*
:   *Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

    Any AutoLISP data to be associated with the reactor object; otherwise
    nil if no data.

*callbacks*
:   *Type:* List

    A list of pairs of the following form:

    (*event-name . callback\_function*)

    * *event-name* is one of the following Insert reactor events:

      | Insert reactor events | |
      | Event name | Description |
      | :vlr-beginInsert | A block is about to be inserted into the drawing database. |
      | :vlr-beginInsertM | A 3D transformation matrix is about to be inserted into the drawing database. |
      | :vlr-otherInsert | A block or matrix has been added to the drawing database. This notification is sent after the insert process completes copying the object into the database, but before ID translation or entity transformation occurs. |
      | :vlr-endInsert | Usually indicates an insert operation on the drawing database is complete. However, in some cases, the transform has not yet happened, or the block that was created has not yet been appended. This means the objects copied are not yet graphical, and you cannot use them in selection sets until the :vlr-commandEnded notification is received. |
      | :vlr-abortInsert | Insert operation was terminated and did not complete, leaving the database in an unstable state. |
    * *callback\_function* is a symbol representing a function to be called when the event fires. Each callback function accepts two arguments:

      *reactor\_object* -- The VLR object that called the callback function.

      *list* -- A list of extra data elements associated with the particular event. The contents of this list for particular events is
      shown in the “Insert reactor callback data” table.

      | Insert reactor callback data | | |
      | Name | List length | Parameters |
      | :vlr-beginInsert | 3 | First parameter is a VLA-object pointing to the database in which the block is being inserted.  Second parameter is a string naming the block to be inserted.  Third parameter is a VLA-object identifying the source database of the block. |
      | :vlr-beginInsertM | 3 | First parameter is a VLA-object pointing to the database in which the 3D transformation matrix is being inserted.  Second parameter is the 3D transformation matrix to be inserted.  Third parameter is a VLA-object identifying the source database of the matrix. |
      | :vlr-otherInsert | 2 | First parameter is a VLA-object pointing to the database in which the block or matrix is being inserted.  Second parameter is a VLA-object identifying the source database of the block or matrix. |
      | :vlr-endInsert  :vlr-abortInsert | 1 | VLA-object pointing to target database. |

### Return Values

*Type:* VLR object

The
*reactor\_object* argument from the
*callback\_function*.

### Examples

N/A

#### Related References

* [vlr-wblock-reactor (AutoLISP/ActiveX)](vlr-wblock-reactor-AutoLISP-ActiveX.md)
* [vlr-xref-reactor (AutoLISP/ActiveX)](vlr-xref-reactor-AutoLISP-ActiveX.md)

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*