# vl-string-right-trim (AutoLISP)

Removes the specified characters from the end of a string

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-string-right-trim char-set str)
```

*char-set*
:   *Type:* String

    A textual value listing the characters to be removed.

*str*
:   *Type:* String

    The textual value to be stripped of
    *char-set*.

## Return Values

*Type:* String

A textual value containing a substring of
*str* with all trailing characters in
*char-set* removed.

## Release Information

*Releases:*

* AutoCAD R14 and later on Windows
* AutoCAD 2011 and later on Mac OS

## Examples

```
(vl-string-right-trim " \t\
" " STR \
\t ")
" STR"

(vl-string-right-trim "1356789" "3CPO is not R2D267891")
"3CPO is not R2D2"

(vl-string-right-trim " " "There are too many spaces here      ")
"There are too many spaces here"
```

#### Related References

* [vl-string-left-trim (AutoLISP)](vl-string-left-trim-AutoLISP.md)
* [vl-string-trim (AutoLISP)](vl-string-trim-AutoLISP.md)
* [substr (AutoLISP)](substr-AutoLISP.md)

#### Related Concepts

* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*