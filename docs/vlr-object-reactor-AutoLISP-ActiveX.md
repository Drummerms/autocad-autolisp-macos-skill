# vlr-object-reactor (AutoLISP/ActiveX)

Constructs a drawing object reactor object

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-object-reactor owners data callbacks)
```

*owners*
:   *Type:* List

    An AutoLISP list of VLA-objects identifying the drawing objects to be watched.

*data*
:   *Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

    Any AutoLISP data to be associated with the reactor object; otherwise
    nil if no data.

*callbacks*
:   *Type:* List

    A list of pairs of the following form:

    (e*vent-name* .
    *callback\_function*)

    * *event-name* is one of the following Object Events:

      | Object events | |
      | Name | Event |
      | :vlr-cancelled | The modification of the object has been canceled. |
      | :vlr-copied | The object has been copied. |
      | :vlr-erased | Erase-flag of the object has been set. |
      | :vlr-unerased | Erase-flag of the object has been reset. |
      | :vlr-goodbye | The object is about to be deleted from memory. |
      | :vlr-openedForModify | The object is about to be modified. |
      | :vlr-modified | The object has been modified. If the modification was canceled, also :vlr-cancelled and :vlr-modifyUndone will be fired. |
      | :vlr-subObjModified | A sub-entity of the object has been modified. This event is triggered for modifications to vertices of polylines or meshes, and for attributes owned by block references. |
      | :vlr-modifyUndone | The object's modification was undone. |
      | :vlr-modifiedXData | The object's extended entity data has been modified. |
      | :vlr-unappended | The object has been detached from the drawing database. |
      | :vlr-reappended | The object has been re-attached to the drawing database. |
      | :vlr-objectClosed | The object's modification has been finished. |
    * *callback\_function* is a symbol representing a function to be called when the event fires. Each callback function accepts three arguments:

      *owner* -- The owner of the VLA-object the event applies to.

      *reactor\_object* -- The VLR object that called the callback function.

      *list* -- A list of extra data elements associated with the particular event. The contents of this list for particular events are
      shown in the “Object Events Callback Data” table.

      | Object events callback data | | |
      | Name | List length | Parameters |
      | :vlr-cancelled  :vlr-erased,  :vlr-unerased  :vlr-goodbye  :vlr-openedForModify  :vlr-modified  :vlr-modifyUndone  :vlr-modifiedXData  :vlr-unappended  :vlr-reappended  :vlr-objectClosed | 0 |  |
      | :vlr-copied | 1 | The object created by the copy operation (ename). |
      | :vlr-subObjModified | 1 | The sub-object (ename) that has been modified |

## Return Values

*Type:* VLR object

The
*reactor\_object* argument from the
*callback\_function*.

## Remarks

The reactor object is added to the drawing database, but does not become persistent.

## Examples

The following code attaches an object reactor to the
myCircle object. It defines the reactor to respond whenever the object is modified (:vlr-modified) and to call the
print-radius function in response to the modification event:

```
(setq circleReactor (vlr-object-reactor (list myCircle)
         "Circle Reactor" '((:vlr-modified . print-radius))))
```

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*