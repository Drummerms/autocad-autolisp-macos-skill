# findtrustedfile (AutoLISP)

Searches the AutoCAD trusted locations for the specified file

*Supported Platforms:* Windows, Mac OS, and Web

## Signature

```
(findtrustedfile filename)
```

*filename*
:   *Type:* String

    Name of the file to be searched for.

## Return Values

*Type:* String or nil

A string containing the fully qualified file name; otherwise
nil, if the specified file is not found.

## Remarks

The
findtrustedfile function makes no assumption about the file type or extension of
*filename*.

## Examples

Windows
:   If the trusted locations and support search file paths contains
    *C:\myapps*, and
    *abc.lsp* is contained in the path, the function retrieves the path name:

    ```
    (findtrustedfile "abc.lsp")
    "C:\\myapps\\abc.lsp"
    ```

    If the folder in which
    *abc.lsp* is not present in both the trusted locations and support search file paths,
    findtrustedfile returns
    nil.

    ```
    (findtrustedfile "abc.lsp")
    nil
    ```

Mac OS and Web
:   If the trusted locations and support search file paths contains
    */myapps*, and
    *abc.lsp* is contained in the path, the function retrieves the path name:

    ```
    (findtrustedfile "abc.lsp")
    "/myapps/abc.lsp"
    ```

    If the folder in which
    *abc.lsp* is not present in both the trusted locations and support search file paths,
    findtrustedfile returns
    nil.

    ```
    (findtrustedfile "abc.lsp")
    nil
    ```

#### Related References

* [getfiled (AutoLISP)](getfiled-AutoLISP.md)
* [findfile (AutoLISP)](findfile-AutoLISP.md)

#### Related Concepts

* [File-Handling Functions Reference (AutoLISP)](File-Handling-Functions-Reference-AutoLISP.md)

[Please send us your comment about this page](..)

[![Creative Commons License](../images/ccLink.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/) *Except where otherwise noted, this work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/). Please see the [Autodesk Creative Commons FAQ](http://autodesk.com/creativecommons) for more information.*