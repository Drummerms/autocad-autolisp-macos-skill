# findfile (AutoLISP)

Searches the AutoCAD library and trusted paths for the specified file or directory

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(findfile filename)
```

*filename*
:   *Type:* String

    Name of the file or directory to be searched for.

## Return Values

*Type:* String or nil

A string containing the fully qualified file name; otherwise
nil, if the specified file or directory is not found.

The file name returned by
findfile is suitable for use with the
open function.

## Remarks

The
findfile function makes no assumption about the file type or extension of
*filename*. If
*filename* does not specify a drive/directory prefix,
findfile searches the AutoCAD library and trusted paths. If a drive/directory prefix is supplied,
findfile looks only in that directory.

## Examples

Windows
:   If the current directory is
    */MyUtilities/lsp* and it contains the file
    *abc.lsp*, the following function call retrieves the path name:

    ```
    (findfile "abc.lsp")
    "C:\\MyUtilities\\lsp\\abc.lsp"
    ```

    If you are editing a drawing in the
    */My Utilities/Support* directory, and the
    ACAD environment variable is set to
    */My Utilities/Support*, and the file
    *xyz.txt* exists only in the
    */My Utilities/Support* directory, then the following command retrieves the path name:

    ```
    (findfile "xyz.txt")
    "C:\\My Utilities\\Support\\xyz.txt"
    ```

    If the file
    *nosuch* is not present in any of the directories on the library or trusted search paths,
    findfile returns
    nil:

    ```
    (findfile "nosuch")
    nil
    ```

Mac OS and Web
:   If the current directory is
    */MyUtilities/lsp* and it contains the file
    *abc.lsp*, the following function call retrieves the path name:

    ```
    (findfile "abc.lsp")
    "/MyUtilities/Lsp/abc.lsp"
    ```

    If you are editing a drawing in the
    */My Utilities/Support*directory, and the
    ACAD environment variable is set to
    */My Utilities/Support*, and the file
    *xyz.txt* exists only in the
    */My Utilities/Support* directory, then the following command retrieves the path name:

    ```
    (findfile "xyz.txt")
    "/MyUtilities/Support/xyz.txt"
    ```

    If the file
    *nosuch* is not present in any of the directories on the library or trusted search paths,
    findfile returns
    nil:

    ```
    (findfile "nosuch")
    nil
    ```

#### Related References

* [getfiled (AutoLISP)](getfiled-AutoLISP.md)
* [findtrustedfile (AutoLISP)](findtrustedfile-AutoLISP.md)
* [vl-directory-files (AutoLISP)](vl-directory-files-AutoLISP.md)
* [vl-filename-directory (AutoLISP)](vl-filename-directory-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*