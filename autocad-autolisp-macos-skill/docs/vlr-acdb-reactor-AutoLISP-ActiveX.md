# vlr-acdb-reactor (AutoLISP/ActiveX)

Constructs a reactor object that notifies when an object is added to, modified in, or erased from a drawing database

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-acdb-reactor data callbacks)
```

*data*
:   *Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

    Any AutoLISP data to be associated with a reactor object; otherwise
    nil, if no data.

*callbacks*
:   *Type:* List

    A list of pairs of the following form:

    (*event-name . callback\_function*)

    * *event-name* is one of the following Database reactor events:

      | Database reactor events | |
      | Name | Event |
      | :vlr-objectAppended | An object has been appended to the drawing database. |
      | :vlr-objectUnAppended | An object has been detached from the drawing database, e.g., by using UNDO. |
      | :vlr-objectReAppended | A detached object has been restored in the drawing database, e.g., by using REDO. |
      | :vlr-objectOpenedForModify | An object is about to be changed. |
      | :vlr-objectModified | An object has been changed. |
      | :vlr-objectErased | An object has been flagged as being erased. |
      | :vlr-objectUnErased | An object's erased-flag has been removed. |
    * *callback\_function* is a symbol representing a function to be called when the event fires. Each callback function accepts two arguments:

      *reactor\_object* -- The VLR object that called the callback function

      *obj* -- The database object associated with the event

## Return Values

*Type:* VLR object

The
*reactor\_object* argument from the
*callback\_function*.

## Remarks

The
vlr-acdb-reactor function constructs a database reactor object.

## Examples

N/A

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*