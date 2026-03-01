# vl-file-rename (AutoLISP)

Renames a file

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-file-rename old-filename new-filename)
```

*old-filename*
:   *Type:* String

    Name of the file you want to rename. If you do not specify a full path name,
    vl-file-rename looks in the AutoCAD default drawing directory.

*new-filename*
:   *Type:* String

    New name to be assigned to the file.

    NOTE:If you do not specify a path name,
    vl-file-rename writes the renamed file to the AutoCAD default drawing directory.

## Return Values

*Type:* T or nil

T, if renaming completed successfully;
nil if renaming failed.

NOTE:If the target file already exists, this function fails.

## Release Information

*Releases:*

* AutoCAD R14 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *old-filename* and
  *new-filename* arguments previously accepted ASCII text strings, but they now accept Unicode text strings.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

Windows
:   ```
    (vl-file-rename "c:/newauto.bat" "c:/myauto.bat")
    T
    ```

Mac OS and Web
:   ```
    (vl-file-rename "/oldstartup.sh" "/mystartup.sh")
    T
    ```

#### Related References

* [findfile (AutoLISP)](findfile-AutoLISP.md)
* [vl-file-copy (AutoLISP)](vl-file-copy-AutoLISP.md)
* [vl-file-delete (AutoLISP)](vl-file-delete-AutoLISP.md)
* [vl-filename-base (AutoLISP)](vl-filename-base-AutoLISP.md)
* [vl-filename-extension (AutoLISP)](vl-filename-extension-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*