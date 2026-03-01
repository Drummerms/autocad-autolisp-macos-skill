# vl-string-search (AutoLISP)

Searches for the specified pattern in a string

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-string-search pattern str [start-pos])
```

*pattern*
:   *Type:* String

    The textual value containing the pattern to be searched for.

*str*
:   *Type:* String

    The textual value to be searched for
    *pattern*.

*start-pos*
:   *Type:* Integer

    A numeric value identifying the starting position of the search; 0 if omitted.

## Return Values

*Type:* Integer

A numeric value representing the position in the string where the specified
*pattern* was found; otherwise
nil if the pattern is not found; the first character of the string is position 0.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *pattern* and
  *str* arguments previously accepted ASCII text strings or characters, but they now accept Unicode text strings or characters.
* Return value was modified to support Unicode characters and might be different than earlier releases. In earlier releases,
  the length of a Unicode character was improperly calculated. For example,
  (vl-string-search "€" "€abc中€" 1) previously returned 11, but now returns 5.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

```
(vl-string-search "foo" "pfooyey on you")
1

(vl-string-search "who" "pfooyey on you")
nil

(vl-string-search "foo" "fooey-more-fooey" 1)
11

(vl-string-search "€" "€abc中€")
0

(vl-string-search "测试" "€abc中€" 1)
nil

(vl-string-search "€" "€abc中€" 1)
5
```

#### Related References

* [vl-string-mismatch (AutoLISP)](vl-string-mismatch-AutoLISP.md)
* [vl-string-position (AutoLISP)](vl-string-position-AutoLISP.md)
* [vl-string-subst (AutoLISP)](vl-string-subst-AutoLISP.md)
* [vl-string-translate (AutoLISP)](vl-string-translate-AutoLISP.md)

#### Related Concepts

* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*