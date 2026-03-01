# open (AutoLISP)

Opens a file for access by the AutoLISP I/O functions

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(open filename mode [encoding])
```

*filename*
:   *Type:* String

    Name and extension of the file to be opened. If you do not specify the full path name of the file,
    open assumes you are referring to the AutoCAD default drawing directory.

*mode*
:   *Type:* String

    Indicates whether the file is open for reading, writing, or appending. Specify a string containing one of the following letters:

    *r* Open for reading.

    *w* Open for writing. If
    *filename* does not exist, a new file is created and opened. If
    *filename* already exists, its existing data is overwritten. Data passed to an open file is not actually written until the file is closed
    with the
    close function.

    *a* Open for appending. If
    *filename* does not exist, a new file is created and opened. If
    *filename* already exists, it is opened and the pointer is positioned at the end of the existing data, so new data you write to the
    file is appended to the existing data.

    The
    *mode* argument can be uppercase or lowercase.

    NOTE:Prior to AutoCAD 2000,
    *mode* had to be specified in lowercase.

*encoding*
:   *Type:* String

    Indicates the character encoding to use when reading the file. When a value isn't provided for the argument, the file is assumed
    to contain multibyte character set (MBCS) which is the legacy behavior.

    Use one of the following values to specify a different character encoding:

    *utf8* UTF-8

    *utf8-bom* UTF-8 with Byte Order Marks

## Return Values

*Type:* File or nil

If successful,
open returns a file descriptor that can be used by the other I/O functions. If mode
"r" is specified and
*filename* does not exist,
open returns
nil.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *filename* argument previously accepted an ASCII text string, but now accepts a Unicode text string.
* *encoding* argument is newly added.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support and no
    *encoding* argument (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

*AutoCAD 2000*

* *mode* argument previously only accepted a lowercase value.

## Examples

Windows
:   Open an existing file:

    ```
    (setq a (open "c:/datafiles/filelist.txt" "r"))
    #<file "c:/datafiles/filelist.txt">
    ```

    The following examples issue
    open against files that do not exist:

    ```
    (setq f (open "c:\\my documents\\
    ew.tst" "w"))
    #<file "c:\\my documents\\
    ew.tst">

    (setq f (open "nosuch.fil" "r"))
    nil

    (setq f (open "logfile" "a"))
    #<file "logfile">
    ```

Mac OS and Web
:   Open an existing file:

    ```
    (setq a (open "/datafiles/filelist.txt" "r"))
    #<file "/datafiles/filelist.txt">
    ```

    The following examples issue
    open against files that do not exist:

    ```
    (setq f (open "/my documents/new.tst" "w"))
    #<file "/my documents/new.tst">

    (setq f (open "nosuch.fil" "r"))
    nil

    (setq f (open "logfile" "a"))
    #<file "logfile">
    ```

#### Related References

* [close (AutoLISP)](close-AutoLISP.md)
* [findfile (AutoLISP)](findfile-AutoLISP.md)
* [read-line (AutoLISP)](read-line-AutoLISP.md)
* [write-line (AutoLISP)](write-line-AutoLISP.md)
* [vl-filename-mktemp (AutoLISP)](vl-filename-mktemp-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*