# strcase (AutoLISP)

Returns a string where all alphabetic characters have been converted to uppercase or lowercase

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(strcase string [which])
```

*string*
:   *Type:* String

    The text string to convert.

*which*
:   *Type:* T or nil

    If specified as
    T, all alphabetic characters in
    *string* are converted to lowercase. Otherwise, characters are converted to uppercase.

## Return Values

*Type:* String

Converted text value.

## Examples

```
(strcase "Sample")
"SAMPLE"

(strcase "Sample" T)
"sample"
```

The
strcase function will correctly handle case mapping of the currently configured character set.

#### Related References

* [strcat (AutoLISP)](strcat-AutoLISP.md)
* [strlen (AutoLISP)](strlen-AutoLISP.md)
* [substr (AutoLISP)](substr-AutoLISP.md)

#### Related Concepts

* [String-Handling Functions Reference (AutoLISP)](String-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*