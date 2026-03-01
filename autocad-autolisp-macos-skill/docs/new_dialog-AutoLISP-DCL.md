# new\_dialog (AutoLISP/DCL)

Begins a new dialog box and displays it, and can also specify a default action

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(new_dialog dlgname dcl_id [action [screen-pt]])
```

*dlgname*
:   *Type:* String

    Dialog box.

*dcl\_id*
:   *Type:* Integer

    The DCL file identifier obtained by
    load\_dialog.

*action*
:   *Type:* String

    AutoLISP expression to use as the default action. If you don't want to define a default action, specify an empty string (""). The
    *action* argument is required if you specify
    *screen-pt*.

    The default action is evaluated when the user picks an active tile that doesn't have an action or callback explicitly assigned
    to it by
    action\_tile or in DCL.

*screen-pt*
:   *Type:* List

    A 2D point that specifies the
    *X,Y* location of the dialog box on the screen. The point specifies the upper-left corner of the dialog box. If you pass the point
    as '(-1 -1), the dialog box is opened in the default position (the center of the AutoCAD drawing area).

## Return Values

*Type:* T or nil

T, if successful; otherwise
nil.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

## Examples

N/A

#### Related References

* [done\_dialog (AutoLISP/DCL)](done_dialog-AutoLISP-DCL.md)
* [load\_dialog (AutoLISP/DCL)](load_dialog-AutoLISP-DCL.md)
* [start\_dialog (AutoLISP/DCL)](start_dialog-AutoLISP-DCL.md)
* [term\_dialog (AutoLISP/DCL)](term_dialog-AutoLISP-DCL.md)
* [unload\_dialog (AutoLISP/DCL)](unload_dialog-AutoLISP-DCL.md)

#### Related Concepts

* [Dialog Box Opening and Closing Functions Reference (AutoLISP/DCL)](Dialog-Box-Opening-and-Closing-Functions-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*