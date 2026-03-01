# strcat (AutoLISP)

Returns a string that is the concatenation of multiple strings

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(strcat [string string_n ...])
```

*string*
:   *Type:* String

    Text values to concatenate.

## Return Values

*Type:* String

Concatenate text string. If no arguments are supplied,
strcat returns a zero-length string.

## Examples

```
(strcat "a" "bout")
"about"

(strcat "a" "b" "c")
"abc"

(strcat "a" "" "c")
"ac"

(strcat)
""
```

#### Related References

* [strcase (AutoLISP)](strcase-AutoLISP.md)
* [strlen (AutoLISP)](strlen-AutoLISP.md)
* [substr (AutoLISP)](substr-AutoLISP.md)

#### Related Concepts

* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*