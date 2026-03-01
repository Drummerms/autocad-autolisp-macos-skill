# vl-string-elt (AutoLISP)

Returns the character code for the character at a specified position in a string

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-string-elt str position)
```

*str*
:   *Type:* String

    A textual value to be inspected.

*position*
:   *Type:* Integer

    A displacement in the string; the first character is displacement 0.

## Return Values

*Type:* Integer or error

A numeric value denoting the character code for the character at the specified position.

NOTE:An error occurs if
*position* is outside the range of the
*str*.

## Release Information

*Releases:*

* AutoCAD R14 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *str* argument previously accepted an ASCII text string or character (range of 1-255), but now accepts a Unicode text string or
  character (range of 1-65536).
* Return value was modified to support Unicode characters and might be different than earlier releases. For example,
  (vl-string-elt "abc中" 3) previously returned 128, but now returns 20013.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

```
(vl-string-elt "May the Force be with you" 8)
70
```

#### Related References

* [vl-string->list (AutoLISP)](vl-string-list-AutoLISP.md)
* [ascii (AutoLISP)](ascii-AutoLISP.md)
* [list (AutoLISP)](list-AutoLISP.md)
* [vl-list\* (AutoLISP)](vl-list-AutoLISP.md)

#### Related Concepts

* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*