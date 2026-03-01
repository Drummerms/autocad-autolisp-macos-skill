# vlr-command-reactor (AutoLISP/ActiveX)

Constructs an editor reactor that notifies of a command event

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-command-reactor data callbacks)
```

*data*
:   *Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

    Any AutoLISP data to be associated with the reactor object; otherwise
    nil if no data is to be associated with the reactor.

*callbacks*
:   *Type:* List

    A list of pairs of the following form:

    (*event-name . callback\_function* )

    * *event-name* is one of the following Command reactor events:

      | Command reactor events | |
      | Event name | Description |
      | :vlr-unknownCommand | A command not known to AutoCAD was issued. |
      | :vlr-commandWillStart | An AutoCAD command has been called. |
      | :vlr-commandEnded | An AutoCAD command has completed. |
      | :vlr-commandCancelled | An AutoCAD command has been canceled. |
      | :vlr-commandFailed | An AutoCAD command failed to complete. |
    * *callback\_function* is a symbol representing a function to be called when the event fires.

      Each callback function accepts two arguments:

      *reactor\_object* -- The VLR object that called the callback function.

      *list* -- A list containing a single element, the string identifying the command.

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