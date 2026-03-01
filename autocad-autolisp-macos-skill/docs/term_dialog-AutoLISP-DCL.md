# term\_dialog (AutoLISP/DCL)

Terminates all current dialog boxes as if the user had canceled each of them

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(term_dialog)
```

No arguments.

## Return Values

*Type:* nil

Always returns
nil.

## Remarks

If an application is terminated while any DCL files are open, AutoCAD automatically calls
term\_dialog. This function is used mainly for aborting nested dialog boxes.

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
* [start\_dialog (AutoLISP/DCL)](start_dialog-AutoLISP-DCL.md)
* [unload\_dialog (AutoLISP/DCL)](unload_dialog-AutoLISP-DCL.md)

#### Related Concepts

* [Dialog Box Opening and Closing Functions Reference (AutoLISP/DCL)](Dialog-Box-Opening-and-Closing-Functions-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*