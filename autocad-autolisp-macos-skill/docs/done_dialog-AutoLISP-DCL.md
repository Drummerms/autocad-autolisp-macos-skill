# done\_dialog (AutoLISP/DCL)

Terminates a dialog box

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(done_dialog [status])
```

*status*
:   *Type:* Integer

    A positive integer that
    start\_dialog will return instead of returning
    1 for OK or
    0 for Cancel. The meaning of any
    *status* value greater than 1 is determined by your application.

## Return Values

*Type:* List

A two-dimensional point that is the (*X*,*Y*) location of the dialog box when the user exited it.

## Remarks

If you provide a callback for the button whose key is
"accept" or
"cancel" (usually the OK and Cancel buttons), the callback must call
done\_dialog explicitly. If it does not, the user can be trapped in the dialog box. If you do not provide an explicit callback for these
buttons and use the standard exit buttons, AutoCAD handles them automatically. Also, an explicit AutoLISP action for the
"accept" button must specify a
*status* of 1 (or an application-defined value); otherwise,
start\_dialog returns the default value, 0, which makes it appear as if the dialog box was canceled.

You must call
done\_dialog from within an action expression or callback function.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

## Examples

N/A

#### Related References

* [load\_dialog (AutoLISP/DCL)](load_dialog-AutoLISP-DCL.md)
* [new\_dialog (AutoLISP/DCL)](new_dialog-AutoLISP-DCL.md)
* [start\_dialog (AutoLISP/DCL)](start_dialog-AutoLISP-DCL.md)
* [term\_dialog (AutoLISP/DCL)](term_dialog-AutoLISP-DCL.md)
* [unload\_dialog (AutoLISP/DCL)](unload_dialog-AutoLISP-DCL.md)

#### Related Concepts

* [Dialog Box Opening and Closing Functions Reference (AutoLISP/DCL)](Dialog-Box-Opening-and-Closing-Functions-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*