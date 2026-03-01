# substr (AutoLISP)

Returns a substring of a string

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(substr str start [length])
```

*str*
:   *Type:* String

    A textual value.

*start*
:   *Type:* Integer

    A positive numeric value indicating the starting position in
    *str*. The first character in the string is position 1.

*length*
:   *Type:* Integer

    A positive numeric value specifying the number of characters to search through in
    *str*. If
    *length* is not specified, the substring continues to the end of
    *str*.

## Return Values

*Type:* String

A substring from
*str*.

## Remarks

The
substr function starts at the
*start* character position of
*str* and continues for
*length* characters.

NOTE:The first character of
*str* is character number 1. This differs from other functions that process elements of a list (like
nth and
ssname) that count the first element as 0.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *str* argument previously accepted an ASCII text string or character, but now accepts a Unicode text string or character.
* Return value was modified to support Unicode characters and might be different than earlier releases. In earlier releases,
  the length of a Unicode character was improperly calculated. For example,
  (substr "中国" 1 1) previously returned "\\", but now returns "中".
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Example

```
(substr "abcde" 2)
"bcde"

(substr "abcde" 2 1)
"b"

(substr "abcde" 3 2)
"cd"

(substr "€abc€" 4 2)
"c€"

(substr "中国" 1 1)
"中"
```

#### Related References

* [strcase (AutoLISP)](strcase-AutoLISP.md)
* [strcat (AutoLISP)](strcat-AutoLISP.md)
* [strlen (AutoLISP)](strlen-AutoLISP.md)

#### Related Concepts

* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*