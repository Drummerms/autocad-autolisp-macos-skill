# read-line (AutoLISP)

Reads a string from the keyboard or from an open file, until an end-of-line marker is encountered

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(read-line [file-desc])
```

*file-desc*
:   *Type:* File

    A file descriptor (obtained from
    open) referring to an open file. If no
    *file-desc* is specified,
    read-line obtains input from the keyboard input buffer.

## Return Values

*Type:* String

The text read by
read-line, without the end-of-line marker. If
read-line encounters the end of the file, it returns
nil.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* Return value was modified to support Unicode characters and might be different than earlier releases.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

Windows
:   Open a file for reading:

    ```
    (setq f (open "c:\\my documents\\
    ew.tst" "r"))
    #<file "c:\\my documents\\
    ew.tst">
    ```

    Use
     *read-line*  to read a line from the file:

    ```
    (read-line f)
    "To boldly go where nomad has gone before."
    ```

    Obtain a line of input from the user:

    ```
    (read-line) To boldly go
    "To boldly go"
    ```

Mac OS and Web
:   Open a file for reading:

    ```
    (setq f (open "/my documents/new.tst" "r"))
    #<file "/my documents/new.tst">
    ```

    Command:

    Use
    read-line to read a line from the file:

    ```
    (read-line f)
    "To boldly go where nomad has gone before."
    ```

    Obtain a line of input from the user:

    ```
    (read-line) To boldly go
    "To boldly go"
    ```

#### Related References

* [open (AutoLISP)](open-AutoLISP.md)
* [close (AutoLISP)](close-AutoLISP.md)
* [read-char (AutoLISP)](read-char-AutoLISP.md)
* [write-line (AutoLISP)](write-line-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*