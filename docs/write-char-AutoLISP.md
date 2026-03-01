# write-char (AutoLISP)

Writes one character to the screen or an open file

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(write-char num [file-desc])
```

*num*
:   *Type:* Integer

    The integer value in the range of 1-65536 representing the character to be written.

*file-desc*
:   *Type:* File

    A file descriptor for an open file.

## Return Values

*Type:* Integer

The
*num* argument.

## Release Information

*Releases:*

* AutoCAD R12 and later on Windows
* AutoCAD 2011 and later on Mac OS

## History

*AutoCAD 2021*

* *num* argument previously accepted an ASCII character code in the range of 1-255, but now accepts an integer that represents a
  Unicode character code in the range of 1-65536.
* Return value was modified to support Unicode characters and might be different than earlier releases. For example,
  (write-char 128) previously returned "€", but now returns "". If you want to return "€", your code will need to be updated to
  (write-char 8364).

  ```
  (setq fp (open "E:\\test.txt" "w" "utf8"))
  (write-char fp 8364)
  8364
  ```
* LISPSYS system variable controls which AutoLISP engine is used and the behavior of the function.
  + 0 - ASCII character support (legacy behavior)
  + 1 or 2 - Unicode character support

  NOTE:After the value of the LISPSYS system variable has been changed, AutoCAD must be restarted for the change to take affect.

## Examples

The following command writes the letter
*C* to the command window, and returns the supplied
*num* argument:

```
(write-char 67)
C67
```

Assuming that
f is the descriptor for an open file, the following command writes the letter
*C* to that file:

```
(write-char 67 f)
67
```

NOTE:write-char cannot write a NULL character (code 0) to a file.

#### Related References

* [open (AutoLISP)](open-AutoLISP.md)
* [close (AutoLISP)](close-AutoLISP.md)
* [read-char (AutoLISP)](read-char-AutoLISP.md)
* [write-line (AutoLISP)](write-line-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*