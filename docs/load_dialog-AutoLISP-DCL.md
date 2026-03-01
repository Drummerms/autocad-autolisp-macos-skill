# load\_dialog (AutoLISP/DCL)

Loads a DCL file

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(load_dialog dclfile)
```

*dclfile*
:   *Type:* String

    DCL file to load. If the
    *dclfile* argument does not specify a file extension, .*dcl* is assumed.

## Return Values

*Type:* Integer

A positive integer value (dcl\_id) if successful, or a negative integer if
load\_dialog cannot open the file. The
dcl\_id is used as a handle in subsequent
new\_dialog and
unload\_dialog calls.

## Remarks

The
load\_dialog function searches for files according to the AutoCAD library search path.

This function is the complement of
unload\_dialog. An application can load multiple DCL files with multiple
load\_dialog calls.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2021 and later on Mac OS

## Examples

N/A

#### Related References

* [done\_dialog (AutoLISP/DCL)](done_dialog-AutoLISP-DCL.md)
* [new\_dialog (AutoLISP/DCL)](new_dialog-AutoLISP-DCL.md)
* [start\_dialog (AutoLISP/DCL)](start_dialog-AutoLISP-DCL.md)
* [term\_dialog (AutoLISP/DCL)](term_dialog-AutoLISP-DCL.md)
* [unload\_dialog (AutoLISP/DCL)](unload_dialog-AutoLISP-DCL.md)

#### Related Concepts

* [Dialog Box Opening and Closing Functions Reference (AutoLISP/DCL)](Dialog-Box-Opening-and-Closing-Functions-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*