# vl-string->list (AutoLISP)

Converts a string into a list of character codes

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-string->list str)
```

*str*
:   *Type:* String

    A textual value.

## Return Values

*Type:* List or nil

A list, each element of which is an integer representing the character codes of the corresponding characters in
*str*.

## Release Information

*Releases:*

* AutoCAD R14 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *str* argument previously accepted an ASCII text string or character, but now accepts a Unicode text string or character.
* Return value was modified to support Unicode characters and might be different than earlier releases. For example,
  (vl-string->list "1€") previously returned (49 128), but now returns (49 8364).
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

```
(vl-string->list "")
nil

(vl-string->list "12")
(49 50)
```

#### Related References

* [vl-string-elt (AutoLISP)](vl-string-elt-AutoLISP.md)
* [vl-list->string (AutoLISP)](vl-list-string-AutoLISP.md)
* [ascii (AutoLISP)](ascii-AutoLISP.md)
* [list (AutoLISP)](list-AutoLISP.md)
* [vl-list\* (AutoLISP)](vl-list-AutoLISP.md)

#### Related Concepts

* [List Manipulation Functions Reference (AutoLISP)](List-Manipulation-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*