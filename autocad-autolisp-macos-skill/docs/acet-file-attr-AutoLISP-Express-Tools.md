# acet-file-attr (AutoLISP/Express Tools)

Gets or sets the protection attributes of a specified file or directory.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

*Library:* acetutil.arx

## Signature

```
(acet-file-attr filename [attr])
```

filename
:   *Type:* String

    Name of the file or directory.

attr
:   *Type:* Integer

    If provided, a combination of one or more attribute flags.

    The following pre-defined constants are provided for this argument and as return values:

    * 1 =
      Acet:READONLY
    * 2 =
      Acet:HIDDEN
    * 4 =
      Acet:SYSTEM
    * 16 =
      Acet:DIRECTORY
    * 32 =
      Acet:ARCHIVE

## Return Values

*Type:* Integer

Returns the new or existing attributes, or -1 on error.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*