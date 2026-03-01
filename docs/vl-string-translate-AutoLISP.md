# vl-string-translate (AutoLISP)

Replaces characters in a string with a specified set of characters

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-string-translate source-set dest-set str)
```

*source-set*
:   *Type:* String

    Characters to be matched.

*dest-set*
:   *Type:* String

    Characters to be substituted for those in
    *source-set*.

*str*
:   *Type:* String

    The textual value to be searched and translated.

## Return Values

*Type:* String

The value of
*str* after any substitutions have been made.

## Release Information

*Releases:*

* AutoCAD R14 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *source-set*,
  *dest-set* and
  *str* arguments previously accepted ASCII text strings or characters, but they now accept Unicode text strings or characters.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

```
(vl-string-translate "abcABC" "123123" "A is a, B is b, C is c")
"1 is 1, 2 is 2, 3 is 3"

(vl-string-translate "abc" "123" "A is a, B is b, C is c")
"A is 1, B is 2, C is 3"
```

#### Related References

* [vl-string-mismatch (AutoLISP)](vl-string-mismatch-AutoLISP.md)
* [vl-string-position (AutoLISP)](vl-string-position-AutoLISP.md)
* [vl-string-search (AutoLISP)](vl-string-search-AutoLISP.md)
* [vl-string-subst (AutoLISP)](vl-string-subst-AutoLISP.md)

#### Related Concepts

* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*