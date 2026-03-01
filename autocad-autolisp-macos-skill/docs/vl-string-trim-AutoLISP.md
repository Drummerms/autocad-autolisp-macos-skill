# vl-string-trim (AutoLISP)

Removes the specified characters from the beginning and end of a string

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-string-trim char-set str)
```

*char-set*
:   *Type:* String

    Characters to be removed.

*str*
:   *Type:* String

    The textual value to be trimmed of
    *char-set*.

## Return Values

*Type:* String

The value of
*str*, after any characters have been trimmed.

## Release Information

*Releases:*

* AutoCAD R14 and later on Windows
* AutoCAD 2011 and later on Mac OS

## Examples

```
(vl-string-trim " \t\
" " \t\
 STR \
\t ")
"STR"

(vl-string-trim "this is junk" "this is junk Don't call this junk! this is junk")
"Don't call this junk!"

(vl-string-trim " " "      Leave me alone   ")
"Leave me alone"
```

#### Related References

* [vl-string-left-trim (AutoLISP)](vl-string-left-trim-AutoLISP.md)
* [vl-string-right-trim (AutoLISP)](vl-string-right-trim-AutoLISP.md)
* [substr (AutoLISP)](substr-AutoLISP.md)

#### Related Concepts

* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*