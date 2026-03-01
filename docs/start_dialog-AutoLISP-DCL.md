# start\_dialog (AutoLISP/DCL)

Displays a dialog box and begins accepting user input

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(start_dialog)
```

No arguments.

## Return Values

*Type:* Integer

The
start\_dialog function returns the optional
*status* passed to
done\_dialog. The default value is
1 if the user presses OK,
0 if the user presses Cancel, or
-1 if all dialog boxes are terminated with
term\_dialog. If
done\_dialog is passed an integer
*status* greater than 1,
start\_dialog returns this value, whose meaning is determined by the application.

## Remarks

You must first initialize the dialog box by a previous
new\_dialog call. The dialog box remains active until an action expression or callback function calls
done\_dialog. Usually
done\_dialog is associated with the tile whose
key is
"accept" (typically the OK button) and the tile whose
key is
"cancel" (typically the Cancel button).

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

## Examples

N/A

#### Related References

* [done\_dialog (AutoLISP/DCL)](done_dialog-AutoLISP-DCL.md)
* [load\_dialog (AutoLISP/DCL)](load_dialog-AutoLISP-DCL.md)
* [new\_dialog (AutoLISP/DCL)](new_dialog-AutoLISP-DCL.md)
* [term\_dialog (AutoLISP/DCL)](term_dialog-AutoLISP-DCL.md)
* [unload\_dialog (AutoLISP/DCL)](unload_dialog-AutoLISP-DCL.md)

#### Related Concepts

* [Dialog Box Opening and Closing Functions Reference (AutoLISP/DCL)](Dialog-Box-Opening-and-Closing-Functions-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*