# vl-file-copy (AutoLISP)

Copies or appends the contents of one file to another file

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(vl-file-copy source-file destination-file [append])
```

*source-file*
:   *Type:* String

    Name of file to be copied. If you do not specify a full path name,
    vl-file-copy looks in the AutoCAD default drawing directory.

*destination-file*
:   *Type:* String

    Name of the destination file. If you do not specify a path name,
    vl-file-copy writes to the AutoCAD default drawing directory.

*append*
:   *Type:* T or nil

    If specified and not
    nil,
    *source-file* is appended to
    *destination-file* (that is, copied to the end of the destination file).

## Return Values

*Type:* Integer or nil

A numeric value, if the copy was successful; otherwise
nil.

Some typical reasons for returning
nil are

* *source-file* is not readable
* *source-file* is a directory
* *append?* is absent or
  nil and
  *destination-file* exists
* *destination-file* cannot be opened for output (that is, it is an illegal file name or a write-protected file)
* *source-file* is the same as
  *destination-file*

## Remarks

Copy or append the contents of one file to another file. The
vl-file-copy function will not overwrite an existing file; it will only append to it.

## Release Information

*Releases:*

* AutoCAD R14 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *source-file* and
  *destination-file* arguments previously accepted ASCII text strings, but they now accept Unicode text strings.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

Windows
:   Copy
    *autoexec.bat* to
    *newauto.bat*:

    ```
    (vl-file-copy "c:/autoexec.bat" "c:/newauto.bat")
    1417
    ```

    Copy
    *test.bat* to
    *newauto.bat*:

    ```
    (vl-file-copy "c:/test.bat" "c:/newauto.bat")
    nil
    ```

    The copy fails because
    *newauto.bat* already exists, and the
    *append* argument was not specified.

    Repeat the previous command, but specify
    *append*:

    ```
    (vl-file-copy "c:/test.bat" "c:/newauto.bat" T)
    185
    ```

    The copy is successful because
    T was specified for the
    *append* argument.

Mac OS and Web
:   Copy
    *oldstart.sh* to
    *newstart.sh*:

    ```
    (vl-file-copy "/oldstart.sh" "/newstart.sh")
    1417
    ```

    Copy
    *start.sh* to
    *newstart.sh*:

    ```
    (vl-file-copy "/start.sh" "/newstart.sh")
    nil
    ```

    The copy fails because
    *newstart.sh* already exists, and the
    *append* argument was not specified.

    Repeat the previous command, but specify
    *append*:

    ```
    (vl-file-copy "/start.sh" "/newstart.sh" T)
    185
    ```

    The copy is successful because
    T was specified for the
    *append* argument.

#### Related References

* [findfile (AutoLISP)](findfile-AutoLISP.md)
* [vl-file-delete (AutoLISP)](vl-file-delete-AutoLISP.md)
* [vl-file-rename (AutoLISP)](vl-file-rename-AutoLISP.md)
* [vl-filename-base (AutoLISP)](vl-filename-base-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*