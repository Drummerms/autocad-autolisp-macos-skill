# About File Descriptors (AutoLISP)

A file descriptor is a pointer to a file opened by the AutoLISP open function.

The open function returns this pointer as an alphanumeric label. You supply the file descriptor as an argument to other AutoLISP functions
that read, write, or close the file.

You use the following functions when working with a file:

* open - Opens a file for access by the AutoLISP I/O functions.
* write-line - Writes a string to the screen or to an open file.
* write-char - Writes one character to the screen or to an open file.
* read-line - Reads a string from the keyboard or from an open file, until an end-of-line marker is encountered.
* read-char - Returns the decimal ASCII code representing the character read from the keyboard input buffer or from an open file.
* print – Prints an expression to the command line or writes an expression to an open file.
* prin1 – Prints an expression to the command line or writes an expression to an open file.
* close – Closes a file opened with the open function.

The following example opens the *myinfo.dat* file for reading. The open function returns a file descriptor which is stored in the file1 variable:

```
(setq file1 (open "c:\\myinfo.dat" "r"))
#<file "c:\\myinfo.dat">
```

Files remain open until you explicitly close them in your AutoLISP program. The close function closes a file. The following code closes the file whose file descriptor is stored in the file1 variable:

```
(close file1)
nil
```

#### Related Concepts

* [About Searching for Files (AutoLISP)](About-Searching-for-Files-AutoLISP.md)
* [About ASCII Codes (AutoLISP)](About-ASCII-Codes-AutoLISP.md)
* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*