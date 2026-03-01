# vlr-window-reactor (AutoLISP/ActiveX)

Constructs an editor reactor object that notifies of an event related to moving or sizing an AutoCAD window

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-window-reactor data callbacks)
```

*data*
:   *Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

    Any AutoLISP data to be associated with the reactor object; otherwise
    nil if no data.

*callbacks*
:   *Type:* List

    A list of pairs of the following form:

    (*event-name . callback\_function*)

    * *event-name* is one of the following Window reactor events:

      | Window reactor events | |
      | Event name | Description |
      | :vlr-docFrameMovedOrResized | An MDI child frame window (a document window) has been moved or resized. |
      | :vlr-mainFrameMovedOrResized | The main AutoCAD window has been moved or resized. |
    * *callback\_function* is a symbol representing a function to be called when the event fires. Each callback function accepts two arguments:

      *reactor\_object* -- The VLR object that called the callback function.

      *list* -- A list of extra data elements associated with the particular event. The contents of this list for particular events are
      shown in the “Window reactor callback data” table.

      | Window reactor callback data | | |
      | Name | List length | Parameters |
      | :vlr-docFrameMovedOrResized  :vlr-mainFrameMovedOrResized | 2 | The first parameter is an integer containing the HWND of the window.  The second parameter indicates whether the window has been moved or resized. The value is T if the window has been moved, nil if the window has been resized. |

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