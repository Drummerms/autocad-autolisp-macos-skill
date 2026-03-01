# vl-directory-files (AutoLISP)

Lists all files in a given directory

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-directory-files [directory pattern directories])
```

*directory*
:   *Type:* String

    Directory name to collect files for; if
    nil or absent,
    vl-directory-files uses the current directory.

*pattern*
:   *Type:* String

    Valid wildcard pattern for the file name; if
    nil or absent,
    vl-directory-files assumes "\*.\*".

*directories*
:   *Type:* Integer

    Value that indicates whether the returned list should include directory names. Specify one of the following:

    *-1* -- List directories only

    *0* -- List files and directories (the default)

    *1* -- List files only

## Return Values

*Type:* List or nil

A list of file and path names; otherwise
nil if no files match the specified pattern.

## Release Information

*Releases:*

* AutoCAD R14 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *directory* and
  *pattern* arguments previously accepted ASCII text strings, but they now accept Unicode text strings.
* Return value was modified to support Unicode characters and might be different than earlier releases. For example,
  (vl-directory-files "c:/") previously returned the directory name "abc中" as "abc?", but now correctly returns the directory name as "abc中". Also previously
  passing a directory name with a Unicode character returned a value of
  nil even if the directory existed.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

Windows
:   ```
    (vl-directory-files "c:/acadwin" "acad*.exe")
    ("ACAD.EXE" "ACADAPP.EXE" "ACADL.EXE" "ACADPS.EXE")

    (vl-directory-files "e:/acadwin" nil -1)
    ("." ".." "SUPPORT" "SAMPLE" "ADS" "FONTS" "IGESFONT" "SOURCE" "ASE")

    (vl-directory-files "E:/acad" nil -1)
    ("." ".." "WIN" "COM" "DOS")
    ```

Mac OS
:   ```
    (vl-directory-files "/myutilities/lsp" "*.lsp")
    (".DS_Store" "utilities.lsp" "blk-insert.lsp")

    (vl-directory-files "/myutilities" nil -1)
    ("." ".." "Help" "Lsp" "Support")
    ```

Web
:   ```
    (vl-directory-files "/acad/Support" "*.lin")
    ("acad.lin")

    (vl-directory-files "/acad/Support" nil -1)
    ("." "..")
    ```

#### Related References

* [findfile (AutoLISP)](findfile-AutoLISP.md)
* [getfiled (AutoLISP)](getfiled-AutoLISP.md)
* [findtrustedfile (AutoLISP)](findtrustedfile-AutoLISP.md)
* [vl-mkdir (AutoLISP)](vl-mkdir-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*