# vl-file-size (AutoLISP)

Determines the size of a file, in bytes

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-file-size filename)
```

*filename*
:   *Type:* String

    Naming the file to be sized. If you do not specify a full path name,
    vl-file-size searches the AutoCAD default drawing directory for the file.

## Return Values

*Type:* Integer

If successful,
vl-file-size returns an integer showing the size of
*filename*. If the file is not readable,
vl-file-size returns
nil. If
*filename* is a directory or an empty file,
vl-file-size returns 0.

## Release Information

*Releases:*

* AutoCAD R14 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *filename* argument previously accepted an ASCII text string, but now accepts a Unicode text string.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

Windows
:   ```
    (vl-file-size "c:/autoexec.bat")
    1417

    (vl-file-size "c:/")
    0
    ```

    In the preceding example,
    vl-file-size returned 0 because
    *c:/* names a directory.

Mac OS and Web
:   ```
    (vl-file-size "/output.txt")
    568

    (vl-file-size "/")
    0
    ```

    In the preceding example,
    vl-file-size returned 0 because
    */* names the <root> of the drive and not a file.

#### Related References

* [findfile (AutoLISP)](findfile-AutoLISP.md)
* [vl-file-systime (AutoLISP)](vl-file-systime-AutoLISP.md)
* [vl-filename-base (AutoLISP)](vl-filename-base-AutoLISP.md)
* [vl-filename-extension (AutoLISP)](vl-filename-extension-AutoLISP.md)
* [vl-filename-directory (AutoLISP)](vl-filename-directory-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*