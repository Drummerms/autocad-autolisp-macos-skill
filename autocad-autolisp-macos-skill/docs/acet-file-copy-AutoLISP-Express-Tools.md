# acet-file-copy (AutoLISP/Express Tools)

Copies a file.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

*Library:* acetutil.arx

## Signature

```
(acet-file-copy from to [force])
```

from
:   *Type:* String

    Name of file to copy.

to
:   *Type:* String

    Name of new file.

force
:   *Type:* T or
    nil

    If provided and non-nil, forces any existing file to be overwritten.

    NOTE:This function will not overwrite read-only files. The read-only flag can be cleared with
    acet-file-attr.

## Return Values

*Type:* T or
nil

Returns
T if successful.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*