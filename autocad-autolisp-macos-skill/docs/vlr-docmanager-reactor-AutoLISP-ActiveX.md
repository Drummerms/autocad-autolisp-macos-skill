# vlr-docmanager-reactor (AutoLISP/ActiveX)

Constructs a reactor object that notifies of events relating to drawing documents

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-docmanager-reactor data callbacks)
```

*data*
:   *Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

    Any AutoLISP data to be associated with the reactor object; otherwise
    nil if no data.

*callbacks*
:   *Type:* List

    A list of pairs of the following form:

    (*event-name . callback\_function*)

    * *event-name* is one of the following DocManager reactor events:

      | DocManager reactor events | |
      | Event name | Description |
      | :vlr-documentCreated | A new document was created for a drawing (new or open).  Useful for updating your per-document structures. |
      | :vlr-documentToBeDestroyed | A document will be destroyed. |
      | :vlr-documentLockModeWillChange | A command is about to start or finish modifying elements in the document, and is obtaining or releasing a lock on the document. |
      | :vlr-documentLockModeChangeVetoed | A reactor invoked veto on itself from a :vlr-documentLockModeChanged callback. |
      | :vlr-documentLockModeChanged | The lock on the document has been obtained or released. |
      | :vlr-documentBecameCurrent | The current document has been changed.  This does not necessarily imply that the document has been activated, because changing the current document is necessary for some operations. To obtain user input, the document must be activated as well. |
      | :vlr-documentToBeActivated | A currently inactive document has just received the activate signal, implying that it is about to become the current document. |
      | :vlr-documentToBeDeactivated | Another window (inside or outside of AutoCAD) has been activated. |
    * *callback\_function* is a symbol representing a function to be called when the event fires. Each callback function accepts two arguments:

      *reactor\_object* -- The VLR object that called the callback function.

      *list* -- A list of extra data elements associated with the particular event. The contents of this list for particular events are
      shown in the “DocManager reactor callback data” table.

      | DocManager reactor callback data | | |
      | Name | List length | Parameters |
      | :vlr-documentCreated  :vlr-documentToBeDestroyed  :vlr-documentBecameCurrent  :vlr-documentToBeActivated  :vlr-documentToBeDeactivated | 1 | The affected document object (VLA-object). |
      | :vlr-documentLockModeChangeVetoed | 2 | First parameter is the affected document object (VLA-object).  Second parameter is the global command string passed in for the lock request. If the callback is being made on behalf of an unlock request, the string will be prefixed with “#”. |
      | :vlr-documentLockModeWillChange  :vlr-documentLockModeChanged | 5 | First parameter is the affected document object (VLA-object).  Second parameter is an integer indicating the lock currently in effect for the document object.  Third parameter is an integer indicating the lock mode that will be in effect after the lock is applied.  Fourth parameter is the strongest lock mode from all other execution contexts.  Fifth parameter is the global command string passed in for the lock request. If the callback is being made on behalf of an unlock request, the string will be prefixed with “#”.  Lock modes may be any of the following:  1—Auto Write Lock  2—Not Locked  4—Shared Write  8—Read  10—Exclusive Write |

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