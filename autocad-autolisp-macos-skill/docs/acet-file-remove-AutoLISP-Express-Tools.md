# acet-file-remove (AutoLISP/Express Tools)

Deletes one or more files.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

*Library:* acetutil.arx

## Signature

```
(acet-file-remove filespec [force])
```

filespec
:   *Type:* String

    File specification, which may include wildcards.

force
:   *Type:* T or
    nil

    If provided and non-nil, indicates that even read-only files should be deleted.

## Return Values

*Type:* Integer

The number of files removed.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*