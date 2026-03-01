# File-Handling Functions Reference (AutoLISP)

The following table provides summary descriptions of the AutoLISP file-handling functions.

| File-handling functions | | Platforms | | | | |
| Windows | | Mac OS | | Web |
| Function | Description | AutoCAD | AutoCAD LT | AutoCAD | AutoCAD LT | AutoCAD |
| [(close file-desc)](close-AutoLISP.md) | Closes an open file | ✓ | ✓ | ✓ | -- | ✓ |
| [(findfile filename)](findfile-AutoLISP.md) | Searches the AutoCAD library path for the specified file | ✓ | ✓ | ✓ | -- | ✓ |
| [(findtrustedfile filename)](findtrustedfile-AutoLISP.md) | Searches the AutoCAD trusted file paths for the specified file | ✓ | ✓ | ✓ | -- | ✓ |
| [(open filename mode)](open-AutoLISP.md) | Opens a file for access by the AutoLISP I/O functions | ✓ | ✓ | ✓ | -- | ✓ |
| [(read-char [file-desc])](read-char-AutoLISP.md) | Returns the decimal ASCII code representing the character read from the keyboard input buffer or from an open file | ✓ | ✓ | ✓ | -- | ✓ |
| [(read-line [file-desc])](read-line-AutoLISP.md) | Reads a string from the keyboard or from an open file | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-directory-files [ directory pattern directories])](vl-directory-files-AutoLISP.md) | Lists all files in a given directory | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-file-copy "source-filename" "destination-filename" [append])](vl-file-copy-AutoLISP.md) | Copies or appends the contents of one file to another file | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-file-delete "filename")](vl-file-delete-AutoLISP.md) | Deletes a file | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-file-directory-p "filename")](vl-file-directory-p-AutoLISP.md) | Determines if a file name refers to a directory | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-file-rename "old-filename" "new-filename")](vl-file-rename-AutoLISP.md) | Renames a file | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-file-size "filename")](vl-file-size-AutoLISP.md) | Determines the size of a file, in bytes | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-file-systime "filename")](vl-file-systime-AutoLISP.md) | Returns last modification time of the specified file | ✓ | ✓ | ✓ | -- | -- |
| [(vl-filename-base "filename")](vl-filename-base-AutoLISP.md) | Returns the name of a file, after stripping out the directory path and extension | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-filename-directory "filename")](vl-filename-directory-AutoLISP.md) | Returns the directory path of a file, after stripping out the name and extension | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-filename-extension "filename")](vl-filename-extension-AutoLISP.md) | Returns the extension from a file name, after stripping out the rest of the name | ✓ | ✓ | ✓ | -- | ✓ |
| [(vl-filename-mktemp ["pattern" "directory" "extension"])](vl-filename-mktemp-AutoLISP.md) | Calculates a unique file name to be used for a temporary file | ✓ | ✓ | ✓ | -- | ✓ |
| [(write-char num [file-desc])](write-char-AutoLISP.md) | Writes one character to the screen or to an open file | ✓ | ✓ | ✓ | -- | ✓ |
| [(write-line string [file-desc])](write-line-AutoLISP.md) | Writes a string to the screen or to an open file | ✓ | ✓ | ✓ | -- | ✓ |

#### Related References

* [Functions Reference (AutoLISP)](Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*