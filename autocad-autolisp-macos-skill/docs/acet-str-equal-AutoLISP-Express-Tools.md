# acet-str-equal (AutoLISP/Express Tools)

Compares strings for equality.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

## Signature

```
(acet-str-equal left right [matchCase])
```

left
:   *Type:* String

    The first string to compare.

right
:   *Type:* String

    The second string to compare.

matchCase
:   *Type:* T or
    nil

    If provided and non-nil, indicates that case sensitive comparison should be used. Normally case is ignored.

## Return Values

*Type:* T or
nil

Returns
T if the strings are identical, otherwise
nil. Also returns
nil if either of the first two arguments are not strings. Displays a usage message if less than two arguments are supplied.

## Remarks

This function uses multibyte comparison appropriate for the current codepage.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*