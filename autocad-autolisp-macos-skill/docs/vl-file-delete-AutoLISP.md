# vl-file-delete (AutoLISP)

Deletes a file

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-file-delete filename)
```

*filename*
:   *Type:* String

    Name of the file to be deleted. If you do not specify a full path name,
    vl-file-delete searches the AutoCAD default drawing directory.

## Return Values

*Type:* T or nil

T if successful;
nil if delete failed.

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
:   Delete
    *newauto.bat*:

    ```
    (vl-file-delete "newauto.bat")
    nil
    ```

    Nothing was deleted because there is no
    *newauto.bat* file in the AutoCAD default drawing directory.

    Delete the
    *newauto.bat* file in the
    *c:\* directory:

    ```
    (vl-file-delete "c:/newauto.bat")
    T
    ```

    The delete was successful because the full path name identified an existing file.

Mac OS
:   Delete
    *newstart.sh*:

    ```
    (vl-file-delete "newstart.sh")
    nil
    ```

    Nothing was deleted because there is no
    *newstart.sh* file in the AutoCAD default drawing directory.

    Delete the
    *newstart.sh* file in the / <root> directory:

    ```
    (vl-file-delete "/newstart.sh")
    T
    ```

    The delete was successful because the full path name identified an existing file.

#### Related References

* [findfile (AutoLISP)](findfile-AutoLISP.md)
* [vl-file-copy (AutoLISP)](vl-file-copy-AutoLISP.md)
* [vl-file-rename (AutoLISP)](vl-file-rename-AutoLISP.md)
* [vl-filename-base (AutoLISP)](vl-filename-base-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*