# vl-file-directory-p (AutoLISP)

Determines if a file name refers to a directory

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-file-directory-p filename)
```

*filename*
:   *Type:* String

    File name. If you do not specify a full path name,
    vl-file-directory-p searches only the AutoCAD default drawing directory.

## Return Values

*Type:* T or nil

T, if
*filename* is the name of a directory;
nil if it is not.

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
    (vl-file-directory-p "sample")
    T

    (vl-file-directory-p "yinyang")
    nil

    (vl-file-directory-p "c:/My Documents")
    T

    (vl-file-directory-p "c:/My Documents/lisp/yinyang.lsp")
    nil
    ```

Mac OS and Web
:   ```
    (vl-file-directory-p "support")
    T

    (vl-file-directory-p "xyz")
    nil

    (vl-file-directory-p "/documents")
    T

    (vl-file-directory-p "/documents/output.txt")
    nil
    ```

#### Related References

* [findfile (AutoLISP)](findfile-AutoLISP.md)
* [vl-directory-files (AutoLISP)](vl-directory-files-AutoLISP.md)
* [vl-filename-directory (AutoLISP)](vl-filename-directory-AutoLISP.md)
* [vl-mkdir (AutoLISP)](vl-mkdir-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*