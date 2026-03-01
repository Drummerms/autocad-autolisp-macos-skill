# vl-list->string (AutoLISP)

Combines the characters associated with a list of integers into a string

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-list->string char-codes-list)
```

*char-codes-list*
:   *Type:* List

    A list of non-negative integers. Each integer must be in the range of 1-65536.

## Return Values

*Type:* String

A textual value consisting of characters, with each character based on one of the integers supplied in
*char-codes-list*.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *char-codes-list* argument previously accepted integers in the range of 1-255, but now accepts integers in the range of 1-65536.
* Return value was modified to support Unicode characters and might be different than earlier releases. For example,
  (vl-list->string (list 49 128)) previously returned "1€", but now returns "1". If you want to return "1€", your code will need to be updated to
  (vl-list->string (list 49 8364)).
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

```
(vl-list->string nil)
""

(vl-list->string '(49 50))
"12"
```

#### Related References

* [list (AutoLISP)](list-AutoLISP.md)
* [vl-list\* (AutoLISP)](vl-list-AutoLISP.md)
* [chr (AutoLISP)](chr-AutoLISP.md)
* [vl-string->list (AutoLISP)](vl-string-list-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*