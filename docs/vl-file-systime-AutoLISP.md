# vl-file-systime (AutoLISP)

Returns last modification time of the specified file

*Supported Platforms:* Windows and Mac OS only

## Signature

```
(vl-file-systime filename)
```

*filename*
:   *Type:* String

    Name of the file to be checked.

## Return Values

*Type:* List or nil

A list containing the modification date and time; otherwise
nil, if the file is not found.

The list returned contains the following elements:

* year
* month
* day of week
* day of month
* hours
* minutes
* seconds

NOTE:Monday is day 1 of day of week, Tuesday is day 2, and so on.

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
    (vl-file-systime    "c:/program files/<AutoCAD installation directory>/sample/visuallisp/yinyang.lsp")
    (1998 4 3 8 10 6 52)
    ```

    The returned value shows that the file was last modified in 1998, in the 4th month of the year (April), the 3rd day of the
    week (Wednesday), on the 8th day of the month, at 10:6:52.

Mac OS
:   ```
    (vl-file-systime "/output.txt")
    (2011 5 4 26 16 3 51 586)
    ```

    The returned value shows that the file was last modified in 2011, in the 5th month of the year (May), the 4th day of the week
    (Thursday), on the 26th day of the month, at 4:03:51 PM.

#### Related References

* [findfile (AutoLISP)](findfile-AutoLISP.md)
* [vl-file-size (AutoLISP)](vl-file-size-AutoLISP.md)
* [vl-filename-base (AutoLISP)](vl-filename-base-AutoLISP.md)
* [vl-filename-extension (AutoLISP)](vl-filename-extension-AutoLISP.md)
* [vl-filename-directory (AutoLISP)](vl-filename-directory-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*