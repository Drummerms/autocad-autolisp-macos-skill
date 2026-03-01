# vl-string-mismatch (AutoLISP)

Returns the length of the longest common prefix for two strings, starting at specified positions

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-string-mismatch str1 str2 [pos1 pos2 ignore-case-p])
```

*str1*
:   *Type:* String

    The first textual value to be matched.

*str2*
:   *Type:* String

    The second textual value to be matched.

*pos1*
:   *Type:* Integer

    A numeric value identifying the position to search from in the first string; 0 if omitted.

*pos2*
:   *Type:* Integer

    A numeric value identifying the position to search from in the second string; 0 if omitted.

*ignore-case-*p
:   *Type:* T or nil

    If
    T is specified for this argument, case is ignored; otherwise, case is considered.

## Return Values

*Type:* Integer

A numeric value.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *str1* and
  *str2* arguments previously accepted ASCII text strings or characters, but these arguments now accept Unicode text strings or characters.
* Return value was modified to support Unicode characters and might be different than earlier releases. In earlier releases,
  the length of a Unicode character was improperly calculated. For example,
  (vl-string-mismatch "abc中abc" "abc中ñ") previously returned 10, but now returns 4.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

```
(vl-string-mismatch "VL-FUN" "VL-VAR")
3

(vl-string-mismatch "vl-fun" "avl-var")
0

(vl-string-mismatch "abc中abc" "abc中ñ")
4

(vl-string-mismatch "€abc" "abc€")
0

(vl-string-mismatch "vl-fun" "avl-var" 0 1)
3

(vl-string-mismatch "VL-FUN" "Vl-vAR")
1

(vl-string-mismatch "VL-FUN" "Vl-vAR" 0 0 T)
3

(vl-string-mismatch "abc€" "ABC€" 0 0 T)
4
```

#### Related References

* [vl-string-position (AutoLISP)](vl-string-position-AutoLISP.md)
* [vl-string-search (AutoLISP)](vl-string-search-AutoLISP.md)
* [vl-string-subst (AutoLISP)](vl-string-subst-AutoLISP.md)
* [vl-string-translate (AutoLISP)](vl-string-translate-AutoLISP.md)

#### Related Concepts

* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*