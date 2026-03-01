# write-line (AutoLISP)

Writes a string to the screen or to an open file

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(write-line str [file-desc])
```

*str*
:   *Type:* String

    A textual value.

*file-desc*
:   *Type:* File

    A file descriptor for an open file.

## Return Values

*Type:* String

The
*str*, quoted in the normal manner. The quotes are omitted when writing to a file.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *str* argument previously accepted an ASCII text string or character, but now accepts a Unicode text string or character.
* Return value was modified to support Unicode characters and might be different than earlier releases.
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

Windows
:   Open a file:

    ```
    (setq f (open "c:\\my documents\\
    ew.tst" "w"))
    #<file "c:\\my documents\\
    ew.tst">
    ```

    Use
    write-line to write a line to the file:

    ```
    (write-line "To boldly go where nomad has gone before." f)
    "To boldly go where nomad has gone before."
    ```

    The line is not physically written until you close the file:

    ```
    (close f)
    nil
    ```

Mac OS
:   Open a file:

    ```
    (setq f (open "/my documents/new.tst" "w"))
    #<file "/my documents/new.tst">
    ```

    Use
    write-line to write a line to the file:

    ```
    (write-line "To boldly go where nomad has gone before." f)
    "To boldly go where nomad has gone before."
    ```

    The line is not physically written until you close the file:

    ```
    (close f)
    nil
    ```

#### Related References

* [open (AutoLISP)](open-AutoLISP.md)
* [close (AutoLISP)](close-AutoLISP.md)
* [read-line (AutoLISP)](read-line-AutoLISP.md)
* [write-char (AutoLISP)](write-char-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*