# vlr-linker-reactor (AutoLISP/ActiveX)

Constructs a reactor object that notifies your application every time an ObjectARX application is loaded or unloaded

*Supported Platforms:* Windows only; not available on Mac OS or Web

## Signature

```
(vlr-linker-reactor data callbacks)
```

*data*
:   *Type:* Integer, Real, String, List, VLA-object, Safearray, Variant, T, or nil

    Any AutoLISP data to be associated with the reactor object.

*callbacks*
:   *Type:* List

    A list of pairs of the following form:

    (*event-name . callback\_function*)

    * *event-name* is one of the following Linker reactor events:

      | Linker reactor events | |
      | Name | Event |
      | :vlr-rxAppLoaded | The dynamic linker has loaded a new ObjectARX program. The program has finished its initialization. |
      | :vlr-rxAppUnLoaded | The dynamic linker has unloaded an ObjectARX program. The program already has done its clean-up. |
    * *callback\_function* is a symbol representing a function to be called when the event fires. Each callback function accepts two arguments:

      *reactor\_object* -- The VLR object that called the callback function.

      *list* -- A list containing the name of the ObjectARX program that was loaded or unloaded (a string).

## Return Values

*Type:* VLR object

The
*reactor\_object* argument from the
*callback\_function*.

## Examples

```
(vlr-linker-reactor nil
   '((:vlr-rxAppLoaded . my-vlr-trace-reaction)))
#<VLR-Linker-Reactor>
```

#### Related Concepts

* [Reactor Functions Reference (AutoLISP/ActiveX)](Reactor-Functions-Reference-AutoLISP-ActiveX.md)
* [AutoLISP Extensions Reference (AutoLISP/ActiveX)](AutoLISP-Extensions-Reference-AutoLISP-ActiveX.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*