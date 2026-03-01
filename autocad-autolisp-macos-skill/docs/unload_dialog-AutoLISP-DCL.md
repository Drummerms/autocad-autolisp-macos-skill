# unload\_dialog (AutoLISP/DCL)

Unloads a DCL file

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(unload_dialog dcl_id)
```

*dcl\_id*
:   *Type:* Integer

    A DCL file identifier obtained from a previous
    load\_dialog call.

## Return Values

*Type:* nil

Always returns
nil.

## Remarks

Unloads the DCL file associated with
*dcl\_id* (obtained from a previous
new\_dialog call) from memory.

While it isn't necessary to unload a DCL definition from memory, it is recommended to unload DCL definitions when they aren't
needed. Unloading DCL files helps to free up system resources and allows you to update a DCL dialog definition from a new
file.

NOTE:DCL on Mac OS uses more memory than on Windows, unload DCL file definitions that are not needed to avoid running low on memory.

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
* [term\_dialog (AutoLISP/DCL)](term_dialog-AutoLISP-DCL.md)

#### Related Concepts

* [Dialog Box Opening and Closing Functions Reference (AutoLISP/DCL)](Dialog-Box-Opening-and-Closing-Functions-Reference-AutoLISP-DCL.md)
* [Programmable Dialog Box Functions By Functionality (AutoLISP/DCL)](Programmable-Dialog-Box-Functions-By-Functionality-AutoLISP-DCL.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*