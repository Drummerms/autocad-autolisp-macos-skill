# acet-file-dir (AutoLISP/Express Tools)

Locate files.

*Supported Platforms:* AutoCAD for Windows only; not available in AutoCAD LT for Windows, or on Mac OS and Web

*Library:* acetutil.arx

## Signature

```
(acet-file-dir pattern [attributes] [starting-directory])
```

pattern
:   *Type:* String

    A file specification, which may include wildcards and/or a directory name.

attributes
:   *Type:* Integer

    If provided, contains a bitcode of file attributes to match see the
    acet-file-attr function.

starting-directory
:   *Type:* String

    If provided, this function will also search subdirectories for files that match pattern (which can also contain a directory
    name). Uses the current working directory, see the
    acet-file-cwd function if a relative path is provided.

## Return Values

*Type:* List or
nil

A list of matching file names, or
nil if no matching files are found.

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*