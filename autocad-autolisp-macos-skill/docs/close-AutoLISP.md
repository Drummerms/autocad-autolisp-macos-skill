# close (AutoLISP)

Closes an open file

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(close file-desc)
```

*file-desc*
:   *Type:* File

    A file descriptor obtained from the
    open function.

## Return Values

*Type:* nil

nil if
*file-desc* is valid; otherwise results in an error message.

After a
close, the file descriptor is unchanged but is no longer valid. Data added to an open file is not actually written until the file
is closed.

## Examples

The following code counts the number of lines in the file
*somefile.txt* and sets the variable
*ct* equal to that number:

```
(setq fil "SOMEFILE.TXT")
(setq x (open fil "r") ct 0)
(while (read-line x)
  (setq ct (1+ ct))
)
(close x)
```

#### Related References

* [open (AutoLISP)](open-AutoLISP.md)
* [findfile (AutoLISP)](findfile-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*