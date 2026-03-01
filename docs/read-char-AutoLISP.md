# read-char (AutoLISP)

Returns the integer representing the character read from the keyboard input buffer or from an open file

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(read-char [file-desc])
```

*file-desc*
:   *Type:* File

    A file descriptor (obtained from
    open) referring to an open file. If no
    *file-desc* is specified,
    read-char obtains input from the keyboard input buffer.

## Return Values

*Type:* Integer

Character code in the range of 1-65536.

The
read-char function returns a single newline character (code 10) whenever it detects an end-of-line character or character sequence.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* Return value was modified to support Unicode characters and might be different than earlier releases. For example, suppose
  the "€" character was in a file named
  *test.txt*. Previously, the value of this character would be returned as ASCII code 128, but with Unicode support the value of this
  character would be returned as Unicode code 8364.

  ```
  (setq fp (open "E:\\test.txt" "r" "utf8"))
  (read-char fp)
  8364
  ```
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

The following example omits
*file-desc*, so
read-char looks for data in the keyboard buffer:

```
(read-char)
```

The keyboard buffer is empty, so
read-char waits for user input:

```
ABC
65
```

The user entered
ABC;
read-char returned the code representing the first character entered (A). The next three calls to
read-char return the data remaining in the keyboard input buffer. This data translates to 66 (the code for the letter B), 67 (C), and
10 (newline), respectively:

```
(read-char)
66

(read-char)
67

(read-char)
10
```

With the keyboard input buffer now empty,
read-char waits for user input the next time it is called:

```
(read-char)
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