# vl-mkdir (AutoLISP)

Creates a directory

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-mkdir directoryname)
```

*directoryname*
:   *Type:* String

    The name of the directory you want to create.

## Return Values

*Type:* T or nil

T if successful,
nil if the directory exists or if unsuccessful.

## Release Information

*Releases:*

* AutoCAD R14 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *directoryname* argument previously accepted an ASCII text string, but now accepts a Unicode text string.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

Windows
:   ```
    (vl-mkdir "c:\\mydirectory")
    T
    ```

Mac OS and Web
:   ```
    (vl-mkdir "/mydirectory")
    T
    ```

#### Related References

* [vl-directory-files (AutoLISP)](vl-directory-files-AutoLISP.md)
* [vl-file-directory-p (AutoLISP)](vl-file-directory-p-AutoLISP.md)
* [vl-filename-directory (AutoLISP)](vl-filename-directory-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*