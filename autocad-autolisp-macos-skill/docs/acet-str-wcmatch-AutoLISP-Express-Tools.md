# acet-str-wcmatch (AutoLISP/Express Tools)

Performs a wild-card match similar to
wcmatch, but allows control over case sensitivity.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-str-wcmatch string pattern [matchCase])
```

string
:   *Type:* String

    The string to search.

pattern
:   *Type:* String

    The wildcard pattern to match. See
    wcmatch for more details.

matchCase
:   *Type:* T or
    nil

    If provided and non-nil, indicates that case sensitive comparison should be used.

## Return Values

*Type:* T or
nil

T if string and pattern match

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*